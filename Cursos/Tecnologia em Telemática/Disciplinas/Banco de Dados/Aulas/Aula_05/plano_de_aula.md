# Plano de Aula: 05 - Relacionamentos no Modelo Entidade-Relacionamento (MER): Grau, Papéis, Cardinalidades e Participação

**Disciplina:** Banco de Dados  
**Curso:** Tecnologia em Telemática  
**Instituição:** Instituto Federal de Educação, Ciência e Tecnologia do Ceará (IFCE) - Campus Tauá  
**Professor:** Prof. Me. Reginaldo Pereira Fernandes  
**Data:** 13 de Outubro de 2026 (Terça-feira)  
**Carga Horária:** 100 minutos (2 horas/aula)  
**Regime Didático:** Mentoria e Tutoria Individualizada (1 Aluno)  

---

## 💡 1. Filosofia Pedagógica e Metodologia

Na **Aula 03**, aprendemos a mapear o mundo real identificando **Entidades** e sua **Taxonomia de Atributos**. Na **Aula 04**, consolidamos os fundamentos arquiteturais e a notação gráfica de Peter Chen através da Lista de Exercícios 01.

Nesta **Aula 05**, avançamos para a peça central da modelagem conceitual: **os Relacionamentos**. As entidades não existem isoladas em uma organização: pessoas trabalham em departamentos, médicos atendem pacientes, professores lecionam disciplinas e alunos cursam matérias.

### Adequação Metodológica: Foco Conceitual & Exemplos Intuitivos (Sem SQL)
1. **Foco Estritamente Conceitual (Sem SQL):** Como a sintaxe e comandos SQL serão introduzidos apenas no Período N2, esta aula não utiliza comandos SQL nem dialetos de SGBD. Toda a análise concentra-se no poder semântico do Modelo Entidade-Relacionamento (MER) de Peter Chen (1976).
2. **Exemplos Didáticos Universais do Cotidiano:** Em vez de jargões técnicos complexos que sobrecarregam a cognição, utilizamos minimundos de fácil apreensão imediata:
   - **Sistema Corporativo/Empresarial:** `DEPARTAMENTO`, `FUNCIONARIO` e `PROJETO` (o exemplo seminal de Chen e Elmasri & Navathe).
   - **Sistema Acadêmico/Universitário:** `ALUNO`, `CURSO`, `DISCIPLINA` e `PROFESSOR`.
   - **Sistema de Saúde/Clínica:** `MEDICO`, `PACIENTE` e `CONSULTA`.
3. **Associação Teórico-Computacional (Exemplos Pareados):** Apresentação das regras conceituais no Diagrama Entidade-Relacionamento (DER) e validação imediata em código Python orientado a objetos, simulando a integridade semântica em memória.
4. **Diagramas Canônicos e Notações Formais:** Uso de diagramas conceituais em TikZ no padrão canônico de Peter Chen e formalização matemática via Teoria dos Conjuntos, priorizando a precisão conceitual e a clareza da modelagem de dados sem ilustrações genéricas descontextualizadas.

---

## 🎯 2. Objetivos de Aprendizagem

### Objetivo Geral
Capacitar o discente a compreender, formalizar e modelar conceitualmente as associações entre entidades no Modelo Entidade-Relacionamento (MER) de Peter Chen, dominando a determinação do grau do relacionamento, a especificação de papéis (*roles*), a aplicação rigorosa das razões de cardinalidade ($1:1$, $1:N$, $N:M$) e das restrições de participação (total e parcial), validando as regras semânticas através de um metamodelo conceitual em Python.

### Objetivos Específicos
1. **Definição Formal de Relacionamento:** Compreender **Tipo de Relacionamento** ($R$), **Conjunto de Relacionamentos** ($R \subseteq E_1 \times E_2 \times \dots$) e **Instância de Relacionamento** ($r = (e_1, e_2)$).
2. **Graus de Relacionamento:**
   - **Unário / Auto-relacionamento (Recursivo):** Uma entidade associa-se a si mesma com diferentes papéis (ex: `FUNCIONARIO` supervisiona `FUNCIONARIO`);
   - **Binário:** Associação entre dois conjuntos de entidades (ex: `FUNCIONARIO` lotado em `DEPARTAMENTO`);
   - **Ternário e N-ário:** Associação simultânea entre três conjuntos de entidades (ex: `MEDICO`, `PACIENTE` e `MEDICAMENTO` em `PRESCREVE`).
3. **Papéis nos Relacionamentos (*Roles*):** Identificar a necessidade semântica da rotulação explícita de papéis nas arestas do relacionamento para desambiguação funcional.
4. **Razões de Cardinalidade:**
   - **1:1 (Um para Um):** Cada departamento possui no máximo um gerente, e cada funcionário gerencia no máximo um departamento.
   - **1:N (Um para Muitos):** Um departamento possui vários funcionários, mas cada funcionário pertence a apenas um departamento.
   - **N:M (Muitos para Muitos):** Um funcionário trabalha em múltiplos projetos, e cada projeto conta com múltiplos funcionários.
5. **Restrições de Participação (Existência):**
   - **Participação Total (Existência Dependente / Linha Dupla):** Todo funcionário deve obrigatoriamente estar alocado em um departamento.
   - **Participação Parcial (Opcional / Linha Simples):** Um funcionário pode ou não ser gerente de um departamento.
   - **Notação Estrutural $(min, max)$:** Especificação precisa dos limites mínimo e máximo de participação de cada entidade.
6. **Atributos de Relacionamentos (Atributos Descritivos):** Compreender quando uma propriedade pertence à associação e não às entidades componentes (ex: `horas_semanais` em `TRABALHA_EM`, `nota_final` em `CURSA`).
7. **Simulação Computacional Pareada:** Implementar um metamodelo conceitual em Python puro para validação de unicidade, cardinalidade e dependência existencial.

---

## ⏱️ 3. Cronograma da Aula (100 Minutos)

| Bloco | Duração | Descrição das Atividades | Metodologia & Recursos |
| :---: | :---: | :--- | :--- |
| **1** | 00 - 15 min | **Acolhimento & Ponte Conceitual:** Retrospectiva da Aula 03 (entidades e atributos). Por que entidades sozinhas não representam a realidade? Apresentação do desafio: como conectar alunos a disciplinas e funcionários a departamentos? | Exposição dialogada e mapa conceitual. |
| **2** | 15 - 40 min | **Conceito Formal e Graus de Relacionamento:** A teoria dos conjuntos ($R \subseteq E_1 \times E_2$). O Losango canônico de Peter Chen. Graus unário (auto-relacionamento com papéis `supervisor`/`supervisionado`), binário e ternário. | Slides Beamer (Widescreen 16:9) e diagramas canônicos de Peter Chen. |
| **3** | 40 - 65 min | **Restrições Estruturais (Cardinalidades e Participação):** Análise aprofundada de $1:1$, $1:N$ e $N:M$. Participação Total (linha dupla) vs. Parcial (linha simples). Notação $(min, max)$ e atributos descritivos de relacionamento. | Diagramas conceituais em TikZ e estudo de casos do cotidiano. |
| **4** | 65 - 85 min | **Laboratório Computacional em Python (Metamodelo Conceitual):** Execução do script Python didático demonstrando a criação de entidades, registro de ligações e interceptação de violações de cardinalidade $1:1$, $1:N$ e participação total. | Laboratório interativo em Python puro (sem SQL). |
| **5** | 85 - 100 min | **Síntese, Resolução de Dúvidas & Preparação:** Alinhamento pedagógico individual, resolução de dúvidas, orientação para o esboço conceitual da AVP1 e introdução à Aula 06 (Entidades Fracas e Modelo EER). | Mentoria personalizada docente-discente. |

---

## 📊 4. Slides Sugeridos e Roteiro de Apresentação

* **Slide 1:** Capa Institucional (Banco de Dados -- Aula 05: Relacionamentos no MER).
* **Slide 2:** Agenda Temática do Encontro (8 seções modulares).
* **Slide 3:** Retrospectiva & Motivação: Por que conectar entidades? A realidade das organizações.
* **Slide 4:** Objetivos de Aprendizagem da Aula 05 (Competências teóricas e práticas).
* **Slide 5:** Definição Formal de Relacionamento ($R \subseteq E_1 \times E_2$) e o Losango de Peter Chen.
* **Slide 6:** Grau do Relacionamento: Relacionamento Binário e Ternário com exemplos didáticos.
* **Slide 7:** Auto-relacionamento Unário e a Importância dos Papéis (*Roles*): `FUNCIONARIO` supervisiona `FUNCIONARIO`.
* **Slide 8:** Razão de Cardinalidade $1:1$ (Um para Um): `DEPARTAMENTO` $\overset{\text{GERENCIA}}{\longleftrightarrow}$ `FUNCIONARIO`.
* **Slide 9:** Razão de Cardinalidade $1:N$ (Um para Muitos): `DEPARTAMENTO` $\overset{\text{POSSUI}}{\longleftrightarrow}$ `FUNCIONARIO`.
* **Slide 10:** Razão de Cardinalidade $N:M$ (Muitos para Muitos): `FUNCIONARIO` $\overset{\text{TRABALHA\_EM}}{\longleftrightarrow}$ `PROJETO`.
* **Slide 11:** Restrições de Participação: Total (Linha Dupla / Obrigatória) vs. Parcial (Linha Simples / Opcional).
* **Slide 12:** Diagrama DER de Síntese: Combinando Cardinalidade e Participação no minimundo empresarial.
* **Slide 13:** A Notação Estrutural Alternativa $(min, max)$ de Chen e Elmasri/Navathe.
* **Slide 14:** Atributos de Relacionamentos: Propriedades que nascem da associação (`horas_semanais`, `nota_final`).
* **Slide 15:** Metamodelo em Python: Validação Conceitual de Cardinalidade em Memória.
* **Slide 16:** Metamodelo em Python: Testes Práticos e Bloqueio de Violações Semânticas.
* **Slide 17:** Conclusão, Síntese das Competências e Conexão com a Aula 06 (Entidades Fracas).
* **Slide 18:** Referências Bibliográficas (Peter Chen, Elmasri & Navathe, Heuser, Silberschatz).

---

## 💻 5. Roteiro do Laboratório Prático Computacional (Python Puro)

1. **Construção do Metamodelo Orientado a Objetos:**
   - Criação das classes `InstanciaRelacionamento` e `DefinicaoRelacionamento`.
   - Implementação das enumerações `TipoCardinalidade` (`1:1`, `1:N`, `N:M`) e `TipoParticipacao` (`TOTAL`, `PARCIAL`).
2. **Registro de Entidades do Minimundo Empresarial:**
   - Conjunto `DEPARTAMENTO`: `Engenharia`, `Recursos Humanos`, `Marketing`.
   - Conjunto `FUNCIONARIO`: `Ana Silva`, `Carlos Souza`, `Beatriz Lima`, `Daniel Rocha`.
   - Conjunto `PROJETO`: `Sistema Web`, `Portal Mobile`, `Migração Cloud`.
3. **Simulação e Validação de Regras Semânticas:**
   - **Teste 1: Cardinalidade 1:1 (`GERENCIA`):** Vincular `Ana` à gerência de `Engenharia`. Tentar vincular `Carlos` ao mesmo departamento já gerenciado e demonstrar o bloqueio semântico de violação 1:1.
   - **Teste 2: Cardinalidade 1:N (`LOTADO_EM`):** Alocar `Beatriz` em `Marketing`. Tentar alocá-la simultaneamente em `RH` e demonstrar a interrupção por violação de regra 1:N.
   - **Teste 3: Cardinalidade N:M com Atributos (`TRABALHA_EM`):** Associar funcionários a múltiplos projetos informando o atributo descritivo `horas_semanais`.
   - **Teste 4: Auto-relacionamento com Papéis (`SUPERVISIONA`):** Estabelecer quem é `supervisor` e quem é `supervisionado`.
   - **Teste 5: Verificação de Participação Total:** Auditar se todos os funcionários cadastrados pertencem a algum departamento, listando pendências de alocação.

---

## 📝 6. Exercícios de Fixação da Aula 05

1. **Definição e Grau:** Em um sistema de biblioteca escolar, explique por que o ato de um aluno pegar um livro emprestado é modelado como um **relacionamento** e não como um atributo da entidade `ALUNO`. O relacionamento `EMPRESTIMO` entre `ALUNO` e `LIVRO` é de que grau?
2. **Auto-relacionamento e Papéis:** Considere o conjunto de entidades `PESSOA`.
   - a) Modele um auto-relacionamento para representar o casamento civil monogâmico. Qual a sua cardinalidade ($1:1$, $1:N$ ou $N:M$)?
   - b) Modele um auto-relacionamento para representar a filiação biológica de paternidade. Quais papéis (*roles*) devem ser atribuídos às arestas? Qual a cardinalidade de pai para filho e de filho para pai?
3. **Razões de Cardinalidade:** Identifique e justifique a cardinalidade mais adequada para cada um dos seguintes relacionamentos do cotidiano:
   - a) `MEDICO` $\overset{\text{ATENDE}}{\longleftrightarrow}$ `PACIENTE` em uma consulta ambulatorial;
   - b) `CURSO` $\overset{\text{POSSUI}}{\longleftrightarrow}$ `TURMA`;
   - c) `CIDADAO` $\overset{\text{POSSUI}}{\longleftrightarrow}$ `PASSAPORTE`;
   - d) `AUTOR` $\overset{\text{ESCREVE}}{\longleftrightarrow}$ `LIVRO`.
4. **Participação e Linha Dupla:** Em um hospital, todo `LEITO` obrigatoriamente pertence a uma `ALA_HOSPITALAR`, mas uma ala recém-inaugurada pode ainda não possuir nenhum leito instalado.
   - a) Qual entidade possui participação total e qual possui participação parcial?
   - b) Como essa restrição é desenhada no diagrama canônico de Peter Chen?
   - c) Como essa restrição é expressa na notação estrutural $(min, max)$?
5. **Atributos de Relacionamento:** No relacionamento `CURSA` entre `ALUNO` e `DISCIPLINA`:
   - a) Por que o atributo `nota_final` não pode pertencer à entidade `ALUNO`?
   - b) Por que ele não pode pertencer à entidade `DISCIPLINA`?
   - c) Em que elemento do Diagrama de Peter Chen a elipse de `nota_final` deve ser conectada?

---

## 📚 7. Referências Bibliográficas

1. **CHEN, Peter Pin-Shan.** *The Entity-Relationship Model: Toward a Unified View of Data*. ACM Transactions on Database Systems (TODS), New York, v. 1, n. 1, p. 9–36, Mar. 1976.
2. **ELMASRI, Ramez; NAVATHE, Shamkant B.** *Sistemas de Banco de Dados*. 7. ed. São Paulo: Pearson Education do Brasil, 2018. (Capítulo 3: Modelagem de Dados Usando o Modelo Entidade-Relacionamento).
3. **HEUSER, Carlos Alberto.** *Projeto de Banco de Dados*. 6. ed. Porto Alegre: Bookman, 2009. (Capítulo 2: O Modelo Entidade-Relacionamento e Capítulo 3: Projeto Conceitual).
4. **SILBERSCHATZ, Abraham; KORTH, Henry F.; SUDARSHAN, S.** *Sistema de Banco de Dados*. 7. ed. Rio de Janeiro: Elsevier, 2020. (Capítulo 6: Projeto de Bancos de Dados e o Modelo E-R).
5. **DATE, C. J.** *Introdução a Sistemas de Bancos de Dados*. 8. ed. Rio de Janeiro: Elsevier / Campus, 2004.
