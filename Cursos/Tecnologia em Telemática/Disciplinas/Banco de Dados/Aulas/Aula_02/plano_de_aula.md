# Plano de Aula: 02 - Arquitetura ANSI/SPARC, Independência de Dados, Catálogo do Sistema e Sublinguagens SQL

**Disciplina:** Banco de Dados  
**Curso:** Tecnologia em Telemática  
**Instituição:** Instituto Federal do Ceará (IFCE) - Campus Tauá  
**Professor:** Prof. Me. Reginaldo Pereira Fernandes  
**Data:** 30 de Setembro de 2026 (Quarta-feira)  
**Carga Horária:** 100 minutos (2 horas/aula)  
**Regime Didático:** Mentoria e Tutoria Individualizada (1 Aluno)  

---

## 🎯 Objetivos de Aprendizagem

### Objetivo Geral
Capacitar o discente a compreender a organização arquitetural em três camadas dos SGBDs modernos, dominar os conceitos e a relevância prática da independência física e lógica de dados para sistemas de infraestrutura de redes/telemática, entender o papel do catálogo do sistema (dicionário de metadados) e aplicar com rigor a taxonomia das sublinguagens SQL (DDL, DML, DQL, DCL e TCL).

### Objetivos Específicos
1. Identificar os três níveis da arquitetura ANSI/SPARC (Externo, Conceitual e Interno) e a função dos mapeamentos entre níveis.
2. Analisar o impacto da independência lógica e da independência física na manutenção e evolução de serviços de rede e banco de dados.
3. Compreender a função do Catálogo do Sistema (Dicionário de Dados) como o repositório central de metadados consultado pelo otimizador e pelo motor de segurança.
4. Diferenciar formalmente as cinco sublinguagens de SQL: DDL, DML, DQL, DCL e TCL, contextualizando suas operações e comandos canônicos.
5. Inspecionar o catálogo do sistema e manipular tabelas e transações via script Python integrado ao SQLite (`sqlite_master`, `ALTER TABLE`, transações com `SAVEPOINT`).

---

## ⏱️ Cronograma da Aula (100 Minutos)

| Bloco | Duração | Descrição das Atividades | Metodologia & Recursos |
| :---: | :---: | :--- | :--- |
| **1** | 00 - 20 min | **Acolhimento & Revisão Conceitual:** Retrospectiva da Aula 01 (banco de dados vs. arquivos), introdução à problemática do acoplamento entre dados e programas e necessidade de níveis de abstração. | Exposição dialogada e diagrama de evolução histórica. |
| **2** | 20 - 45 min | **Arquitetura ANSI/SPARC de 3 Níveis:** Apresentação detalhada dos níveis Externo (Visões de Usuários/Serviços), Conceitual (Esquema Lógico Global da Empresa) e Interno (Estruturas Físicas de Armazenamento, Índices, Páginas). Mapeamento Externo-Conceitual e Conceitual-Interno. | Slides Beamer (Widescreen 16:9) e esquemas gráficos comparativos. |
| **3** | 45 - 65 min | **Independência de Dados & Catálogo do Sistema:** Independência Lógica vs. Física. O Catálogo do Sistema (Dicionário de Metadados) e a introspecção de esquemas nos SGBDs modernos (`sqlite_master`, `information_schema`, `pg_catalog`). | Demonstração conceitual e análise de casos práticos em sistemas de telecom. |
| **4** | 65 - 85 min | **Taxonomia das Sublinguagens SQL & Laboratório:** Classificação rigorosa de DDL, DML, DQL, DCL e TCL. Prática computacional com Python e SQLite executando consultas ao catálogo do sistema, migrações DDL e transações com pontos de salvamento (*Savepoints*). | Laboratório prático individual (VS Code / Jupyter Notebook). |
| **5** | 85 - 100 min | **Fechamento, Exercícios & Orientações:** Síntese dos conceitos abordados, resolução de dúvidas, apresentação das questões do Bloco 2 da Lista de Exercícios 01 (prevista para o Sábado Letivo - Aula 04) e introdução à Aula 03 (Modelagem MER). | Alinhamento de mentoria e fechamento de plano de estudos. |

---

## 💻 Roteiro do Laboratório Prático Computacional

1. **Introspecção do Catálogo do Sistema:**
   - Criação de uma tabela de ativos de rede (`roteadores_core`).
   - Consulta à tabela interna `sqlite_master` para inspecionar metadados de tabelas, índices e esquemas DDL gerados.
2. **Demonstração de DDL e Independência Física:**
   - Execução de `ALTER TABLE` adicionando coluna de monitoramento SNMP (`snmp_community`), verificando a preservação das consultas já implementadas.
3. **Demonstração de DML e DQL:**
   - Carga de dados de roteadores com parâmetros de rede (IP, fabricante, capacidade).
   - Consulta filtrada e formatada com operadores de ordenação e projeção.
4. **Demonstração de TCL (Controle Transacional):**
   - Início de bloco transacional com `SAVEPOINT`.
   - Simulação de erro operacional e reversão com `ROLLBACK TO SAVEPOINT`, garantindo atomicidade e consistência.

---

## 📝 Exercícios de Fixação (Lista 1 -- Bloco 2)

1. Explique por que a arquitetura ANSI/SPARC introduziu o nível conceitual intermediário, em vez de mapear diretamente as visões de aplicação (nível externo) sobre as estruturas em disco (nível interno).
2. Diferencie, com exemplos concretos aplicados a serviços de telecomunicações, **Independência Lógica de Dados** de **Independência Física de Dados**.
3. O que são metadados em um SGBD? Como o otimizador de consultas e o subsistema de segurança utilizam o catálogo do sistema?
4. Classifique cada comando SQL a seguir na sua respectiva sublinguagem (DDL, DML, DQL, DCL ou TCL) e explique sua função:
   - a) `ALTER TABLE interfaces ADD COLUMN mtu INTEGER DEFAULT 1500;`
   - b) `GRANT SELECT, INSERT ON roteadores TO operador_noc;`
   - c) `SAVEPOINT ponto_restauracao_1;`
   - d) `DELETE FROM logs_snmp WHERE data_evento < '2026-01-01';`
   - e) `SELECT hostname, ip_gerencia FROM dispositivos WHERE status = 'ONLINE';`
