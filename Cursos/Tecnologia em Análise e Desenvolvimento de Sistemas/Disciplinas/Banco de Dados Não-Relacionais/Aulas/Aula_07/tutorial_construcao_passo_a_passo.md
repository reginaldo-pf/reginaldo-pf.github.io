# Guia Passo a Passo: CRUD Avançado, Atualizações Atômicas e Indexação no MongoDB

* **Curso:** Tecnologia em Análise e Desenvolvimento de Sistemas (ADS) — IFCE Campus Tauá
* **Disciplina:** Banco de Dados Não-Relacionais (ADS16) — Aula 07
* **Docente:** Prof. Me. Reginaldo Fernandes
* **Ambiente de Trabalho:** Linux / Docker / MongoDB 8.0 / MongoDB Compass / MongoSH / Python 3 (`PyMongo`)

---

## Parte 1: Fundamentos Teóricos da Indexação e Complexidade Computacional

### 1.1 O Custo Oculto da Busca Sequencial (`COLLSCAN`)
Em coleções recém-criadas ou com poucas dezenas de documentos (como os testes iniciais feitos na Aula 06), qualquer consulta parece instantânea aos olhos do desenvolvedor. Contudo, quando o banco de dados armazena dezenas ou centenas de milhares de registros, uma consulta desprovida de índices força o motor de armazenamento a realizar uma varredura completa da coleção: **`COLLSCAN` (*Collection Scan*)**.

No `COLLSCAN`, o MongoDB precisa carregar do disco (ou do cache WiredTiger) bloco por bloco de documentos BSON, deserializar suas chaves e testar a condição lógica contra cada registro individualmente.
* **Complexidade Temporal Assintótica:** $\mathcal{O}(N)$, onde $N$ representa o Tamanho da Coleção (número total de documentos).
* **Impacto no Hardware:** Sob concorrência de múltiplos clientes simultâneos, dezenas de `COLLSCANs` concorrentes esgotam o tempo de CPU em operações de decodificação e desalojam dados úteis da memória RAM, forçando constantes leituras lentas de I/O em disco.

---

### 1.2 A Estrutura de Árvore Balanceada ($B\text{-Tree}$) no Motor WiredTiger
Para eliminar a varredura linear, o MongoDB utiliza estruturas de dados em **Árvore Balanceada ($B\text{-Tree}$)** mantidas ordenadas pelo motor de armazenamento **WiredTiger**.

Em uma $B\text{-Tree}$:
1. **Nó Raiz (*Root Node*):** Ponto de entrada da busca, contendo faixas de valores e ponteiros para nós intermediários.
2. **Nós Internos (*Internal Nodes*):** Direcionam a pesquisa descendo pelos ramos adequados através de comparações binárias rápidas.
3. **Nós Folha (*Leaf Nodes*):** Contêm os valores das chaves indexadas estritamente ordenados e o endereço de armazenamento do documento correspondente (RecordId / ponteiro em disco).
4. **Fator de Ramificação (*Fan-out*, $b$):** O número médio de ponteiros filhos que cada nó pode conter (tipicamente entre $50$ e $200$ entradas por página de memória de $4\text{ KB}$).

```
                  [ Raiz: Preço 100 | Preço 500 ]
                     /            |            \
       [Nó: 10 .. 99]      [Nó: 100 .. 499]    [Nó: 500 .. 1000]
        /          \            /         \         /          \
   [Folhas BSON] [Folhas]   [Folhas]   [Folhas]  [Folhas]   [Folhas]
```

---

### 1.3 Exemplo Analítico Pareado: $\mathcal{O}(N)$ vs $\mathcal{O}(\log_{b} N)$

#### 1. Cálculo Matemático Passo a Passo:
Considere a coleção `produtos` do e-commerce *ShopGrids* com $N = 100.000$ produtos e um Fator de Ramificação de $b = 100$ chaves por nó da $B\text{-Tree}$:

1. **Sem Índice (`COLLSCAN`):**
   * Número de documentos a examinar no pior caso:
     $$\text{Operações}_{\text{scan}} = N = 100.000 \text{ documentos lidos}$$
2. **Com Índice $B\text{-Tree}$ (`IXSCAN`):**
   * A altura da árvore $h$ é dada pelo logaritmo na base $b$:
     $$h \approx \lceil \log_{b}(N) \rceil = \left\lceil \frac{\ln(100.000)}{\ln(100)} \right\rceil = \lceil 2.5 \rceil = 3 \text{ acessos a nós}$$
   * **Ganho Teórico de Eficiência:**
     $$\text{Redução de I/O} = \left( 1 - \frac{3}{100.000} \right) \times 100\% = 99.997\%$$

#### 2. Demonstração em Código Python Pareado:
O trecho abaixo mede a diferença analítica computacional entre percorrer linearmente uma lista não ordenada vs realizar busca binária/árvore:

```python
import time
import bisect

# Colecao simulada com N = 100.000 itens
N = 100_000
dados_lineares = list(range(N))
dados_ordenados = sorted(dados_lineares) # Estrutura do Indice

alvo = 99_999 # Pior caso (elemento final)

# 1. Busca Linear (Simulacao de COLLSCAN - O(N))
t0 = time.perf_counter()
for item in dados_lineares:
    if item == alvo:
        break
tempo_linear = (time.perf_counter() - t0) * 1000

# 2. Busca Binaria / Arvore (Simulacao de IXSCAN - O(log N))
t0 = time.perf_counter()
pos = bisect.bisect_left(dados_ordenados, alvo)
tempo_indice = (time.perf_counter() - t0) * 1000

print(f"COLLSCAN (Linear): {tempo_linear:.4f} ms")
print(f"IXSCAN (Indice)  : {tempo_indice:.4f} ms")
print(f"Ganho Relativo   : {tempo_linear / max(tempo_indice, 0.0001):.1f}x mais rapido")
```

---

## Parte 2: Operadores CRUD Avançados e Atualizações Atômicas

Antes de criar os índices, precisamos dominar os operadores avançados que compõem consultas profissionais de alta precisão.

### 2.1 O Operador `$elemMatch` em Arrays de Subdocumentos
Um dos erros conceituais mais recorrentes cometidos por desenvolvedores júnior ao manipular MongoDB é acreditar que filtros com múltiplos critérios em arrays avaliam o mesmo subdocumento.

#### O Problema do Falso Positivo:
Considere o seguinte pedido na coleção `pedidos`:
```json
{
  "_id": 101,
  "codigo": "PED-990",
  "itens": [
    { "sku": "MOUSE-01", "preco": 150.0, "qtd": 1 },
    { "sku": "CABO-HDMI", "preco": 20.0, "qtd": 4 }
  ]
}
```

Se executarmos a consulta:
```javascript
db.pedidos.find({
  "itens.preco": { $gt: 100 },
  "itens.qtd": { $gte: 3 }
})
```
O documento **será retornado**! Por quê? Porque o MongoDB verifica se *algum* item tem `preco > 100` (o Mouse atende) e se *algum* item tem `qtd >= 3` (o Cabo atende). Os critérios foram satisfeitos por **elementos diferentes** do array!

#### A Solução Rigorosa com `$elemMatch`:
O operador `$elemMatch` restringe a avaliação lógica para que **todas as condições sejam satisfeitas pelo mesmo elemento**:
```javascript
db.pedidos.find({
  itens: {
    $elemMatch: {
      preco: { $gt: 100 },
      qtd: { $gte: 3 }
    }
  }
})
// O pedido 101 NÃO é retornado, eliminando o falso positivo!
```

---

### 2.2 O Operador `$expr`: Comparando Dois Campos do Mesmo Documento
Normalmente, as cláusulas de `find()` comparam o valor de um campo com uma constante (`{ preco: { $gt: 50 } }`). Quando precisamos comparar **dois campos pertencentes ao próprio documento**, utilizamos `$expr` com sintaxe de agregação (onde o nome do campo é prefixado com `$`):

```javascript
// Localizar produtos cujo estoque atual esta abaixo do estoque minimo de seguranca:
db.produtos.find({
  $expr: {
    $lt: ["$estoque.atual", "$estoque.minimo"]
  }
})

// Localizar pedidos onde o total pago foi menor que o subtotal (houve desconto aplicado):
db.pedidos.find({
  $expr: {
    $lt: ["$pagamento.total_pago", "$pagamento.subtotal"]
  }
})
```

---

### 2.3 Operadores `$all` e `$size`
* **`$all`:** O array deve conter todos os elementos listados, independentemente da ordem:
  ```javascript
  // Produtos que contenham simultaneamente as tags 'gamer' e 'sem fio':
  db.produtos.find({ tags: { $all: ["gamer", "sem fio"] } })
  ```
* **`$size`:** Busca arrays com um comprimento exato:
  ```javascript
  // Pedidos que contenham exatamente 1 item:
  db.pedidos.find({ itens: { $size: 1 } })
  ```

---

### 2.4 Atualizações Atômicas Avançadas sem Conflito de Concorrência
Nunca leia um valor para a memória do servidor Python/Node, modifique-o no código e regrave com `$set` em ambientes concorrentes, pois isso gera **Condição de Corrida (*Race Condition*)**. Em vez disso, utilize operadores atômicos executados diretamente pelo motor WiredTiger.

#### 1. Operadores Numéricos Atômicos:
* **`$inc`:** Incrementa ou decrementa contadores de forma atômica:
  ```javascript
  // Venda realizada: decrementa 2 do estoque e incrementa 2 no total vendido:
  db.produtos.updateOne(
    { sku: "NOTE-DELL-G15" },
    { 
      $inc: { 
        "estoque.atual": -2,
        "metricas.vendas_totais": 2
      }
    }
  )
  ```
* **`$min` e `$max`:** Altera o campo apenas se o novo valor for estritamente menor ou maior que o valor existente no banco:
  ```javascript
  // Registra o menor preco historico atingido pelo produto:
  db.produtos.updateOne(
    { sku: "NOTE-DELL-G15" },
    { $min: { "historico.menor_preco": 4299.00 } }
  )
  ```

#### 2. Operadores de Lista (`$push`, `$addToSet`, `$slice`):
* **`$addToSet`:** Adiciona elementos ao array somente se eles ainda não existirem (semântica de Conjunto Matemático):
  ```javascript
  db.produtos.updateOne(
    { sku: "NOTE-DELL-G15" },
    { $addToSet: { tags: "promocao-black-friday" } }
  )
  ```
* **`$push` com `$slice` (Manutenção do *Subset Pattern*):**
  Ao adicionar um novo log de acesso ou avaliação, mantemos o array limitado aos últimos 5 itens para evitar o crescimento descontrolado (*Unbounded Array*):
  ```javascript
  db.produtos.updateOne(
    { sku: "NOTE-DELL-G15" },
    {
      $push: {
        ultimas_avaliacoes: {
          $each: [{ nota: 5, autor: "Carlos", data: new Date() }],
          $slice: -5 // Mantem apenas os 5 mais recentes
        }
      }
    }
  )
  ```

#### 3. O Poder dos `arrayFilters` e o Identificador `$[<elem>]`:
Quando precisamos atualizar um item específico dentro de um array de subdocumentos sem saber o seu índice numérico, usamos `arrayFilters`:

```javascript
// Atualizar o status apenas do item cujo SKU seja 'MOUSE-01' no pedido 'PED-990':
db.pedidos.updateOne(
  { codigo: "PED-990" },
  { 
    $set: { 
      "itens.$[itemAlvo].status_entrega": "SEPARADO_EM_ESTOQUE",
      "itens.$[itemAlvo].data_separacao": new Date()
    } 
  },
  {
    arrayFilters: [ { "itemAlvo.sku": "MOUSE-01" } ]
  }
)
```

---

## Parte 3: Tipos de Índices na Prática

### 3.1 Comandos Fundamentais de Gestão de Índices
```javascript
// Listar indices existentes na colecao:
db.produtos.getIndexes()

// Remover um indice pelo nome ou pela especificacao da chave:
db.produtos.dropIndex("sku_1")
db.produtos.dropIndex({ sku: 1 })
```

---

### 3.2 Índices Simples (*Single Field Index*)
Criados sobre um único campo:
```javascript
db.produtos.createIndex({ sku: 1 }, { unique: true, name: "idx_sku_unico" })
```
* **Direção (`1` vs `-1`):** Em índices simples, a ordem de indexação (ascendente `1` ou descendente `-1`) **não afeta o desempenho**, pois a $B\text{-Tree}$ pode ser percorrida de trás para frente com o mesmo custo computacional.
* **Opção `unique: true`:** Garante unicidade estrita no nível do banco de dados, rejeitando inserções duplicadas.

---

### 3.3 Índices Compostos (*Compound Index*)
Criados quando as consultas combinam múltiplos critérios de filtro ou filtros aliados a ordenações:
```javascript
db.produtos.createIndex({ categoria: 1, preco: -1 }, { name: "idx_categoria_preco" })
```

#### Regra dos Prefixos de Índice (*Index Prefixes*):
Um índice composto em `{ A: 1, B: 1, C: 1 }` pode atender consultas sobre:
* `{ A: 1 }` (Prefixo de 1 campo)
* `{ A: 1, B: 1 }` (Prefixo de 2 campos)
* `{ A: 1, B: 1, C: 1 }` (Índice completo)

**Atenção:** Ele **NÃO** atenderá consultas que busquem apenas `{ B: 1 }` ou `{ C: 1 }` sem conter o campo `A`!

---

### 3.4 Índices Multikey (Indexação de Arrays)
Quando criamos um índice sobre um campo que armazena arrays (ex: `tags: ["eletronicos", "hardware", "promocao"]`), o MongoDB automaticamente cria um **Índice Multikey**.
O motor WiredTiger gera uma entrada na $B\text{-Tree}$ para cada valor contido no array de cada documento.

```javascript
db.produtos.createIndex({ tags: 1 })
```

> **⚠️ Regra de Restrição Crítica:**
> Em um índice composto, **no máximo um dos campos indexados pode ser um array**!
> Tentar criar `db.produtos.createIndex({ tags: 1, cores_disponiveis: 1 })` causará erro (`cannot index parallel arrays`) caso existam documentos onde ambos os campos sejam arrays, pois isso exigiria calcular o produto cartesiano de entradas ($M \times N$).

---

### 3.5 Otimizações de Memória: Índices Parciais, Esparsos e TTL

1. **Índices Parciais (`partialFilterExpression`):**
   Indexam apenas os documentos que atendem a um predicado, economizando dezenas de megabytes de memória RAM:
   ```javascript
   // Indexar apenas pedidos que estejam com status 'PENDENTE' (pedidos concluidos nao ocupam RAM no indice):
   db.pedidos.createIndex(
     { cliente_id: 1, data_criacao: -1 },
     { partialFilterExpression: { status: "PENDENTE" } }
   )
   ```
2. **Índices Esparsos (`sparse: true`):**
   Contêm entradas apenas para documentos que realmente contêm o campo indexado.
3. **Índices TTL (*Time To Live*):**
   Removem documentos automaticamente após determinado intervalo de tempo (ideal para sessões de login, carrinhos abandonados e logs):
   ```javascript
   // Apagar o documento automaticamente 3600 segundos (1 hora) apos a data_expiracao:
   db.sessoes_ativas.createIndex(
     { data_expiracao: 1 },
     { expireAfterSeconds: 0 }
   )
   ```

---

## Parte 4: A Regra de Ouro ESR e Busca Textual Ponderada

### 4.1 A Regra de Ouro ESR (*Equality, Sort, Range*)
Ao desenhar um índice composto para consultas complexas que combinam igualdades, ordenação e faixas, a ordem de declaração dos campos no índice deve seguir rigorosamente a sequência **ESR**:

```
1. [E] Equality  (Igualdade) -> Campos com valores exatos (status: 'ATIVO', categoria: 'Informatica')
2. [S] Sort      (Ordenação) -> Campos usados na clausula sort ({ data_cadastro: -1 })
3. [R] Range     (Faixa)     -> Campos com operadores de faixa (preco: { $gte: 100, $lte: 500 })
```

#### Por que o *Sort* DEVE vir antes do *Range*?
* Se o índice for `{ status: 1, preco: 1, data_cadastro: -1 }` (E-R-S):
  Ao encontrar os registros que batem com `status = 'ATIVO'`, o motor entra na faixa de `preco`. Dentro da faixa de preço, os documentos estão espalhados com diferentes datas de cadastro. O MongoDB é forçado a coletar todos os documentos e alocar um buffer em memória RAM para executar a etapa **`SORT`**.
  * Se o volume exceder **100 MB**, a consulta falha com `Executor error during find command :: caused by :: Sort exceeded memory limit`.
* Se o índice for `{ status: 1, data_cadastro: -1, preco: 1 }` (E-S-R):
  O MongoDB filtra `status = 'ATIVO'` e já encontra os documentos ordenados cronologicamente na própria árvore $B\text{-Tree}$! Em seguida, percorre a árvore apenas testando o predicado de preço, **eliminando completamente a etapa de `SORT` em memória**!

---

### 4.2 Índices Textuais (*Full-Text Search*) e Ranqueamento por Escore
Quando o usuário digita na barra de busca `"teclado ergonômico preto"`, usar expressões regulares (`$regex`) é inviável em larga escala, pois não aproveita raízes gramaticais (*stemming*) e executa comparações caractere a caractere.

O MongoDB oferece suporte a **Índices Textuais nativos**:
* Realiza **tokenização** (separação de palavras).
* Elimina **Stopwords** (artigos, preposições como *"de"*, *"para"*, *"com"*).
* Aplica **Stemming** (redução da palavra ao radical: *"correndo"*, *"correu"* $\to$ *"corr"*).

#### 1. Criando o Índice Textual com Pesos Ponderados (*Weights*):
Podemos atribuir importância maior ao título do produto do que à descrição longa:
```javascript
db.produtos.createIndex(
  {
    titulo: "text",
    tags: "text",
    descricao: "text"
  },
  {
    weights: {
      titulo: 10,   // Ocorrencia no titulo tem peso maximo
      tags: 5,       // Tags tem peso intermediario
      descricao: 1   // Descricao tem peso normal
    },
    default_language: "portuguese",
    name: "idx_busca_textual_produtos"
  }
)
```

#### 2. Executando a Busca e Ordenando pelo Escore de Relevância:
```javascript
db.produtos.find(
  { $text: { $search: "teclado ergonomico sem fio" } },
  { score: { $meta: "textScore" }, titulo: 1, preco: 1 }
).sort({ score: { $meta: "textScore" } })
```

---

## Parte 5: Diagnóstico com `explain()`, Covered Queries e Benchmark

### 5.1 Os Três Modos da Ferramenta `explain()`
Para auditar a estratégia do otimizador de consultas:
```javascript
// 1. Apenas o plano escolhido sem executar a query:
db.produtos.find({ sku: "NOTE-1" }).explain("queryPlanner")

// 2. Executa a query e exibe estatisticas reais de execucao (RECOMENDADO):
db.produtos.find({ sku: "NOTE-1" }).explain("executionStats")

// 3. Testa e exibe as estatisticas de todos os planos candidatos testados:
db.produtos.find({ sku: "NOTE-1" }).explain("allPlansExecution")
```

---

### 5.2 Decodificando as Métricas Vitais do `executionStats`

| Campo no JSON | Significado Técnico | Meta de Engenharia |
| :--- | :--- | :--- |
| `stage` | O estágio executado (`COLLSCAN`, `IXSCAN`, `FETCH`, `SORT`). | `IXSCAN` (ou sem `FETCH`). |
| `totalDocsExamined` | Total de documentos físicos lidos do disco/cache. | O mais próximo possível de `nReturned`. |
| `totalKeysExamined` | Total de nós/chaves da $B\text{-Tree}$ inspecionados. | O mais próximo possível de `nReturned`. |
| `nReturned` | Número real de documentos devolvidos à aplicação. | Documentos solicitados pelo cliente. |
| `executionTimeMillis` | Tempo total de processamento no motor em ms. | $\le 1\text{ ms}$ para buscas pontuais. |

$$\text{Razão de Eficiência} = \frac{\text{totalDocsExamined}}{\text{nReturned}} \quad (\text{Ideal } = 1.0; \quad \text{COLLSCAN } = \frac{50.000}{10} = 5.000)$$

---

### 5.3 O Santo Graal: *Covered Queries* (Consultas Cobertas)
Uma **Consulta Coberta (*Covered Query*)** é aquela onde:
1. Todos os campos do filtro estão no índice.
2. Todos os campos retornados na projeção estão no mesmo índice.
3. O campo `_id` é explicitamente excluído da projeção (`_id: 0`), a menos que ele faça parte do próprio índice.

Quando isso acontece, o MongoDB **NUNCA precisa carregar o documento BSON da memória/disco**! A consulta é respondida inteiramente dentro da estrutura enxuta do índice na RAM:
* **Estágio:** Apenas `IXSCAN` $\to$ `PROJECTION_COVERED` (o estágio `FETCH` desaparece!).
* **`totalDocsExamined`:** **$0$** (zero documentos lidos!).

```javascript
// Criando o indice composto:
db.produtos.createIndex({ categoria: 1, preco: 1, sku: 1 })

// Consulta 100% coberta:
db.produtos.find(
  { categoria: "Eletrônicos", preco: { $lte: 2000 } },
  { categoria: 1, preco: 1, sku: 1, _id: 0 } // _id: 0 eh OBRIGATORIO!
).explain("executionStats")
```

---

### 5.4 Benchmark Automatizado em Laboratório
No laboratório da disciplina, executamos o script `codigo/benchmark_indexacao_explain.py` sobre 50.000 documentos sintéticos do *ShopGrids*.

Os resultados obtidos evidenciam o impacto brutal da indexação:
* **Consulta sem Índice (`COLLSCAN`):** $68.4\text{ ms}$ | $50.000$ documentos examinados.
* **Consulta com Índice Simples (`IXSCAN` + `FETCH`):** $1.2\text{ ms}$ | $15$ documentos examinados.
* **Consulta Coberta (*Covered Query*):** $0.2\text{ ms}$ | **$0$** documentos examinados.

A indexação reduziu a latência em **$99.7\%$** e eliminou totalmente a saturação de I/O de disco.
