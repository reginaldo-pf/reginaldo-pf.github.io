# Plano de Aula: 09 - Fundamentos Formais do Modelo Relacional e Restrições de Integridade

* **Curso:** Tecnologia em Telemática  
* **Componente Curricular:** Banco de Dados  
* **Docente Responsável:** Prof. Me. Reginaldo Fernandes  
* **Semestre Letivo:** 2026.2  
* **Carga Horária:** 2 h/a (100 minutos)  
* **Data da Aula:** 21 de Outubro de 2026 (Quarta-feira)  
* **Módulo:** Unidade II (N1) — Fundamentos Formais do Modelo Relacional (Edgar F. Codd, 1970)  

---

## 🧭 1. Princípios e Diretrizes Pedagógicas da Aula

1. **Transição Epistemológica: Do Conceitual (MER) para o Lógico-Matemático (Relacional):** Após concluirmos a modelagem conceitual (Aulas 03 a 08), iniciamos na **Aula 09** o estudo formal do **Modelo Relacional de Dados**, proposto por **Edgar Frank Codd (1970)** no artigo histórico *"A Relational Model of Data for Large Shared Data Banks"*.
2. **Rigor Matemático e Modelagem Pura (Sem Linguagens de Programação):** O foco desta etapa da disciplina é estritamente a **modelagem lógica e matemática de dados** (teoria dos conjuntos e relações matemáticas). O estudante domina a diferença entre Esquema Intensional ($R$) e Estado Extensional ($r(R)$), Grau e Cardinalidade, Superchave e Chave Candidata, e as quatro restrições formais de integridade utilizando **notação textual de esquemas**, **diagramas de esquema com arcos direcionados** e **tabelas de auditoria de instâncias**.
3. **Estudo de Caso Integrado ("Clínica Médica VidaPlena"):** Todos os conceitos formais (domínio atômico, tupla, unicidade de chave, proibição de `NULL` na PK e integridade referencial de FK com políticas de Restrição, Cascata e Anulação) são demonstrados visualmente sobre o mesmo minimundo trabalhado nas aulas anteriores, preparando o terreno para as regras sistemáticas de mapeamento MER $\to$ Relacional das Aulas 10 e 11.

---

## 🎯 2. Objetivos de Aprendizagem

### Objetivo Geral
Capacitar o estudante a compreender e aplicar os fundamentos matemáticos do **Modelo Relacional de Dados (Codd, 1970)**, dominando a estrutura formal de domínios, atributos, tuplas e relações, a hierarquia de chaves (superchave, candidata, primária e estrangeira), os diagramas de esquema relacional e as regras universais de integridade (domínio, chave, entidade e referencial).

### Objetivos Específicos
1. **Contexto Histórico e Motivação de Codd (1970):** Compreender como o Modelo Relacional superou os modelos hierárquico e em rede ao separar a lógica matemática dos ponteiros físicos de disco.
2. **Estrutura Formal da Relação:** Definir matematicamente Domínio ($D_i$), Atributo ($A_i$), Esquema de Relação $R(A_1, A_2, \dots, A_n)$, Tupla $t = \langle v_1, v_2, \dots, v_n \rangle$ e Estado/Instância $r(R) \subseteq \text{dom}(A_1) \times \text{dom}(A_2) \times \dots \times \text{dom}(A_n)$.
3. **Métricas Estruturais (Grau vs. Cardinalidade):** Distinguir a **Aridade/Grau** de uma relação (número $n$ de atributos/colunas, propriedade estática do esquema) da **Cardinalidade** de uma relação (número $m$ de tuplas/linhas, propriedade dinâmica da instância).
4. **Propriedades Matemáticas das Relações:** Explicar a atomicidade de valores (Primeira Forma Normal - 1FN), a inexistência de ordem entre tuplas, a proibição de tuplas duplicadas e a semântica do valor especial `NULL` (desconhecido, inaplicável ou indisponível).
5. **Teoria das Chaves:** Distinguir formalmente **Superchave ($SK$)** de **Chave Candidata ($CK$ — superchave mínima irredutível)**, **Chave Primária ($PK$)** e **Chave Alternativa/Secundária ($AK$)**.
6. **Restrições de Integridade e Diagramas de Esquema Relacional:** Formular e auditar as restrições de **Domínio**, **Chave**, **Integridade de Entidade** e **Integridade Referencial (Chave Estrangeira - $FK$)**, representando os vínculos por meio de arcos direcionados ($FK \longrightarrow PK$).
7. **Anomalias em Operações sobre Tuplas:** Analisar como as operações formais de **Inserção**, **Exclusão** e **Modificação** de tuplas podem violar restrições e como o modelo reage (Rejeição/Restrição, Propagação em Cascata ou Anulação).

---

## ⏱️ 3. Cronograma da Aula (100 Minutos)

| Bloco | Duração | Descrição das Atividades | Metodologia & Recursos |
| :---: | :---: | :--- | :--- |
| **1** | 00 - 15 min | **A Revolução de Edgar F. Codd (1970) e a Transição Conceitual $\to$ Lógico:** Por que o DER precisa ser convertido em relações matemáticas? Vocabulário Formal vs. Comercial. | Exposição dialogada e contextualização histórica. |
| **2** | 15 - 40 min | **Anatomia Matemática da Relação:** Domínios atômicos, Produto Cartesiano, Esquema $R$ vs. Instância $r(R)$, Grau vs. Cardinalidade, propriedades de conjunto e semântica do `NULL`. | Slides Beamer (Widescreen 16:9) e diagramas em TikZ. |
| **3** | 40 - 65 min | **Hierarquia de Chaves e as 4 Restrições de Integridade:** Superchave, Chave Candidata (minimalidade), PK, FK, Integridade de Entidade e Integridade Referencial com arcos direcionados. | Resolução de exemplos nos slides sobre o esquema `DEPARTAMENTO_CLINICO` e `MEDICO`. |
| **4** | 65 - 85 min | **Estudo de Caso e Auditoria Tabular de Instâncias Relacionais:** Construção de Diagramas de Esquema Relacional e inspeção passo a passo de tuplas válidas e inválidas na Clínica "VidaPlena". | Prática analítica de modelagem descritiva, esquemática e tabular. |
| **5** | 85 - 100 min | **Síntese, Exercícios Analíticos e Ponte para a Aula 10:** Revisão geral e preparação para o algoritmo de **Mapeamento MER $\to$ Relacional (Aula 10)**. | Mentoria pedagógica e fechamento. |

---

## 📊 4. Slides da Apresentação (22 Lâminas em Beamer 16:9)

* **Slides 1 a 4:** Capa Institucional, Agenda, Ponte Pedagógica (Do DER ao Relacional) e Objetivos de Aprendizagem.
* **Slides 5 e 6:** Edgar Frank Codd (1970) e Tabela de Equivalência Terminológica (Formal vs. Mercado vs. Físico).
* **Slides 7 a 10:** Anatomia Visual de uma Relação em TikZ, Definição Matemática Formal ($R$ vs. $r(R)$), Grau vs. Cardinalidade, as 4 Propriedades das Relações e a Semântica do Valor `NULL`.
* **Slides 11 a 13:** Teoria Formal das Chaves: Hierarquia Matemática ($SK \supset CK \supset PK$), Minimalidade, Chave Alternativa ($AK$) e Notação Textual de Esquemas Relacionais.
* **Slides 14 a 17:** As 4 Restrições de Integridade: Classificação Geral, Domínio e Chave, Integridade de Entidade ($PK \neq \text{NULL}$), Integridade Referencial com Diagrama de Arco em TikZ ($FK \longrightarrow PK$) e Anomalias em Operações de Modificação.
* **Slides 18 e 19:** Estudo de Caso Completo e Auditoria Tabular de Instâncias Relacionais: Diagrama de Esquema com 4 Relações Conectadas da Clínica "VidaPlena" e Matriz de Verificação de Tuplas e Exclusões.
* **Slides 20 a 22:** Quadro Resumo das 4 Restrições Formais, Exercícios de Fixação e Referências Bibliográficas.

---

## 📐 5. Roteiro de Prática de Modelagem Relacional (Esquemas + Auditoria Tabular)

1. **Etapa 1 — Representação Intensional (Esquema Textual):**
   - Escrever os esquemas relacionais na notação formal $R(\underline{PK}, A_1, A_2, \dots, FK)$:
     - $\text{DEPARTAMENTO\_CLINICO}(\underline{\text{cod\_depto}}, \text{nome\_depto}, \text{bloco})$ — Grau $n = 3$.
     - $\text{MEDICO}(\underline{\text{matricula}}, \text{cpf}, \text{nome}, \text{crm}, \text{cod\_depto\_fk}, \text{mat\_superv\_fk})$ — Grau $n = 6$.
     - $\text{PACIENTE}(\underline{\text{id\_prontuario}}, \text{cpf}, \text{nome\_paciente}, \text{data\_nasc})$ — Grau $n = 4$.
     - $\text{DEPENDENTE}(\underline{\text{id\_prontuario\_fk}, \dashuline{\text{nome\_dep}}}, \text{data\_nasc}, \text{parentesco})$ — Grau $n = 4$.
2. **Etapa 2 — Desenho do Diagrama de Esquema Relacional (Arcos Direcionados):**
   - Desenhar cada esquema como um retângulo compartimentado com seus atributos.
   - Traçar as setas direcionadas partindo de cada Chave Estrangeira ($FK$) e apontando exatamente para a Chave Primária ($PK$) referenciada (incluindo o arco recursivo $\text{mat\_superv\_fk} \longrightarrow \text{matricula}$).
3. **Etapa 3 — Auditoria Tabular de Operações sobre Tuplas:**
   - Avaliar um lote de propostas de inserção e exclusão de tuplas $\langle v_1, v_2, \dots, v_n \rangle$, classificando cada uma como **ACEITA** ou **REJEITADA** e justificando formalmente qual restrição de Codd foi acionada (Domínio/1FN, Unicidade de Chave, Integridade de Entidade ou Integridade Referencial).

---

## 📝 6. Exercícios de Fixação da Aula 09

1. **Métricas e Estrutura Formal de uma Relação:**
   Considere o esquema relacional $\text{ALUNO}(\underline{\text{matricula}}, \text{cpf}, \text{nome}, \text{email}, \text{curso}, \text{semestre\_ingresso})$ que possui atualmente 450 tuplas válidas no estado atual da relação.
   - a) Qual é o **Grau (ou Aridade)** e qual é a **Cardinalidade** atual da relação `ALUNO`?
   - b) Se um novo atributo `telefone_celular` for adicionado ao esquema e 30 novas tuplas de calouros forem inseridas na instância, quais serão os novos valores de grau e cardinalidade?
   - c) Por que não podem existir duas tuplas idênticas em uma relação matemática?

2. **Superchaves vs. Chaves Candidatas (Minimalidade):**
   No esquema $\text{ALUNO}(\underline{\text{matricula}}, \text{cpf}, \text{nome}, \text{curso})$ acima, sabe-se que cada aluno possui uma `matricula` única e também um `cpf` único, mas podem existir alunos homônimos (mesmo `nome`).
   - a) Classifique cada um dos seguintes subconjuntos de atributos como **Superchave (Apenas)**, **Chave Candidata** ou **Não-Chave**:
     - I. $\{\text{matricula}\}$
     - II. $\{\text{cpf}\}$
     - III. $\{\text{matricula}, \text{nome}\}$
     - IV. $\{\text{nome}, \text{curso}\}$
     - V. $\{\text{matricula}, \text{cpf}\}$
   - b) Explique com rigor o **Princípio da Minimalidade (Irredutibilidade)** que diferencia uma Chave Candidata de uma Superchave genérica.

3. **Integridade de Entidade vs. Integridade Referencial (Uso do `NULL`):**
   Um estudante afirmou: *"Como toda chave é importante no Modelo Relacional, nem a Chave Primária (PK) nem a Chave Estrangeira (FK) podem jamais assumir o valor `NULL`."*
   - a) Avalie a afirmação do estudante: ela está totalmente correta, parcialmente correta ou incorreta? Justifique formalmente.
   - b) Apresente um exemplo prático do minimundo da Clínica Médica em que uma Chave Estrangeira **deve permitir** o valor `NULL` e outro exemplo em que ela **não deve permitir** `NULL`.

4. **Auditoria Formal de Instâncias e Violações em Operações sobre Tuplas:**
   Considere o esquema $\text{CURSO}(\underline{\text{cod\_curso}}, \text{nome\_curso})$ contendo as tuplas $\langle 1, \text{'Telemática'} \rangle$ e $\langle 2, \text{'Agronegócio'} \rangle$, e o esquema $\text{DISCIPLINA}(\underline{\text{cod\_disc}}, \text{nome\_disc}, \text{cod\_curso\_fk})$, onde $\text{cod\_curso\_fk} \longrightarrow \text{CURSO}(\underline{\text{cod\_curso}})$, contendo a tupla $\langle 101, \text{'Banco de Dados'}, 1 \rangle$. Indique se cada operação formal abaixo será **Aceita** ou **Rejeitada** e qual restrição específica do Modelo Relacional foi violada em caso de rejeição:
   - a) Inserir em `DISCIPLINA` a tupla $\langle \text{NULL}, \text{'Redes de Computadores'}, 1 \rangle$.
   - b) Inserir em `DISCIPLINA` a tupla $\langle 101, \text{'Sistemas Operacionais'}, 1 \rangle$.
   - c) Inserir em `DISCIPLINA` a tupla $\langle 102, \text{'Zootecnia Geral'}, 9 \rangle$.
   - d) Inserir em `DISCIPLINA` a tupla $\langle 103, \text{'Língua Portuguesa Instrumental'}, \text{NULL} \rangle$ (sabendo que uma disciplina optativa livre pode não estar vinculada a um curso específico).
   - e) Excluir de `CURSO` a tupla $\langle 1, \text{'Telemática'} \rangle$ sob política de **Restrição (Rejeição)**.

5. **Conexão com o Projeto Prático (AVP1):**
   Escolha **duas entidades fortes** conectadas por um relacionamento $1:N$ do seu escopo da AVP1 (elaborado nas Aulas 07 e 08) e escreva seus respectivos esquemas relacionais na notação textual formal $R(\underline{\text{PK}}, A_1, A_2, \dots)$, desenhando também o arco direcionado da Chave Estrangeira ($FK \longrightarrow PK$).

---

## 📚 7. Referências Bibliográficas

* **CODD, Edgar Frank.** *A Relational Model of Data for Large Shared Data Banks*. Communications of the ACM (CACM), New York, v. 13, n. 6, p. 377–387, June 1970.
* **ELMASRI, Ramez; NAVATHE, Shamkant B.** *Sistemas de Banco de Dados*. 7. ed. São Paulo: Pearson Education do Brasil, 2018. (Capítulo 5: O Modelo de Dados Relacional e as Restrições de Banco de Dados Relacional).
* **HEUSER, Carlos Alberto.** *Projeto de Banco de Dados*. 6. ed. Porto Alegre: Bookman, 2009. (Capítulo 4: Projeto Lógico — O Modelo Relacional).
* **SILBERSCHATZ, Abraham; KORTH, Henry F.; SUDARSHAN, S.** *Sistema de Banco de Dados*. 7. ed. Rio de Janeiro: Elsevier, 2020. (Capítulo 2: Introdução ao Modelo Relacional).
* **DATE, C. J.** *Introdução a Sistemas de Bancos de Dados*. 8. ed. Rio de Janeiro: Elsevier / Campus, 2004.
