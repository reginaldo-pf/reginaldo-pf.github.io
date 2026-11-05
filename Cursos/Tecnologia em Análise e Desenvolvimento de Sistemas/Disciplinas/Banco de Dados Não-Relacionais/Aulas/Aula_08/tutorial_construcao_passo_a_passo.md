# Guia Passo a Passo: MongoDB Aggregation Framework e Business Intelligence

* **Curso:** Tecnologia em Análise e Desenvolvimento de Sistemas (ADS) — IFCE Campus Tauá  
* **Disciplina:** Banco de Dados Não-Relacionais (ADS16) — Aula 08  
* **Docente Responsável:** Prof. Me. Reginaldo Fernandes  
* **Ambiente de Trabalho:** Linux / Docker / MongoDB 8.0 / MongoDB Compass / MongoSH / Python 3 (`PyMongo`)  

---

## Parte 1: Arquitetura de Fluxo de Dados (*Dataflow*) e Comparação Formal com SQL

### 1.1 O Desafio da Análise de Dados em Ambientes Distribuídos
Nas Aulas 06 e 07, exploramos a modelagem de documentos BSON e criamos índices $B\text{-Tree}$ de alto desempenho para buscas transacionais via método `find()`. No entanto, aplicações corporativas exigem a geração contínua de relatórios consolidados e métricas de inteligência de negócio:
* Qual o faturamento total e ticket médio por mês?
* Quais os 5 produtos e categorias mais vendidos em volume financeiro?
* Qual a distribuição de clientes por faixa de consumo e região geográfica?

Executar esse processamento na camada de aplicação (no servidor Python ou Node.js) transfere gigabytes de dados desnecessários pela rede, sobrecarrega a memória RAM da aplicação e ignora a capacidade analítica interna do banco de dados. O **MongoDB Aggregation Framework** resolve esse gargalo processando as transformações diretamente no servidor de dados através de uma arquitetura funcional de **Pipeline de Dados (*Dataflow Pipeline*)**.

---

### 1.2 O Conceito de Pipeline de Agregação
Um pipeline de agregação é uma esteira sequencial ordenada composta por múltiplos **estágios (*stages*)**. 
* Cada estágio recebe como entrada um fluxo (*stream*) de documentos BSON.
* Realiza uma operação específica (como filtrar, transformar, agrupar ou desconstruir).
* Produz uma nova coleção efêmera de documentos que serve como entrada estrita para o estágio subsequente.
* **Imutabilidade:** Os documentos originais armazenados no disco ou na coleção física nunca são alterados.

```
+------------------+      +----------------+      +---------------+      +---------------+
| Coleção Original | ---> | Estágio 1      | ---> | Estágio 2     | ---> | Saída Final   |
| (pedidos)        |      | ($match selet) |      | ($group soma) |      | (Relatório)   |
+------------------+      +----------------+      +---------------+      +---------------+
```

---

### 1.3 Mapeamento Formal: Álgebra SQL vs MongoDB Pipeline

| Cláusula SQL (Relacional) | Estágio do MongoDB | Função Estrutural |
| :--- | :--- | :--- |
| `WHERE` | `$match` | Filtragem horizontal de documentos com suporte a índices $B\text{-Tree}$. |
| `SELECT / AS` | `$project` / `$addFields` | Projeção vertical, inclusão/exclusão de atributos e campos derivados. |
| `GROUP BY / AGG()` | `$group` | Agrupamento por chave única ou composta e aplicação de acumuladores. |
| `HAVING` | `$match` (pós-`$group`) | Filtragem condicional sobre documentos já sintetizados. |
| `ORDER BY` | `$sort` | Ordenação crescente (`1`) ou decrescente (`-1`). |
| `LIMIT / OFFSET` | `$limit` / `$skip` | Paginação determinística e restrição volumétrica. |
| `JOIN` | `$lookup` | Cruzamento externo (*Left Outer Join*) com outra coleção da base. |
| `EXPLODE / UNNEST` | `$unwind` | Desconstrução de arrays em múltiplos documentos independentes. |

---

## Parte 2: Estágios Fundamentais no MongoDB Compass e no MongoSH

### 2.1 Filtragem Precoce com `$match`
O estágio `$match` utiliza a mesma sintaxe de filtros do método `find()`. Quando colocado na **primeira posição do pipeline**, ele permite que o otimizador do WiredTiger utilize índices já existentes, descartando dados irrelevantes antes que entrem na esteira de memória.

```javascript
// Filtrando apenas pedidos entregues com valor superior ou igual a R$ 100,00
{
  $match: {
    status: "entregue",
    valor_total: { $gte: 100.0 }
  }
}
```

---

### 2.2 Projeção e Enriquecimento: `$project` vs `$addFields`
* **`$project`:** Modifica radicalmente o formato do documento. Por padrão, todos os campos não especificados são descartados. Para ocultar a chave primária `_id`, deve-se declarar explicitamente `_id: 0`.
* **`$addFields`:** Preserva integralmente todas as chaves existentes no documento, adicionando exclusivamente os novos campos calculados.

```javascript
// Exemplo com $project: criando campo derivado e formatando saída
{
  $project: {
    _id: 0,
    numero_pedido: 1,
    cliente_nome: 1,
    valor_liquido: {
      $subtract: ["$valor_total", "$desconto_total"]
    }
  }
}
```

---

### 2.3 Ordenação e Paginação: `$sort`, `$skip` e `$limit`
A sequência de ordenação e paginação é essencial para relatórios de grande porte.

```javascript
// Pipeline completo de listagem das 5 compras mais recentes
[
  { $match: { status: "entregue" } },
  { $sort: { data_pedido: -1 } },
  { $skip: 0 },
  { $limit: 5 }
]
```

---

## Parte 3: Agrupamentos e Acumuladores Analíticos (`$group`)

### 3.1 A Chave de Agrupamento `_id`
No estágio `$group`, a chave `_id` define a identidade única de cada grupo de saída:
1. **Agrupamento Global (KPI Único):** `_id: null` consolida a coleção inteira em uma única métrica global (ex.: faturamento total da loja).
2. **Agrupamento por Campo Simples:** `_id: "$cliente_estado"` agrupa por Unidade Federativa.
3. **Agrupamento por Chave Composta:** `_id: { ano: { $year: "$data_pedido" }, canal: "$canal" }` agrega por período temporal e canal de venda em um subdocumento.

---

### 3.2 Operadores Acumuladores em Ação

* **`$sum`:** Realiza somatórios numéricos ou contagem simples quando recebe a constante 1:
  `total_faturado: { $sum: "$valor_total" }` | `quantidade: { $sum: 1 }`
* **`$avg`:** Calcula a média aritmética dos valores:
  `ticket_medio: { $avg: "$valor_total" }`
* **`$min` e `$max`:** Determina o piso e teto observados no grupo.
* **`$push`:** Acumula os valores de cada registro em uma lista sequencial, preservando todas as repetições.
* **`$addToSet`:** Cria uma lista agregada que atua como conjunto matemático rigoroso, **eliminando entradas duplicadas**.

```javascript
// MongoSH: Agrupamento de pedidos por canal de venda
db.pedidos.aggregate([
  { $match: { status: "entregue" } },
  {
    $group: {
      _id: "$canal",
      faturamento_total: { $sum: "$valor_total" },
      ticket_medio: { $avg: "$valor_total" },
      formas_usadas: { $addToSet: "$forma_pagamento" },
      total_vendas: { $sum: 1 }
    }
  },
  { $sort: { faturamento_total: -1 } }
]);
```

---

## Parte 4: Desconstrução de Arrays (`$unwind`) e Junções Externas (`$lookup`)

### 4.1 O Estágio `$unwind`
Em bancos orientados a documentos, entidades `1:N` são frequentemente modeladas como listas embutidas de subdocumentos (como a lista `itens` em cada documento de `pedido`). 

O operador `$unwind` "desmembra" essa lista: se um documento possuir um array com 3 itens, o estágio produzirá **3 documentos distintos**, cada um contendo um elemento individual no lugar do array original.

```javascript
// Desmembrando itens para calcular os produtos com maior faturamento
db.pedidos.aggregate([
  { $match: { status: "entregue" } },
  { $unwind: "$itens" },
  {
    $group: {
      _id: "$itens.sku",
      produto: { $first: "$itens.nome" },
      categoria: { $first: "$itens.categoria" },
      total_unidades: { $sum: "$itens.quantidade" },
      receita_gerada: { $sum: "$itens.subtotal" }
    }
  },
  { $sort: { receita_gerada: -1 } },
  { $limit: 5 }
]);
```

> **Atenção:** Caso um documento contenha o campo nulo ou uma lista vazia `[]`, ele será descartado por padrão. Para manter pedidos sem itens no fluxo, utilize a diretiva `{ $unwind: { path: "$itens", preserveNullAndEmptyArrays: true } }`.

---

### 4.2 O Estágio `$lookup` (*Left Outer Join*)
O `$lookup` possibilita conectar duas coleções distintas da mesma base de dados. Os documentos correspondentes são anexados como um array de subdocumentos.

```javascript
// Cruzando dados de produtos com a colecao de avaliacoes
db.produtos.aggregate([
  {
    $lookup: {
      from: "avaliacoes",
      localField: "_id",
      foreignField: "produto_id",
      as: "avaliacoes_recebidas"
    }
  },
  {
    $project: {
      sku: 1,
      nome: 1,
      preco: 1,
      total_avaliacoes: { $size: "$avaliacoes_recebidas" },
      nota_media: {
        $cond: [
          { $gt: [{ $size: "$avaliacoes_recebidas" }, 0] },
          { $round: [{ $avg: "$avaliacoes_recebidas.nota" }, 1] },
          0.0
        ]
      }
    }
  },
  { $sort: { nota_media: -1 } },
  { $limit: 5 }
]);
```

---

## Parte 5: Dashboards Multi-Perspectiva (`$facet`), Otimização e Benchmark

### 5.1 O Estágio `$facet`
O estágio `$facet` resolve a necessidade de dashboards executivos onde a interface do usuário precisa exibir múltiplos painéis e gráficos simultaneamente (ex.: cartões de KPI, gráfico por método de pagamento e ranking regional). Em vez de disparar 3 ou mais requisições separadas ao banco, o `$facet` processa múltiplos sub-pipelines sobre o mesmo fluxo de entrada em uma única viagem de rede (*Single Round-Trip*).

```javascript
db.pedidos.aggregate([
  { $match: { status: "entregue" } },
  {
    $facet: {
      "resumo_kpis": [
        {
          $group: {
            _id: null,
            faturamento: { $sum: "$valor_total" },
            lucro: { $sum: "$lucro_bruto" },
            pedidos: { $sum: 1 }
          }
        }
      ],
      "pagamento": [
        {
          $group: {
            _id: "$forma_pagamento",
            total: { $sum: "$valor_total" }
          }
        },
        { $sort: { total: -1 } }
      ]
    }
  }
]);
```

---

### 5.2 Limite de 100 MB de RAM e a Diretiva `allowDiskUse`
Cada estágio do pipeline de agregação está sujeito a um limite rígido de **100 MB de memória RAM**. Caso uma operação de agrupamento (`$group`) ou ordenação não indexada (`$sort`) sobre uma coleção volumosa atinja esse limiar, o MongoDB cancela a operação emitindo uma exceção:

```
QueryExceededMemoryLimitNoDiskUseAllowed: Sort exceeded memory limit of 104857600 bytes
```

* **Mitigação 1 (Arquitetural):** Filtrar documentos com `$match` no início e utilizar índices $B\text{-Tree}$.
* **Mitigação 2 (Cargas Batch / Relatórios Noturnos):** Permitir transbordamento para o disco passando o modificador:
  `db.pedidos.aggregate(pipeline, { allowDiskUse: true })`

---

### 5.3 Análise Comparativa do Benchmark
A execução do script `benchmark_aggregation_opt.py` sobre 10.000 pedidos confirma na prática o impacto da otimização:
1. **Pipeline Não-Otimizado:** Realiza `$unwind` no início, expandindo o fluxo para mais de 25.000 documentos em memória antes de filtrar, resultando em latência elevada (~140 ms).
2. **Pipeline Otimizado:** Aplica `$match` precoce na chave indexada `{ status: 1, data_pedido: 1 }`, reduzindo o volume de trabalho inicial para ~7.500 documentos e atingindo tempos de resposta inferiores a 15 ms (*Speedup* $> 9\times$).
