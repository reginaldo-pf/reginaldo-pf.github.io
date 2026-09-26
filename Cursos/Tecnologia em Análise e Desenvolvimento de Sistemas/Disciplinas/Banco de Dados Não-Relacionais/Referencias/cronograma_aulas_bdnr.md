# Planejamento Semestral: Bancos de Dados Não-Relacionais (NoSQL)
**IFCE Campus Tauá -- Tecnologia em Análise e Desenvolvimento de Sistemas (ADS)**  
**Código:** ADS16 | **Carga Horária:** 40h (20 Encontros de 2h/aula) | **Semestre:** 2026.2 -- 2027.1  

---

## 1. Diretrizes Pedagógicas e Sistema de Avaliação

### 1.1. Estrutura das Avaliações por Período
Conforme o Regulamento da Organização Didática (ROD) do IFCE e a orientação pedagógica, a disciplina divide-se em dois períodos letivos (**N1** e **N2**):

- **1º Período (N1):**
  - **AVP1 (Avaliação Prática 1):** Prova prática em laboratório de informática envolvendo modelagem e manipulação de documentos com MongoDB e estratégias de cache com Redis.
  - **AVT1 (Avaliação Teórica 1):** Avaliação teórica individual sobre Teorema CAP/PACELC, ACID vs BASE, trade-offs de escalabilidade, modelos Chave-Valor e Documentos.
  - **Lista de Exercícios 1 (AV3):** Atividades e listas contínuas desenvolvidas ao longo do 1º período.
- **2º Período (N2):**
  - **AVP2 (Avaliação Prática 2):** Prova prática ou entrega e defesa de projeto em laboratório aplicando Bancos de Família de Colunas, Grafos e/ou Integração com API.
  - **AVT2 (Avaliação Teórica 2):** Avaliação teórica individual sobre Família de Colunas, Teoria dos Grafos, Bancos Vetoriais, Persistência Poliglota e Arquitetura de Software.
  - **Lista de Exercícios 2 (AV3):** Atividades e listas contínuas desenvolvidas ao longo do 2º período.

### 1.2. Diretriz Estrita para Sábados Letivos (Sem Conteúdo Novo)
Foram alocados dois sábados letivos ao longo do semestre:
1. **10/10/2026 (Aula 03):** Oficina prática de ferramental (Docker e Docker Compose para NoSQL) e resolução assistida de exercícios de nivelamento.
2. **14/11/2026 (Aula 09):** Laboratório de fixação e revisão prática integrado (MongoDB + Redis), funcionando como simulado e plantão preparatório imediatamente anterior à AVP1 e AVT1.

---

## 2. Proposta de Modernização da Ementa

Para que a disciplina atenda às demandas atuais do ecossistema de software (2026/2027), a ementa formal do PUD é enriquecida com os seguintes tópicos práticos:

1. **Containers e DevOps para Bancos NoSQL (Docker & Docker Compose):**
   - Abandono de instalações manuais locais no SO. Os estudantes sobem instâncias isoladas e reproduzíveis de Redis, MongoDB e Neo4j em segundos.
2. **Pipelines Analíticos de Agregação e Schemas JSON:**
   - Domínio do MongoDB Aggregation Framework (`$match`, `$group`, `$lookup`, `$facet`) e validação de schema para aplicações corporativas.
3. **Bancos de Dados Vetoriais (Vector Databases) & IA Generativa (Modernização Chave):**
   - Introdução à representação vetorial (*embeddings*), cálculo de similaridade de cosseno e uso prático de bancos vetoriais (ChromaDB / Atlas Vector Search) para RAG (*Retrieval-Augmented Generation*).
4. **Persistência Poliglota & Microsserviços:**
   - Integração de múltiplos bancos (Relacional + NoSQL) em aplicações modernas com back-end em Python (FastAPI).

---

## 3. Cronograma Detalhado dos 20 Encontros (40 Horas)

| Encontro | Data | Dia | Carga | Módulo / Período | Conteúdo Programático e Atividades |
| :---: | :---: | :---: | :---: | :---: | :--- |
| **01** | 29/09/2026 | Ter | 2h | Unidade I (N1) | **Apresentação e Paradigma NoSQL:** Limitações de escala vertical no modelo relacional, propriedades ACID sob concorrência maciça, os 3 Vs do Big Data e motivações do NoSQL. |
| **02** | 06/10/2026 | Ter | 2h | Unidade I (N1) | **Fundamentos Arquiteturais:** Teorema CAP (Brewer), Teorema PACELC, Propriedades BASE (*Basically Available, Soft state, Eventual consistency*) e taxonomia dos 4 modelos NoSQL. |
| **03** | 10/10/2026 | **Sáb** | 2h | Laboratório (N1) | **Sábado Letivo (Sem Conteúdo Novo):** Oficina prática de Docker e Docker Compose para NoSQL. Nivelamento prático, subindo instâncias de Redis e MongoDB em laboratório. Resolução assistida da Lista 1. |
| **04** | 13/10/2026 | Ter | 2h | Unidade I (N1) | **Modelo Chave-Valor (Key-Value) com Redis:** Arquitetura em memória, volatilidade e persistência (RDB/AOF), estruturas de dados nativas (Strings, Hashes, Lists, Sets, Sorted Sets). |
| **05** | 20/10/2026 | Ter | 2h | Unidade II (N1) | **Redis em Aplicações Reais:** Estratégias de Caching (Cache-Aside, Write-Through), expiração com TTL, controle de sessão de usuários e filas de mensagens. |
| **06** | 27/10/2026 | Ter | 2h | Unidade I (N1) | **Modelo Orientado a Documentos (MongoDB):** Conceitos de BSON/JSON, modelagem de dados NoSQL: Decisão de Incorporação (*Embedding*) vs Referenciamento (*Referencing*) e boas práticas. |
| **07** | 03/11/2026 | Ter | 2h | Unidade I (N1) | **Operações CRUD e Indexação no MongoDB:** Filtros avançados, operadores de atualização (`$set`, `$inc`, `$push`), índices simples e compostos, análise de planos de execução (`explain`). |
| **08** | 10/11/2026 | Ter | 2h | Unidade II (N1) | **MongoDB Aggregation Framework:** Construção de pipelines analíticos com estágios (`$match`, `$group`, `$project`, `$sort`, `$lookup`, `$unwind`). Resolução de relatórios analíticos de negócio. |
| **09** | 14/11/2026 | **Sáb** | 2h | Laboratório (N1) | **Sábado Letivo (Sem Conteúdo Novo):** Laboratório de fixação intensiva e revisão prática integrada (Redis + MongoDB). Simulação prática de desafios e plantão de dúvidas preparatório para AVP1 e AVT1. |
| **10** | 17/11/2026 | Ter | 2h | **Avaliação N1** | **AVP1 -- Avaliação Prática 1 (Laboratório):** Desafio prático individual/dupla em laboratório envolvendo modelagem de documentos, consultas analíticas em MongoDB e caching de dados com Redis. |
| **11** | 24/11/2026 | Ter | 2h | **Avaliação N1** | **AVT1 -- Avaliação Teórica 1:** Prova teórica individual sobre Teorema CAP/PACELC, trade-offs arquiteturais, modelos Chave-Valor e Documentos. **Entrega final da Lista de Exercícios 1 (AV3).** |
| **12** | 01/12/2026 | Ter | 2h | Unidade I (N2) | **Modelo de Família de Colunas (Wide-Column):** Arquitetura distribuída *peer-to-peer*, partição de anel, fator de replicação, consistência ajustável (Apache Cassandra / DynamoDB). |
| **13** | 08/12/2026 | Ter | 2h | Unidade I (N2) | **Modelagem Orientada a Consultas (Query-Driven):** Estratégia de modelagem no Cassandra (desnormalização intencional baseada nas consultas), linguagem CQL e chaves de partição/clusterização. |
| **14** | 15/12/2026 | Ter | 2h | Unidade I (N2) | **Modelo Orientado a Grafos (Graph Databases):** Teoria dos Grafos aplicada a bancos de dados, nós, relacionamentos, propriedades e índices. Cenários ideais: redes sociais, fraudes e logística. |
| -- | *16/12 a 25/01* | -- | -- | *Recesso* | *Recesso Escolar / Férias Docentes e Discentes* |
| **15** | 26/01/2027 | Ter | 2h | Unidade II (N2) | **Neo4j e Linguagem Cypher:** Escrita de consultas em Cypher (`MATCH`, `CREATE`, `WHERE`, `RETURN`), travessia de relacionamentos, busca do menor caminho (*Shortest Path*) e algoritmos de grafos. |
| **16** | 02/02/2027 | Ter | 2h | Modernização (N2) | **Bancos de Dados Vetoriais (Vector DBs) & IA:** O papel dos dados vetoriais para Inteligência Artificial, embeddings, similaridade por cosseno e busca semântica em aplicações RAG (prática com ChromaDB / Atlas Vector). |
| -- | *09/02/2027* | -- | -- | *Feriado* | *Terça-feira de Carnaval (Sem expediente letivo)* |
| **17** | 16/02/2027 | Ter | 2h | Unidade II (N2) | **Integração NoSQL com Aplicações (Back-end):** Conexão via drivers e ODMs (Python `pymongo`, `redis-py` ou `neo4j`), tratamento de conexões (pools), segurança, controle de permissões e boas práticas. |
| **18** | 23/02/2027 | Ter | 2h | Unidade II (N2) | **Persistência Poliglota na Arquitetura de Software:** Padrões arquiteturais modernos (CQRS, Event Sourcing), quando combinar SQL com múltiplos NoSQL. Orientações finais para a avaliação prática. |
| **19** | 02/03/2027 | Ter | 2h | **Avaliação N2** | **AVP2 -- Avaliação Prática 2 (Laboratório / Projeto):** Avaliação prática de desenvolvimento / defesa de solução integrada utilizando modelos de Grafos, Colunas e integração com aplicação. |
| **20** | 09/03/2027 | Ter | 2h | **Avaliação N2** | **AVT2 -- Avaliação Teórica 2:** Prova teórica individual cobrindo Modelos de Colunas, Grafos, Bancos Vetoriais, Persistência Poliglota e Arquitetura. **Entrega final da Lista de Exercícios 2 (AV3) e Fechamento.** |

---

## 4. Distribuição da Carga Horária por Tópico

- **Fundamentos, Arquitetura & Teorema CAP/PACELC:** 4h (10%)
- **Bancos Chave-Valor (Redis):** 4h (10%)
- **Bancos Orientados a Documentos (MongoDB):** 6h (15%)
- **Bancos de Família de Colunas (Cassandra / DynamoDB):** 4h (10%)
- **Bancos Orientados a Grafos (Neo4j):** 4h (10%)
- **Bancos Vetoriais & IA Generativa (Modernização):** 2h (5%)
- **Integração de Aplicações, Segurança & Persistência Poliglota:** 4h (10%)
- **Sábados Letivos (Oficina Docker + Laboratório de Fixação Preparatório):** 4h (10%)
- **Processos Avaliativos (AVP1, AVT1, AVP2, AVT2):** 8h (20%)
- **Total:** **40 horas (20 encontros de 2h)**
