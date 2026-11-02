# Plano de Aula: 07 - CRUD Avançado, Atualizações Atômicas e Indexação de Alta Performance no MongoDB

* **Curso:** Tecnologia em Análise e Desenvolvimento de Sistemas (ADS)  
* **Componente Curricular:** Banco de Dados Não-Relacionais (ADS16)  
* **Docente Responsável:** Prof. Me. Reginaldo Fernandes  
* **Semestre Letivo:** 2026.2  
* **Carga Horária:** 2 h/a (120 minutos)  
* **Data da Aula:** 03 de Novembro de 2026 (Terça-feira)  
* **Módulo:** Unidade I (N1) — O Modelo Orientado a Documentos (MongoDB)  

---

## 🧭 1. Princípios e Diretrizes Pedagógicas da Aula

1. **Contextualização Prática e o Problema da Escala (Gargalo de I/O):**
   Na Aula 06, estruturamos os esquemas BSON do e-commerce *ShopGrids*. Contudo, à medida que a loja cresce de algumas centenas de registros para dezenas de milhares de produtos e pedidos, consultas sem indexação provocam varreduras completas da coleção (**`COLLSCAN` — *Collection Scan***), com complexidade assintótica $\mathcal{O}(N)$ ($N$ representando o Tamanho da Coleção). Isso eleva o consumo de CPU a 100%, esgota a memória do cache do motor WiredTiger e bloqueia operações concorrentes.
2. **Método Teórico Clássico e Estruturas em Árvore Balanceada ($B\text{-Tree}$):**
   Apresentação formal da estrutura de dados em árvore balanceada ($B\text{-Tree}$) utilizada pelo MongoDB/WiredTiger. Análise da redução assintótica de $\mathcal{O}(N)$ para $\mathcal{O}(\log N)$, onde $h \approx \lceil \log_{b}(N) \rceil$ representa a Altura da Árvore e $b$ denota o Fator de Ramificação (*Fan-out* do nó). Formulação matemática da **Regra de Ouro ESR** (*Equality, Sort, Range*) e sua prova lógica na árvore composta.
3. **Abordagem Computacional e Operações Avançadas:**
   Domínio de filtros complexos com operadores de arrays e documentos (`$elemMatch`, `$expr`, `$all`, `$size`), atualizações atômicas pontuais sem reescrita de documentos (`$inc`, `$mul`, `$min`, `$max`, `$push`, `$addToSet`, `$slice`) e modificações seletivas em listas com `arrayFilters`. Criação e gerenciamento de índices simples, compostos, multikey e textuais via **MongoDB Compass**, **`mongosh`** e **Python (`PyMongo`)**.
4. **Tomada de Decisão Visual e Diagnóstico com `explain()`:**
   Uso da ferramenta diagnóstica `explain("executionStats")` para quantificar as métricas de performance: `totalDocsExamined` (Total de Documentos Examinados), `totalKeysExamined` (Total de Chaves de Índice Inspecionadas), `nReturned` (Número de Documentos Retornados), `executionTimeMillis` (Tempo de Execução em Milissegundos) e verificação do estágio ideal **`Covered Query`** (*Consulta Coberta* com `docsExamined: 0`). Apresentação de gráficos comparativos claros de latência e consumo de I/O gerados em laboratório.

---

## 🎯 2. Objetivos de Aprendizagem

### Objetivo Geral
Capacitar os estudantes a diagnosticar gargalos de busca em coleções volumosas do MongoDB, projetar e implementar estratégias avançadas de indexação ($B\text{-Tree}$, ESR, Multikey e Textual) e manipular documentos complexos com filtros avançados e operadores de atualização atômica no **MongoDB Compass**, no terminal **`mongosh`** e em aplicações **Python (`PyMongo`)**.

### Objetivos Específicos
1. **Filtros e Operadores Avançados:** Diferenciar o comportamento de busca em arrays e subdocumentos, dominando o operador `$elemMatch` para evitar falsos positivos, e utilizando `$expr` para comparar dois campos do mesmo documento.
2. **Operadores de Modificação Atômica:** Executar atualizações atômicas e concorrentes com `$inc`, `$mul`, manipular listas com `$push`, `$addToSet` e `$slice` (mantendo arrays limitados), e aplicar o operador posicional complexo `$[<identificador>]` com `arrayFilters`.
3. **Teoria de Indexação e Estruturas $B\text{-Tree}$:** Compreender o funcionamento interno do motor WiredTiger, a organização dos blocos ordenados na memória e o cálculo do ganho assintótico de $\mathcal{O}(N)$ para $\mathcal{O}(\log N)$.
4. **Índices Compostos e a Regra ESR:** Aplicar rigorosamente a ordenação dos campos em índices compostos: primeiro Igualdade (*Equality*), segundo Ordenação (*Sort*) e terceiro Faixa (*Range*), prevenindo estouro do buffer de memória no sort (`Sort exceeded memory limit`).
5. **Índices Multikey e Índices Textuais:** Indexar arrays (respeitando a restrição de no máximo um array por índice composto) e criar índices textuais com pesos ponderados (*weights*), executando buscas com radical de palavras (*stemming*) e ordenação pelo escore de relevância (`$meta: "textScore"`).
6. **Planos de Execução (`explain`):** Interpretar árvores de estágios de execução (`COLLSCAN`, `IXSCAN`, `FETCH`, `SORT`), identificar índices ineficientes e construir consultas 100% cobertas (*Covered Queries*).

---

## ⏱️ 3. Cronograma Recomendado da Aula (120 Minutos)

| Bloco | Duração | Descrição das Atividades | Metodologia & Recursos |
| :---: | :---: | :--- | :--- |
| **1. Gargalos & Teoria** | 00 – 25 min | **O Problema da Escala e a Teoria da $B\text{-Tree}$:** O custo do `COLLSCAN` sob concorrência maciça; estrutura da árvore $B\text{-Tree}$ no WiredTiger; complexidade assintótica $\mathcal{O}(N)$ vs $\mathcal{O}(\log N)$; exemplo matemático pareado de acessos em disco. | Exposição dialogada com slides Beamer. |
| **2. CRUD Avançado** | 25 – 50 min | **Filtros Complexos e Atualizações Atômicas:** `$elemMatch` em itens de pedidos; expressões com `$expr`; atômicos `$inc`, `$push`, `$addToSet`, `$slice` e `arrayFilters` no **Compass** e **`mongosh`**. | Demonstração guiada na interface gráfica e shell. |
| **3. Índices & Regra ESR** | 50 – 80 min | **Construção de Índices e Regra de Ouro ESR:** Índices Simples, Compostos e Multikey; a prova lógica da sequência *Equality*, *Sort* e *Range*; índices parciais e esparsos para economia de RAM. | Resolução pareada e prática com PyMongo. |
| **4. Busca Textual** | 80 – 95 min | **Índices Textuais e Relevância:** *Full-Text Search* em múltiplos campos com pesos diferenciados (*weights*); operador `$text`, tokenização, *stopwords* e ordenação por relevância (`textScore`). | Prática interativa no catálogo de produtos. |
| **5. Diagnóstico & Lab** | 95 – 120 min | **Diagnóstico com `explain()` e Benchmark:** Análise das métricas `executionStats`, identificação de gargalos `FETCH` e construção de *Covered Queries*; execução de benchmark visual com 50.000 documentos. | Laboratório prático e visualização gráfica. |

---

## 📊 4. Roteiro de Slides Sugeridos (Apresentação Beamer)

* **Slides 1–2:** Capa Institucional (IFCE Campus Tauá, ADS16) e Agenda do Encontro.
* **Slides 3–7 (Seção 1 — Contextualização Prática e Teoria da $B\text{-Tree}$):**
  - O gargalo de leitura no *ShopGrids*: o colapso de um `COLLSCAN` com $N = 50.000$ registros.
  - Estrutura interna da árvore $B\text{-Tree}$ no motor WiredTiger.
  - Exemplo analítico pareado: cálculo do número de saltos em $\mathcal{O}(N)$ vs $\mathcal{O}(\log_{b} N)$ com Fator de Ramificação $b = 100$.
  - Comparação imediata com a medição de tempo no Python (`PyMongo`).
* **Slides 8–13 (Seção 2 — CRUD Avançado: Filtros Complexos e Atualizações Atômicas):**
  - O operador `$elemMatch`: resolvendo o erro clássico de falso positivo em arrays de subdocumentos.
  - Operador `$expr`: comparando campos internos do mesmo documento (ex: estoque atual vs estoque mínimo).
  - Modificadores atômicos numéricos: `$inc`, `$mul`, `$min` e `$max`.
  - Modificadores atômicos de array: `$push`, `$addToSet`, `$slice` (manutenção do *Subset Pattern*).
  - Atualização seletiva com `arrayFilters` e o identificador `$[<elem>]`.
* **Slides 14–19 (Seção 3 — Tipos de Índices e a Regra de Ouro ESR):**
  - O que é um índice no MongoDB e como gerenciar (`createIndex`, `dropIndex`, `getIndexes`).
  - Índices Simples: direção ascendente (`1`) e descendente (`-1`).
  - Índices Compostos e a Regra **ESR** (*Equality, Sort, Range*).
  - Análise gráfica do porquê o *Sort* deve vir antes do *Range*.
  - Índices Parciais (`partialFilterExpression`) e Índices Esparsos (`sparse`): otimização de RAM.
* **Slides 20–23 (Seção 4 — Índices Multikey e Busca Textual Ponderada):**
  - Índices Multikey: indexando arrays de categorias/tags e a regra do array único.
  - Índices Textuais (*Full-Text Search*): tokenização, eliminação de *stopwords* e radicalização (*stemming*).
  - Criação de índice textual com pesos (`weights`) no título e na descrição.
  - Consulta com `$text`, `$search` e ordenação por relevância métrica (`$meta: "textScore"`).
* **Slides 24–28 (Seção 5 — Diagnóstico com `explain()`, Covered Queries e Conclusão):**
  - Os três níveis do comando `explain`: `queryPlanner`, `executionStats` e `allPlansExecution`.
  - Estágios de execução fundamentais: `COLLSCAN`, `IXSCAN`, `FETCH` e `SORT`.
  - Métrica de Eficiência: Razão $\frac{\text{totalDocsExamined}}{\text{nReturned}}$.
  - *Covered Queries* (Consultas Cobertas): o ápice de performance com `docsExamined: 0`.
  - Apresentação visual do Benchmark (redução de 99.8% do tempo de resposta) e encerramento.

---

## 💻 5. Recursos e Códigos Práticos de Apoio

* [`codigo/povoar_dados_benchmark.py`](codigo/povoar_dados_benchmark.py): Script de carga massiva sintética de 50.000 documentos nas coleções `produtos` e `pedidos` utilizando `bulk_write`.
* [`codigo/crud_avancado_operadores.py`](codigo/crud_avancado_operadores.py): Demonstração comentada em Python de filtros com `$elemMatch`, `$expr` e atualizações atômicas com `arrayFilters`.
* [`codigo/indices_textuais_busca.py`](codigo/indices_textuais_busca.py): Criação de índices de texto com pesos e ranqueamento por escore.
* [`codigo/benchmark_indexacao_explain.py`](codigo/benchmark_indexacao_explain.py): Benchmark com cronometragem real, extração de métricas de `explain()` e geração de gráficos didáticos no padrão visual (`seaborn-v0_8-colorblind`).
* [`codigo/mongosh_aula07_avancado.js`](codigo/mongosh_aula07_avancado.js): Roteiro para execução interativa no terminal shell do MongoDB.
* [`codigo/demonstracao_aula07.ipynb`](codigo/demonstracao_aula07.ipynb): Notebook Jupyter interativo com explicações teóricas e práticas pareadas.

---

## 📝 6. Exercícios de Fixação

1. **Complexidade Assintótica e Estrutura da $B\text{-Tree}$:**
   Considere uma coleção de produtos no MongoDB com $N = 100.000$ documentos.
   a) Explique o que acontece a nível de hardware (CPU e I/O de disco) quando uma consulta por código SKU é executada sem índice. Qual é a complexidade assintótica $\mathcal{O}$ desse processo?
   b) Se for criado um índice $B\text{-Tree}$ sobre o campo `sku` com Fator de Ramificação médio de $b = 100$ chaves por nó, qual é o número teórico máximo de nós inspecionados para encontrar qualquer produto? Calcule o valor passo a passo.

2. **Filtros em Arrays e o Operador `$elemMatch`:**
   Dada a coleção `pedidos` com documentos contendo o array `itens: [{ sku: "A1", preco: 80, qtd: 1 }, { sku: "B2", preco: 25, qtd: 5 }]`:
   a) Explique por que a consulta `db.pedidos.find({ "itens.preco": { $gt: 50 }, "itens.qtd": { $gte: 3 } })` retorna o pedido acima, embora nenhum item satisfaça ambos os critérios simultaneamente.
   b) Reescreva a consulta utilizando o operador `$elemMatch` para corrigir a lógica e garantir que a condição seja avaliada no mesmo item do pedido.

3. **A Regra ESR (*Equality, Sort, Range*):**
   Uma consulta muito frequente na API do e-commerce realiza a seguinte operação:
   `db.produtos.find({ status: "ATIVO", preco: { $gte: 100, $lte: 500 } }).sort({ data_cadastro: -1 })`
   a) Com base na regra ESR, qual é a ordem exata dos campos na criação do índice composto ideal?
   b) O que ocorre com o plano de execução (`explain`) se invertermos e criarmos o índice na ordem `{ status: 1, preco: 1, data_cadastro: -1 }`? Explique a diferença entre usar o índice para ordenação vs realizar `SORT` em memória.

4. **Atualizações Atômicas e `arrayFilters`:**
   Um cliente do e-commerce comprou 2 unidades do produto cujo código de item é `"PROD-102"`, pertencente ao pedido de identificador `1590`. Ao mesmo tempo, o status desse item individual deve mudar de `"PENDENTE"` para `"SEPARADO"`.
   Escreva o comando `updateOne` (no `mongosh` ou Python) utilizando o operador posicional complexo `$[<elem>]` com `arrayFilters` e modificadores atômicos para realizar essa alteração sem alterar os outros itens do array.

5. **Covered Queries (Consultas Cobertas) e Índices Textuais:**
   a) O que caracteriza uma *Covered Query* e por que ela atinge a máxima performance possível no MongoDB? Quais condições são exigidas no filtro e na projeção?
   b) Crie um comando para gerar um índice textual sobre os campos `titulo` (com peso 10) e `descricao` (com peso 2) na coleção `produtos`, e escreva a consulta para buscar a palavra `"ergonômico"` ordenando os resultados pelos mais relevantes.
