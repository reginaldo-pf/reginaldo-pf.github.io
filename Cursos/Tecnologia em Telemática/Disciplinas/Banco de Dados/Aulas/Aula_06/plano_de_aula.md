# Plano de Aula: 06 - Entidades Fracas e Modelo EER (Especialização/Generalização)

* **Curso:** Tecnologia em Telemática  
* **Componente Curricular:** Banco de Dados  
* **Docente Responsável:** Prof. Me. Reginaldo Fernandes  
* **Semestre Letivo:** 2026.2  
* **Carga Horária:** 2 h/a (100 minutos)  
* **Data da Aula:** 14 de Outubro de 2026 (Quarta-feira)  
* **Módulo:** Unidade III (N1) — Modelagem Conceitual Avançada no MER/EER  

---

## 🧭 1. Princípios e Diretrizes Pedagógicas da Aula

1. **Foco Estritamente Conceitual (Sem DDL/SQL):** Nesta fase da Unidade III (N1), a formalização é centrada na semântica de alto nível dos dados. O objetivo é capacitar os alunos a distinguir entidades autônomas de entidades subordinadas e a categorizar taxonomias organizacionais antes de qualquer código SQL de criação de tabelas (`CREATE TABLE`).
2. **Exemplos Pareados e Minimundos Práticos de Telemática e Negócios:**
   - **Minimundo de Infraestrutura de Redes (Telemática):** Entidade forte `DISPOSITIVO_REDE` e entidade fraca `PORTA_INTERFACE` (identificada unicamente pelo número da porta dentro de cada roteador). Especialização de `DISPOSITIVO` em `ROTEADOR` e `SWITCH`.
   - **Minimundo Corporativo/Empresarial (Elmasri & Navathe):** Entidade forte `FUNCIONARIO` e entidade fraca `DEPENDENTE` (com discriminador `nome_dependente`). Especialização de `FUNCIONARIO` em `ENGENHEIRO`, `SECRETARIO` e `TECNICO`.
3. **Associação Teórico-Computacional (Exemplos Pareados):** Apresentação das regras conceituais nos diagramas canônicos (retângulo duplo, losango duplo, linha dupla, discriminador tracejado e triângulos EER) seguida imediatamente pela validação algorítmica em Python orientado a objetos, simulando a integridade semântica em memória.
4. **Diagramas Canônicos e Notações Formais:** Uso de diagramas canônicos em TikZ no padrão de Peter Chen e no Modelo Entidade-Relacionamento Estendido (EER), priorizando a precisão conceitual e a clareza da modelagem de dados sem ilustrações genéricas descontextualizadas.

---

## 🎯 2. Objetivos de Aprendizagem

### Objetivo Geral
Capacitar os estudantes a identificar, formalizar e diagramar **entidades fracas** com suas respectivas dependências de existência e identificação, bem como projetar hierarquias conceituais de **especialização e generalização** no Modelo Entidade-Relacionamento Estendido (EER), aplicando restrições de disjunção e completude a cenários de telecomunicações e sistemas corporativos.

### Objetivos Específicos
1. **Diferenciação Semântica Forte vs. Fraca:** Identificar situações em que uma entidade não possui atributos próprios suficientes para formar uma chave primária independente.
2. **Dependência Existencial e de Identificação:** Compreender por que a existência e a identificação de uma entidade fraca dependem obrigatoriamente de uma entidade proprietária (*owner entity*).
3. **Chave Parcial (Discriminador):** Definir o conceito de discriminador e entender como ele, em conjunto com a chave primária da entidade proprietária, forma a chave identificadora completa.
4. **Gramática Canônica de Peter Chen para Entidades Fracas:** Dominar a notação gráfica oficial: retângulo duplo para entidade fraca, losango duplo para relacionamento identificador, participação total (linha dupla) e elipse com sublinhado tracejado para o discriminador.
5. **Fundamentos do Modelo EER:** Compreender as motivações para a extensão do MER tradicional rumo à representação de superclasses e subclasses.
6. **Mecanismo de Herança de Tipos:** Aplicar a regra de herança universal de atributos e de relacionamentos da superclasse para suas subclasses.
7. **Restrições de Disjunção e Integralidade:** Classificar hierarquias em Disjuntas ($d$) vs. Sobrepostas ($o$) e Totais (linha dupla) vs. Parciais (linha simples).
8. **Simulação Computacional Pareada:** Implementar um metamodelo em Python demonstrando chaves compostas por dependência e validação de herança de instâncias em memória.

---

## ⏱️ 3. Cronograma da Aula (100 Minutos)

| Bloco | Duração | Descrição das Atividades | Metodologia & Recursos |
| :---: | :---: | :--- | :--- |
| **1** | 00 - 15 min | **Acolhimento & Ponte Conceitual:** Retrospectiva da Aula 05 (relacionamentos e cardinalidades). Apresentação do desafio: e quando uma entidade não tem chave própria (ex: portas de um switch ou dependentes de um funcionário)? | Exposição dialogada e problema disparador. |
| **2** | 15 - 40 min | **Entidades Fracas e Relacionamentos Identificadores:** Conceito formal, entidade proprietária, chave parcial (discriminador) e notação canônica de Chen (retângulo duplo e losango duplo). | Slides Beamer (Widescreen 16:9) e diagramas canônicos em TikZ. |
| **3** | 40 - 65 min | **Modelo EER: Especialização e Generalização:** Conceito de superclasse/subclasse, herança de atributos e relacionamentos. Restrições de Disjunção ($d/o$) e Completude (Total/Parcial). | Diagramas EER comparativos e estudo de caso em Telemática. |
| **4** | 65 - 85 min | **Laboratório Computacional em Python (Metamodelo EER):** Execução do script Python didático demonstrando a criação de entidades fracas com chaves compostas e hierarquias com herança estrita em memória. | Laboratório interativo em Python puro (sem SQL). |
| **5** | 85 - 100 min | **Síntese, Resolução de Dúvidas & Alinhamento AVP1:** Revisão das regras de ouro, esclarecimento de dúvidas conceituais e orientação para o sábado letivo (Aula 07 - Estudo Dirigido da AVP1). | Mentoria pedagógica e encerramento. |

---

## 📊 4. Slides Sugeridos e Roteiro de Apresentação

* **Slide 1:** Capa Institucional (Banco de Dados -- Aula 06: Entidades Fracas e Modelo EER).
* **Slide 2:** Agenda Temática do Encontro (8 seções modulares).
* **Slide 3:** Retrospectiva & Problema Desafiador: Entidades sem identidade própria autônoma.
* **Slide 4:** Objetivos de Aprendizagem da Aula 06.
* **Slide 5:** O Conceito Formal de Entidade Fraca (*Weak Entity*) e Dependência de Existência.
* **Slide 6:** Chave Parcial (*Discriminador*) e Formação da Chave Composta de Identificação.
* **Slide 7:** Notação Canônica de Peter Chen: Retângulo Duplo, Losango Duplo e Sublinhado Tracejado.
* **Slide 8:** Diagrama TikZ Completo: `FUNCIONARIO` $\overset{\text{POSSUI\_DEP}}{\Longleftrightarrow}$ `DEPENDENTE`.
* **Slide 9:** Caso Telemática: `DISPOSITIVO_REDE` $\overset{\text{CONTEM\_PORTA}}{\Longleftrightarrow}$ `PORTA_INTERFACE`.
* **Slide 10:** Motivação do Modelo EER: Por que estender o Modelo Entidade-Relacionamento clássico?
* **Slide 11:** Conceito de Superclasse, Subclasse e Herança de Atributos/Relacionamentos.
* **Slide 12:** Especialização (*Top-Down*) vs. Generalização (*Bottom-Up*).
* **Slide 13:** Restrições de Disjunção: Especialização Disjunta ($d$) vs. Sobreposta ($o$).
* **Slide 14:** Restrições de Integralidade/Completude: Total (Linha Dupla) vs. Parcial (Linha Simples).
* **Slide 15:** Matriz Canônica de Combinações: ($d$, Total), ($d$, Parcial), ($o$, Total) e ($o$, Parcial).
* **Slide 16:** Diagrama EER em TikZ no Contexto de Telemática: `DISPOSITIVO` $\to$ `ROTEADOR` / `SWITCH`.
* **Slide 17:** Laboratório Computacional em Python: Estrutura da Entidade Fraca e Verificação de Dependência.
* **Slide 18:** Laboratório Computacional em Python: Implementação de Hierarquia com Herança e Bloqueio de Disjunção.
* **Slide 19:** Síntese Conceitual, Checklist de Competências e Conexão com o Sábado Letivo (Aula 07 - AVP1).
* **Slide 20:** Referências Bibliográficas (Peter Chen, Elmasri & Navathe, Heuser, Silberschatz).

---

## 💻 5. Roteiro do Laboratório Prático Computacional (Python Puro)

1. **Construção do Metamodelo de Entidade Fraca:**
   - Criação da classe `EntidadeProprietaria` com chave primária intrínseca (ex: `ip_gestao` ou `cpf`).
   - Criação da classe `EntidadeFraca` com atributo discriminador (ex: `numero_porta` ou `nome_dependente`).
   - Geração dinâmica da chave primária composta: `(pk_proprietaria, discriminador)`.
   - Validação de que instâncias com o mesmo discriminador são permitidas em proprietários diferentes, mas bloqueadas no mesmo proprietário.
2. **Construção do Metamodelo de Especialização/Generalização (EER):**
   - Criação da classe base `Superclasse` com atributos gerais e dicionário polimórfico de instâncias.
   - Criação das classes derivadas `Subclasse` com atributos especializados e verificação de herança.
   - Implementação de validador de restrição de disjunção (`DISJUNTA` vs. `SOBREPOSTA`) e integralidade (`TOTAL` vs. `PARCIAL`).
3. **Cenários de Teste Executados:**
   - **Teste 1 (Entidade Fraca - Isolamento):** Tentar cadastrar uma porta sem vincular a um dispositivo e comprovar o bloqueio de dependência existencial.
   - **Teste 2 (Entidade Fraca - Discriminador Duplicado):** Cadastrar `Porta 1` no Switch `SW-01` e `Porta 1` no Router `RT-01` (sucesso). Tentar cadastrar outra `Porta 1` no `SW-01` (bloqueio por violação de discriminador).
   - **Teste 3 (EER - Herança de Atributos):** Instanciar um `Roteador` e demonstrar o acesso aos atributos herdados (`patrimonio`, `fabricante`) e específicos (`protocolos_roteamento`).
   - **Teste 4 (EER - Restrição Disjunta):** Tentar classificar uma instância disjunta simultaneamente em duas subclasses incompatíveis e observar o disparo de erro semântico.

---

## 📝 6. Exercícios de Fixação da Aula 06

1. **Conceito de Entidade Fraca e Dependência:**
   Em uma universidade, cada disciplina oferece anualmente várias **Turmas** (ex: Turma A, Turma B). As turmas são identificadas apenas pela letra dentro da disciplina e do semestre.
   - a) Por que a entidade `TURMA` é classificada como fraca em relação à entidade `DISCIPLINA`?
   - b) Qual é o discriminador de `TURMA` e como é formada a sua chave identificadora completa?
   - c) Explique a diferença entre dependência existencial e dependência de identificação nesse cenário.

2. **Gramática Canônica de Peter Chen:**
   Desenhe ou descreva minuciosamente a representação gráfica canônica no DER de Peter Chen para a seguinte regra de negócio:
   *"Um funcionário cadastrado no RH (com CPF e nome) pode cadastrar seus dependentes para fins de plano de saúde. Um dependente possui apenas o primeiro nome e data de nascimento."*
   Indique os formatos gráficos exatos do retângulo, losango, linhas de participação e elipses de atributos.

3. **Caso de Telemática: Portas e Roteadores:**
   Um provedor regional de internet (ISP) gerencia centenas de roteadores de borda. Cada roteador possui um endereço IP de gestão exclusivo (`ip_gestao`). Cada roteador possui de 4 a 48 interfaces de rede, nomeadas localmente como `eth0`, `eth1`, etc.
   - a) Modele o diagrama canônico contendo a entidade proprietária, a entidade fraca e o relacionamento identificador.
   - b) Se um roteador for desativado e removido do sistema, o que conceitualmente deve acontecer com os registros de suas portas de interface?

4. **Herança e Atributos no Modelo EER:**
   Em um sistema de telecomunicações, a superclasse `EQUIPAMENTO_REDE` possui os atributos `numero_serie`, `fabricante` e `data_aquisicao`. Ela é especializada nas subclasses `ROTEADOR` (com atributo `capacidade_throughput`), `ANTENA` (com atributos `frequencia_operacao` e `ganho_dbi`) e `SERVIDOR_RACK` (com `quantidade_nucleos` e `memoria_ram_gb`).
   - a) Explique o que é a herança de tipos e quais atributos uma instância de `ANTENA` possui no total.
   - b) Essa especialização deve ser classificada como Disjunta ($d$) ou Sobreposta ($o$)? Justifique.
   - c) Ela deve ser classificada como Total ou Parcial? Justifique com base no domínio de telecomunicações.

5. **Restrições de Especialização e Matriz de Decisão:**
   Considere o domínio de um hospital universitário com a superclasse `PESSOA`.
   - a) Apresente um exemplo do minimundo em que a especialização seja **Sobreposta ($o$) e Parcial**.
   - b) Apresente um exemplo do minimundo em que a especialização seja **Disjunta ($d$) e Total**.
   - c) O que acontece com a integridade do banco de dados se uma aplicação tentar cadastrar um indivíduo em duas subclasses de uma especialização definida formalmente como disjunta?

---

## 📚 7. Referências Bibliográficas

* **CHEN, Peter Pin-Shan.** *The Entity-Relationship Model: Toward a Unified View of Data*. ACM Transactions on Database Systems (TODS), New York, v. 1, n. 1, p. 9–36, Mar. 1976.
* **ELMASRI, Ramez; NAVATHE, Shamkant B.** *Sistemas de Banco de Dados*. 7. ed. São Paulo: Pearson Education do Brasil, 2018. (Capítulo 3: Modelagem Conceitual e Capítulo 4: O Modelo Entidade-Relacionamento Estendido - EER).
* **HEUSER, Carlos Alberto.** *Projeto de Banco de Dados*. 6. ed. Porto Alegre: Bookman, 2009. (Capítulo 2: O Modelo Entidade-Relacionamento e Capítulo 3: Generalização e Especialização).
* **SILBERSCHATZ, Abraham; KORTH, Henry F.; SUDARSHAN, S.** *Sistema de Banco de Dados*. 7. ed. Rio de Janeiro: Elsevier, 2020. (Capítulo 6: Projeto de Bancos de Dados e o Modelo E-R Estendido).
* **DATE, C. J.** *Introdução a Sistemas de Bancos de Dados*. 8. ed. Rio de Janeiro: Elsevier / Campus, 2004.
