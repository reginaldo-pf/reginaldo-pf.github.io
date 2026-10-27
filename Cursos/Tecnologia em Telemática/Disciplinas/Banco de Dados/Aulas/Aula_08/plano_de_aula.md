# Plano de Aula: 08 - Laboratório de Modelagem Conceitual com Ferramentas CASE (brModelo e Draw.io)

* **Curso:** Tecnologia em Telemática  
* **Componente Curricular:** Banco de Dados  
* **Docente Responsável:** Prof. Me. Reginaldo Fernandes  
* **Semestre Letivo:** 2026.2  
* **Carga Horária:** 2 h/a (100 minutos)  
* **Data da Aula:** 20 de Outubro de 2026 (Terça-feira)  
* **Módulo:** Unidade III (N1) — Laboratório Prático de Modelagem Conceitual e Construção do DER/EER e Dicionário de Dados da AVP1  

---

## 🧭 1. Princípios e Diretrizes Pedagógicas da Aula

1. **Ponte Direta com o Sábado Letivo (Aula 07):** Na Aula 07, o aluno definiu o escopo textual do minimundo e elaborou o rascunho preliminar à mão do seu Projeto Prático (AVP1). Nesta **Aula 08**, o foco é transformar esse rascunho conceitual em um **artefato técnico de nível profissional**, combinando a **modelagem gráfica em ferramentas CASE** com a **modelagem descritiva e textual (Dicionário de Dados)**.
2. **Domínio Comparativo de Duas Abordagens CASE (brModelo vs. Draw.io):**
   - **brModelo (Web / Desktop 3.x):** Ferramenta acadêmica consagrada no Brasil, fundamentada no livro de **Carlos Alberto Heuser**. Utiliza atributos com pinos/círculos preenchidos (identificador) e vazios (descritores), cardinalidades $(min, max)$ posicionadas junto às entidades e triângulos de especialização com restrições $(t/p, e/c)$.
   - **Draw.io / diagrams.net:** Ferramenta de diagramação vetorial universal que possui a biblioteca *Entity Relation*, permitindo desenhar fielmente a **gramática gráfica original de Peter Chen (1976)** e **Elmasri & Navathe** (elipses conectadas, sublinhado contínuo/tracejado, elipses duplas/tracejadas, retângulos e losangos duplos e círculos $d/o$).
3. **Modelagem Descritiva e Textual Complementar (Dicionário de Dados Conceitual):** Um diagrama gráfico DER/EER, por mais completo que seja, não explicita regras semânticas de domínio, fórmulas de cálculo de atributos derivados ou restrições de negócio complexas. Por isso, o estudante aprende a elaborar a **Especificação Tabular de Entidades/Atributos** e a **Matriz Descritiva de Relacionamentos e Papéis** para compor a documentação oficial da AVP1.

---

## 🎯 2. Objetivos de Aprendizagem

### Objetivo Geral
Capacitar o estudante a utilizar ferramentas CASE de modelagem de dados (**brModelo** e **Draw.io**) para construir, validar, documentar e exportar o Diagrama Entidade-Relacionamento Estendido (DER/EER) e o Dicionário de Dados Conceitual do seu Projeto Prático (AVP1), compreendendo as equivalências notacionais entre o padrão internacional de **Peter Chen / Elmasri** e o padrão brasileiro de **Carlos Alberto Heuser**.

### Objetivos Específicos
1. **Conceito e Arquitetura de Ferramentas CASE:** Compreender a diferença entre uma simples ferramenta de desenho vetorial e uma ferramenta CASE dotada de metamodelo semântico e catálogo de metadados.
2. **Equivalência Notacional Chen vs. Heuser:** Traduzir sem perda semântica as formas geométricas de atributos (PK, simples, composto, multivalorado, derivado), participação (linha simples/dupla vs. cardinalidade mínima $0/1$) e especialização EER ($d/o$ vs. $e/c$, Total/Parcial vs. $t/p$).
3. **Operação Prática no brModelo:** Criar entidades, adicionar atributos identificadores e compostos com pinos gráficos, configurar relacionamentos binários e autorrelacionamentos com papéis (*roles*) e aplicar o triângulo de especialização/generalização.
4. **Operação Prática no Draw.io (diagrams.net):** Ativar a paleta *Entity Relation*, configurar elipses duplas (multivalorados), elipses tracejadas (derivados), losangos e retângulos com borda dupla (entidades fracas) e exportar em alta resolução (PDF vetorial / PNG 300 DPI).
5. **Padrões de Qualidade Estética e Eliminação de Antipadrões:** Aplicar convenções de nomenclatura (`SUBSTANTIVO_SINGULAR` em caixa alta para entidades, `VERBO_ATIVO` para relacionamentos e `snake_case` para atributos), organização topológica sem cruzamento de linhas e proibição estrita de chaves estrangeiras (FK) no nível conceitual.
6. **Modelagem Descritiva e Textual (Dicionário de Dados):** Elaborar as tabelas formais do Dicionário de Dados Conceitual (classificação morfológica de atributos, obrigatoriedade, unicidade e regras de negócio) e a Matriz de Relacionamentos.

---

## ⏱️ 3. Cronograma da Aula (100 Minutos)

| Bloco | Duração | Descrição das Atividades | Metodologia & Recursos |
| :---: | :---: | :--- | :--- |
| **1** | 00 - 15 min | **Revisão do Escopo AVP1 & Introdução às Ferramentas CASE:** Inspeção rápida do formulário preenchido na Aula 07. O que é uma ferramenta CASE e por que documentar esquemas de banco de dados profissionalmente? | Exposição dialogada e revisão de escopo. |
| **2** | 15 - 35 min | **Comparativo de Notações: Peter Chen (Draw.io) vs. Heuser (brModelo):** Tradução visual de formas geométricas para atributos, relacionamentos, entidades fracas e hierarquias EER ($d/o \leftrightarrow e/c$). | Slides Beamer 16:9 com diagramas comparativos lado a lado em TikZ. |
| **3** | 35 - 65 min | **Laboratório Guiado Mão na Massa (brModelo & Draw.io):** Construção passo a passo do DER/EER do projeto do aluno (entidades fortes, atributos especiais, relacionamentos $1:1, 1:N, N:M$, auto-relacionamento, entidade fraca e EER). | Prática assistida em computador (Mentoria 1-para-1). |
| **4** | 65 - 85 min | **Modelagem Descritiva e Textual (Dicionário de Dados e Auditoria Visual):** Construção das tabelas do Dicionário de Dados Conceitual e inspeção visual contra antipadrões (ex: ausência de FKs e papéis explícitos). | Elaboração documental tabular e checklist de qualidade CASE. |
| **5** | 85 - 100 min | **Exportação Vetorial, Checklist de Qualidade e Ponte para a Aula 09:** Exportação do DER em PDF/PNG, revisão final e introdução ao próximo passo da disciplina: o **Modelo Relacional Formal (Codd, 1970)** na Aula 09. | Fechamento e verificação do entregável AVP1. |

---

## 📊 4. Slides da Apresentação (24 Lâminas em Beamer 16:9)

* **Slides 1 a 4:** Capa Institucional, Agenda, Ponte Pedagógica (Do Papel ao CASE) e Objetivos de Aprendizagem.
* **Slides 5 e 6:** O Que é uma Ferramenta CASE (Desenho vs. Metamodelo Semântico) e Panorama de Ferramentas (brModelo e Draw.io).
* **Slides 7 a 11:** O Duelo de Notações no Brasil: Comparativos Visuais em TikZ de Atributos (PK, Simples, Composto, Multivalorado, Derivado), Cardinalidades (Linha Dupla vs. $(min, max)$), Entidade Fraca e Especialização EER ($d/o$ vs. Triângulo $(t/p, e/c)$).
* **Slides 12 a 14:** Guia Prático do **brModelo**: Formas Geométricas Nativas, Posição Invertida das Cardinalidades e Estudo de Caso Clínica "VidaPlena" na Notação de Heuser.
* **Slides 15 e 16:** Guia Prático do **Draw.io (diagrams.net)**: Paleta Visual *Entity Relation* de Peter Chen e Estudo de Caso Clínica "VidaPlena" na Notação Clássica de Chen.
* **Slides 17 e 18:** Boas Práticas de Layout Topológico e Comparação Visual de Antipadrões ("Errado vs. Certo" no DER).
* **Slides 19 a 21:** Modelagem Descritiva e Textual: O Papel do Dicionário de Dados Conceitual, Especificação Tabular de Entidades/Atributos e Matriz Descritiva de Relacionamentos.
* **Slides 22 a 24:** Checklist Final de Qualidade do DER/EER (AVP1), Exercícios de Fixação e Referências Bibliográficas.

---

## 📐 5. Roteiro do Laboratório Prático (Modelagem Gráfica + Descritiva)

1. **Etapa 1 — Configuração da Área de Trabalho no Draw.io ou brModelo:**
   - Definir página em formato **A4 Paisagem (*Landscape*)** ou tela infinita com grade ativa (*Grid* 10px).
   - Configurar fonte padrão sem serifa (`Inter`, `Helvetica` ou `Nunito Sans`).
2. **Etapa 2 — Posicionamento Topológico das Entidades:**
   - Posicionar as entidades principais (fortes e superclasses) no centro do diagrama e as entidades subordinadas (fracas e especializações) nas extremidades para evitar cruzamento de linhas.
   - Aplicar nomes no singular e em letras maiúsculas (`PACIENTE`, `MEDICO`, `DEPARTAMENTO_CLINICO`).
3. **Etapa 3 — Adição da Taxonomia Geométrica de Atributos:**
   - Inserir chaves primárias com sublinhado sólido na elipse (Draw.io) ou pino preto preenchido (brModelo).
   - Inserir o atributo composto ramificado, o atributo multivalorado (elipse dupla ou cardinalidade $(1, n)$) e o atributo derivado (elipse tracejada).
4. **Etapa 4 — Conexão de Relacionamentos e Hierarquia EER:**
   - Traçar os relacionamentos $1:1$, $1:N$, $N:M$ (com atributo próprio ligado ao losango) e o auto-relacionamento com rótulos de papéis explícitos nas arestas.
   - Desenhar a entidade fraca com retângulo duplo, losango duplo, linha dupla e discriminador sublinhado tracejado.
   - Desenhar a árvore de especialização EER indicando explicitamente as restrições ($d/o$ e linha dupla/simples, ou triângulo $(t/p, e/c)$).
5. **Etapa 5 — Elaboração do Dicionário de Dados Descritivo e Auditoria Visual:**
   - Construir a Tabela de Especificação de Atributos (Nome, Entidade, Classificação Conceitual, Domínio Semântico, Obrigatoriedade e Regra de Negócio).
   - Construir a Matriz de Relacionamentos (Losango, Entidades Conectadas, Cardinalidades em Chen e Heuser, Participação e Atributos Próprios).
   - Auditar visualmente o diagrama garantindo que **nenhuma chave estrangeira (`_fk`)** foi desenhada como atributo no DER.

---

## 📝 6. Exercícios de Fixação da Aula 08

1. **Equivalência de Notações (Chen vs. Heuser/brModelo):**
   Durante uma entrevista técnica ou análise de documentação legada, você encontrará diagramas feitos tanto no padrão internacional de Peter Chen quanto no padrão brasileiro do brModelo (Carlos Alberto Heuser).
   - a) Como um **atributo identificador (PK)**, um **atributo composto** e um **atributo multivalorado** são representados geometricamente no brModelo em comparação às elipses de Peter Chen?
   - b) Na notação de Heuser (brModelo), o que significam as siglas **(t, e)** e **(p, c)** posicionadas ao lado do triângulo de especialização/generalização? Qual é a equivalência exata no modelo EER de Elmasri & Navathe?

2. **Leitura de Cardinalidades $(min, max)$ no brModelo:**
   Considere o relacionamento `MEDICO` `(0, 1)` ——— `<> DIRIGE <>` ——— `(1, 1)` `DEPARTAMENTO`.
   - a) Explique o significado da cardinalidade mínima `0` e máxima `1` posicionada ao lado de `MEDICO` na convenção adotada pelo brModelo/Heuser.
   - b) Como essa mesma regra é representada usando linhas simples/duplas e razão de cardinalidade no DER clássico de Peter Chen?

3. **Detecção de Erros Sintáticos e Antipadrões em Ferramentas CASE:**
   Um estudante construiu um DER para uma biblioteca e cometeu os seguintes equívocos na ferramenta CASE:
   - I. Criou a entidade `EMPRESTIMOS` como um retângulo regular sem chave primária, ligando `LEITOR` a `EMPRESTIMOS` e `EMPRESTIMOS` a `LIVRO`, além de colocar outro losango `REALIZA` entre eles.
   - II. Conectou diretamente o retângulo `AUTOR` ao retângulo `LIVRO` por uma linha reta sem nenhum losango intermediário.
   - III. Criou um atributo `cpf_cliente_fk` dentro da entidade `PEDIDO` para tentar ligar o pedido ao cliente.
   Identifique qual regra formal do Modelo Entidade-Relacionamento foi violada em cada um dos três itens (I, II e III) e explique como corrigi-los graficamente na ferramenta CASE.

4. **Modelagem Descritiva e Dicionário de Dados Complementar:**
   Mesmo um diagrama DER/EER perfeitamente desenhado no Draw.io ou brModelo não consegue expressar todas as regras de domínio de um sistema. Cite **três informações cruciais** que não aparecem no desenho gráfico do DER e que devem obrigatoriamente constar no **Dicionário de Dados Conceitual**.

5. **Prática de Laboratório (Entregável AVP1):**
   Utilizando o escopo validado na Aula 07, construa o diagrama conceitual completo no **Draw.io** ou **brModelo**, exporte-o em formato PDF/PNG de alta definição e elabore o Dicionário de Dados tabular descritivo do seu projeto.

---

## 📚 7. Referências Bibliográficas

* **HEUSER, Carlos Alberto.** *Projeto de Banco de Dados*. 6. ed. Porto Alegre: Bookman, 2009.
* **CHEN, Peter Pin-Shan.** *The Entity-Relationship Model: Toward a Unified View of Data*. ACM Transactions on Database Systems (TODS), v. 1, n. 1, p. 9–36, 1976.
* **ELMASRI, Ramez; NAVATHE, Shamkant B.** *Sistemas de Banco de Dados*. 7. ed. São Paulo: Pearson Education do Brasil, 2018.
* **SILBERSCHATZ, Abraham; KORTH, Henry F.; SUDARSHAN, S.** *Sistema de Banco de Dados*. 7. ed. Rio de Janeiro: Elsevier, 2020.
* **CANDIDO, Carlos H.** *brModelo Web & Desktop: Modelagem Conceitual e Lógica de Bancos de Dados*. Disponível em: https://www.brmodeloweb.com.
