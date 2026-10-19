# Plano de Aula: 07 - Sábado Letivo: Estudo Dirigido do Projeto Prático (AVP1) — Definição do Escopo do Minimundo

**Disciplina:** Banco de Dados  
**Curso:** Tecnologia em Telemática  
**Instituição:** Instituto Federal de Educação, Ciência e Tecnologia do Ceará (IFCE) - Campus Tauá  
**Professor:** Prof. Me. Reginaldo Pereira Fernandes  
**Data:** 17 de Outubro de 2026 (Sábado Letivo)  
**Carga Horária:** 100 minutos (2 horas/aula assíncronas)  
**Regime Didático:** Mentoria e Tutoria Individualizada (1 Aluno) -- Estudo Dirigido Assíncrono (AVP1 - Etapa 1)  

---

## 💡 1. Filosofia Pedagógica e Metodologia

De acordo com o planejamento semestral da disciplina e o calendário acadêmico do IFCE Campus Tauá, os sábados letivos são dedicados a atividades assíncronas de consolidação e desenvolvimento orientado, sem introdução de conteúdo teórico inédito.

A **Aula 07** inaugura formalmente o desenvolvimento do **Projeto Prático de Banco de Dados — Fase 1 (AVP1)**, que responde por **40% da nota do Período N1**:
$$N1 = (AVT1 \times 0.40) + (AVP1_{\text{Projeto Fase 1}} \times 0.40) + (\overline{\text{Listas}}_{1,2,3} \times 0.20)$$

### Diretrizes Metodológicas da Etapa 1 do Projeto
1. **Modelagem Conceitual Estruturada:** Aplicação da **notação canônica de Peter Chen (1976)** e do **Modelo Entidade-Relacionamento Estendido (EER)** em domínios de sistemas de informação (como **Clínica Médica**, **Gestão Acadêmica Universitária**, **Sistema de Biblioteca** ou **Comércio Eletrônico / Varejo**).
2. **Engenharia de Requisitos e Especificação Conceitual:** Levantamento de requisitos de dados e especificação conceitual preliminar que servirá de insumo direto para a **Aula 08** (*Laboratório Prático de Modelagem Conceitual com Ferramentas CASE*).
3. **Metodologia de Extração Gramatical Sistemática (Heuser; Elmasri & Navathe):**
   - **Substantivos e Sintagmas Nominais $\to$** Candidatos a **Conjuntos de Entidades** e **Atributos**;
   - **Locuções Verbais Transitivas $\to$** Candidatas a **Tipos de Relacionamento**;
   - **Advérbios e Quantificadores ("todo", "no máximo um", "vários") $\to$** **Razões de Cardinalidade** ($1:1, 1:N, N:M$) e **Restrições de Participação** $(min, max)$;
   - **Subordinação de Identidade $\to$** **Entidades Fracas** e **Chaves Parciais (Discriminadores)**;
   - **Relações "É-UM" (*IS-A*) $\to$** Hierarquias de **Especialização / Generalização (EER)**.

---

## 🎯 2. Objetivos de Aprendizagem

### Objetivo Geral
Orientar o estudante na definição formal do escopo do minimundo do seu **Projeto Prático de Banco de Dados (AVP1)**, capacitando-o a redigir a especificação narrativa de requisitos de dados e a catalogar todas as entidades regulares, atributos (simples, compostos, multivalorados, derivados e identificadores), relacionamentos ($1:1$, $1:N$, $N:M$ e unários), entidades fracas e hierarquias EER exigidos na avaliação.

### Objetivos Específicos
1. **Delimitação de Escopo (Minimundo):** Redigir uma descrição textual clara, coesa e sem ambiguidades de um sistema de informação (entre 15 e 25 linhas), contemplando regras explícitas de negócio.
2. **Identificação de Entidades Fortes e Taxonomia de Atributos (Aula 03):** Levantar no mínimo **5 conjuntos de entidades regulares**, especificando para o conjunto global do projeto todos os cinco tipos canônicos de atributos de Peter Chen (identificador, simples, composto, multivalorado e derivado).
3. **Especificação de Relacionamentos, Cardinalidades e Participações (Aula 05):** Definir os relacionamentos entre as entidades cobrindo as cardinalidades **$1:1$**, **$1:N$** e **$N:M$** (com atributo descritivo próprio), além de **auto-relacionamento (recursivo)** com papéis (*roles*) e restrições estruturais $(min, max)$.
4. **Modelagem de Entidade Fraca e Relacionamento Identificador (Aula 06):** Incorporar e justificar ao menos **1 Entidade Fraca** dependente existencialmente e em identificação de uma entidade proprietária, destacando seu **discriminador (chave parcial)**.
5. **Modelagem de Especialização/Generalização no EER (Aula 06):** Projetar ao menos **1 Hierarquia de Herança (Superclasse/Subclasses)**, definindo formalmente as restrições de **Disjunção** ($d$ ou $o$) e de **Integralidade/Completude** (Total ou Parcial).
6. **Validação Computacional do Escopo em Python:** Utilizar o script de apoio em Python para validar automaticamente se o dicionário conceitual do minimundo cumpre 100% dos requisitos obrigatórios da rubrica da AVP1.

---

## ⏱️ 3. Roteiro de Trabalho Assíncrono (100 Minutos Equivalentes)

| Etapa | Duração | Descrição das Atividades | Entregável Parcial |
| :---: | :---: | :--- | :--- |
| **1** | 00 - 20 min | **Estudo do Caso Modelo ("Clínica Médica VidaPlena"):** Leitura analítica do minimundo modelo resolvido, observando como o texto narrativo se transforma em tabelas de entidades, relacionamentos, entidade fraca e hierarquia EER. | Compreensão do padrão de referência da AVP1. |
| **2** | 20 - 40 min | **Escolha do Tema e Redação do Minimundo (Etapa 1 do Formulário):** Seleção de um dos 3 minimundos sugeridos (Gestão Acadêmica, Biblioteca ou E-Commerce) ou proposta de tema equivalente, e redação da narrativa de regras de negócio. | Texto descritivo do minimundo (15 a 25 linhas). |
| **3** | 40 - 65 min | **Catálogo de Entidades, Atributos e Entidade Fraca (Etapas 2 e 3):** Preenchimento do quadro de entidades fortes, classificação completa de atributos (composto, multivalorado, derivado, PK) e especificação da Entidade Fraca com discriminador. | Dicionário conceitual de entidades e atributos. |
| **4** | 65 - 85 min | **Matriz de Relacionamentos, Hierarquia EER e Esboço DER (Etapas 4 e 5):** Especificação dos relacionamentos ($1:1, 1:N, N:M$, recursivo), definição da árvore de herança EER ($d/o$, Total/Parcial) e rascunho esquemático do DER de Peter Chen. | Matriz de relacionamentos, especificação EER e esboço DER. |
| **5** | 85 - 100 min | **Conferência no Validador Python e Finalização:** Execução do checklist de conformidade e consolidação do documento para utilização imediata na **Aula 08** (Laboratório CASE com brModelo/Draw.io). | **Documento de Escopo AVP1 finalizado**. |

---

## 📖 4. Estudo de Caso Modelo Resolvido: Clínica Médica "VidaPlena"

Para demonstrar o nível de detalhamento esperado na **Etapa 1 da AVP1**, apresentamos a seguir um exemplo completo e resolvido: uma **Clínica Médica e Ambulatorial**.

### 4.1. Narrativa de Requisitos de Dados do Minimundo Modelo
> *"A **Clínica Médica VidaPlena** necessita de um banco de dados para gerenciar seus atendimentos, corpo clínico e pacientes. Na clínica, todas as pessoas ligadas ao quadro funcional são cadastradas como **Colaboradores**, possuindo matrícula (identificador único), CPF, nome completo, data de admissão, tempo de serviço (calculado automaticamente a partir da data de admissão), endereço residencial (composto por logradouro, número, bairro e cidade) e um ou mais telefones de contato. Todo colaborador é obrigatoriamente e exclusivamente classificado em uma de duas categorias: **Médico** (para o qual se registra o número do CRM e suas especialidades médicas, podendo ter várias) ou **Atendente Administrativo** (para o qual se registra o ramal telefônico e o turno de trabalho). Além disso, um médico sênior pode atuar como **preceptor/supervisor** de vários médicos residentes recém-contratados.*  
> *A clínica está organizada em **Departamentos Clínicos** (identificados por um código único, nome e bloco de atendimento). Cada departamento é chefiado por exatamente um médico diretor, e um médico pode dirigir no máximo um departamento. Por outro lado, um departamento aloca diversos médicos, sendo que cada médico está vinculado a um único departamento principal.*  
> *Os **Pacientes** são identificados por um código de prontuário único, possuindo CPF, nome completo, data de nascimento, idade atual (calculada a partir da data de nascimento) e múltiplos e-mails de contato. Um paciente titular pode cadastrar seus **Dependentes** para cobertura familiar; os dependentes não possuem código próprio global, sendo identificados pelo seu primeiro nome combinado ao prontuário do paciente titular, além de registrarem data de nascimento e grau de parentesco.*  
> *Por fim, os médicos realizam **Consultas** aos pacientes, e ao longo do tratamento os médicos prescrevem diversos **Exames Laboratoriais** (identificados por código TUSS, nome do exame e preparo exigido) aos pacientes. Um médico pode solicitar vários exames e um exame pode ser solicitado em diversas prescrições, registrando-se nessa solicitação a data do pedido e a justificativa clínica."*

### 4.2. Extração Conceitual Estruturada do Caso Modelo

1. **Entidades Regulares (Fortes) e Seus Atributos:**
   - `COLABORADOR` (Superclasse): $\underline{\text{matricula}}$ (PK), `cpf`, `nome_completo`, `data_admissao`, `tempo_servico` *(derivado)*, `endereco` *(composto: logradouro, numero, bairro, cidade)*, `telefones` *(multivalorado)*.
   - `DEPARTAMENTO_CLINICO`: $\underline{\text{cod\_depto}}$ (PK), `nome_depto`, `bloco`.
   - `PACIENTE`: $\underline{\text{id\_prontuario}}$ (PK), `cpf`, `nome_paciente`, `data_nascimento`, `idade` *(derivado)*, `emails` *(multivalorado)*.
   - `EXAME_LABORATORIAL`: $\underline{\text{cod\_tuss}}$ (PK), `nome_exame`, `preparo_exigido`.

2. **Hierarquia de Especialização/Generalização (Modelo EER):**
   - **Superclasse:** `COLABORADOR` $\to$ **Subclasses:** `MEDICO` (atributos específicos: `crm`, e multivalorado `especialidades`) e `ATENDENTE` (atributos específicos: `ramal`, `turno`).
   - **Restrições EER:** **Disjunta ($d$)** (um colaborador é médico OU atendente, nunca ambos) e **Total (Linha Dupla)** (todo colaborador cadastrado deve pertencer a uma das duas subclasses).

3. **Entidade Fraca e Relacionamento Identificador:**
   - **Entidade Proprietária (*Owner*):** `PACIENTE` ($\underline{\text{id\_prontuario}}$).
   - **Entidade Fraca (Retângulo Duplo):** `DEPENDENTE`.
   - **Relacionamento Identificador (Losango Duplo):** `POSSUI_DEP` ($1:N$, com participação total de `DEPENDENTE`).
   - **Chave Parcial (Discriminador - Sublinhado Tracejado):** $\dashuline{\text{nome\_dependente}}$ (acompanhado dos atributos simples `data_nascimento` e `parentesco`). Chave global composta: $(\text{id\_prontuario}, \text{nome\_dependente})$.

4. **Matriz de Relacionamentos do Caso Modelo:**
   - `DIRIGE` (`MEDICO` $1 : 1$ `DEPARTAMENTO_CLINICO`): Participação parcial de `MEDICO` $(0, 1)$ e total de `DEPARTAMENTO_CLINICO` $(1, 1)$.
   - `LOTADO_EM` (`DEPARTAMENTO_CLINICO` $1 : N$ `MEDICO`): Participação total de `MEDICO` $(1, 1)$ e total de `DEPARTAMENTO_CLINICO` $(1, N)$.
   - `SUPERVISIONA` (`MEDICO` $1 : N$ `MEDICO` — **Auto-relacionamento Unário**): Papéis `preceptor` $(0, N)$ e `residente` $(0, 1)$.
   - `ATENDIDO_POR` / `SOLICITA_EXAME` (`PACIENTE` $N : M$ `EXAME_LABORATORIAL`): Relacionamento $N:M$ com atributos descritivos próprios `data_pedido`, `medico_solicitante` e `justificativa_clinica`.

---

## 🗂️ 5. Catálogo de Minimundos Sugeridos (AVP1)

O estudante deve escolher **um (1)** dos três domínios abaixo (ou propor um quarto domínio equivalente) para desenvolver seu Projeto Prático (AVP1):

### Opção A (Recomendada): Sistema de Gestão Acadêmica Universitária ("SGA-Universidade")
- **Contexto:** Controle de cursos, departamentos acadêmicos, professores, técnicos administrativos, alunos, disciplinas, matrículas e dependentes institucionais.
- **Elementos sugeridos:**
  - *Hierarquia EER:* `SERVIDOR` $\to$ `PROFESSOR` (`titulacao`, `area_pesquisa` multivalorado) e `TECNICO_ADM` (`setor`, `cargo`).
  - *Entidades Fortes:* `DEPARTAMENTO_ACADEMICO`, `CURSO`, `DISCIPLINA`, `ALUNO`.
  - *Entidade Fraca:* `MODULO_PROGRAMATICO` (ou `DEPENDENTE_ALUNO` / `AVALIACAO_ETAPA` identificada pelo número da etapa dentro da disciplina).
  - *Relacionamentos:* Professor `COORDENA` Curso ($1:1$), Curso `POSSUI` Disciplinas ($1:N$), Aluno `CURSA` Disciplina ($N:M$ com atributos `semestre_letivo`, `nota_final` e `frequencia`), Disciplina `PRE_REQUISITO_DE` Disciplina (Auto-relacionamento $N:M$ ou $1:N$).

### Opção B: Sistema de Gestão de Biblioteca e Empréstimos ("BiblioTech")
- **Contexto:** Controle de acervo bibliográfico, editoras, autores, exemplares físicos nas estantes, usuários leitores e histórico de empréstimos.
- **Elementos sugeridos:**
  - *Hierarquia EER:* `USUARIO_LEITOR` $\to$ `LEITOR_ESTUDANTE` (`curso`, `semestre`) e `LEITOR_DOCENTE` (`departamento`, `limite_dias_especial`).
  - *Entidades Fortes:* `OBRA_LIVRO`, `EDITORA`, `AUTOR`, `FUNCIONARIO_BIBLIOTECA`.
  - *Entidade Fraca:* `EXEMPLAR_FISICO` (identificado pelo $\dashuline{\text{numero\_sequencial\_tombo}}$ combinado ao `isbn` da `OBRA_LIVRO`, pois um mesmo livro possui os exemplares nº 1, nº 2, nº 3).
  - *Relacionamentos:* Editora `PUBLICA` Obra ($1:N$), Autor `ESCREVE` Obra ($N:M$ com atributo `ordem_autoria`), Funcionário `GERENCIA` Setor ($1:1$), Funcionário `SUPERVISIONA` Funcionário (Auto-relacionamento $1:N$).

### Opção C: Sistema Comercial de Vendas, Estoque e E-Commerce ("MercadoFácil")
- **Contexto:** Gestão de clientes, produtos, categorias mercadológicas, fornecedores, vendedores, pedidos de compra e itens de pedido.
- **Elementos sugeridos:**
  - *Hierarquia EER:* `CLIENTE` $\to$ `PESSOA_FISICA` (`cpf`, `data_nascimento`) e `PESSOA_JURIDICA` (`cnpj`, `inscricao_estadual`, `razao_social`).
  - *Entidades Fortes:* `PRODUTO`, `CATEGORIA`, `FORNECEDOR`, `PEDIDO`, `VENDEDOR`.
  - *Entidade Fraca:* `ITEM_PEDIDO` (ou `ENDERECO_ENTREGA_DEPENDENTE`), onde cada item é numerado sequencialmente ($\dashuline{\text{num\_item}} = 1, 2, 3\dots$) apenas dentro de um `PEDIDO` específico.
  - *Relacionamentos:* Vendedor `GERENCIA` Filial/Equipe ($1:1$), Cliente `REALIZA` Pedido ($1:N$), Fornecedor `FORNECE` Produto ($N:M$ com `preco_custo` e `prazo_entrega_dias`), Categoria `SUBCATEGORIA_DE` Categoria (Auto-relacionamento $1:N$).

---

## 📝 6. Roteiro Oficial do Estudo Dirigido (Caderno de Entrega AVP1 - Etapa 1)

O trabalho deste Sábado Letivo está estruturado em **5 Questões/Etapas Práticas** (totalizando **10,0 pontos** da Etapa 1 da AVP1), disponíveis no caderno oficial impresso [`estudo_dirigido_avp1.pdf`](file:///home/reginaldo-fernandes/Aulas/Cursos/Tecnologia%20em%20Telem%C3%A1tica/Disciplinas/Banco%20de%20Dados/Aulas/Aula_07/materiais/estudo_dirigido_avp1.pdf):

1. **Etapa 1 (2,0 pts) — Identificação do Tema e Narrativa do Minimundo:** Definição do domínio e redação do texto descritivo completo (15 a 25 linhas) contendo todas as regras de negócio de forma explícita.
2. **Etapa 2 (2,0 pts) — Catálogo de Entidades Regulares e Taxonomia Completa de Atributos:** Listagem de no mínimo 5 entidades fortes com descrição semântica e especificação explícita de atributos identificadores (PK), simples, pelo menos 1 atributo composto (com subatributos), pelo menos 1 atributo multivalorado e pelo menos 1 atributo derivado (com regra de cálculo).
3. **Etapa 3 (2,0 pts) — Especificação de Relacionamentos, Cardinalidades e Participações:** Preenchimento da matriz contendo obrigatoriamente: 1 relacionamento $1:1$, 1 relacionamento $1:N$, 1 relacionamento $N:M$ com atributo descritivo próprio e 1 auto-relacionamento (unário) com papéis explícitos, indicando as restrições $(min, max)$.
4. **Etapa 4 (2,0 pts) — Especificação de Entidade Fraca e Hierarquia EER:**
   - **4.a (1,0 pt):** Definição da Entidade Proprietária, Entidade Fraca, Relacionamento Identificador e Chave Parcial (Discriminador), justificando a dependência existencial e de identificação.
   - **4.b (1,0 pt):** Definição da Superclasse e no mínimo 2 Subclasses no modelo EER, listando os atributos herdados, os atributos específicos de cada subclasse e classificando a hierarquia quanto à Disjunção ($d$ ou $o$) e Integralidade (Total ou Parcial).
5. **Etapa 5 (2,0 pts) — Esboço Integrado do Diagrama Entidade-Relacionamento Estendido (DER/EER):** Desenho preliminar (à mão com régua/gabarito na notação canônica de Peter Chen) integrando os elementos especificados nas Etapas 2, 3 e 4, preparando a base para a digitalização na ferramenta CASE na **Aula 08**.

---

## 📊 7. Barema Oficial da Etapa 1 do Projeto Prático (AVP1)

| Etapa | Componente do Escopo AVP1 | Critério de Avaliação Técnica | Pontuação |
| :---: | :--- | :--- | :---: |
| **Etapa 1** | Narrativa do Minimundo | Clareza, coesão textual e cobertura das regras de negócio | **2,0 pts** |
| **Etapa 2** | Entidades Fortes & Atributos | Mínimo de 5 entidades e presença de PK, composto, multivalorado e derivado | **2,0 pts** |
| **Etapa 3** | Matriz de Relacionamentos | Presença correta de $1:1$, $1:N$, $N:M$ (c/ atributo) e auto-relacionamento c/ papéis | **2,0 pts** |
| **Etapa 4** | Entidade Fraca & Modelo EER | Correta identificação do discriminador fraco e das restrições EER ($d/o$, Total/Parcial) | **2,0 pts** |
| **Etapa 5** | Esboço Preliminar DER/EER | Uso rigoroso da gramática gráfica canônica de Peter Chen (1976) | **2,0 pts** |
| **Total** | **Escopo do Projeto AVP1** | **Nota da Etapa 1 do Projeto Prático (Insumo para a Aula 08)** | **10,0 pts** |

---

## 📚 8. Referências Bibliográficas

1. **CHEN, Peter Pin-Shan.** *The Entity-Relationship Model: Toward a Unified View of Data*. ACM Transactions on Database Systems (TODS), v. 1, n. 1, p. 9–36, 1976.
2. **ELMASRI, Ramez; NAVATHE, Shamkant B.** *Sistemas de Banco de Dados*. 7. ed. São Paulo: Pearson Education do Brasil, 2018.
3. **HEUSER, Carlos Alberto.** *Projeto de Banco de Dados*. 6. ed. Porto Alegre: Bookman, 2009.
4. **SILBERSCHATZ, Abraham; KORTH, Henry F.; SUDARSHAN, S.** *Sistema de Banco de Dados*. 7. ed. Rio de Janeiro: Elsevier, 2020.
5. **DATE, C. J.** *Introdução a Sistemas de Bancos de Dados*. 8. ed. Rio de Janeiro: Elsevier / Campus, 2004.
