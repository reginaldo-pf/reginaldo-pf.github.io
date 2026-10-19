# Estudo Dirigido do Projeto Prático (AVP1) — Etapa 1: Definição do Escopo do Minimundo

**Instituição:** Instituto Federal de Educação, Ciência e Tecnologia do Ceará (IFCE) - Campus Tauá  
**Curso:** Tecnologia em Telemática  
**Disciplina:** Banco de Dados (Semestre 2026.2)  
**Docente:** Prof. Me. Reginaldo Pereira Fernandes  
**Data de Aplicação:** 17 de Outubro de 2026 (Sábado Letivo -- Aula 07)  
**Peso da AVP1 no Período N1:** 40% da Nota N1 ($10,0\text{ pontos}$)  

---

## 📋 1. Diretrizes Gerais e Checklist Obrigatório do Escopo

1. **Propósito Pedagógico:** Este estudo dirigido estrutura a concepção da **Fase 1 do Projeto Prático de Banco de Dados (AVP1)**. A especificação produzida nesta atividade servirá como insumo imediato para a **Aula 08 (20/10/2026)**, na qual será construído o Diagrama Entidade-Relacionamento Estendido (DER/EER) em ferramentas CASE (*brModelo* / *Draw.io*).
2. **Definição do Domínio do Minimundo:** O projeto deve abordar um sistema de informação estruturado (ex.: Clínica Médica, Gestão Acadêmica Universitária, Sistema de Biblioteca, Rede Hoteleira ou E-Commerce), escolhido a partir do catálogo sugerido ou de proposta equivalente.
3. **Checklist de Construtos Conceituais Obrigatórios (Notação Peter Chen / EER):**
   - [x] **Mínimo de 5 Conjuntos de Entidades Regulares (Fortes)** com chaves primárias sublinhadas;
   - [x] **Taxonomia Completa de Atributos de Peter Chen:** Atributos identificadores (PK), simples/monovalorados, ao menos **1 atributo composto** (ramificado em subatributos), ao menos **1 atributo multivalorado** (elipse dupla) e ao menos **1 atributo derivado** (elipse tracejada com regra de cálculo);
   - [x] **Relacionamentos Binários nos 3 Graus de Cardinalidade:** Ao menos um relacionamento **$1:1$**, um **$1:N$** e um **$N:M$ com atributo descritivo próprio**, especificando as restrições de participação $(min, max)$;
   - [x] **Auto-relacionamento (Unário/Recursivo):** Ao menos 1 relacionamento recursivo com rotulação explícita de papéis (*roles*);
   - [x] **Entidade Fraca (*Weak Entity*):** Ao menos 1 entidade fraca (retângulo duplo) vinculada por relacionamento identificador (losango duplo e participação total) a uma entidade proprietária, com **chave parcial / discriminador** (sublinhado tracejado);
   - [x] **Hierarquia de Especialização/Generalização (Modelo EER):** Ao menos 1 superclasse especializada em 2 ou mais subclasses, especificando a restrição de **Disjunção** ($d$ ou $o$) e de **Integralidade** (Total ou Parcial).

---

## 🏥 2. Exemplo Modelo Resolvido: Clínica Médica "VidaPlena"

### 2.1. Narrativa de Requisitos de Dados do Caso Modelo
> *"A **Clínica Médica VidaPlena** deseja informatizar o controle de seu quadro clínico, departamentos, pacientes e prescrições de exames. Todo profissional contratado é registrado como **Colaborador**, possuindo matrícula única (`matricula`), CPF, nome completo, data de admissão, `tempo_servico` (calculado a partir da data de admissão), `endereco` residencial (composto por `rua`, `numero` e `bairro`) e múltiplos `telefones` de contato. Todo colaborador é obrigatoriamente e exclusivamente especializado em uma de duas funções: **Médico** (registrando o número do `crm` e uma ou mais `especialidades`) ou **Atendente** (registrando o `ramal` e o `turno`). Médicos seniores atuam como preceptores que supervisionam vários médicos residentes.*  
> *A clínica possui diversos **Departamentos Clínicos** (`cod_depto`, `nome_depto` e `bloco`). Cada departamento é chefiado por um único médico diretor ($1:1$), e cada departamento aloca vários médicos ($1:N$).*  
> *Os **Pacientes** possuem código de prontuário único (`id_prontuario`), CPF, nome, data de nascimento e `idade` (calculada). Um paciente titular pode cadastrar seus **Dependentes** familiares; cada dependente não possui código próprio global, sendo identificado pelo seu primeiro nome (`nome_dep`) em conjunto com o prontuário do titular, além de possuir data de nascimento e parentesco. Por fim, os pacientes realizam diversos **Exames Laboratoriais** (`cod_exame`, `nome_exame` e `preparo`) em um relacionamento $N:M$ que registra a `data_solicitacao` e o `resultado_laudo`."*

### 2.2. Quadro Resumo de Extração Conceitual do Caso Modelo

| Construto MER/EER | Elemento no Caso Modelo | Especificação Técnica e Restrições Semânticas |
| :--- | :--- | :--- |
| **Entidades Fortes** | `COLABORADOR`, `DEPTO_CLINICO`, `PACIENTE`, `EXAME` | Chaves primárias: `matricula`, `cod_depto`, `id_prontuario`, `cod_exame`. |
| **Atributos Especiais** | Composto, Multivalorado, Derivado | Composto: `endereco` (`rua`, `num`, `bairro`); Multivalorado: `telefones`, `especialidades`; Derivado: `tempo_servico`, `idade`. |
| **Hierarquia EER** | `COLABORADOR` $\to$ `MEDICO`, `ATENDENTE` | Especialização **Disjunta ($d$)** e **Total (Linha Dupla)**. Herança universal de `matricula` e atributos básicos. |
| **Entidade Fraca** | `DEPENDENTE` (Proprietário: `PACIENTE`) | Relacionamento identificador `POSSUI_DEP` ($1:N$, participação total). Discriminador: `nome_dep`. PK global: `(id_prontuario, nome_dep)`. |
| **Relacionamentos** | `DIRIGE` ($1:1$), `ALOCA` ($1:N$), `SUPERVISIONA` ($1:N$), `REALIZA_EXAME` ($N:M$) | Auto-relacionamento `SUPERVISIONA` com papéis `preceptor`/`residente`. `REALIZA_EXAME` ($N:M$) com atributo `data_solicitacao`. |

---

## 🗂️ 3. Catálogo de Opções de Minimundos Sugeridos

1. **Opção A — Sistema de Gestão Acadêmica Universitária ("SGA-Universidade"):**
   - *Hierarquia EER:* `SERVIDOR` $\to$ `PROFESSOR` e `TECNICO_ADM`.
   - *Entidades Fortes:* `DEPARTAMENTO_ACADEMICO`, `CURSO`, `DISCIPLINA`, `ALUNO`.
   - *Entidade Fraca:* `ETAPA_AVALIATIVA` (ou `DEPENDENTE_SERVIDOR`).
   - *Relacionamentos:* `COORDENA` ($1:1$), `OFERTA` ($1:N$), `MATRICULA_EM` ($N:M$ com `semestre`, `nota_final`, `frequencia`), `PRE_REQUISITO` (Auto-relacionamento em `DISCIPLINA`).
2. **Opção B — Sistema de Gestão de Biblioteca e Acervo ("BiblioTech"):**
   - *Hierarquia EER:* `USUARIO_LEITOR` $\to$ `LEITOR_ALUNO` e `LEITOR_PROFESSOR`.
   - *Entidades Fortes:* `OBRA_LIVRO`, `EDITORA`, `AUTOR`, `FUNCIONARIO`.
   - *Entidade Fraca:* `EXEMPLAR_FISICO` (identificado por `num_exemplar` dentro de cada `OBRA_LIVRO`).
   - *Relacionamentos:* `CHEFIA_SETOR` ($1:1$), `PUBLICA` ($1:N$), `ESCREVE` ($N:M$ com `ordem_autoria`), `SUPERVISIONA` (Auto-relacionamento em `FUNCIONARIO`).
3. **Opção C — Sistema Comercial de E-Commerce e Pedidos ("MercadoFácil"):**
   - *Hierarquia EER:* `CLIENTE` $\to$ `PESSOA_FISICA` e `PESSOA_JURIDICA`.
   - *Entidades Fortes:* `PRODUTO`, `CATEGORIA`, `FORNECEDOR`, `VENDEDOR`, `PEDIDO`.
   - *Entidade Fraca:* `ITEM_PEDIDO` (ou `PARCELA_PAGAMENTO`, identificado por `numero_sequencial` dentro de `PEDIDO`).
   - *Relacionamentos:* `GERENCIA_LOJA` ($1:1$), `REALIZA_PEDIDO` ($1:N$), `FORNECE_PRODUTO` ($N:M$ com `preco_custo` e `prazo_dias`), `SUBCATEGORIA_DE` (Auto-relacionamento em `CATEGORIA`).

---

## ✍️ 4. Etapas do Formulário de Especificação do Aluno (10,0 Pontos)

- **Etapa 1 (2,0 pts):** Identificação do Tema Escolhido e Narrativa Completa das Regras de Negócio (15 a 20 linhas).
- **Etapa 2 (2,0 pts):** Catálogo de no mínimo 5 Entidades Fortes e especificação explícita dos Atributos Especiais (Composto, Multivalorado e Derivado).
- **Etapa 3 (2,0 pts):** Matriz de Relacionamentos ($1:1$, $1:N$, $N:M$ com atributo descritivo e Unário/Recursivo com papéis e restrições $(min, max)$).
- **Etapa 4 (2,0 pts):** Especificação da Entidade Fraca (Proprietário, Relacionamento Identificador e Discriminador) e da Hierarquia EER (Superclasse, Subclasses, Disjunção $d/o$ e Integralidade Total/Parcial).
- **Etapa 5 (2,0 pts):** Esboço Integrado do Diagrama Conceitual (DER/EER na notação canônica de Peter Chen).
