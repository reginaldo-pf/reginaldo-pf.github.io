# Plano de Aula 13: Álgebra Relacional (Parte 2) — Junções ($\bowtie, \bowtie_\theta, \ltimes, \rtimes, \sqsubset\bowtie, \bowtie\sqsupset, \sqsubset\bowtie\sqsupset$) e Divisão ($\div$)

## 1. Identificação
* **Instituição:** Instituto Federal de Educação, Ciência e Tecnologia do Ceará (IFCE) — Campus Tauá
* **Curso:** Tecnologia em Telemática
* **Disciplina:** Banco de Dados
* **Professor:** Prof. Me. Reginaldo Fernandes
* **Unidade Temática:** Unidade II — Fundamentos do Modelo Relacional e Linguagens Formais de Consulta (Álgebra Relacional - Parte 2)
* **Data Prevista:** 10/11/2026 (Terça-feira)
* **Carga Horária:** 2 horas-aula (100 minutos)
* **Regime Didático:** Mentoria Individual / PBL (Aprendizagem Baseada em Problemas)

---

## 2. Objetivos de Aprendizagem

### Objetivo Geral
Capacitar o discente a formular consultas relacionais avançadas com rigor matemático e eficiência computacional por meio dos operadores derivados da **Álgebra Relacional**, dominando a família de operadores de junção (Theta-join, Equi-join, Junção Natural, Semi-junções e Junções Externas) e o operador de Divisão Relacional para expressar quantificações universais ("para todo"), utilizando cenários e minimundos comuns do cotidiano e de negócios.

### Objetivos Específicos
Ao final desta aula, o discente será capaz de:
1. **Compreender a Gênese da Junção:** Explicar a ineficiência assintótica do produto cartesiano ingênuo ($\times$) e demonstrar como a composição $\sigma_\theta(R \times S)$ fundamenta matematicamente o operador de Theta-join ($\bowtie_\theta$).
2. **Diferenciar Famílias de Junção:**
   - **Theta-Join ($\bowtie_\theta$):** Avaliar condições booleanas arbitrárias de comparação ($=, <, \le, >, \ge, \neq$), como faixas de valores e cupons promocionais.
   - **Equi-Join:** Identificar o caso particular onde o predicado $\theta$ contém exclusivamente conjunções de igualdades, preservando atributos duplicados com nomes qualificados.
   - **Junção Natural ($\bowtie$):** Aplicar a regra formal de casamento implícito por atributos homônimos com projeção automática que elimina colunas duplicadas.
3. **Analisar Tuplas Órfãs (*Dangling Tuples*):** Diagnosticar a perda de informações que ocorre nas junções internas (*Inner Joins*) quando não há correspondência entre chaves primárias e estrangeiras (ex: livros sem empréstimo ou clientes sem compras).
4. **Dominar as Junções Externas (*Outer Joins*):**
   - **Left Outer Join ($\sqsubset\bowtie$):** Preservar todas as tuplas da relação esquerda, preenchendo ausências com valores nulos ($\text{NULL}$).
   - **Right Outer Join ($\bowtie\sqsupset$):** Preservar todas as tuplas da relação direita.
   - **Full Outer Join ($\sqsubset\bowtie\sqsupset$):** Preservar a união completa das informações de ambas as relações.
5. **Aplicar Semi-Junção ($\ltimes, \rtimes$) e Anti-Junção ($\triangleright$):**
   - Formular semi-junções para filtrar tuplas de uma tabela sem alocar atributos da outra, compreendendo seu impacto vital na redução de tráfego de rede em bancos de dados distribuídos.
   - Empregar a anti-junção para isolar diretamente registros não referenciados ($R \triangleright S \equiv R - (R \ltimes S)$).
6. **Dominar o Operador de Divisão Relacional ($\div$):**
   - Modelar consultas com semântica de quantificação universal ("quais alunos cursaram *todas* as disciplinas obrigatórias?", "quais clientes compraram *todos* os livros de uma lista?").
   - Provar formalmente a decomposição de $R \div S$ em operadores primitivos: $\pi_X(R) - \pi_X((\pi_X(R) \times S) - R)$.

---

## 3. Cronograma Pedagógico (100 Minutos — 5 Blocos)

| Bloco | Tempo | Etapa Didática | Conteúdos e Metodologia | Recursos |
| :--- | :--- | :--- | :--- | :--- |
| **Bloco 1** | 15 min | **Ponte Pedagógica & A Gênese da Junção** | Recapitulação da Aula 12: fechamento e produto cartesiano ($\times$). O problema da explosão combinatória ($O(|R| \times |S|)$). Motivação formal: por que sintetizar $\sigma_\theta \circ \times$ em um novo operador? Apresentação do minimundo didático de Comércio de Livros e Assinaturas. | Slides 1 a 6 |
| **Bloco 2** | 25 min | **Theta-Join, Equi-Join e Junção Natural ($\bowtie$)** | Formalismo do Theta-join ($\bowtie_\theta$): grau aditivo e cardinalidade limitada. Exemplo com cupons de desconto. Equi-join e a duplicação de colunas. Junção Natural ($\bowtie$): critério de homonímia, projeção implícita e propriedades de comutatividade/associatividade. Conceito formal de *Dangling Tuples*. | Slides 7 a 14 |
| **Bloco 3** | 15 min | **Semi-Junções ($\ltimes, \rtimes$) e Anti-Junção ($\triangleright$)** | Semi-join: definição $\pi_{\text{atr}(R)}(R \bowtie S)$. Por que não carrega colunas da direita? Aplicação em otimização de consultas e matrizes/filiais. Anti-join ($\triangleright$): identificação imediata de livros nunca emprestados. | Slides 15 a 17 |
| **Bloco 4** | 20 min | **Junções Externas (*Outer Joins*) e Valores Nulos** | A limitação da perda de dados nas junções estritas. A semântica formal do $\text{NULL}$. Left Outer Join ($\sqsubset\bowtie$), Right Outer Join ($\bowtie\sqsupset$) e Full Outer Join ($\sqsubset\bowtie\sqsupset$). Análise comparativa visual de preenchimento. | Slides 18 a 21 |
| **Bloco 5** | 25 min | **Operador de Divisão ($\div$) & Oficina de Desafios** | O desafio do "Para Todo" (quantificador universal $\forall$). Definição formal de $R \div S$, grau subtrativo ($n - m$). Prova matemática e algoritmo das 5 etapas da divisão. Resolução guiada de 4 desafios práticos do cotidiano (biblioteca, livraria, comércio e histórico escolar). | Slides 22 a 35 |

---

## 4. Guia Conceitual Completo: Junções e Divisão

### 4.1 O Operador Theta-Join ($\bowtie_\theta$)
O operador Theta-Join combina um produto cartesiano irrestrito seguido imediatamente por uma operação de seleção booleana com predicado $\theta$:
$$R \bowtie_\theta S = \sigma_\theta(R \times S)$$
Onde:
* $\theta$ é uma condição da forma $A_i \ \theta \ B_j$, com $\theta \in \{=, \neq, <, \le, >, \ge\}$.
* **Grau:** $\text{grau}(R \bowtie_\theta S) = \text{grau}(R) + \text{grau}(S)$.
* **Cardinalidade:** $0 \le |R \bowtie_\theta S| \le |R| \times |S|$.

### 4.2 O Operador de Junção Natural ($\bowtie$)
A Junção Natural é uma operação que realiza a igualdade sobre todos os atributos de mesmo nome presentes nos esquemas de $R$ e $S$, projetando apenas uma ocorrência de cada atributo homônimo:
$$R \bowtie S = \pi_{X \cup Y \cup Z}\left(\sigma_{R.Y_1 = S.Y_1 \,\land\, \dots \,\land\, R.Y_k = S.Y_k}(R \times S)\right)$$
Onde $X = \text{atr}(R) - \text{atr}(S)$, $Z = \text{atr}(S) - \text{atr}(R)$ e $Y = \text{atr}(R) \cap \text{atr}(S)$.
* **Grau:** $\text{grau}(R) + \text{grau}(S) - |Y|$.

### 4.3 As Semi-Junções ($\ltimes, \rtimes$) e Anti-Junção ($\triangleright$)
* **Semi-junção Esquerda ($R \ltimes S$):** Retorna apenas as tuplas de $R$ que possuem pelo menos uma tupla correspondente em $S$:
  $$R \ltimes S = \pi_{\text{atr}(R)}(R \bowtie S)$$
* **Anti-junção ($R \triangleright S$):** Retorna as tuplas de $R$ para as quais **não existe** nenhuma correspondência em $S$:
  $$R \triangleright S = R - (R \ltimes S)$$

### 4.4 As Junções Externas (*Outer Joins*)
* **Left Outer Join ($R \sqsubset\bowtie S$):** Inclui todas as tuplas da junção natural ($R \bowtie S$) somadas às tuplas de $R$ que não tiveram correspondência em $S$, preenchendo os atributos de $S$ com valores nulos ($\text{NULL}$).
* **Right Outer Join ($R \bowtie\sqsupset S$):** De forma análoga, preserva todas as tuplas de $S$, preenchendo as ausências de atributos de $R$ com $\text{NULL}$.
* **Full Outer Join ($R \sqsubset\bowtie\sqsupset S$):** Combina os resultados do Left Outer Join e Right Outer Join, preservando tuplas órfãs de ambas as tabelas.

### 4.5 O Operador de Divisão Relacional ($R \div S$)
Seja a relação $R$ com esquema $R(X_1, \dots, X_n, Y_1, \dots, Y_m)$ e a relação $S$ com esquema $S(Y_1, \dots, Y_m)$, onde $\text{atr}(S) \subset \text{atr}(R)$. A divisão $R \div S$ produz uma nova relação $T$ com esquema $T(X_1, \dots, X_n)$ tal que:
$$R \div S = \{ t_x \mid \forall t_y \in S, \ \langle t_x, t_y \rangle \in R \}$$
* **Grau:** $\text{grau}(R) - \text{grau}(S)$.
* **Identidade com Operadores Fundamentais:**
  $$R \div S = \pi_X(R) - \pi_X\left( (\pi_X(R) \times S) - R \right)$$

---

## 5. Exercícios Práticos Resolvidos no Contexto Cotidiano

### Instâncias Didáticas de Referência

**Relação LIVRO:**
| isbn | titulo | categoria | ano |
| :---: | :---: | :---: | :---: |
| L01 | Algoritmos | Computacao | 2020 |
| L02 | O Pequeno Principe | Literatura | 2018 |
| L03 | Quimica Geral | Exatas | 2021 |
| L04 | Dom Casmurro | Literatura | 2019 |

**Relação EMPRESTIMO:**
| id_emp | isbn | leitor | data_emp |
| :---: | :---: | :---: | :---: |
| E101 | L01 | Alice Lima | 10/11/2026 |
| E102 | L01 | Bob Silva | 15/11/2026 |
| E103 | L02 | Carlos Dias | 12/11/2026 |
| E104 | L04 | Diana Melo | 18/11/2026 |

**Relação DISC_OBRIGATORIAS:**
| cod_disc |
| :---: |
| MAT01 |
| PROG01 |

**Relação HISTORICO:**
| id_alu | cod_disc |
| :---: | :---: |
| 101 | MAT01 |
| 101 | PROG01 |
| 101 | FIS01 |
| 102 | MAT01 |
| 103 | PROG01 |
| 104 | MAT01 |
| 104 | PROG01 |

**Relação ALUNO:**
| id_alu | nome | cidade |
| :---: | :---: | :---: |
| 101 | Ana Lima | Tauá |
| 102 | Bruno Souza | Crateús |
| 103 | Carla Mendes | Tauá |
| 104 | Diana Moreira | Arneiroz |

---

### Exercício 1: Junção Natural e Seleção de Obras
**Enunciado:** Recupere o `titulo` da obra, o nome do `leitor` e a `data_emp` dos empréstimos realizados para livros da categoria `'Computacao'`.  
**Resolução Formal:**
1. Filtrar previamente os livros da categoria desejada (otimização por Push-Down):
   $$\text{LIVROS\_COMP} \leftarrow \sigma_{\text{categoria} = '\text{Computacao}'}(\text{LIVRO})$$
2. Realizar a junção natural pelo atributo comum `isbn`:
   $$\text{JUNCAO} \leftarrow \text{LIVROS\_COMP} \bowtie \text{EMPRESTIMO}$$
3. Projetar os atributos requeridos:
   $$\text{RESULTADO} \leftarrow \pi_{\text{titulo, leitor, data\_emp}}(\text{JUNCAO})$$
* **Tuplas Resultantes:**
  - $\langle \text{'Algoritmos'}, \text{'Alice Lima'}, \text{'10/11/2026'} \rangle$
  - $\langle \text{'Algoritmos'}, \text{'Bob Silva'}, \text{'15/11/2026'} \rangle$

---

### Exercício 2: Detecção de Obras Nunca Emprestadas via Anti-Junção
**Enunciado:** Identifique o `isbn` e o `titulo` de todos os livros do acervo que **jamais foram emprestados a nenhum leitor**.  
**Resolução Formal:**
1. Aplicar a Anti-junção diretamente entre `LIVRO` e `EMPRESTIMO`:
   $$\text{NUNCA\_EMPRESTADOS} \leftarrow \text{LIVRO} \triangleright \text{EMPRESTIMO}$$
   *(Equivalente formal: $\text{LIVRO} - \pi_{\text{atr(LIVRO)}}(\text{LIVRO} \bowtie \text{EMPRESTIMO})$)*
2. Projetar as colunas solicitadas:
   $$\text{RESULTADO} \leftarrow \pi_{\text{isbn, titulo}}(\text{NUNCA\_EMPRESTADOS})$$
* **Tuplas Resultantes:**
  - $\langle \text{'L03'}, \text{'Quimica Geral'} \rangle$

---

### Exercício 3: Relatório de Clientes e Vendas com Left Outer Join
**Enunciado:** Gere uma listagem completa de todos os clientes cadastrados (`nome` e `cidade`), informando o `id_ped` correspondente caso exista, sem excluir os clientes que ainda não efetuaram compras.  
**Resolução Formal:**
1. Aplicar a Junção Externa Esquerda:
   $$\text{RELAT\_COMPLETO} \leftarrow \text{CLIENTE} \sqsubset\bowtie \text{PEDIDO}$$
2. Projetar os campos pertinentes:
   $$\text{RESULTADO} \leftarrow \pi_{\text{nome, cidade, id\_ped}}(\text{RELAT\_COMPLETO})$$
* **Tuplas Resultantes:**
  - $\langle \text{'Ana Lima'}, \text{'Tauá'}, 501 \rangle$
  - $\langle \text{'Ana Lima'}, \text{'Tauá'}, 503 \rangle$
  - $\langle \text{'Bruno Silva'}, \text{'Fortaleza'}, \text{NULL} \rangle$
  - $\langle \text{'Carla Dias'}, \text{'Tauá'}, 502 \rangle$
  - $\langle \text{'Diego Melo'}, \text{'Sobral'}, 504 \rangle$
  - $\langle \text{'Eva Rocha'}, \text{'Tauá'}, \text{NULL} \rangle$

---

### Exercício 4: Verificação de Conclusão de Núcleo Obrigatório via Divisão
**Enunciado:** Identifique os estudantes (`id_alu` e `nome`) que cursaram e foram aprovados em **TODAS as disciplinas obrigatórias** contidas na tabela `DISC_OBRIGATORIAS`.  
**Resolução Formal:**
1. Aplicar o Operador de Divisão sobre a tabela de histórico:
   $$\text{ALUNOS\_APTOS} \leftarrow \text{HISTORICO} \div \text{DISC\_OBRIGATORIAS}$$
   *Esquema de entrada:* `HISTORICO(id_alu, cod_disc)` e `DISC_OBRIGATORIAS(cod_disc)`.  
   *Grau resultante:* $2 - 1 = 1$ atributo (`id_alu`).  
   *Valores que satisfazem:* O aluno 101 cursou (MAT01, PROG01, FIS01); o aluno 104 cursou (MAT01, PROG01). Logo, $\text{ALUNOS\_APTOS} = \{ \langle 101 \rangle, \langle 104 \rangle \}$.
2. Recuperar o `nome` do estudante cruzando com a tabela `ALUNO` por Junção Natural:
   $$\text{RESULTADO} \leftarrow \pi_{\text{id\_alu, nome}}(\text{ALUNOS\_APTOS} \bowtie \text{ALUNO})$$
* **Tuplas Resultantes:**
  - $\langle 101, \text{'Ana Lima'} \rangle$
  - $\langle 104, \text{'Diana Moreira'} \rangle$

---

## 6. Referências Bibliográficas

1. **CODD, Edgar Frank.** *A Relational Model of Data for Large Shared Data Banks*. Communications of the ACM (CACM), New York, v. 13, n. 6, p. 377–387, June 1970.
2. **CODD, Edgar Frank.** *Relational Completeness of Data Base Sublanguages*. In: Rustin, R. (Ed.). *Data Base Systems*. Englewood Cliffs: Prentice-Hall, 1972. p. 65–98.
3. **ELMASRI, Ramez; NAVATHE, Shamkant B.** *Sistemas de Banco de Dados*. 7. ed. São Paulo: Pearson Education do Brasil, 2018. (Capítulo 8: Álgebra Relacional e Cálculo Relacional — Operações Relacionais Adicionais).
4. **HEUSER, Carlos Alberto.** *Projeto de Banco de Dados*. 6. ed. Porto Alegre: Bookman, 2009. (Capítulo 5: Operações Derivadas: Junções e Divisão).
5. **SILBERSCHATZ, Abraham; KORTH, Henry F.; SUDARSHAN, S.** *Sistema de Banco de Dados*. 7. ed. Rio de Janeiro: GEN/LTC, 2020. (Capítulo 6: Linguagens Formais de Consulta Relacional — Junções e Operações Adicionais).
6. **DATE, Chris J.** *Introdução a Sistemas de Bancos de Dados*. 8. ed. Rio de Janeiro: Elsevier Campus, 2004. (Capítulo 6: Álgebra Relacional: Junções e Divisão Relacional).