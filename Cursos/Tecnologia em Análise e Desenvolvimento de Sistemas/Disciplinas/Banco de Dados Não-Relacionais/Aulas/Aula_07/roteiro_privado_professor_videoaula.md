# 🔒 Roteiro do Professor: Aula 07 — CRUD Avançado, Atualizações Atômicas e Indexação de Alta Performance no MongoDB

* **Curso:** Tecnologia em Análise e Desenvolvimento de Sistemas (ADS) — IFCE Campus Tauá
* **Disciplina:** Banco de Dados Não-Relacionais (ADS16)
* **Docente:** Prof. Me. Reginaldo Fernandes
* **Data Prevista:** 03 de Novembro de 2026
* **Arquivos de Apoio:** `materiais/main.pdf` (apresentação de 28 slides), `tutorial_construcao_passo_a_passo.md`, pasta `codigo/`.

---

## 🧭 Visão Geral e Estratégia Pedagógica

Esta aula representa o ponto de virada da Unidade I: os discentes já sabem como criar coleções e modelar documentos (Aula 06); agora precisam aprender como fazer o banco suportar **concorrência real, escala e latência submilisegundo**. 

A metodologia combina:
1. **O Choque da Realidade:** Demonstrar ao vivo uma consulta com $N = 50.000$ documentos travando o Compass/Terminal em `COLLSCAN` (50 a 150 ms) e o salto para $\le 1$ ms após criar o índice $B\text{-Tree}$.
2. **A Desmistificação Matemática:** Explicar por que a árvore balanceada reduz $50.000$ leituras em disco para apenas $2$ ou $3$ acessos a nós.
3. **Poder Expressivo:** Ensinar operadores que a maioria dos desenvolvedores júnior desconhece (`$elemMatch`, `$expr`, `arrayFilters`).

---

## ⏱️ Bloco a Bloco: Condução da Aula (120 Minutos)

### Bloco 1: O Problema da Escala e a Teoria da $B\text{-Tree}$ (00 a 25 min)
* **Abertura (5 min):** Retomar o e-commerce *ShopGrids*. Fazer a pergunta provocadora: *"O que acontece quando o catálogo pula de 50 produtos para 500.000 e 10.000 clientes buscam produtos simultaneamente na Black Friday?"*
* **O Gargalo `COLLSCAN` (10 min):**
  - Mostrar que sem índice o banco é forçado a ler todos os $N$ documentos do disco/memória.
  - Complexidade assintótica linear $\mathcal{O}(N)$ ($N$ = Tamanho da Coleção).
* **A Estrutura $B\text{-Tree}$ no Motor WiredTiger (10 min):**
  - Explicar a árvore balanceada: chaves ordenadas, nós internos (*pointers*) e folhas (*leaf nodes*).
  - Demonstrar a redução para $\mathcal{O}(\log_{b} N)$, onde $b$ é o Fator de Ramificação (*Fan-out*).
  - **Cálculo pareado no quadro:** Para $N = 100.000$ e $b = 100$:
    $$h \approx \lceil \log_{100}(100.000) \rceil = \lceil 2.5 \rceil = 3 \text{ acessos!}$$
  - Enfatizar a economia de $99.997\%$ de esforço computacional.

---

### Bloco 2: CRUD Avançado — Filtros Complexos e Atualizações Atômicas (25 a 50 min)
* **Armadilha Clássica 1 — O Falso Positivo em Arrays:**
  - Mostrar no projetor:
    ```javascript
    db.pedidos.find({ "itens.preco": { $gt: 100 }, "itens.qtd": { $gte: 2 } })
    ```
  - Perguntar: *"Esse filtro garante que um mesmo item custe > 100 e tenha qtd >= 2?"*
  - Deixar a turma responder e revelar: **NÃO!** Se o item A custar 150 (qtd 1) e o item B custar 20 (qtd 5), o documento bate!
  - Apresentar a solução mandatória: **`$elemMatch`**.
* **Operador `$expr` (5 min):**
  - Mostrar a necessidade de comparar dois campos do mesmo documento sem agregação completa:
    ```javascript
    // Produtos em que o estoque atual está abaixo do estoque de segurança
    db.produtos.find({ $expr: { $lt: ["$estoque.atual", "$estoque.minimo"] } })
    ```
* **Operações Atômicas e Concorrência (10 min):**
  - Diferenciar `$set` de `$inc`: por que nunca ler o valor, somar no Python e regravar com `$set` (evitar *Race Condition*).
  - Arrays: `$push`, `$addToSet` (sem duplicatas) e o modificador `$slice: -5` para manter o histórico podado (garantindo o *Subset Pattern*).
* **O Poder dos `arrayFilters` (10 min):**
  - Demonstrar como atualizar apenas um subdocumento específico de um array:
    ```javascript
    db.pedidos.updateOne(
      { codigo_pedido: "PED-2026-001" },
      { $set: { "itens.$[item].status": "SEPARADO" } },
      { arrayFilters: [ { "item.sku": "PROD-102" } ] }
    )
    ```

---

### Bloco 3: Tipos de Índices e a Regra de Ouro ESR (50 a 80 min)
* **Gerenciando Índices no MongoSH e Compass (5 min):**
  - `createIndex`, `getIndexes`, `dropIndex`.
  - Direção: para índices simples, `{ preco: 1 }` e `{ preco: -1 }` são idênticos em custo de travessia.
* **Índices Compostos e a Regra ESR (15 min):**
  - Ensinar o mnemônico **ESR**:
    1. **E — Equality (Igualdade):** Campos de filtro exato (`status: "ATIVO"`, `categoria: "Livros"`).
    2. **S — Sort (Ordenação):** Campos usados no `$sort` (`data_criacao: -1`).
    3. **R — Range (Faixa):** Campos com operadores de desigualdade (`preco: { $gte: 100 }`, `$in`).
  - **Por que a ordem importa?**
    - Se colocarmos o *Range* antes do *Sort*, o motor faz varredura em faixa e os nós subsequentes não estarão em ordem contígua, forçando o banco a alocar um buffer em memória e executar um **`SORT` em RAM**.
    - Se o resultado do `SORT` ultrapassar **100 MB**, a consulta aborta com erro fatal: `Sort exceeded memory limit`.
* **Índices Parciais e Esparsos (10 min):**
  - Como economizar memória RAM indexando apenas documentos relevantes:
    ```javascript
    db.pedidos.createIndex(
      { cliente_id: 1, data_criacao: -1 },
      { partialFilterExpression: { status: "PENDENTE" } }
    )
    ```

---

### Bloco 4: Índices Multikey e Busca Textual Ponderada (80 a 95 min)
* **Índices Multikey em Arrays (5 min):**
  - Explicar como o WiredTiger cria uma entrada no índice para cada elemento do array.
  - **Regra de Restrição Crítica:** O MongoDB proíbe índices compostos onde dois ou mais campos sejam arrays (`cannot index parallel arrays`). Explicar a razão da explosão combinatória cartesiana.
* **Busca Textual (*Full-Text Search*) (10 min):**
  - Diferença entre `$regex` (lento, varre texto caractere por caractere) e `Text Index` (rápido, baseado em dicionário invertido).
  - Criar índice textual com pesos:
    ```javascript
    db.produtos.createIndex(
      { titulo: "text", descricao: "text", "tags": "text" },
      { weights: { titulo: 10, descricao: 2, tags: 5 }, default_language: "portuguese" }
    )
    ```
  - Executar busca e projetar o escore de relevância:
    ```javascript
    db.produtos.find(
      { $text: { $search: "teclado mecânico ergonômico" } },
      { score: { $meta: "textScore" } }
    ).sort({ score: { $meta: "textScore" } })
    ```

---

### Bloco 5: Diagnóstico com `explain()` e Benchmark Visual (95 a 120 min)
* **Decifrando o `explain("executionStats")` (10 min):**
  - Mostrar os campos cruciais no JSON retornado:
    - `stage`: `COLLSCAN` (perigo) vs `IXSCAN` (ótimo).
    - `totalDocsExamined` vs `nReturned`.
    - `executionTimeMillis`.
* **O Santo Graal: *Covered Queries* (5 min):**
  - Demonstrar que quando todos os campos requisitados na projeção estão no próprio índice (e excluindo `_id: 0`), o MongoDB elimina o estágio `FETCH` (`totalDocsExamined: 0`).
* **Demonstração Prática do Benchmark em Python (10 min):**
  - Executar ao vivo `python3 benchmark_indexacao_explain.py`.
  - Exibir o gráfico de barras comparativo (`benchmark_performance_indices.png`).
  - Mostrar a queda do tempo de ~120 ms para ~0.4 ms e fechamento da aula com os exercícios.

---

## ⚠️ Armadilhas Comuns e Como Evitá-las em Aula

1. **Armadilha do `$elemMatch`:**
   Muitos alunos escrevem `db.pedidos.find({ "itens.preco": { $gt: 100 }, "itens.qtd": { $gte: 2 } })` e juram que está certo. Mostre um documento propositalmente disfuncional no Compass onde o preço 150 tem quantidade 1 e um item de preço 10 tem quantidade 5. O documento é retornado! Isso fixa o conceito de que o `$elemMatch` é obrigatório para casamento no mesmo subdocumento.
2. **Armadilha do Array Duplo em Índices Multikey:**
   Se um aluno tentar executar `db.produtos.createIndex({ tags: 1, cores: 1 })` e ambos os campos contiverem listas, o MongoDB retornará erro `cannot index parallel arrays`. Explique que se um produto tem 10 tags e 10 cores, o MongoDB precisaria gerar 100 entradas no índice para um único documento.
3. **Armadilha do `_id` na Covered Query:**
   Ao tentar fazer uma consulta coberta em `{ sku: 1, preco: 1 }`:
   `db.produtos.find({ sku: "A1" }, { preco: 1 })`
   O aluno verá no `explain` que `totalDocsExamined` ainda é 1! Por quê? Porque o MongoDB tenta retornar o campo `_id` por padrão, forçando o estágio `FETCH`. Para cobrir 100%, é obrigatório projetar `{ preco: 1, _id: 0 }`.
4. **Armadilha de quebrar a Regra ESR:**
   Colocar `{ status: 1, preco: 1, data_criacao: -1 }` para uma busca com faixa em preço e ordenação por data. O MongoDB usará o índice para o filtro, mas fará `SORT` em memória para ordenar por data. Mostre a diferença no `explain` entre ter o estágio `SORT` vs não tê-lo.
