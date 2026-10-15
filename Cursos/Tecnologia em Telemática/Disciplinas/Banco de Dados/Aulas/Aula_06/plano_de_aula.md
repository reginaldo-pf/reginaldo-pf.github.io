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
2. **Exemplos Didáticos e Cotidianos de Fácil Identificação:**
   - **Minimundo Hoteleiro e de Locação:** Entidade forte `HOTEL` e entidade fraca `QUARTO` (identificada unicamente pelo número do quarto dentro de cada hotel).
   - **Minimundo Corporativo de RH (Elmasri & Navathe):** Entidade forte `FUNCIONARIO` e entidade fraca `DEPENDENTE` (com discriminador `nome_dependente`).
   - **Minimundo de Gestão de Transportes/Frotas:** Superclasse `VEICULO` especializada nas subclasses `CARRO` e `CAMINHAO`.
3. **Associação Teórico-Computacional (Exemplos Pareados):** Apresentação das regras conceituais nos diagramas canônicos (retângulo duplo, losango duplo, linha dupla, discriminador tracejado e triângulos EER) seguida imediatamente pela validação algorítmica em Python orientado a objetos, simulando a integridade semântica em memória.
4. **Diagramas Canônicos e Notações Formais:** Uso de diagramas canônicos em TikZ no padrão de Peter Chen e no Modelo Entidade-Relacionamento Estendido (EER), priorizando a precisão conceitual e a clareza da modelagem de dados sem ilustrações genéricas descontextualizadas.

---

## 🎯 2. Objetivos de Aprendizagem

### Objetivo Geral
Capacitar os estudantes a identificar, formalizar e diagramar **entidades fracas** com suas respectivas dependências de existência e identificação, bem como projetar hierarquias conceituais de **especialização e generalização** no Modelo Entidade-Relacionamento Estendido (EER), aplicando restrições de disjunção e completude a cenários intuitivos do cotidiano.

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
| **1** | 00 - 15 min | **Acolhimento & Ponte Conceitual:** Retrospectiva da Aula 05 (relacionamentos e cardinalidades). Apresentação do desafio: e quando uma entidade não tem chave própria (ex: quartos de um hotel ou dependentes de um funcionário)? | Exposição dialogada e problema disparador. |
| **2** | 15 - 40 min | **Entidades Fracas e Relacionamentos Identificadores:** Conceito formal, entidade proprietária, chave parcial (discriminador) e notação canônica de Chen (retângulo duplo e losango duplo). | Slides Beamer (Widescreen 16:9) e diagramas canônicos em TikZ. |
| **3** | 40 - 65 min | **Modelo EER: Especialização e Generalização:** Conceito de superclasse/subclasse, herança de atributos e relacionamentos. Restrições de Disjunção ($d/o$) e Completude (Total/Parcial). | Diagramas EER comparativos com taxonomia de veículos. |
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
* **Slide 9:** Caso Cotidiano Hoteleiro: `HOTEL` $\overset{\text{POSSUI\_QUARTO}}{\Longleftrightarrow}$ `QUARTO`.
* **Slide 10:** Motivação do Modelo EER: Por que estender o Modelo Entidade-Relacionamento clássico?
* **Slide 11:** Conceito de Superclasse, Subclasse e Herança de Atributos/Relacionamentos.
* **Slide 12:** Especialização (*Top-Down*) vs. Generalização (*Bottom-Up*).
* **Slide 13:** Restrições de Disjunção: Especialização Disjunta ($d$) vs. Sobreposta ($o$).
* **Slide 14:** Restrições de Integralidade/Completude: Total (Linha Dupla) vs. Parcial (Linha Simples).
* **Slide 15:** Matriz Canônica de Combinações: ($d$, Total), ($d$, Parcial), ($o$, Total) e ($o$, Parcial).
* **Slide 16:** Diagrama EER em TikZ no Contexto de Veículos: `VEICULO` $\to$ `CARRO` / `CAMINHAO`.
* **Slide 17:** Laboratório Computacional em Python: Estrutura da Entidade Fraca e Verificação de Dependência.
* **Slide 18:** Laboratório Computacional em Python: Implementação de Hierarquia com Herança e Bloqueio de Disjunção.
* **Slide 19:** Síntese Conceitual, Checklist de Competências e Conexão com o Sábado Letivo (Aula 07 - AVP1).
* **Slide 20:** Referências Bibliográficas (Peter Chen, Elmasri & Navathe, Heuser, Silberschatz).

---

## 💻 5. Roteiro do Laboratório Prático Computacional (Python Puro)

1. **Construção do Metamodelo de Entidade Fraca:**
   - Criação da classe `Hotel` com chave primária intrínseca (`id_hotel`).
   - Criação da classe `Quarto` com atributo discriminador (`numero_quarto`).
   - Geração dinâmica da chave primária composta: `(id_hotel, numero_quarto)`.
   - Validação de que instâncias com o mesmo discriminador são permitidas em hotéis diferentes, mas bloqueadas no mesmo hotel.
2. **Construção do Metamodelo de Especialização/Generalização (EER):**
   - Criação da classe base `Veiculo` com atributos universais (`placa`, `marca`, `modelo`, `ano`).
   - Criação das classes derivadas `Carro` e `Caminhao` com atributos especializados e verificação de herança.
   - Implementação de validador de restrição de disjunção (`DISJUNTA` vs. `SOBREPOSTA`) e integralidade (`TOTAL` vs. `PARCIAL`).
3. **Cenários de Teste Executados:**
   - **Teste 1 (Entidade Fraca - Isolamento):** Tentar cadastrar um quarto sem vincular a um hotel e comprovar o bloqueio de dependência existencial.
   - **Teste 2 (Entidade Fraca - Discriminador Duplicado):** Cadastrar `Quarto 101` no Hotel Tauá e `Quarto 101` no Hotel Fortaleza (sucesso). Tentar cadastrar outro `Quarto 101` no Hotel Tauá (bloqueio por violação de discriminador).
   - **Teste 3 (EER - Herança de Atributos):** Instanciar um `Carro` e demonstrar o acesso aos atributos herdados (`placa`, `marca`, `modelo`) e específicos (`quantidade_portas`, `capacidade_porta_malas_litros`).
   - **Teste 4 (EER - Restrição Disjunta):** Tentar classificar uma instância de veículo simultaneamente como Carro e Caminhão e observar o disparo de erro semântico de disjunção ($d$).

---

## 📝 6. Exercícios de Fixação da Aula 06

1. **Conceito de Entidade Fraca e Dependência:**
   Em uma rede de hotéis, cada filial possui vários **Quartos** (ex: Quarto 101, Quarto 102). O número do quarto é único apenas dentro de cada hotel, mas se repete em outros estabelecimentos da mesma rede.
   - a) Por que a entidade `QUARTO` é classificada como fraca em relação à entidade `HOTEL`?
   - b) Qual é o discriminador de `QUARTO` e como é formada a sua chave identificadora completa?
   - c) Explique a diferença entre dependência existencial e dependência de identificação nesse cenário.

2. **Gramática Canônica de Peter Chen:**
   Desenhe ou descreva minuciosamente a representação gráfica canônica no DER de Peter Chen para a seguinte regra de negócio:
   *"Um funcionário cadastrado no RH (com CPF e nome) pode cadastrar seus dependentes para fins de plano de saúde. Um dependente possui apenas o primeiro nome e data de nascimento."*
   Indique os formatos gráficos exatos do retângulo, losango, linhas de participação e elipses de atributos.

3. **Caso de Dependência de Identificação:**
   Considere um condomínio residencial com vários **Blocos** de edifícios, onde cada bloco possui múltiplos **Apartamentos**. O número do apartamento (ex: 101, 202) se repete em cada bloco.
   - a) Modele o diagrama canônico contendo a entidade proprietária (`BLOCO`), a entidade fraca (`APARTAMENTO`) e o relacionamento identificador.
   - b) Se um bloco for demolido ou desativado, o que conceitualmente deve acontecer com os registros de seus apartamentos?

4. **Herança e Atributos no Modelo EER:**
   Em uma locadora de automóveis, a superclasse `VEICULO` possui os atributos `placa`, `marca`, `modelo` e `ano`. Ela é especializada nas subclasses `CARRO` (com atributos `quantidade_portas` e `capacidade_porta_malas`), `CAMINHAO` (com atributos `capacidade_carga_toneladas` e `quantidade_eixos`) e `MOTO` (com atributos `cilindradas` e `partida_eletrica`).
   - a) Explique o que é a herança de tipos e quais atributos uma instância de `CARRO` possui no total.
   - b) Essa especialização deve ser classificada como Disjunta ($d$) ou Sobreposta ($o$)? Justifique.
   - c) Ela deve ser classificada como Total ou Parcial? Justifique com base no domínio da locadora.

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
