# Plano de Aula 14: Cálculo Relacional (CRT e CRD) e Princípios de Otimização de Consultas

## 1. Identificação
* **Instituição:** Instituto Federal de Educação, Ciência e Tecnologia do Ceará (IFCE) — Campus Tauá
* **Curso:** Tecnologia em Telemática
* **Disciplina:** Banco de Dados
* **Professor:** Prof. Me. Reginaldo Fernandes
* **Unidade Temática:** Unidade II — Fundamentos do Modelo Relacional e Linguagens Formais de Consulta (Cálculo Relacional e Otimização)
* **Data Prevista:** 11/11/2026 (Quarta-feira)
* **Carga Horária:** 2 horas-aula (100 minutos)
* **Regime Didático:** Mentoria Individual / PBL (Aprendizagem Baseada em Problemas)

---

## 2. Objetivos de Aprendizagem

### Objetivo Geral
Capacitar o discente a compreender o paradigma declarativo formal das linguagens de consulta através do **Cálculo Relacional de Tuplas (CRT)** e do **Cálculo Relacional de Domínios (CRD)** fundamentados na Lógica de Predicados de Primeira Ordem, reconhecendo o Teorema da Equivalência de Codd, os critérios de segurança de fórmulas e aplicando as heurísticas e equivalências da Álgebra Relacional que regem o **Otimizador de Consultas (*Query Optimizer*)** dos SGBDs relacionais modernos.

### Objetivos Específicos
Ao final desta aula, o discente será capaz de:
1. **Compreender a Dualidade Epistemológica (Procedural vs. Declarativo):**
   - Diferenciar a abordagem procedural da Álgebra Relacional (*"como obter o resultado através de uma sequência de operações"*) da abordagem declarativa e lógica do Cálculo Relacional (*"o que obter como resultado, especificando predicados e propriedades desejadas"*).
   - Compreender por que a linguagem SQL comercial foi concebida sobre os alicerces do Cálculo Relacional, delegando a estratégia de execução procedimental ao SGBD.
2. **Dominar o Cálculo Relacional de Tuplas (CRT / TRC):**
   - Formular consultas na sintaxe canônica $\{ t \mid P(t) \}$, onde $t$ é uma variável que representa tuplas completas de uma relação.
   - Construir fórmulas bem formadas combinando átomos de pertinência ($t \in R$), comparações de atributos ($t[A] \ \theta \ s[B]$) e constantes ($t[A] \ \theta \ c$), utilizando conectivos lógicos ($\land, \lor, \neg, \to$) e quantificadores existenciais ($\exists$) e universais ($\forall$).
3. **Analisar a Segurança das Expressões no Cálculo (*Safety*):**
   - Diagnosticar o perigo de fórmulas matematicamente sintáticas que geram relações infinitas (ex: $\{ t \mid \neg(t \in R) \}$).
   - Definir formalmente o **Domínio de uma Fórmula** ($DOM(\psi)$) e provar por que os SGBDs exigem restrição estrita a expressões seguras (*Safe Expressions*).
4. **Dominar o Cálculo Relacional de Domínios (CRD / DRC):**
   - Formular consultas na sintaxe $\{ \langle x_1, x_2, \dots, x_n \rangle \mid P(x_1, \dots, x_n) \}$, onde cada variável $x_i$ assume valores sobre o domínio de um atributo individual.
   - Compreender a relevância histórica do CRD como base conceitual da linguagem visual interativa **QBE (Query By Example)** da IBM.
5. **Compreender o Teorema de Codd e a Completude Relacional:**
   - Explicar a equivalência matemática formal provada por Edgar F. Codd em 1972: $\text{Álgebra Relacional} \equiv \text{CRT Seguro} \equiv \text{CRD Seguro}$.
   - Definir o conceito de **Completude Relacional (*Relational Completeness*)** como régua avaliativa de linguagens de consulta em SGBDs.
6. **Dominar os Princípios e Heurísticas de Otimização de Consultas (*Query Optimization*):**
   - Compreender o pipeline interno do SGBD: Consulta Declarativa (SQL) $\to$ Parser $\to$ Árvore Canônica de Álgebra Relacional $\to$ Otimizador Lógico $\to$ Otimizador Físico $\to$ Plano de Execução.
   - Aplicar as regras canônicas de equivalência algébrica: comutatividade/associatividade de junções, comutatividade de seleções e a heurística fundamental do **Push-Down Selection e Push-Down Projection** ("empurrar seleções e projeções para baixo na árvore").
   - Comparar quantitativamente planos não otimizados versus planos otimizados calculando a redução drástica de tuplas intermediárias.

---

## 3. Cronograma Pedagógico (100 Minutos — 5 Blocos)

| Bloco | Tempo | Etapa Didática | Conteúdos e Metodologia | Recursos |
| :--- | :--- | :--- | :--- | :--- |
| **Bloco 1** | 15 min | **O Paradigma Declarativo & Fundamentos Lógicos** | Por que o desenvolvedor não deve programar loops procedurais? A visão de Codd: a Lógica de Predicados de Primeira Ordem como linguagem de especificação de dados. O que é o Cálculo Relacional? Álgebra vs. Cálculo lado a lado. | Slides 1 a 6 |
| **Bloco 2** | 25 min | **Cálculo Relacional de Tuplas (CRT)** | Variáveis de tupla, átomos, fórmulas bem formadas. Quantificador existencial ($\exists$) e universal ($\forall$). Regras de De Morgan aplicadas a consultas. Tradução de consultas cotidianas para o formalismo do CRT. | Slides 7 a 15 |
| **Bloco 3** | 15 min | **Segurança de Expressões & Cálculo de Domínios (CRD)** | O problema das relações infinitas. O Domínio da Fórmula ($DOM(\psi)$) e expressões seguras. O Cálculo Relacional de Domínios (CRD): variáveis de atributos e o nascimento do paradigma QBE (IBM). | Slides 16 a 22 |
| **Bloco 4** | 25 min | **Teorema de Codd & Otimização de Consultas** | Completude Relacional. Do SQL à execução física: a Árvore de Consulta Canônica. Catálogo de equivalências algébricas. Heurística de ouro: *Push-down selection* e *Push-down projection*. Análise de árvores TikZ com cálculo de tuplas intermediárias. | Slides 23 a 31 |
| **Bloco 5** | 20 min | **Oficina de Exercícios & Síntese Comparativa** | Resolução passo a passo de 4 desafios práticos (conversão Álgebra $\leftrightarrow$ CRT $\leftrightarrow$ SQL e refatoração de árvores de consulta). Quadro comparativo das 3 linguagens formais. Orientações para a Lista de Exercícios 02 (N1). | Slides 32 a 40 |

---

## 4. Roteiro Detalhado dos Slides (`materiais/main.pdf`)

1. **Capa Institucional:** Aula 14 — Cálculo Relacional (CRT e CRD) e Princípios de Otimização de Consultas.
2. **Agenda do Encontro:** Sumário modular dividindo os conteúdos em 9 blocos temáticos.
3. **Ponte Pedagógica: O que Consolidamos nas Aulas 12 e 13?** A Álgebra Relacional como linguagem formal procedural completa ($\sigma, \pi, \rho, \cup, -, \times, \bowtie, \div$).
4. **O Paradigma Declarativo: Por que o Cálculo?** A necessidade de expressar *o que* se deseja sem engessar a estratégia computacional do algoritmo.
5. **A Raiz Formal: Lógica de Predicados de Primeira Ordem:** Tuplas como proposições lógicas que avaliam como Verdadeiro ou Falso.
6. **Divisor de Seção:** Cálculo Relacional de Tuplas (CRT / TRC).
7. **Sintaxe Fundamental do CRT:** Estrutura $\{ t \mid P(t) \}$, definição da variável de tupla livre $t$ e da fórmula de filtragem $P(t)$.
8. **Anatomia dos Átomos do CRT:** Pertinência ($t \in R$), comparação de atributos ($t[A] \ \theta \ s[B]$) e constantes ($t[A] \ \theta \ c$).
9. **Quantificadores Lógicos no CRT:** O Quantificador Existencial ($\exists s \in R$) para relacionar tuplas e o Quantificador Universal ($\forall s \in R$) para requisitos totais.
10. **Consultas Simples em CRT:** Seleções e projeções expressas formalmente no CRT (exemplos com instâncias de provedor de internet e redes).
11. **Junções Expressas em CRT:** Como o quantificador existencial ($\exists$) conecta chaves primárias e estrangeiras declarativamente.
12. **Divisor de Seção:** Segurança de Expressões e Relações Infinitas.
13. **O Perigo das Fórmulas Inseguras:** Fórmulas sintaticamente corretas na lógica que exigiriam a alocação de todo o universo complementar infinito.
14. **O Domínio da Fórmula ($DOM(\psi)$):** Conjunto finito de constantes presentes na consulta ou nas instâncias das relações envolvidas.
15. **Critério de Segurança de Codd:** Fórmulas onde todo valor retornado pertence obrigatoriamente a $DOM(\psi)$.
16. **Divisor de Seção:** Cálculo Relacional de Domínios (CRD / DRC).
17. **Sintaxe Fundamental do CRD:** Notação $\{ \langle x_1, \dots, x_n \rangle \mid P(x_1, \dots, x_n) \}$ operando sobre variáveis de valores de atributos.
18. **Comparativo Lado a Lado: CRT vs. CRD:** Contrastes sintáticos, escopo de variáveis e facilidade de mapeamento.
19. **O Impacto do CRD na Indústria: Query By Example (QBE):** A interface tabular visual concebida por Moshé Zloof na IBM inspirada no CRD.
20. **Divisor de Seção:** O Teorema de Codd e a Completude Relacional.
21. **O Teorema da Equivalência de Edgar F. Codd (1972):** Prova matemática de que Álgebra Relacional, CRT Seguro e CRD Seguro possuem rigorosamente o mesmo poder expressivo.
22. **O Conceito de Linguagem Relacionalmente Completa:** Requisito formal para que uma linguagem de banco de dados comercial (como o SQL) seja considerada completa.
23. **Por que o SQL Adotou a Sintaxe do Cálculo?** Mapeamento direto: `SELECT` (projeção/variável livre) `FROM` (pertinência $\in$) `WHERE` (predicado $P(t)$).
24. **Divisor de Seção:** Princípios de Otimização de Consultas (*Query Optimization*).
25. **O Pipeline Interno do SGBD:** Da instrução SQL submetida pelo usuário ao plano de execução físico com varredura de discos e índices.
26. **A Árvore de Consulta Canônica:** Como o parser traduz a sintaxe SQL diretamente em uma árvore algébrica ingênua (produtos cartesianos no fundo, filtros no topo).
27. **Catálogo de Regras de Equivalência Algébrica:** Comutatividade, associatividade, distribuição de operadores e cascatas.
28. **Heurística Fundamental 1: Empurrar Seleções para Baixo (*Push-Down Selection*):** Redução drástica de cardinalidade antes da realização de cruzamentos pesados.
29. **Heurística Fundamental 2: Empurrar Projeções para Baixo (*Push-Down Projection*):** Redução do tamanho das tuplas intermediárias em memória.
30. **Estudo de Caso Visual com TikZ:** Árvore não otimizada ($100.000$ tuplas) vs. Árvore otimizada ($10$ tuplas) comparadas lado a lado.
31. **Divisor de Seção:** Exercícios e Desafios Práticos Resolvidos.
32. **Desafio 1 (Tradução Tripla):** Consulta de clientes VIP formulada em Álgebra Relacional, CRT e SQL.
33. **Desafio 2 (Quantificação Universal):** Formulação da exigência "clientes que contrataram todos os planos básicos" em CRT com $\forall$ e sua transformação via De Morgan com $\exists$.
34. **Desafio 3 (Análise de Segurança):** Identificação e correção de expressão insegura com negação irrestrita.
35. **Desafio 4 (Refatoração de Árvore de Consulta):** Otimização de uma árvore canônica calculando a economia de tuplas intermediárias.
36. **Síntese Executiva:** Quadro comparativo definitivo: Álgebra vs. CRT vs. CRD vs. SQL.
37. **Checklist de Aprendizagem:** Autoavaliação do discente para consolidação da Unidade II (N1).
38. **Orientações para o Sábado Letivo (Aula 15):** Apresentação da Lista de Exercícios 02 (N1) assíncrona.
39. **Ponte Pedagógica para a Unidade IV (Aula 16):** Introdução à Teoria do Projeto Relacional e Normalização (Dependências Funcionais).
40. **Referências Bibliográficas:** Obras clássicas de Codd, Elmasri & Navathe, Heuser, Silberschatz e Date.

---

## 5. Guia Conceitual Completo: Cálculo Relacional e Otimização

### 5.1 O Paradigma do Cálculo Relacional de Tuplas (CRT)
O CRT especifica o resultado de uma consulta descrevendo as propriedades lógicas que as tuplas desejadas devem satisfazer:
$$\{ t \mid P(t) \}$$
Onde:
* $t$ é a **variável de tupla livre** cujo esquema define a relação resultante.
* $P(t)$ é uma fórmula bem formada composta por átomos conectados por $\land, \lor, \neg, \to$ e quantificadores.

#### Átomos Legais no CRT:
1. **Pertinência:** $t \in R$, indicando que $t$ é uma tupla da relação $R$.
2. **Comparação de Atributos:** $t[A] \ \theta \ s[B]$, onde $A$ e $B$ são atributos e $\theta \in \{=, \neq, <, \le, >, \ge\}$.
3. **Comparação com Constante:** $t[A] \ \theta \ c$, onde $c$ é um valor constante no domínio de $A$.

#### Quantificadores e Leis de Dualidade:
* **Existencial:** $\exists s \in R (P(s))$ — Existe pelo menos uma tupla $s$ em $R$ que torna $P(s)$ verdadeira.
* **Universal:** $\forall s \in R (P(s))$ — Todas as tuplas $s$ em $R$ satisfazem $P(s)$.
* **Equivalências de De Morgan:**
  $$\forall s (P(s)) \equiv \neg \exists s (\neg P(s))$$
  $$\exists s (P(s)) \equiv \neg \forall s (\neg P(s))$$

---

### 5.2 Segurança de Fórmulas no Cálculo
Uma fórmula $P(t)$ é considerada **insegura** se puder gerar uma relação com infinitas tuplas.  
*Exemplo inseguro:*
$$\{ t \mid \neg(t \in \text{CLIENTE}) \}$$
Essa expressão matemática é sintaticamente válida na lógica pura, mas semanticamente inviável em computação, pois retornaria todas as combinações infinitas do universo que não constam na tabela `CLIENTE`.

**Definição do Domínio da Fórmula ($DOM(\psi)$):**  
Conjunto finito formado por todas as constantes textualmente citadas na fórmula $\psi$ somadas a todos os valores existentes nos atributos das relações referenciadas em $\psi$.

**Regra de Segurança de Codd:**  
Uma expressão $\{ t \mid P(t) \}$ é dita **segura** se:
1. Toda tupla $t$ que satisfaz $P(t)$ possui valores de atributos estritamente contidos em $DOM(P)$.
2. Para qualquer subexpressão com quantificador existencial $\exists u (P_1(u))$, se $u$ satisfaz $P_1$, seus valores obrigatoriamente pertencem ao domínio de $P_1$.
3. Para qualquer subexpressão com quantificador universal $\forall u (P_1(u))$, se valores fora de $DOM(P_1)$ forem testados para $u$, $P_1(u)$ deve ser garantidamente verdadeira.

---

### 5.3 O Teorema da Equivalência e Completude Relacional
Em seu célebre artigo de 1972 (*Relational Completeness of Data Base Sublanguages*), Edgar Frank Codd estabeleceu formalmente o algoritmo de tradução mútua entre a Álgebra Relacional e o Cálculo Relacional Seguro:
$$\text{Álgebra Relacional} \iff \text{CRT Seguro} \iff \text{CRD Seguro}$$
* **Completude Relacional:** Qualquer linguagem de banco de dados capaz de expressar no mínimo o poder declarativo da Álgebra Relacional básica é dita *relacionalmente completa*.

---

### 5.4 Princípios e Heurísticas de Otimização de Consultas
O processamento de uma consulta em um SGBD segue o fluxo:
$$\text{SQL} \xrightarrow{\text{Parser}} \text{Árvore Canônica} \xrightarrow{\text{Otimizador Lógico}} \text{Árvore Otimizada} \xrightarrow{\text{Otimizador Físico}} \text{Código Executável}$$

#### Catálogo de Equivalências Algébricas Centrais:
1. **Comutatividade e Associatividade da Junção:**
   $$R \bowtie S \equiv S \bowtie R$$
   $$(R \bowtie S) \bowtie T \equiv R \bowtie (S \bowtie T)$$
2. **Cascata de Seleções:**
   $$\sigma_{c_1 \land c_2 \land \dots \land c_k}(R) \equiv \sigma_{c_1}(\sigma_{c_2}(\dots(\sigma_{c_k}(R))\dots))$$
3. **Empurrar Seleções para Baixo (*Push-Down Selection*):**
   $$\sigma_c(R \bowtie S) \equiv (\sigma_c(R)) \bowtie S \quad \text{(se } c \text{ envolve apenas atributos de } R\text{)}$$
4. **Empurrar Projeções para Baixo (*Push-Down Projection*):**
   $$\pi_L(R \bowtie S) \equiv \pi_L(\pi_{L_1}(R) \bowtie \pi_{L_2}(S))$$
   onde $L_1$ contém os atributos de $L \cap \text{atr}(R)$ mais os atributos de junção, e $L_2$ o análogo para $S$.

---

## 6. Exercícios Práticos Resolvidos no Contexto Cotidiano

### Instâncias Didáticas de Referência

**Relação CLIENTE(id_cli, nome, cidade, status):**
| id_cli | nome | cidade | status |
| :---: | :---: | :---: | :---: |
| 10 | Ana Lima | Tauá | Ativo |
| 20 | Bruno Souza | Crateús | Inativo |
| 30 | Carla Dias | Tauá | Ativo |
| 40 | Diego Melo | Arneiroz | Ativo |

**Relação PEDIDO(id_ped, id_cli, valor, data):**
| id_ped | id_cli | valor | data |
| :---: | :---: | :---: | :---: |
| 501 | 10 | 500.00 | 01/11/2026 |
| 502 | 30 | 1000.00 | 02/11/2026 |
| 503 | 10 | 200.00 | 03/11/2026 |
| 504 | 40 | 300.00 | 04/11/2026 |

**Relação LIVRO(isbn, titulo, preco):**
| isbn | titulo | preco |
| :---: | :---: | :---: |
| L01 | Algoritmos | 25.00 |
| L02 | O Pequeno Príncipe | 20.00 |
| L03 | Banco de Dados | 85.00 |

---

### Exercício 1: Tradução Formal Tripla (Álgebra $\leftrightarrow$ CRT $\leftrightarrow$ SQL)
**Enunciado:** Recupere o `nome` e a `cidade` dos clientes da cidade de `'Tauá'` que possuem compras de valor superior a R\$ 400,00.  
**Resoluções Formais:**
* **Álgebra Relacional:**
  $$\pi_{\text{nome, cidade}}\left(\sigma_{\text{cidade} = '\text{Tauá}' \,\land\, \text{valor} > 400}(\text{CLIENTE} \bowtie \text{PEDIDO})\right)$$
* **Cálculo Relacional de Tuplas (CRT):**
  $$\begin{aligned}
  \{ t^{(2)} \mid &\exists c \in \text{CLIENTE} \, (c[\text{cidade}] = '\text{Tauá}' \land t[\text{nome}] = c[\text{nome}] \land t[\text{cidade}] = c[\text{cidade}] \\
  &\land \exists p \in \text{PEDIDO} \, (p[\text{id\_cli}] = c[\text{id\_cli}] \land p[\text{valor}] > 400)) \}
  \end{aligned}$$
* **Linguagem SQL Comercial:**
  ```sql
  SELECT c.nome, c.cidade
  FROM CLIENTE c
  JOIN PEDIDO p ON c.id_cli = p.id_cli
  WHERE c.cidade = 'Tauá' AND p.valor > 400;
  ```
* **Tuplas Resultantes:**
  - $\langle \text{'Ana Lima'}, \text{'Tauá'} \rangle$
  - $\langle \text{'Carla Dias'}, \text{'Tauá'} \rangle$

---

### Exercício 2: Quantificação Universal e De Morgan no CRT
**Enunciado:** Formule no CRT a consulta para recuperar os clientes que compraram **todos** os livros promocionais com preço menor que R\$ 30,00. Demonstre a equivalência entre a forma com $\forall$ e a forma com $\exists$.  
**Resolução Formal:**
* **Forma com Quantificador Universal ($\forall$):**
  $$\begin{aligned}
  \{ c[\text{nome}] \mid c \in \text{CLIENTE} \land \forall l \in \text{LIVRO} \, (l[\text{preco}] < 30.00 \to \exists p \in \text{PEDIDO} \, (p[\text{id\_cli}] = c[\text{id\_cli}] \land p[\text{isbn}] = l[\text{isbn}])) \}
  \end{aligned}$$
* **Forma com Quantificador Existencial ($\exists$ via De Morgan):**
  Lembrando que $(P \to Q) \equiv (\neg P \lor Q)$ e que $\forall x (A) \equiv \neg \exists x (\neg A)$:
  $$\begin{aligned}
  \{ c[\text{nome}] \mid c \in \text{CLIENTE} \land \neg \exists l \in \text{LIVRO} \, (l[\text{preco}] < 30.00 \land \neg \exists p \in \text{PEDIDO} \, (p[\text{id\_cli}] = c[\text{id\_cli}] \land p[\text{isbn}] = l[\text{isbn}])) \}
  \end{aligned}$$
  *(Lê-se intuitivamente: "Clientes para os quais NÃO EXISTE nenhum livro barato que ele NÃO tenha comprado").*

---

### Exercício 3: Análise e Correção de Insegurança no CRT
**Enunciado:** Avalie a expressão abaixo no CRT, julgue sua segurança e reescreva-a caso seja insegura:
$$\psi = \{ t \mid \neg(t \in \text{PEDIDO}) \land t[\text{valor}] > 100 \}$$
**Julgamento Formal:**
* A expressão é **INSEGURA**. Ela tenta selecionar tuplas que *não pertencem* a `PEDIDO` e que possuem valor $> 100$. O conjunto de tuplas do universo que satisfazem essa propriedade é infinito. Os atributos que compõem $t$ sequer estão restritos aos atributos de `PEDIDO`.
* **Expressão Segura Equivalente:**
  Se o objetivo era listar clientes que não realizaram nenhum pedido de valor alto:
  $$\{ c[\text{id\_cli, nome}] \mid c \in \text{CLIENTE} \land \neg \exists p \in \text{PEDIDO} (p[\text{id\_cli}] = c[\text{id\_cli}] \land p[\text{valor}] > 100) \}$$
  Todos os valores provêm obrigatoriamente de $DOM(\psi)$.

---

### Exercício 4: Otimização de Árvore de Consulta com Métricas de Custo
**Enunciado:** Considere as relações $R(\text{id\_cli, nome})$ com $100.000$ tuplas e $S(\text{id\_cli, valor})$ com $500.000$ tuplas. Apenas $500$ pedidos tiveram valor superior a R\$ 1000,00.  
Avalie o custo de tuplas intermediárias da consulta:
$$\pi_{\text{nome}}\left(\sigma_{\text{valor} > 1000 \,\land\, R.\text{id\_cli} = S.\text{id\_cli}}(R \times S)\right)$$
* **Plano Canônico Não Otimizado:**
  1. Produto Cartesiano $R \times S$: gera $100.000 \times 500.000 = \mathbf{50.000.000.000}$ (50 bilhões de tuplas).
  2. Filtragem de casamento e valor sobre 50 bilhões de tuplas.
  3. Custo astronômico.
* **Plano Otimizado por Equivalências (Push-Down Selection + Junção Natural):**
  1. Empurrar seleção de valor para $S$: $S' \leftarrow \sigma_{\text{valor} > 1000}(S)$. Produz apenas $\mathbf{500}$ tuplas.
  2. Executar Junção $R \bowtie S'$: cruza $100.000$ com $500$, gerando no máximo $\mathbf{500}$ tuplas intermediárias.
  3. Projetar $\pi_{\text{nome}}$ sobre 500 tuplas.
  * **Ganho Computacional:** Redução de $5 \times 10^{10} \to 500$ tuplas em memória temporária (fator de ganho de $100.000.000\times$).
  * **Ganho Computacional:** Redução de $5 \times 10^{10} \to 500$ tuplas em memória temporária (fator de ganho de $100.000.000\times$).

---

## 7. Referências Bibliográficas

1. **CODD, Edgar Frank.** *A Relational Model of Data for Large Shared Data Banks*. Communications of the ACM (CACM), New York, v. 13, n. 6, p. 377–387, June 1970.
2. **CODD, Edgar Frank.** *Relational Completeness of Data Base Sublanguages*. In: RUSTIN, R. (Ed.). *Data Base Systems*. Englewood Cliffs: Prentice-Hall, 1972. p. 65–98.
3. **ELMASRI, Ramez; NAVATHE, Shamkant B.** *Sistemas de Banco de Dados*. 7. ed. São Paulo: Pearson Education do Brasil, 2018. (Capítulo 8: Álgebra Relacional e Cálculo Relacional; Capítulo 19: Algoritmos para Otimização de Consultas).
4. **HEUSER, Carlos Alberto.** *Projeto de Banco de Dados*. 6. ed. Porto Alegre: Bookman, 2009. (Capítulo 5: Linguagens Formais de Consulta e Otimização).
5. **SILBERSCHATZ, Abraham; KORTH, Henry F.; SUDARSHAN, S.** *Sistema de Banco de Dados*. 7. ed. Rio de Janeiro: GEN/LTC, 2020. (Capítulo 6: Linguagens Formais; Capítulo 13: Otimização de Consultas).
6. **DATE, Chris J.** *Introdução a Sistemas de Bancos de Dados*. 8. ed. Rio de Janeiro: Elsevier Campus, 2004. (Capítulo 7: Cálculo Relacional; Capítulo 18: Otimização).