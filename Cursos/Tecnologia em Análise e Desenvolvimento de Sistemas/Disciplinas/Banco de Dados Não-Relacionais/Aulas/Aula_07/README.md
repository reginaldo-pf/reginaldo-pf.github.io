# Aula 07: CRUD Avançado, Atualizações Atômicas e Indexação de Alta Performance no MongoDB

* **Curso:** Tecnologia em Análise e Desenvolvimento de Sistemas (ADS)  
* **Componente Curricular:** Banco de Dados Não-Relacionais (ADS16)  
* **Docente Responsável:** Prof. Me. Reginaldo Fernandes  
* **Semestre Letivo:** 2026.2  
* **Data da Aula:** 03 de Novembro de 2026 (Terça-feira)  
* **Carga Horária:** 2 h/a (120 minutos)  
* **Módulo:** Unidade I (N1) — O Modelo Orientado a Documentos (MongoDB)  

---

## 🎯 Competências e Objetivos

- [x] Compreender as limitações de escalabilidade de consultas sem índice (**`COLLSCAN`** com complexidade $\mathcal{O}(N)$) e a fundamentação teórica das árvores balanceadas (**$B\text{-Tree}$**) no motor de armazenamento WiredTiger, obtendo redução assintótica para $\mathcal{O}(\log N)$.
- [x] Dominar **filtros complexos** no MongoDB com operadores lógicos, operadores de arrays (`$elemMatch`, `$all`, `$size`), expressões internas com `$expr` (comparação de campos do mesmo documento) e regex.
- [x] Executar **atualizações atômicas avançadas** sem reescrita de documentos: operadores aritméticos (`$inc`, `$mul`, `$min`, `$max`), operadores de manipulação de listas (`$push`, `$addToSet`, `$slice`) e modificações seletivas em subdocumentos de arrays utilizando **`arrayFilters`** com o operador `$[<identificador>]`.
- [x] Projetar e construir **índices simples, compostos e multikey** no **MongoDB Compass (GUI)**, no terminal **`mongosh`** e via **Python (`PyMongo`)**.
- [x] Dominar e provar a **Regra de Ouro ESR** (*Equality, Sort, Range*) para eliminar ordenações custosas em memória RAM (`SORT`) e evitar o erro fatal de limite de buffer (*Sort memory limit*).
- [x] Implementar **índices textuais (*Full-Text Search*)** com pesos diferenciados (*weights*), tokenização nativa, remoção de *stopwords*, radicalização de palavras (*stemming*) e ordenação por pontuação de relevância (`$meta: "textScore"`).
- [x] Diagnosticar planos de execução utilizando a ferramenta **`explain("executionStats")`**, interpretando os estágios (`COLLSCAN`, `IXSCAN`, `FETCH`, `SORT`), a razão entre documentos examinados e retornados ($\frac{\text{totalDocsExamined}}{\text{nReturned}}$), e construindo **Covered Queries** (Consultas Cobertas com `totalDocsExamined = 0`).

---

## 📁 Estrutura de Arquivos da Aula 07

- [`tutorial_construcao_passo_a_passo.md`](tutorial_construcao_passo_a_passo.md): **Guia Passo a Passo Completo** — dividido em 5 partes:
  1. Fundamentos Teóricos da Indexação e Complexidade Computacional ($B\text{-Tree}$ vs. COLLSCAN, $\mathcal{O}(N)$ vs. $\mathcal{O}(\log N)$ e WiredTiger).
  2. Operadores CRUD Avançados e Atualizações Atômicas no **MongoDB Compass** e **`mongosh`** (`$elemMatch`, `$expr`, `$inc`, `$push`, `$slice`, `arrayFilters`).
  3. Tipos de Índices: Simples, Compostos, Multikey, Parciais, Esparsos e TTL.
  4. A Regra de Ouro ESR (*Equality, Sort, Range*) e Busca Textual Ponderada com Relevância (`textScore`).
  5. Diagnóstico de Performance com `explain("executionStats")`, *Covered Queries* e Benchmark com 50.000 documentos.
- [`plano_de_aula.md`](plano_de_aula.md): Roteiro pedagógico estruturado nos 4 pilares metodológicos e diretrizes do IFCE Campus Tauá.
- [`roteiro_privado_professor_videoaula.md`](roteiro_privado_professor_videoaula.md): Roteiro exclusivo do docente com diretrizes didáticas, armadilhas comuns dos discentes e marcações de tempo.
- [`index.html`](index.html): Portal web interativo da Aula 07, reunindo a fundamentação teórica, blocos de código com realce de sintaxe, visualizadores de planos `explain`, gráficos e links para download.
- `codigo/`:
  - [`docker-compose.yml`](codigo/docker-compose.yml): Configuração para subir instâncias locais do MongoDB 8.0 e Mongo Express (GUI web na porta `8081`).
  - [`requirements.txt`](codigo/requirements.txt): Dependências Python (`pymongo`, `matplotlib`, `numpy`).
  - [`povoar_dados_benchmark.py`](codigo/povoar_dados_benchmark.py): Povoamento de 50.000 produtos e pedidos sintéticos no banco `ecommerce_shopgrids` para validação empírica.
  - [`crud_avancado_operadores.py`](codigo/crud_avancado_operadores.py): Demonstração prática dos operadores `$elemMatch`, `$expr`, `$inc`, `$push` e `arrayFilters`.
  - [`indices_textuais_busca.py`](codigo/indices_textuais_busca.py): Criação de índices de texto com pesos e ranqueamento por escore.
  - [`benchmark_indexacao_explain.py`](codigo/benchmark_indexacao_explain.py): Benchmark com medição real de latência, planos de execução e geração do gráfico comparativo `benchmark_performance_indices.png`.
  - [`mongosh_aula07_avancado.js`](codigo/mongosh_aula07_avancado.js): Script completo e comentado para execução no shell interativo `mongosh`.
  - [`demonstracao_aula07.ipynb`](codigo/demonstracao_aula07.ipynb): Notebook Jupyter interativo com narrativa teórica e prática pareada.
  - [`produtos_amostra_aula07.json`](codigo/produtos_amostra_aula07.json): Amostra representativa para testes rápidos no MongoDB Compass.
- `materiais/`:
  - [`main.pdf`](materiais/main.pdf) e módulos LaTeX Beamer 16:9 (`secao1_*.tex` a `secao5_*.tex`) prontos para apresentação em aula.

---

## 🚀 Como Executar o Laboratório Localmente

1. **Subir os Contêineres:**
   ```bash
   cd codigo
   docker compose up -d
   ```
2. **Instalar Dependências Python:**
   ```bash
   pip install -r requirements.txt
   ```
3. **Povoar a Base para o Benchmark:**
   ```bash
   python3 povoar_dados_benchmark.py
   ```
4. **Executar o Benchmark Comparativo:**
   ```bash
   python3 benchmark_indexacao_explain.py
   ```
5. **Acessar as Ferramentas:**
   * **MongoDB Compass:** `mongodb://localhost:27017`
   * **Mongo Express:** `http://localhost:8081`
   * **Terminal mongosh:** `docker exec -it shopgrids-mongodb mongosh`
