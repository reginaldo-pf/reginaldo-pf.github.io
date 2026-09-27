# Planejamento Semestral: Banco de Dados
**Curso:** Tecnologia em Telemática -- IFCE Campus Tauá  
**Docente:** Prof. Reginaldo Pereira Fernandes  
**Carga Horária Total:** 80 horas (40 Encontros de 100 min / 2 h/a cada)  
**Regime Didático Especial:** Mentoria / Tutoria Individual (1 Aluno)  
**Semestre Letivo:** 2026.2 / 2027.1  

---

## 🎯 1. Filosofia Pedagógica e Metodologia

Devido à dinâmica de **turma individual (um único aluno)**, a disciplina adota um modelo pedagógico fortemente baseado em **Mentoria Prática e Aprendizagem Baseada em Projetos (PBL)**:

1. **Aulas Presenciais (100 min):** Divididas em fundamentação teórica formal (50 min) e prática imediata de modelagem/laboratório computacional (50 min).
2. **Sábados Letivos (Assíncronos / Sem conteúdo novo):** Dedicados exclusivamente à consolidação, resolução e aplicação das **Listas de Exercícios Avaliativas**, respeitando o ritmo de estudo autônomo do aluno.
3. **Avaliação Prática por Projetos (AVP):** O aluno desenvolverá um **Projeto de Banco de Dados Real para Telemática** em duas fases sequenciais:
   - **Fase 1 (N1):** Documento de requisitos, Modelagem Conceitual (MER/DER), Mapeamento Lógico Relacional e Normalização (1FN, 2FN, 3FN).
   - **Fase 2 (N2):** Implementação física no PostgreSQL, scripts DDL/DML, consultas analíticas com JOINs, Views, Triggers, Stored Procedures em PL/pgSQL e integração com aplicação em Python.
4. **Avaliação Teórica (AVT):** Uma avaliação individual formal por período (AVT1 e AVT2) para verificação do rigor conceitual e matemático (álgebra relacional, dependências funcionais, ACID, etc.).

---

## 📊 2. Sistema de Avaliação

### Nota da 1ª Etapa (N1)
$$N1 = (AVT1 \times 0.40) + (AVP1_{\text{Projeto Fase 1}} \times 0.40) + (\overline{\text{Listas}}_{1,2,3} \times 0.20)$$

* **AVT1 (40%):** Avaliação Teórica 1 escrita individual (Aula 21).
* **AVP1 (40%):** Projeto de Banco de Dados -- Fase 1 (Modelagem DER + Esquema Normalizado + DDL).
* **Listas N1 (20%):** Média aritmética das Listas 01 (Sábado Aula 04), 02 (Sábado Aula 15) e 03 (Sábado Aula 20).

### Nota da 2ª Etapa (N2)
$$N2 = (AVT2 \times 0.40) + (AVP2_{\text{Projeto Fase 2}} \times 0.40) + (\overline{\text{Listas}}_{4,5,6} \times 0.20)$$

* **AVT2 (40%):** Avaliação Teórica 2 escrita individual (Aula 39).
* **AVP2 (40%):** Projeto de Banco de Dados -- Fase 2 (Banco em PostgreSQL + Carga DML + Queries JOINs/Views + Triggers + Conexão Python) (Aula 40).
* **Listas N2 (20%):** Média aritmética das Listas 04 (Aula 26/27), 05 (Sábado Aula 30) e 06 (Sábado Aula 37).

### Média Final (MF)
$$MF = \frac{N1 + N2}{2} \ge 6.0 \implies \text{Aprovação}$$

---

## 📅 3. Cronograma Detalhado dos 40 Encontros (80 Horas)

### Unidade N1: Fundamentos, Modelagem Conceitual, Modelo Relacional e Normalização

| Aula | Data | Tipo / Formato | Unidade Curricular & Conteúdo Detalhado (100 min) | Entregável / Avaliação |
| :---: | :---: | :---: | :--- | :---: |
| **01** | 29/09/2026 (Ter) | Presencial | **Unidade I:** Apresentação do plano de ensino, critérios de avaliação e introdução aos Bancos de Dados vs. Arquivos convencionais. | Ambientação |
| **02** | 30/09/2026 (Qua) | Presencial | **Unidade I:** Arquitetura ANSI/SPARC de 3 níveis, independência lógica/física de dados, catálogo do sistema e linguagens SQL (DDL, DML, DCL, DQL). | Teórico-Prático |
| **03** | 06/10/2026 (Ter) | Presencial | **Unidade III:** Fases do Projeto de BD e Introdução ao Modelo Entidade-Relacionamento (MER): entidades e tipos de atributos. | Exercícios |
| **04** | 10/10/2026 (Sáb) | Sábado Letivo | **Assíncrono (Sem conteúdo novo):** Aplicação e resolução da **Lista de Exercícios 01 (N1)**. | **Lista 01 (N1)** |
| **05** | 13/10/2026 (Ter) | Presencial | **Unidade III:** Relacionamentos no MER: grau, papéis, restrições de cardinalidade (1:1, 1:N, N:M) e restrições de participação (total/parcial). | Modelagem |
| **06** | 14/10/2026 (Qua) | Presencial | **Unidade III:** Entidades Fracas, chaves parciais/discriminadores e introdução a herança/especialização no EER. | Modelagem |
| **07** | 17/10/2026 (Sáb) | Sábado Letivo | **Assíncrono (Sem conteúdo novo):** Estudo dirigido e definição do escopo do **Projeto de Banco de Dados (AVP1)** voltado para Telemática. | Escopo AVP1 |
| **08** | 20/10/2026 (Ter) | Presencial | **Unidade III:** Laboratório de Modelagem Conceitual com Ferramentas CASE (brModelo/Draw.io). Construção do DER do projeto. | Laboratório |
| **09** | 21/10/2026 (Qua) | Presencial | **Unidade II:** Fundamentos Formais do Modelo Relacional: tuplas, atributos, domínios, chaves candidatas/primárias e integridade referencial. | Teórico |
| **10** | 27/10/2026 (Ter) | Presencial | **Unidade IV:** Mapeamento Lógico Relacional (Parte 1): Regras para entidades regulares, entidades fracas e relacionamentos 1:1 e 1:N. | Prática |
| **11** | 03/11/2026 (Ter) | Presencial | **Unidade IV:** Mapeamento Lógico Relacional (Parte 2): Tabelas associativas para N:M, atributos multivalorados e ternários. | Prática |
| **12** | 04/11/2026 (Qua) | Presencial | **Unidade II:** Álgebra Relacional (Parte 1): Operadores fundamentais ($\sigma, \pi, \cup, -, \times, \rho$) com resolução formal passo a passo. | Teórico-Prático |
| **13** | 10/11/2026 (Ter) | Presencial | **Unidade II:** Álgebra Relacional (Parte 2): Junção natural ($\bowtie$), Theta-join, Outer Joins e Operador de Divisão ($\div$). | Teórico-Prático |
| **14** | 11/11/2026 (Qua) | Presencial | **Unidade II:** Cálculo Relacional de Tuplas (CRT) e de Domínios (CRD): equivalência com a Álgebra e princípios de otimização de consultas. | Teórico |
| **15** | 14/11/2026 (Sáb) | Sábado Letivo | **Assíncrono (Sem conteúdo novo):** Aplicação e resolução da **Lista de Exercícios 02 (N1)** (Mapeamento Relacional e Álgebra Relacional). | **Lista 02 (N1)** |
| **16** | 17/11/2026 (Ter) | Presencial | **Unidade IV:** Teoria do Projeto Relacional: Anomalias de atualização, redundância e definição de Dependências Funcionais (DFs) e Axiomas de Armstrong. | Teórico |
| **17** | 18/11/2026 (Qua) | Presencial | **Unidade IV:** Normalização de Dados Relacionais: Primeira Forma Normal (1FN) e Segunda Forma Normal (2FN). | Exercícios |
| **18** | 24/11/2026 (Ter) | Presencial | **Unidade IV:** Normalização de Dados Relacionais: Terceira Forma Normal (3FN) e Forma Normal de Boyce-Codd (FNBC). | Exercícios |
| **19** | 25/11/2026 (Qua) | Presencial | **Oficina do Projeto AVP1:** Mentoria individual, validação do DER, mapeamento lógico e normalização do projeto do aluno. | Tutoria AVP1 |
| **20** | 28/11/2026 (Sáb) | Sábado Letivo | **Assíncrono (Sem conteúdo novo):** Aplicação e resolução da **Lista de Exercícios 03 (N1)** (Dependências Funcionais e Normalização). | **Lista 03 (N1)** |
| **21** | 01/12/2026 (Ter) | Presencial | **Final N1:** Aplicação da **Avaliação Teórica 1 (AVT1)** e entrega/defesa do **Projeto de BD - Fase 1 (AVP1)**. | **AVT1 + AVP1** |

---

### Unidade N2: Linguagem SQL, Implementação Física, Consultas Avançadas, Programação e Administração

| Aula | Data | Tipo / Formato | Unidade Curricular & Conteúdo Detalhado (100 min) | Entregável / Avaliação |
| :---: | :---: | :---: | :--- | :---: |
| **22** | 02/12/2026 (Qua) | Presencial | **Unidade II (Início N2):** Instalação do PostgreSQL e DBeaver. Comandos SQL DDL: `CREATE DATABASE`, `CREATE TABLE` e tipos de dados. | Laboratório |
| **23** | 08/12/2026 (Ter) | Presencial | **Unidade II:** Integridade Referencial em DDL: `FOREIGN KEY`, ações em cascata (`ON DELETE/UPDATE`), constraints `CHECK` e `ALTER TABLE`. | Laboratório |
| **24** | 09/12/2026 (Qua) | Presencial | **Unidade II:** Manipulação de Dados em SQL (DML): comandos `INSERT INTO`, `UPDATE` e `DELETE` com integridade transacional. | Laboratório |
| **25** | 15/12/2026 (Ter) | Presencial | **Unidade II:** Consultas Básicas em SQL (DQL): sintaxe do `SELECT`, filtros `WHERE`, operadores lógicos, `LIKE`, `IN`, `BETWEEN` e `NULL`. | Laboratório |
| **26** | 16/12/2026 (Qua) | Presencial | **Unidade II:** Cláusulas `ORDER BY`, paginação com `LIMIT/OFFSET`, funções escalares e lançamento da **Lista 04 (N2)**. | **Lançamento Lista 04** |
| *--* | *20/12 a 19/01* | *Recesso* | *Recesso Acadêmico de Fim de Ano e Férias.* | *--* |
| **27** | 20/01/2027 (Qua) | Presencial | **Unidade II:** Retorno do recesso. Funções de agregação (`COUNT`, `SUM`, `AVG`, `MIN`, `MAX`), agrupamento com `GROUP BY` e filtro `HAVING`. | **Entrega Lista 04** |
| **28** | 26/01/2027 (Ter) | Presencial | **Unidade II:** Junção de Tabelas em SQL (Parte 1): produto cartesiano vs. junções qualificadas com `INNER JOIN` em múltiplas tabelas. | Laboratório |
| **29** | 27/01/2027 (Qua) | Presencial | **Unidade II:** Junções Avançadas em SQL (Parte 2): `LEFT`, `RIGHT`, `FULL OUTER JOIN`, `CROSS JOIN` e autorrelacionamento (`Self-Join`). | Laboratório |
| **30** | 30/01/2027 (Sáb) | Sábado Letivo | **Assíncrono (Sem conteúdo novo):** Aplicação e resolução da **Lista de Exercícios 05 (N2)** (Consultas com múltiplos JOINs e Agrupamentos). | **Lista 05 (N2)** |
| **31** | 02/02/2027 (Ter) | Presencial | **Unidade II:** Subconsultas (Subqueries): subconsultas correlacionadas, operadores `IN`, `EXISTS`, `ANY`, `ALL` e expressões CTE (`WITH`). | Laboratório |
| **32** | 03/02/2027 (Qua) | Presencial | **Unidade II:** Operações de Conjunto (`UNION`, `INTERSECT`, `EXCEPT`) e criação/gerenciamento de Visões (`CREATE VIEW`). | Laboratório |
| *--* | *08/02 a 13/02* | *Carnaval* | *Recesso de Carnaval.* | *--* |
| **33** | 16/02/2027 (Ter) | Presencial | **Unidade II:** Processamento de Transações: propriedades ACID, comandos `BEGIN`, `COMMIT`, `ROLLBACK` e níveis de isolamento no PostgreSQL. | Teórico-Prático |
| **34** | 17/02/2027 (Qua) | Presencial | **Unidade II:** Introdução à Programação no SGBD: Stored Procedures e Funções em PL/pgSQL (variáveis, condicionais, loops e retornos). | Programação BD |
| **35** | 23/02/2027 (Ter) | Presencial | **Unidade II:** Gatilhos (Triggers) em Bancos de Dados: eventos `BEFORE/AFTER`, `ROW/STATEMENT`, variáveis `NEW/OLD` e logs de auditoria. | Programação BD |
| **36** | 24/02/2027 (Qua) | Presencial | **Unidade II / Telemática:** Índices (B-Tree/Hash), análise de planos com `EXPLAIN` e integração do banco de dados com script em Python (`psycopg2`). | Integração Python |
| **37** | 27/02/2027 (Sáb) | Sábado Letivo | **Assíncrono (Sem conteúdo novo):** Aplicação e resolução da **Lista de Exercícios 06 (N2)** (Transações, Views, Funções PL/pgSQL e Triggers). | **Lista 06 (N2)** |
| **38** | 02/03/2027 (Ter) | Presencial | **Oficina do Projeto AVP2:** Testes de carga, validação de regras de negócio, conferência de relatórios SQL e alinhamento da defesa. | Tutoria AVP2 |
| **39** | 03/03/2027 (Qua) | Presencial | **Avaliação Teórica 2 (AVT2):** Avaliação escrita individual sobre SQL, ACID, Triggers e concorrência. | **AVT2** |
| **40** | 09/03/2027 (Ter) | Presencial | **Final N2:** Apresentação e Demonstração Prática do **Projeto de Banco de Dados - Fase 2 (AVP2)** com SGBD ativo e fechamento do semestre. | **AVP2 + Fechamento** |
