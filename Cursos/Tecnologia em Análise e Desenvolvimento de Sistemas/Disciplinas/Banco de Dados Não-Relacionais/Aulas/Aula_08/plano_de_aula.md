# Plano de Aula: 08 - MongoDB Aggregation Framework: Pipelines Analíticos, Acumuladores e Business Intelligence

* **Curso:** Tecnologia em Análise e Desenvolvimento de Sistemas (ADS)  
* **Componente Curricular:** Banco de Dados Não-Relacionais (ADS16)  
* **Docente Responsável:** Prof. Me. Reginaldo Fernandes  
* **Semestre Letivo:** 2026.2  
* **Carga Horária:** 2 h/a (120 minutos)  
* **Data da Aula:** 10 de Novembro de 2026 (Terça-feira)  
* **Módulo:** Unidade II (N1) — Framework de Agregação e Relatórios de Inteligência de Negócio no MongoDB  

---

## 🧭 1. Contextualização Prática e Metodologia da Aula

1. **Contextualização Prática e o Problema da Análise em Alta Escala:**  
   Nas Aulas 06 e 07, modelamos e indexamos a base de dados transacional do e-commerce *ShopGrids*. No entanto, à medida que a diretoria de operações necessita de relatórios consolidados — faturamento mensal consolidado, ticket médio de vendas, top produtos mais rentáveis, margem bruta por categoria e comportamento de recompra —, operações puras de CRUD (`find`) mostram-se insuficientes. Recuperar milhões de documentos inteiros para processar cálculos analíticos na aplicação satura a banda de rede, estoura a memória RAM dos microsserviços e gera concorrência destrutiva no banco. A solução arquitetural consiste em transferir o processamento diretamente para o motor de banco de dados por meio do **MongoDB Aggregation Framework**.
2. **Método Teórico Clássico e Álgebra de Fluxo de Dados (*Dataflow*):**  
   Comparação formal entre o modelo relacional declarativo em SQL (`SELECT`, `WHERE`, `GROUP BY`, `HAVING`, `JOIN`) e o paradigma de processamento funcional em fluxo sequencial (*Dataflow Pipeline*). Demonstração analítica da equivalência entre operadores acumuladores e as funções estatísticas: média amostral ($\bar{X} = \frac{1}{N}\sum x_i$), somatório ($\sum$), extremos ($\min, \max$) e contagem ($N$). Análise matemática do custo de desconstrução de arrays (`$unwind`), demonstrando o crescimento de cardinalidade de $N$ pedidos para $\sum_{i=1}^{N} k_i$ itens processados.
3. **Abordagem Computacional e Construção de Pipelines:**  
   Implementação progressiva de pipelines no **MongoDB Compass (Aggregation Pipeline Builder)**, no shell interativo **`mongosh`** e em aplicações **Python (`PyMongo`)**. Domínio dos estágios fundamentais: `$match`, `$project`, `$addFields`, `$sort`, `$limit`, `$skip`, `$group`, `$unwind`, `$lookup` e `$facet`.
4. **Tomada de Decisão Visual e Métricas de Performance:**  
   Inspeção das métricas analíticas e planos de execução com `explain("executionStats")`. Análise das restrições de arquitetura: limite estrito de 100 MB de RAM por estágio, uso da diretiva `allowDiskUse` para cargas em lote e regras de otimização automática (*Pipeline Sequence Optimization* e *Early Filtering* com `$match` posicionado no início para uso de índices $B\text{-Tree}$). Apresentação do gráfico comparativo de latência e consumo de memória gerado pelo benchmark em laboratório.

---

## 🎯 2. Objetivos de Aprendizagem

### Objetivo Geral
Capacitar os estudantes a projetar, otimizar e implementar pipelines de agregação analítica no MongoDB utilizando **MongoDB Compass**, **`mongosh`** e **Python (`PyMongo`)**, transformando coleções volumosas e desnormalizadas em relatórios consolidados de inteligência de negócio (*Business Intelligence*).

### Objetivos Específicos
1. **Compreender o Paradigma de Pipeline:** Assimilar a arquitetura de fluxo de dados onde cada estágio recebe um fluxo de documentos BSON, aplica transformações ou filtros e entrega uma saída imutável para o estágio subsequente.
2. **Mapear Consultas SQL para Estágios de Agregação:** Estabelecer a correspondência exata entre comandos SQL (`WHERE`, `GROUP BY`, `HAVING`, `ORDER BY`, `LIMIT`, `JOIN`) e os estágios equivalentes do MongoDB (`$match`, `$group`, `$sort`, `$limit`, `$lookup`).
3. **Dominar Acumuladores e Agrupamentos Complexos:** Implementar agrupamentos por chaves simples e compostas com `$group`, calculando somatórios (`$sum`), médias aritméticas (`$avg`), extremos (`$min`, `$max`) e gerando coleções agregadas com `$push` e `$addToSet`.
4. **Desconstruir Arrays com `$unwind`:** Tratar coleções com listas aninhadas, desmembrando itens de pedidos para calcular faturamento por SKU e categoria, controlando a preservação de arrays vazios com `preserveNullAndEmptyArrays`.
5. **Realizar Junções Externas com `$lookup`:** Cruzar documentos de coleções distintas (*Left Outer Join*) de forma eficiente, reconhecendo a importância de índices na coleção estrangeira para evitar degradação de I/O.
6. **Construir Dashboards com `$facet` e Otimizar Desempenho:** Executar múltiplos fluxos analíticos em paralelo em uma única requisição com `$facet`, respeitar o limite de 100 MB de memória RAM e posicionar filtros `$match` no início do pipeline para aproveitamento da árvore $B\text{-Tree}$.

---

## ⏱️ 3. Cronograma Recomendado da Aula (120 Minutos)

| Bloco | Duração | Descrição das Atividades | Recursos & Metodologia |
| :---: | :---: | :--- | :--- |
| **1. Fundamentos e Comparação** | 00 – 25 min | **Do SQL ao Pipeline de Agregação:** Gargalos de processamento analítico no cliente; arquitetura *Dataflow*; equivalência estrutural com o SQL tradicional; o pipeline visual no MongoDB Compass. | Exposição dialogada com slides Beamer e demonstração no Compass. |
| **2. Filtragem e Projeção** | 25 – 45 min | **Estágios Fundamentais (`$match`, `$project`, `$addFields`, `$sort`):** Filtragem precoce orientada por índices; enriquecimento com novos campos calculados; ordenação e paginação analítica. | Demonstração guiada no shell `mongosh`. |
| **3. Agrupamento e Acumuladores** | 45 – 70 min | **O Poder do `$group` e Cálculos Analíticos:** Agrupamento por períodos temporais (`$year`, `$month`); acumuladores `$sum`, `$avg`, `$push` e `$addToSet`; relatório de faturamento e ticket médio. | Resolução pareada e prática com PyMongo. |
| **4. Desconstrução e Junção** | 70 – 95 min | **Manipulação de Coleções Complexas (`$unwind` e `$lookup`):** Desconstrução de subdocumentos em arrays; cruzamento multicoleção entre pedidos, catálogo de produtos, clientes e avaliações (*Left Outer Join*); análise de cardinalidade e índices estrangeiros. | Laboratório assistido e exercícios práticos. |
| **5. Otimização e Laboratório** | 95 – 120 min | **Estágios Avançados (`$facet`), Limites de RAM e Benchmark:** Relatórios multi-perspectiva para painéis executivos; limite de 100 MB de RAM e `allowDiskUse`; análise de benchmark com gráfico comparativo. | Laboratório prático individual e discussão de resultados. |

---

## 🖥️ 4. Roteiro Slide a Slide Sugerido

* **Slide 1:** Capa da Aula e Apresentação do Módulo (Framework de Agregação no MongoDB).
* **Slide 2:** Sumário e Agenda Executiva da Aula.
* **Slide 3:** Preparação do Ambiente Prático: Atualização da Base no MongoDB com as 4 coleções canônicas (`python3 povoar_dados_aula08.py`).
* **Slide 4:** Além do CRUD: Por que consultas simples com `find()` não atendem às demandas de Business Intelligence.
* **Slide 5:** O Conceito de Aggregation Pipeline: Fluxo contínuo, transformações em memória e imutabilidade dos dados originais.
* **Slide 6:** Equivalência Conceitual entre a Álgebra SQL e os Estágios de Pipeline do MongoDB.
* **Slide 7:** O Estágio `$match`: Filtragem seletiva precoce e o aproveitamento de índices $B\text{-Tree}$.
* **Slide 8:** Os Estágios `$project` e `$addFields`: Seleção de campos, exclusão do `_id` e enriquecimento de documentos.
* **Slide 9:** Ordenação e Paginação Analítica: Uso seguro de `$sort`, `$limit` e `$skip`.
* **Slide 10:** O Estágio `$group`: A chave de agrupamento `_id` (simples e composta) e o prefixo `$` para referência de campos.
* **Slide 11:** Tabela Comparativa de Acumuladores: `$sum`, `$avg`, `$min`, `$max`, `$count`, `$first` e `$last`.
* **Slide 12:** Diferença Estrutural entre `$push` (preservação de histórico) e `$addToSet` (conjunto deduplicado).
* **Slide 13:** Exemplo Pareado: Cálculo manual do faturamento e ticket médio versus pipeline no MongoSH.
* **Slide 14:** O Estágio `$unwind`: Desconstrução de arrays de itens e a atenção à explosão volumétrica em memória.
* **Slide 15:** O Estágio `$lookup`: Junção externa (*Left Outer Join*) entre `pedidos` e catálogo `produtos`.
* **Slide 16:** Junção Externa com `clientes`: Enriquecimento cadastral, localização geográfica e análise de ticket por cliente.
* **Slide 17:** Junção Externa com `avaliacoes`: Cálculo analítico de nota média e contagem de reviews por SKU.
* **Slide 18:** O Estágio `$facet`: Dashboards executivos multi-perspectiva com processamento em passo único.
* **Slide 19:** Otimização Interna do Pipeline: Limite de 100 MB de RAM, `allowDiskUse` e regras de reordenação automática da engine.
* **Slide 20:** Validação Empírica: Gráfico comparativo de latência e consumo de memória entre pipelines otimizados e não-otimizados.
* **Slide 21:** Encerramento e Apresentação dos Desafios Práticos de Laboratório.

---

## 🧪 5. Laboratório Prático e Exercícios de Fixação

Os exercícios devem ser executados no terminal **`mongosh`** ou via **Python (`PyMongo`)** utilizando o banco `ecommerce_shopgrids`:

1. **Exercício 1 (Faturamento e Distribuição por Status de Pedido):**  
   Construa um pipeline sobre a coleção `pedidos` que agrupe pelo campo `status` ('ENTREGUE', 'CANCELADO', 'PENDENTE', etc.). O relatório deve exibir o faturamento total acumulado (`pagamento.total_pago`), o ticket médio e o total de pedidos, ordenados pelo maior faturamento.
2. **Exercício 2 (Top 5 Clientes VIP com Enriquecimento Cadastral):**  
   Filtre pedidos entregues (`status: 'ENTREGUE'`), agrupe por `cliente_id` somando o total pago e, utilizando `$lookup` com a coleção `clientes`, recupere o nome, cidade, estado e segmento dos 5 maiores compradores da loja.
3. **Exercício 3 (Análise de Itens com `$unwind`):**  
   Desconstrua o array de `itens` de pedidos entregues (`status: 'ENTREGUE'`) e agrupe por `itens.sku`. Calcule a quantidade total vendida (`$sum: '$itens.qtd'`) e a receita acumulada (`$multiply: ['$itens.preco', '$itens.qtd']`). Ordene pela quantidade total de peças vendidas de forma decrescente e limite aos 10 primeiros.
4. **Exercício 4 (Cruzamento com `$lookup` e Catálogo de Produtos):**  
   A partir da coleção `pedidos`, filtre os pedidos entregues (`status: 'ENTREGUE'`), aplique `$unwind` em `itens` e realize um `$lookup` com a coleção `produtos` (unindo `itens.sku` com `sku`). Projete o código do pedido (`codigo`), o SKU, o título do produto (`produtos.titulo`), a categoria e a quantidade adquirida.
5. **Exercício 5 (Satisfação de Consumidores com `$lookup` em Avaliações):**  
   A partir da coleção `produtos` (categoria 'Informática' e status 'ATIVO'), execute um `$lookup` com a coleção `avaliacoes` pela chave `sku`. Projete o título, preço, contagem de reviews e nota média calculada, filtrando itens com nota média $\ge 4.5$ e no mínimo 2 avaliações.
6. **Exercício 6 (Dashboard Consolidado com `$facet`):**  
   Elabore um pipeline utilizando `$facet` sobre a coleção `pedidos` filtrando pedidos entregues que calcule simultaneamente:
   - Os KPIs gerais da loja (faturamento total somando `pagamento.total_pago`, ticket médio e total de pedidos entregues).
   - O ranking dos 5 maiores pedidos em valor financeiro (`pagamento.total_pago`), projetando `codigo`, `cliente_id` e o valor pago.
