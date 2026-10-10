# Plano de Aula: 04 - Aplicação da Lista de Exercícios 01 (N1): Atividade Avaliativa Assíncrona de Consolidação

**Disciplina:** Banco de Dados  
**Curso:** Tecnologia em Telemática  
**Instituição:** Instituto Federal de Educação, Ciência e Tecnologia do Ceará (IFCE) - Campus Tauá  
**Professor:** Prof. Me. Reginaldo Pereira Fernandes  
**Data:** 10 de Outubro de 2026 (Sábado Letivo)  
**Carga Horária:** 100 minutos (2 horas/aula assíncronas)  
**Regime Didático:** Mentoria e Tutoria Individualizada (1 Aluno) -- Atividade Avaliativa Assíncrona  

---

## 💡 1. Filosofia Pedagógica e Metodologia

Conforme o planejamento pedagógico para turmas em tutoria individual e o calendário acadêmico do IFCE Campus Tauá, os sábados letivos são reservados para atividades assíncronas de consolidação, sem introdução de conteúdo novo. 

A **Aula 04** destina-se formalmente à aplicação, resolução e entrega da **Lista de Exercícios 01 (N1)**, primeira avaliação formativa e somativa da disciplina, correspondendo a **20% da nota do Período N1** segundo a equação oficial:
$$N1 = (AVT1 \times 0.40) + (AVP1_{\text{Projeto Fase 1}} \times 0.40) + (\overline{\text{Listas}}_{1,2,3} \times 0.20)$$

### Adequação Metodológica: Foco Conceitual & Notação Canônica em LaTeX/TikZ (Sem SQL)
Como as aulas práticas de sintaxe e codificação em SQL iniciarão formalmente no Período N2 (a partir da Aula 22), **esta avaliação não exige comandos ou códigos em SQL**. Todo o instrumental de avaliação foca na compreensão conceitual profunda e na produção gráfica rigorosa de:
1. **Fundamentos de SGBD vs. Sistemas de Arquivos:** Vantagens conceituais, controle de redundância, integridade transacional ACID, controle de concorrência e tolerância a falhas via WAL (*Write-Ahead Logging*).
2. **Arquitetura ANSI/SPARC de 3 Níveis:** Nível Externo (Visões de Redes), Nível Conceitual (Global) e Nível Interno (Físico), com mapeamentos bidirecionais assegurando a Independência Lógica e Física de Dados.
3. **Catálogo do Sistema (Dicionário de Metadados):** Otimizador de Consultas Baseado em Custo (CBO) e Subsistema de Segurança e Controle de Acesso.
4. **Ciclo de Vida do Projeto de BD:** Fases de Requisitos, Conceitual, Lógico e Físico, e justificativa formal da independência tecnológica do MER.
5. **Ontologia e Taxonomia do MER:** Classificação ontológica rigorosa de Entidades, Conjuntos de Entidades e Atributos (identificadores, simples, compostos, multivalorados, derivados e nulos).
6. **Elaboração de Diagramas Vetoriais em LaTeX + TikZ:** Construção gráfica de diagramas arquiteturais e Diagramas Entidade-Relacionamento (DER) segundo a **notação canônica de Peter Chen (1976)**, utilizando o pacote TikZ em LaTeX para renderização de alta qualidade.

---

## 🎯 2. Objetivos de Aprendizagem

### Objetivo Geral
Avaliar e consolidar os conhecimentos teóricos, conceituais e arquiteturais sobre Fundamentos de SGBD, Arquitetura ANSI/SPARC de 3 Níveis, Independência de Dados, Catálogo do Sistema, Ciclo de Vida do Projeto de Banco de Dados e Modelagem Conceitual de Entidades e Atributos utilizando a Notação Canônica do Diagrama Entidade-Relacionamento (DER) de Peter Chen implementado em LaTeX/TikZ.

### Objetivos Específicos
1. **Fundamentos de SGBD:** Analisar criticamente as deficiências de sistemas de arquivos convencionais frente aos SGBDs (redundância, concorrência, ACID e WAL).
2. **Arquitetura ANSI/SPARC & Catálogo:** Diferenciar os 3 níveis de abstração, explicar a independência física e lógica no contexto de redes/NOC, e modelar o diagrama esquemático completo da arquitetura em TikZ com repositório central de metadados.
3. **Ciclo de Vida do Projeto de BD:** Detalhar as quatro fases canônicas e fundamentar a independência tecnológica do projeto conceitual frente a SGBDs e dialetos SQL.
4. **Ontologia e Taxonomia Canônica:** Classificar com precisão entidades, conjuntos de entidades e atributos (simples, compostos, monovalorados, multivalorados, armazenados, derivados, nulos e identificadores) em ativos de telecomunicações (`ROTEADOR_BORDA_BGP`).
5. **Produção de Diagramas Gráficos (DER Chen) em LaTeX/TikZ:** Elaborar diagramas conceituais rigorosos na notação clássica de Peter Chen (retângulos, elipses simples, duplas, tracejadas, ramificadas e chaves sublinhadas) para cenários reais de infraestrutura de redes (`SERVIDOR_VIRTUALIZADO`, `PONTO_DE_PRESENCA`, `ENLACE_OPTICO`, `EQUIPAMENTO_TRANSMISSAO` e `ROTEADOR_CLIENTE`).
6. **Análise Comparativa de Notações:** Contrastar o rigor semântico da Notação de Peter Chen (1976) contra a Notação Pé de Galinha (*Crow's Foot* / Martin).

---

## ⏱️ 3. Roteiro de Trabalho Assíncrono (100 Minutos Equivalentes)

| Parte | Duração | Descrição das Atividades | Entregável Parcial |
| :---: | :---: | :--- | :--- |
| **I** | 00 - 30 min | **Fundamentos de SGBD e Arquitetura ANSI/SPARC:** Resolução das questões 1 e 2 (conceitos teóricos e independência) e desenho/código TikZ do Diagrama da Arquitetura ANSI/SPARC (Questão 3). | Respostas dissertativas Q1-Q2 e Diagrama TikZ Q3. |
| **II** | 30 - 50 min | **Ciclo de Vida e Ontologia de Atributos:** Resolução das questões 4 e 5, discriminando as 4 fases do projeto e classificando os atributos de `ROTEADOR_BORDA_BGP`. | Respostas analíticas Q4 e Q5. |
| **III** | 50 - 85 min | **Produção de Diagramas DER Chen em TikZ:** Resolução das questões 6, 7 e 8 com modelagem conceitual rigorosa de datacenters e do Backbone Óptico IFCE, normalização de planilha e análise comparativa Chen vs Martin. | Código TikZ ou imagens dos DERs Q6, Q7 e Q8. |
| **Revisão** | 85 - 100 min | **Conferência, Preenchimento e Finalização:** Verificação do checklist de conformidade, preenchimento à caneta das respostas e desenho dos diagramas no caderno impresso ou folhas anexas. | Caderno de resolução por escrito da Lista 01. |

---

## 📝 4. Caderno Oficial da Lista de Exercícios 01 (N1) -- 8 Questões

* **Valor Total:** 10,0 pontos (com peso de 20% na nota final N1).
* **Sem Código SQL:** A lista é estritamente conceitual e arquitetural.
* **Data de Entrega Improrrogável:** **12 de Outubro de 2026** (Segunda-feira).
* **Forma de Entrega:** Entrega obrigatoriamente **por escrito (manuscrita)** preenchida à caneta no caderno impresso [`lista_01.pdf`](file:///home/reginaldo-fernandes/Aulas/Cursos/Tecnologia%20em%20Telem%C3%A1tica/Disciplinas/Banco%20de%20Dados/Aulas/Aula_04/materiais/lista_01.pdf) ou em folhas anexas devidamente identificadas.
* **Critério de Notação:** Os diagramas conceituais devem adotar estritamente a **notação canônica de Peter Chen (1976)**, desenhados com régua/gabarito.

---

### PARTE I: Fundamentos de SGBD & Arquitetura ANSI/SPARC (3,0 Pontos)

**Questão 1 (Valor: 1,0 ponto) -- Fundamentos de SGBD vs. Sistemas de Arquivos Planos**  
Compare tecnicamente o armazenamento de dados em arquivos planos gerenciados pelo sistema operacional versus um SGBD sob os 4 pilares:
- a) Redundância e inconsistência de dados;
- b) Controle de concorrência (*locks*, *race conditions*, *lost updates*);
- c) Garantia das propriedades ACID (Atomicidade, Consistência, Isolamento e Durabilidade);
- d) Recuperação de falhas e integridade pós-pane via *Write-Ahead Logging* (WAL).

**Questão 2 (Valor: 1,0 ponto) -- Níveis de Abstração ANSI/SPARC e Independência de Dados**  
- a) Explique a função e o escopo de cada nível: Externo (Visões), Conceitual (Global) e Interno (Físico).
- b) Diferencie conceitualmente Independência Física de Dados de Independência Lógica de Dados.
- c) Ilustre com dois cenários reais de redes/NOC: migração para SSD NVMe com índices B-Tree e adição de nova entidade no esquema conceitual.

**Questão 3 (Valor: 1,0 ponto) -- [DIAGRAMA TIKZ] Arquitetura ANSI/SPARC de Três Níveis**  
Construa o diagrama esquemático completo da Arquitetura ANSI/SPARC adaptado ao contexto de Telemática:
- Nível Externo com 2 visões (Operador NOC e Gestor de TI);
- Nível Conceitual unificado;
- Nível Interno com armazenamento físico e estruturas B-Tree;
- Mapeamentos bidirecionais (Independência Lógica e Física);
- Repositório Central de Metadados (Catálogo do Sistema), Otimizador CBO e Motor de Segurança.

---

### PARTE II: Ciclo de Vida do Projeto & Ontologia de Atributos (2,5 Pontos)

**Questão 4 (Valor: 1,0 ponto) -- Fases do Projeto de BD e Independência Tecnológica**  
- a) Descreva o objetivo, entrada e saída das 4 fases: Análise de Requisitos, Projeto Conceitual, Projeto Lógico e Projeto Físico.
- b) Justifique por que o Modelo Entidade-Relacionamento (MER) é independente de SGBDs e de comandos SQL.

**Questão 5 (Valor: 1,5 ponto) -- Ontologia do Modelo Conceitual e Taxonomia Canônica de Atributos**  
- a) Defina formalmente a diferença entre Entidade, Conjunto de Entidades (*Entity Set*) e Instância de Entidade, exemplificando com o IFCE Campus Tauá.
- b) Classifique os 5 atributos da entidade `ROTEADOR_BORDA_BGP`:
  1. `tag_patrimonial_ifce` (identificador simples);
  2. `coordenadas_rack` (composto: bloco, sala, rack, unidade U);
  3. `prefixos_ipv6_bgp` (multivalorado: múltiplos blocos);
  4. `horas_ininterruptas_uptime` (derivado: $t_{\text{atual}} - t_{\text{boot}}$);
  5. `motivo_ultima_falha` (nulo quando em operação contínua sem falhas).

---

### PARTE III: Produção de Diagramas Conceituais (DER Peter Chen) em LaTeX/TikZ (4,5 Pontos)

**Questão 6 (Valor: 1,5 ponto) -- [DIAGRAMA DER TIKZ] Entidade SERVIDOR_VIRTUALIZADO**  
Construa o DER de Peter Chen em TikZ contendo:
- Retângulo: `SERVIDOR_VIRTUALIZADO`;
- Chave Primária: `uuid_maquina` (sublinhado);
- Simples: `nome_virtual` e `memoria_ram_gb`;
- Composto: `alocacao_cluster` ramificado em `nome_datacenter`, `host_fisico_id` e `storage_pool`;
- Multivalorado: `enderecos_ip_interfaces` (elipse dupla);
- Derivado: `custo_estimado_mensal` (tracejado, fórmula com memória RAM e storage).

**Questão 7 (Valor: 2,0 pontos) -- [DIAGRAMA DER TIKZ] Minimundo do Backbone Óptico Regional do IFCE**  
Modele os 3 conjuntos de entidades com todos os atributos no DER Peter Chen:
1. `PONTO_DE_PRESENCA`: `id_pop` (chave), `cidade`, `endereco_completo` (composto), `telefones_contato` (multivalorado) e `disponibilidade_anual` (derivado).
2. `ENLACE_OPTICO`: `codigo_enlace` (chave), `distancia_km`, `atenuacao_db_km`, `tipo_fibra` e `comprimentos_onda_nm` (multivalorado).
3. `EQUIPAMENTO_TRANSMISSAO`: `patrimonio_id` (chave), `modelo`, `data_instalacao` e `slot_rack` (composto: sala, rack, posicao_u).

**Questão 8 (Valor: 1,0 ponto) -- [DIAGRAMA DER & ANÁLISE] Engenharia Reversa de Planilha & Peter Chen vs Crow's Foot**  
- a) Análise crítica da planilha que armazena `[ID_Equip, Fabricante, Modelo, Localizacao_Fisica, Servidores_DNS, Data_Compra, Anos_Operacao]`.
- b) Construção do DER Chen para `ROTEADOR_CLIENTE` com atributos decompostos.
- c) Análise comparativa aprofundada: Notação Peter Chen (1976) vs. Notação Pé de Galinha (*Crow's Foot* / James Martin).

---

## 📊 5. Barema Oficial de Avaliação (10,0 Pontos)

| Questão | Categoria | Descrição do Critério | Pontuação |
| :---: | :--- | :--- | :---: |
| **Q1** | Fundamentos de SGBD | Contraste técnico SGBD vs Arquivos (Redundância, Concorrência, ACID e WAL) | **1,0 pt** |
| **Q2** | Arquitetura ANSI/SPARC | Abstração em 3 Níveis e Independência Física vs Lógica em Redes | **1,0 pt** |
| **Q3** | Diagrama Arquitetural | Diagrama ANSI/SPARC em TikZ com NOC/TI, Mapeamentos e Catálogo | **1,0 pt** |
| **Q4** | Ciclo de Vida de BD | As 4 Fases Canônicas e Independência Tecnológica do MER | **1,0 pt** |
| **Q5** | Ontologia de Atributos | Entidade/Conjunto/Instância e Taxonomia em `ROTEADOR_BORDA_BGP` | **1,5 pt** |
| **Q6** | Diagrama DER Chen | DER TikZ de `SERVIDOR_VIRTUALIZADO` com todos os tipos de atributos | **1,5 pt** |
| **Q7** | Diagrama DER Chen | DER TikZ do Backbone Óptico (POP, Enlace e Equipamento com atributos) | **2,0 pts** |
| **Q8** | Diagrama DER & Análise | Normalização de planilha, DER TikZ de `ROTEADOR_CLIENTE` e Chen vs Martin | **1,0 pt** |
| **Total** | **Consolidação N1** | **Nota Máxima da Lista de Exercícios 01** | **10,0 pts** |

---

## 📚 6. Referências Bibliográficas

1. **ELMASRI, Ramez; NAVATHE, Shamkant B.** *Sistemas de Banco de Dados*. 7. ed. São Paulo: Pearson, 2018.
2. **SILBERSCHATZ, Abraham; KORTH, Henry F.; SUDARSHAN, S.** *Sistema de Banco de Dados*. 7. ed. Rio de Janeiro: Elsevier, 2020.
3. **CHEN, Peter Pin-Shan.** *The Entity-Relationship Model -- Toward a Unified View of Data*. ACM Transactions on Database Systems (TODS), v. 1, n. 1, p. 9–36, 1976.
4. **DATE, C. J.** *Introdução a Sistemas de Bancos de Dados*. 8. ed. Rio de Janeiro: Elsevier, 2004.
5. **TANTAN, Till et al.** *The TikZ and PGF Packages: Manual for Version 3.1.10*. CTAN, 2023.
