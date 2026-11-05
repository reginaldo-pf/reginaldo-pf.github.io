# 🔒 Roteiro do Professor: Aula 08 — MongoDB Aggregation Framework e Business Intelligence

* **Curso:** Tecnologia em Análise e Desenvolvimento de Sistemas (ADS) — IFCE Campus Tauá  
* **Componente Curricular:** Banco de Dados Não-Relacionais (ADS16)  
* **Docente Responsável:** Prof. Me. Reginaldo Fernandes  
* **Data Prevista:** 10 de Novembro de 2026 (Terça-feira)  
* **Carga Horária:** 2 h/a (120 minutos)  
* **Materiais de Apoio:** `materiais/main.pdf` (apresentação Beamer 16:9), `tutorial_construcao_passo_a_passo.md`, pasta `codigo/`.

---

## 🧭 Visão Geral e Dinâmica da Aula

Esta aula encerra os conceitos teóricos do 1º Período (N1) referentes ao MongoDB, capacitando os discentes a construir relatórios analíticos de inteligência de negócio sobre coleções com dados aninhados.

A condução da aula apoia-se em três eixos:
1. **Ponte com o Conhecimento Prévio (SQL):** Apoiar-se no domínio prévio que a turma possui de SQL (`GROUP BY`, `SUM`, `AVG`, `JOIN`) para mapear intuitivamente cada conceito para o paradigma de pipeline de documentos.
2. **Construção Visual Primeiro (Compass):** Utilizar a aba **Aggregations** do MongoDB Compass para montar os estágios interativamente, permitindo que os alunos vejam a transformação dos dados a cada bloco inserido antes de codificar em Python.
3. **Consciência de Engenharia e Limites Físicos:** Enfatizar as restrições reais de servidores de produção (o teto de 100 MB de RAM por estágio e o impacto de posicionar `$match` antes ou depois de `$unwind`).

---

## ⏱️ Bloco a Bloco: Condução da Aula (120 Minutos)

### Bloco 1: Do SQL ao Pipeline de Agregação (00 a 25 min)
* **Abertura Provocativa (5 min):** Perguntar: *"Se o diretor da loja ShopGrids pedir um gráfico do ticket médio de vendas por mês nos últimos 2 anos, como vocês implementariam isso usando apenas o método find()?"*
  - Destacar que baixar 100.000 pedidos em um script Node/Python para calcular a média em um loop estoura a memória do back-end e satura a rede.
* **Apresentação do Conceito de Dataflow (10 min):**
  - Explicar a esteira de montagem: Documentos entram $\to$ sofrem transformações intermediárias $\to$ saem agregados.
  - Ressaltar que a coleção física original permanece intacta (imutabilidade).
* **Mapeamento de Cláusulas SQL $\to$ Estágios Mongo (10 min):**
  - Fazer a correlação direta no quadro:
    - `WHERE` $\implies$ `$match`
    - `GROUP BY` $\implies$ `$group`
    - `SELECT` $\implies$ `$project`
    - `JOIN` $\implies$ `$lookup`
    - `ORDER BY` $\implies$ `$sort`

---

### Bloco 2: Filtragem, Projeção e Ordenação (25 a 45 min)
* **Demonstração do `$match` e Importância da Ordem (10 min):**
  - Mostrar que `$match` na primeira posição usa índice $B\text{-Tree}$ da coleção.
  - Mostrar o que ocorre se colocarmos `$match` após estágios pesados (degradação drástica).
* **Projeção com `$project` e `$addFields` (10 min):**
  - Ensinar quando usar `$project` (remodelagem total de schema) versus `$addFields` (adicionar apenas uma métrica sem perder os outros campos).
  - Lembrar da obrigatoriedade do `_id: 0` para ocultar o identificador nativo.

---

### Bloco 3: Agrupamentos e Acumuladores Analíticos (45 a 70 min)
* **A Chave `_id` no `$group` (10 min):**
  - Demonstrar os três cenários:
    1. `_id: null` para métrica total da loja.
    2. `_id: "$status"` para agregação por campo simples.
    3. `_id: { ano: { $year: "$data_pedido" }, mes: { $month: "$data_pedido" } }` para chave composta temporal.
* **Operadores Acumuladores (15 min):**
  - Praticar `$sum: "$valor_total"` e `$sum: 1` (contagem de ocorrências).
  - Demonstrar a diferença crítica entre `$push` (preserva duplicatas para auditoria de histórico) e `$addToSet` (elimina duplicatas como conjunto matemático).

---

### Bloco 4: Desconstrução de Arrays e Junções Externas (70 a 95 min)
* **O Operador `$unwind` (15 min):**
  - Mostrar visualmente no Compass a expansão de um pedido com 3 itens em 3 documentos independentes.
  - Alertar sobre a explosão volumétrica de dados na memória.
  - Explicar o parâmetro `preserveNullAndEmptyArrays: true` para não perder registros sem itens.
* **O Operador `$lookup` (10 min):**
  - Demonstrar a junção entre a coleção `produtos` e a coleção `avaliacoes`.
  - Ressaltar: o campo de destino (`foreignField`) **precisa impreterivelmente de um índice** para não transformar a junção em um `COLLSCAN` repetido.

---

### Bloco 5: Dashboards, Otimização e Laboratório (95 a 120 min)
* **O Estágio `$facet` (10 min):**
  - Explicar como montar um painel de BI com KPIs e gráficos executando tudo em uma única viagem de rede (*Round-Trip Time* reduzido).
* **Limites de RAM e o Gráfico de Benchmark (15 min):**
  - Explicar o erro de limite de memória de 100 MB (`QueryExceededMemoryLimitNoDiskUseAllowed`) e o modificador `{ allowDiskUse: true }`.
  - Projetar o slide com a imagem `benchmark_aggregation_opt.png` e comparar os tempos medidos em laboratório.

---

## ⚠️ Armadilhas Comuns dos Alunos e Como Destravar

1. **Esquecer o Cifrão (`$`) ao Referenciar Campos:**
   - *Erro típico:* `{ $sum: "valor_total" }` $\to$ O MongoDB tentará somar o texto constante "valor_total", gerando resultado zero.
   - *Correção:* Explicar a regra: para referenciar o valor contido no campo do documento, use sempre `"$valor_total"`.
2. **Esquecer de Usar `$unwind` Antes de Agrupar por Itens:**
   - *Erro típico:* Tentar fazer `{ $group: { _id: "$itens.categoria" } }` esperando categorias únicas e recebendo arrays de categorias agregadas.
   - *Correção:* Demonstrar que arrays exigem `$unwind` prévio para atomizar cada item em um registro.
3. **Ocultar o `_id` no `$project`:**
   - *Erro típico:* Alunos especificam campos e ficam surpresos ao ver o `_id` na saída.
   - *Correção:* Relembrar que o `_id` é o único campo que vem por padrão e precisa ser explicitamente desligado com `_id: 0`.

---

## 🎬 Dicas para Gravação de Videoaula / Demonstração Prática

* **Resolução de Tela:** 1920x1080 (16:9), fonte do terminal e do Compass aumentada em pelo menos 130%.
* **Compass Aggregation Builder:** Utilize o botão de expansão de estágios e mostre a prévia dos documentos em cada etapa da construção.
* **Transições Didáticas:** Ao apresentar o `$group`, abra o MongoDB Compass lado a lado com o terminal `mongosh` e execute a mesma agregação para fixar a correspondência visual e textual.
