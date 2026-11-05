# Aula 08: MongoDB Aggregation Framework — Pipelines Analíticos e Inteligência de Negócio

* **Curso:** Tecnologia em Análise e Desenvolvimento de Sistemas (ADS)  
* **Componente Curricular:** Banco de Dados Não-Relacionais (ADS16)  
* **Docente Responsável:** Prof. Me. Reginaldo Fernandes  
* **Semestre Letivo:** 2026.2  
* **Data da Aula:** 10 de Novembro de 2026 (Terça-feira)  
* **Carga Horária:** 2 h/a (120 minutos)  
* **Módulo:** Unidade II (N1) — Framework de Agregação e Relatórios de Inteligência de Negócio no MongoDB  

---

## 🎯 Competências e Objetivos

- [x] Compreender os fundamentos da **arquitetura funcional em esteira de dados (*Dataflow Pipeline*)** e a equivalência formal com a álgebra relacional SQL (`WHERE`, `GROUP BY`, `HAVING`, `ORDER BY`, `LIMIT`, `JOIN`).
- [x] Dominar os estágios fundamentais de processamento: **`$match`** (filtragem precoce suportada por índices $B\text{-Tree}$), **`$project`** (remodelagem de schema e expressões derivadas) e **`$addFields`** (enriquecimento sem descarte de atributos).
- [x] Construir agrupamentos analíticos com **`$group`** sobre chaves simples e compostas temporais (`$year`, `$month`), aplicando operadores acumuladores: **`$sum`**, **`$avg`**, **`$min`**, **`$max`**, **`$count`**, **`$push`** e **`$addToSet`**.
- [x] Desconstruir listas de subdocumentos embutidos utilizando o estágio **`$unwind`**, controlando a preservação de dados vazios via parâmetro `preserveNullAndEmptyArrays`.
- [x] Implementar junções externas entre coleções distintas utilizando **`$lookup`** (*Left Outer Join*), analisando as restrições de performance e a obrigatoriedade de índices na chave estrangeira (`foreignField`).
- [x] Projetar relatórios multi-perspectiva para painéis executivos com o estágio **`$facet`**, consolidando múltiplos fluxos de métricas em uma única requisição.
- [x] Identificar restrições de infraestrutura (o limite estrito de **100 MB de RAM por estágio**), habilitar o transbordamento temporário para disco com **`allowDiskUse: true`** e validar o ganho empírico de latência por meio de benchmarks gráficos.

---

## 📁 Estrutura de Arquivos da Aula 08

- [`tutorial_construcao_passo_a_passo.md`](tutorial_construcao_passo_a_passo.md): **Guia Passo a Passo Completo** — dividido em 5 partes:
  1. Arquitetura de Fluxo de Dados (*Dataflow*) e Comparação Formal com a Álgebra SQL.
  2. Estágios Fundamentais no MongoDB Compass e MongoSH (`$match`, `$project`, `$addFields`, `$sort`, `$limit`, `$skip`).
  3. Agrupamentos e Acumuladores Analíticos (`$group`, acumuladores estatísticos e conjuntos com `$push`/`$addToSet`).
  4. Desconstrução de Arrays (`$unwind`) e Junções Externas Multicoleção (`$lookup`).
  5. Dashboards Multi-Perspectiva (`$facet`), Limites de RAM, Otimizações da Engine e Benchmark.
- [`plano_de_aula.md`](plano_de_aula.md): Roteiro metodológico detalhado para 120 minutos, objetivos de aprendizagem, cronograma em 5 blocos e exercícios de fixação.
- [`roteiro_privado_professor_videoaula.md`](roteiro_privado_professor_videoaula.md): Roteiro exclusivo do docente com estratégias de condução, armadilhas comuns dos discentes e marcações de tempo.
- [`index.html`](index.html): Portal web interativo da Aula 08, contendo fundamentação teórica, código interativo com abas, diagramas e comparativos de benchmark.
- `codigo/`:
  - [`docker-compose.yml`](codigo/docker-compose.yml): Configuração para subir instâncias locais do MongoDB 8.0 e Mongo Express (GUI web na porta `8081`).
  - [`requirements.txt`](codigo/requirements.txt): Dependências Python (`pymongo`, `matplotlib`, `numpy`, `pandas`).
  - [`povoar_dados_aula08.py`](codigo/povoar_dados_aula08.py): Script de geração e carga sintética de 10.000 pedidos, clientes e catálogo do *ShopGrids*.
  - [`pipelines_analiticos.py`](codigo/pipelines_analiticos.py): Demonstração em Python (`PyMongo`) dos 5 relatórios analíticos de inteligência de negócio.
  - [`benchmark_aggregation_opt.py`](codigo/benchmark_aggregation_opt.py): Medição empírica de latência e alocação de memória gerando o gráfico comparativo `benchmark_aggregation_opt.png`.
  - [`mongosh_aula08_aggregation.js`](codigo/mongosh_aula08_aggregation.js): Script completo com pipelines comentados para execução no terminal `mongosh`.
  - [`demonstracao_aula08.ipynb`](codigo/demonstracao_aula08.ipynb): Caderno interativo Jupyter Notebook para exploração dos dados com Pandas e MongoDB.
  - [`pedidos_amostra_aula08.json`](codigo/pedidos_amostra_aula08.json): Amostra de documentos para testes rápidos na interface gráfica MongoDB Compass.
- `materiais/`:
  - [`main.pdf`](materiais/main.pdf) e módulos LaTeX Beamer 16:9 (`secao1_*.tex` a `secao5_*.tex`) prontos para exibição.
  - [`benchmark_aggregation_opt.png`](materiais/benchmark_aggregation_opt.png): Gráfico de alta resolução demonstrando o ganho de velocidade com otimização.

---

## 🚀 Como Executar o Laboratório Localmente

1. **Subir os Contêineres:**
   ```bash
   cd codigo
   docker compose up -d
   ```
2. **Instalar Dependências no Ambiente Virtual:**
   ```bash
   pip install -r requirements.txt
   ```
3. **Povoar a Base de Dados ShopGrids:**
   ```bash
   python3 povoar_dados_aula08.py
   ```
4. **Executar os Pipelines Analíticos em Python:**
   ```bash
   python3 pipelines_analiticos.py
   ```
5. **Executar o Benchmark de Otimização e Gerar o Gráfico:**
   ```bash
   python3 benchmark_aggregation_opt.py
   ```
6. **Acessar as Ferramentas Gráficas e Linha de Comando:**
   * **MongoDB Compass:** Conectar em `mongodb://localhost:27017` e abrir a aba *Aggregations*.
   * **Mongo Express (Web):** Acessar `http://localhost:8081` no navegador.
   * **Terminal mongosh:** Executar `docker exec -it shopgrids-mongodb-aula08 mongosh`.
