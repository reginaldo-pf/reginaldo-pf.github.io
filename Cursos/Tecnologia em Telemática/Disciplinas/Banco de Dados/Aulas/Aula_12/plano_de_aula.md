# Plano de Aula 12: Álgebra Relacional (Parte 1) — Operadores Fundamentais ($\sigma, \pi, \cup, -, \times, \rho$)

## 1. Identificação
* **Instituição:** Instituto Federal de Educação, Ciência e Tecnologia do Ceará (IFCE) — Campus Tauá
* **Curso:** Tecnologia em Telemática
* **Disciplina:** Banco de Dados
* **Professor:** Prof. Me. Reginaldo Fernandes
* **Unidade Temática:** Unidade II — Fundamentos do Modelo Relacional e Linguagens Formais de Consulta (Álgebra Relacional - Parte 1)
* **Data Prevista:** 04/11/2026 (Quarta-feira)
* **Carga Horária:** 2 horas-aula (100 minutos)
* **Regime Didático:** Mentoria Individual / PBL (Aprendizagem Baseada em Problemas)

---

## 2. Objetivos de Aprendizagem

### Objetivo Geral
Capacitar o discente a formular consultas formais rigorosas sobre bancos de dados relacionais utilizando o conjunto de operadores fundamentais da **Álgebra Relacional de Codd**, compreendendo a propriedade estrutural do fechamento relacional e a modelagem procedural que serve de alicerce para o otimizador de consultas dos SGBDs modernos.

### Objetivos Específicos
Ao final desta aula, o discente será capaz de:
1. **Compreender a Natureza da Álgebra Relacional:** Diferenciar uma linguagem formal procedural (que especifica a sequência ordenada de passos de extração) de uma linguagem declarativa como o SQL padrão (que declara apenas o resultado almejado), entendendo o papel da álgebra como representação canônica interna no *Query Optimizer*.
2. **Dominar o Princípio do Fechamento Relacional (Closure Property):** Explicar por que todo operador da álgebra relacional consome uma ou duas relações e produz obrigatoriamente uma nova relação válida, viabilizando o aninhamento recursivo de expressões complexas.
3. **Aplicar o Operador de Seleção ($\sigma$):** Definir o predicado booleano de seleção $p$, operar conectivos lógicos ($\land, \lor, \neg$) e operadores de comparação ($=, \neq, <, \le, >, \ge$), entendendo a seleção como um filtro horizontal que preserva o grau/aridade da tabela e filtra cardinalidade.
4. **Aplicar o Operador de Projeção ($\pi$):** Extrair subconjuntos de atributos verticais de uma relação, demonstrando por que a definição matemática clássica de conjunto de Codd impõe a **eliminação mandatória de tuplas duplicadas**, em contraste com o comportamento padrão de multiconjuntos (*bags*) do SQL comercial.
5. **Aplicar o Operador de Renomeação ($\rho$):** Empregar as três formas sintáticas do operador $\rho$ para desambiguar atributos coincidentes em cruzamentos, apoiar autorrelacionamentos recursivos e nomear esquemas intermediários.
6. **Operar sobre Conjuntos ($\cup, -, \cap$):** Avaliar e verificar rigorosamente os critérios de **Compatibilidade de União (Union-Compatibility)** (mesma aridade e domínios correspondentes idênticos), aplicando União, Diferença e Interseção (provando sua derivação por diferenças sucessivas).
7. **Construir e Analisar Produtos Cartesianos ($\times$):** Calcular o grau ($n + m$) e a cardinalidade ($|R| \times |S|$) resultantes da concatenação de tuplas, entendendo por que o produto cartesiano irrestrito gera explosão combinatória e como a sua composição com a seleção ($\sigma \circ \times$) fundamenta o operador de Junção.
8. **Representar Consultas por Árvores de Expressão (Query Trees):** Mapear expressões algébricas aninhadas em grafos acíclicos dirigidos hierárquicos e compreender a heurística clássica de otimização de consultas *"empurrar a seleção para baixo"* (*push-down selections*).

---

## 3. Cronograma Pedagógico (100 Minutos — 5 Blocos)

| Bloco | Tempo | Etapa Didática | Conteúdos e Metodologia | Recursos |
| :--- | :--- | :--- | :--- | :--- |
| **Bloco 1** | 15 min | **Ponte Conceitual & Fechamento Relacional** | Transição do projeto lógico (Aulas 09 a 11) para manipulação de dados. Por que estudar a álgebra formal de Codd (1970)? Álgebra procedural vs. SQL declarativo. O princípio de fechamento relacional (*closure*). Apresentação do minimundo didático da Livraria/Biblioteca. | Slides 1 a 8 |
| **Bloco 2** | 25 min | **Filtros Unários: Seleção ($\sigma$), Projeção ($\pi$) e Renomeação ($\rho$)** | Formalismo da Seleção ($\sigma$): filtro horizontal, predicados booleanos e comutatividade. Formalismo da Projeção ($\pi$): filtro vertical e a regra de ouro da eliminação automática de duplicatas (conjunto vs. *bag* do SQL). Operador $\rho$ para desambiguação. | Slides 9 a 18 |
| **Bloco 3** | 20 min | **Operações Canônicas de Conjuntos ($\cup, -, \cap$)** | O conceito fundamental de Compatibilidade de União (*Union-Compatibility*). União ($\cup$): consolidação deduplicada. Diferença ($-$): assimetria e detecção de ausências/invariantes. Interseção ($\cap$): derivação formal $R - (R - S)$. | Slides 19 a 23 |
| **Bloco 4** | 20 min | **Produto Cartesiano ($\times$) & Árvores de Consulta** | Produto Cartesiano ($\times$): grau aditivo e cardinalidade multiplicativa. A perigosa explosão combinatória cega. O nascimento da Junção: casamento $\sigma_{\text{cond}}(R \times S)$. Construção gráfica de *Query Trees* e a heurística de otimização de "empurrar a seleção". | Slides 24 a 31 |
| **Bloco 5** | 20 min | **Oficina de Exercícios Guiados & Mentoria** | Resolução passo a passo de 4 desafios com instâncias tabulares completas (consultas em livrarias e escolas). Quadro comparativo sinóptico dos 6 operadores. Checklist de verificação e ponte para a Aula 13 (Junções e Divisão). | Slides 32 a 41 |

---

## 4. Roteiro Detalhado dos Slides (`materiais/main.pdf`)

1. **Capa:** Apresentação Institucional da Aula 12 — Álgebra Relacional (Parte 1): Operadores Fundamentais ($\sigma, \pi, \cup, -, \times, \rho$).
2. **Agenda do Encontro:** Sumário modular dividindo os tópicos em 9 seções lógicas.
3. **Ponte Pedagógica: O que Consolidamos até a Aula 11?** Relembrando a modelagem de entidades, normalização relacional e o algoritmo canônico de mapeamento lógico para 1FN.
4. **Da Estrutura Lógica à Consulta:** O dilema de extrair fatos úteis a partir de tabelas normalizadas. Apresentação da resposta formal de Edgar F. Codd (1970).
5. **O que é a Álgebra Relacional e por que Estudá-la?** Natureza procedural vs. declarativa; papel central no motor de otimização de consultas (*Query Optimizer*) dos SGBDs.
6. **O Princípio Fundamental do Fechamento Relacional (Closure):** A garantia formal de que o operando e o resultado são sempre relações matematicamente válidas, permitindo aninhamento recursivo ilimitado.
7. **Visão Geral dos 6 Operadores Fundamentais:** Quadro comparativo dos operadores unários ($\sigma, \pi, \rho$) e binários ($\cup, -, \times$).
8. **Minimundo Didático de Referência:** Apresentação da tabela base cotidiana `LIVRO(isbn, titulo, categoria, ano, preco)` com 6 tuplas e 5 atributos.
9. **Divisor de Seção:** Operador de Seleção ($\sigma$) — O Filtro Horizontal.
10. **Definição Formal da Seleção ($\sigma$):** Notação $\sigma_p(R)$, avaliação booleana $p(t)$, invariância do grau e contração da cardinalidade.
11. **Anatomia do Predicado de Seleção ($p$):** Cláusulas de comparação ($=, \neq, <, \le, >, \ge$) e operadores lógicos ($\land, \lor, \neg$).
12. **Demonstração Passo a Passo da Seleção:** Exemplo 1 ($\sigma_{\text{cat} = '\text{Computacao}'}$) e Exemplo 2 ($\sigma_{\text{preco} < 60 \land \text{ano} \ge 2019}$) com tabelas antes e depois.
13. **Propriedades Algébricas da Seleção:** Comutatividade ($\sigma_{p1}(\sigma_{p2}(R)) \equiv \sigma_{p2}(\sigma_{p1}(R))$) e fatoração de conjunções em cascatas.
14. **Divisor de Seção:** Operadores de Projeção ($\pi$) e Renomeação ($\rho$).
15. **Definição Formal da Projeção ($\pi$):** Notação $\pi_L(R)$, filtro vertical, extração de subconjunto de colunas e novo grau igual ao comprimento da lista $L$.
16. **A Regra de Ouro da Eliminação de Duplicatas:** A natureza estrita de conjunto relacional e o contraste didático com o `SELECT` multiconjunto (*bag*) do SQL comercial.
17. **Demonstração Passo a Passo da Projeção:** Exemplo com `CLIENTE(id_cli, nome, cidade, uf)` projetando `cidade, uf` com fusão visual de tuplas redundantes.
18. **O Operador de Renomeação ($\rho$ - Rho):** As 3 variantes sintáticas para renomear relações, atributos individuais ou ambos simultaneamente, resolvendo ambiguidades.
19. **Divisor de Seção:** Operações Tradicionais de Conjuntos ($\cup, -, \cap$).
20. **O Princípio da Compatibilidade de União (Union-Compatibility):** Prova de por que duas relações necessitam de igual aridade e domínios correspondentes idênticos para operações de conjuntos.
21. **Operador de União ($\cup$):** Definição matemática $R \cup S$, comutatividade, associatividade e consolidação de leitores de biblioteca com deduplicação.
22. **Operador de Diferença de Conjuntos ($-$):** Definição $R - S$, assimetria essencial ($R - S \neq S - R$) e identificação de subconjuntos exclusivos.
23. **Operador de Interseção ($\cap$):** Derivação matemática canônica a partir de subtrações sucessivas: $R \cap S \equiv R - (R - S)$.
24. **Divisor de Seção:** Operador de Produto Cartesiano ($\times$).
25. **Definição Formal do Produto Cartesiano ($\times$):** Concatenação de tuplas $t_1 \cdot t_2$, independência de compatibilidade de união, grau somado e cardinalidade multiplicada.
26. **Demonstração Prática do Produto Cartesiano:** Cruzamento de `CURSO` ($2$ tuplas) $\times$ `TURNO` ($2$ tuplas) gerando $4$ tuplas no minimundo escolar.
27. **O Produto Cartesiano como Base da Junção ($\bowtie$):** O perigo do consumo de memória e a solução clássica através de seleção restritiva com integridade referencial: $\sigma_{FK = PK}(R \times S)$.
28. **Divisor de Seção:** Expressões Compostas e Árvores de Consulta (Query Trees).
29. **Construção de Consultas Algébricas Complexas:** Comparativo entre a sintaxe aninhada única em linha e a notação em etapas lineares com variáveis intermediárias ($\leftarrow$).
30. **Árvores de Consulta Relacional (Query Trees):** Representação estrutural em grafo com nós folha (tabelas base), nós internos (operadores) e raiz (resultado), com execução *bottom-up*.
31. **Heurística Fundamental de Otimização: "Empurrar Seleções para Baixo":** Análise de custo comparando a filtragem prévia antes do cruzamento versus a filtragem tardia sobre o produto cartesiano gigante.
32. **Divisor de Seção:** Exercícios e Desafios Práticos Resolvidos.
33. **Desafio 1 (Acadêmico):** Seleção Composta e Projeção na relação de alunos universitários.
34. **Desafio 2 (Comércio/Livraria):** Diferença de conjuntos para identificar clientes que nunca realizaram nenhum pedido.
35. **Desafio 3 (Produtos e Categorias):** Junção manual simulada através de Produto Cartesiano seguido de Seleção e Projeção ($\pi \circ \sigma \circ \times$).
36. **Desafio 4 (Contatos Acadêmicos):** Padronização de esquemas com renomeação ($\rho$) e união ($\cup$) entre docentes e monitores.
37. **Divisor de Seção:** Síntese Executiva e Próximos Passos.
38. **Quadro Sinóptico dos 6 Operadores Fundamentais:** Tabela completa resumindo Símbolo, Sintaxe, Aridade, Efeito no Grau e Efeito na Cardinalidade.
39. **Checklist de Autoavaliação do Estudante:** 4 perguntas de diagnóstico formativo para fixação dos conceitos centrais.
40. **Ponte Pedagógica para a Aula 13:** Apresentação das operações derivadas avançadas: Junção Natural ($\bowtie$), Theta-join ($\bowtie_p$), Outer Joins e Operador de Divisão ($\div$).
41. **Referências Bibliográficas:** Obras clássicas de Edgar F. Codd, Ramez Elmasri & Shamkant Navathe, Carlos Alberto Heuser, Abraham Silberschatz e C. J. Date.

---

## 5. Guia Conceitual Completo: Os 6 Operadores Fundamentais de Codd

### 5.1 O Princípio do Fechamento Relacional (*Closure*)
A Álgebra Relacional é uma álgebra matemática fechada. Isso significa formalmente que:
$$\forall \text{ operador } \omega \in \{\sigma, \pi, \rho, \cup, -, \times\}, \quad \omega(R_1, \dots, R_k) = R_{\text{nova}}$$
Onde $R_{\text{nova}}$ é uma relação matemática válida possuindo um esquema bem definido $S(R_{\text{nova}})$ e uma extensão de tuplas $r(R_{\text{nova}})$. Como consequência imediata, qualquer relação resultante pode ser utilizada imediatamente como argumento para uma operação subsequente, permitindo o aninhamento arbitrário de consultas.

### 5.2 Operador de Seleção ($\sigma$)
* **Símbolo:** $\sigma$ (sigma grego minúsculo).
* **Finalidade:** Filtro horizontal de tuplas com base em uma condição lógica booleana.
* **Sintaxe Formal:** $\sigma_p(R) = \{ t \in R \mid p(t) = \text{VERDADEIRO} \}$
* **Natureza:** Operador unário.
* **Efeito no Esquema (Grau):** O grau permanece **rigorosamente inalterado** ($\text{grau}(\sigma_p(R)) = \text{grau}(R)$). Todos os atributos da tabela original são mantidos na saída.
* **Efeito na Instância (Cardinalidade):** A cardinalidade resultante $k$ varia entre $0$ e $|R|$:
  $$0 \le |\sigma_p(R)| \le |R|$$
* **Propriedades Algébricas:**
  - **Comutatividade:** $\sigma_{p1}(\sigma_{p2}(R)) \equiv \sigma_{p2}(\sigma_{p1}(R))$
  - **Fatoração Conjuntiva:** $\sigma_{p1 \land p2}(R) \equiv \sigma_{p1}(\sigma_{p2}(R))$

### 5.3 Operador de Projeção ($\pi$)
* **Símbolo:** $\pi$ (pi grego minúsculo).
* **Finalidade:** Filtro vertical que seleciona colunas específicas e descarta as colunas não solicitadas.
* **Sintaxe Formal:** $\pi_{A_1, A_2, \dots, A_k}(R) = \{ t[A_1, \dots, A_k] \mid t \in R \}$
* **Natureza:** Operador unário.
* **Efeito no Esquema (Grau):** O grau da relação resultante é igual ao número de atributos contidos na lista de projeção $k$:
  $$\text{grau}(\pi_L(R)) = k \le \text{grau}(R)$$
* **Efeito na Instância (Eliminação de Duplicatas):**
  Como as relações no modelo relacional de Codd são rigorosamente conjuntos matemáticos, **quaisquer tuplas que se tornem idênticas após a exclusão de colunas discriminatórias são automaticamente unificadas em uma única tupla**. Logo:
  $$|\pi_L(R)| \le |R|$$
  *(Apenas será rigorosamente igual a $|R|$ se a lista $L$ contiver uma superchave da relação $R$)*.
* **Propriedades Algébricas:**
  - **Projeção em Cascata:** Se $L_1 \subseteq L_2 \subseteq \text{atributos}(R)$, então $\pi_{L_1}(\pi_{L_2}(R)) \equiv \pi_{L_1}(R)$.

### 5.4 Operador de Renomeação ($\rho$)
* **Símbolo:** $\rho$ (rho grego minúsculo).
* **Finalidade:** Atribuir novos nomes a relações ou a colunas individuais para desambiguar identificadores em cruzamentos ou definir esquemas de relações temporárias.
* **Formas Canônicas:**
  1. $\rho_S(R)$: Altera o identificador da relação para $S$, preservando os nomes das colunas.
  2. $\rho_{(B_1, B_2, \dots, B_n)}(R)$: Altera os nomes de todas as colunas de $R$ para $B_1, \dots, B_n$, mantendo o nome da relação.
  3. $\rho_{S(B_1, B_2, \dots, B_n)}(R)$: Altera simultaneamente o nome da relação para $S$ e redefine todos os seus atributos para $B_1, \dots, B_n$.

### 5.5 Compatibilidade de União (*Union-Compatibility*)
Para que duas relações $R(A_1, \dots, A_n)$ e $S(B_1, \dots, B_m)$ possam ser operadas por operadores de conjuntos ($\cup, -, \cap$), elas devem obrigatoriamente satisfazer duas condições formais simultâneas:
1. **Mesma Aridade (Grau):** $n = m$.
2. **Domínios Pareados Idênticos:** Para todo $i \in \{1, 2, \dots, n\}$, tem-se $\operatorname{dom}(A_i) = \operatorname{dom}(B_i)$.
*(Observação: Os nomes literais dos atributos não precisam ser idênticos; o resultado herda por convenção os nomes da relação à esquerda do operador).*

### 5.6 Operador de União ($\cup$)
* **Sintaxe Formal:** $R \cup S = \{ t \mid t \in R \lor t \in S \}$
* **Natureza:** Operador binário de conjuntos (requer compatibilidade de união).
* **Propriedades:** Comutativo ($R \cup S \equiv S \cup R$) e Associativo ($(R \cup S) \cup T \equiv R \cup (S \cup T)$).
* **Cardinalidade:** $\max(|R|, |S|) \le |R \cup S| \le |R| + |S|$ (elimina duplicatas de tuplas presentes em ambas).

### 5.7 Operador de Diferença de Conjuntos ($-$)
* **Sintaxe Formal:** $R - S = \{ t \mid t \in R \land t \notin S \}$
* **Natureza:** Operador binário de conjuntos (requer compatibilidade de união).
* **Propriedades:** **Não comutativo** ($R - S \neq S - R$). É o operador formal utilizado para responder a consultas com negação existencial (*"quais $X$ nunca realizaram $Y$?"*).
* **Cardinalidade:** $0 \le |R - S| \le |R|$.

### 5.8 Operador de Interseção ($\cap$)
* **Sintaxe Formal:** $R \cap S = \{ t \mid t \in R \land t \in S \}$
* **Derivação Primitiva:** A interseção não é um operador independente na formulação básica de Codd, pois pode ser derivada diretamente da diferença:
  $$R \cap S \equiv R - (R - S) \equiv S - (S - R)$$
* **Propriedades:** Comutativo ($R \cap S \equiv S \cap R$).
* **Cardinalidade:** $0 \le |R \cap S| \le \min(|R|, |S|)$.

### 5.9 Operador de Produto Cartesiano ($\times$)
* **Sintaxe Formal:** $R \times S = \{ t_1 \cdot t_2 \mid t_1 \in R \land t_2 \in S \}$
* **Natureza:** Operador binário combinatório. **Não requer compatibilidade de união**.
* **Dimensões Resultantes:**
  - $\text{grau}(R \times S) = \text{grau}(R) + \text{grau}(S)$
  - $|R \times S| = |R| \times |S|$
* **Conexão com a Junção:**
  O produto cartesiano gera todas as combinações tupla a tupla indiscriminadamente. Ao aplicar uma seleção com condição de igualdade sobre atributos correlatos ($\text{Chave Estrangeira} = \text{Chave Primária}$), obtemos o operador derivado de **Junção ($\bowtie$)**:
  $$R \bowtie_{\text{condição}} S \equiv \sigma_{\text{condição}}(R \times S)$$

---

## 6. Banco de Exercícios e Casos Práticos de Aplicação

### Instâncias Didáticas de Teste (Minimundo de Comércio e Livraria Escolar)

**Relação LIVRO:**
| isbn | titulo | categoria | ano | preco |
| :---: | :--- | :---: | :---: | :---: |
| L01 | Algoritmos | Computacao | 2020 | 85.00 |
| L02 | O Pequeno Principe | Literatura | 2018 | 35.00 |
| L03 | Banco de Dados | Computacao | 2022 | 90.00 |
| L04 | Dom Casmurro | Literatura | 2019 | 42.00 |
| L05 | Inteligencia Artificial | Computacao | 2023 | 110.00 |
| L06 | Quimica Organica | Exatas | 2021 | 55.00 |

**Relação CLIENTE:**
| id_cli | nome | cidade | uf |
| :---: | :--- | :--- | :---: |
| 101 | Carlos Silva | Taua | CE |
| 102 | Maria Souza | Fortaleza | CE |
| 103 | Joao Lima | Taua | CE |
| 104 | Ana Ribeiro | Iguatu | CE |
| 105 | Pedro Rocha | Fortaleza | CE |

**Relação PEDIDO:**
| id_ped | id_cli_fk | data | valor |
| :---: | :---: | :---: | :---: |
| 501 | 101 | 10/10/2026 | 120.00 |
| 502 | 103 | 12/10/2026 | 85.00 |
| 503 | 101 | 15/10/2026 | 210.00 |
| 504 | 104 | 20/10/2026 | 45.00 |

---

### Exercício 1: Seleção Composta com Projeção
**Enunciado:** Formule uma expressão na Álgebra Relacional que recupere o `titulo` e o `preco` dos livros que pertencem à categoria `'Literatura'` OU que custem menos de R\$ 60,00, ordenando a sequência de passos lógicos.  
**Resolução Formal:**
1. $\text{PASSO1} \leftarrow \sigma_{\text{categoria} = '\text{Literatura}' \,\lor\, \text{preco} < 60.00}(\text{LIVRO})$
2. $\text{RESULTADO} \leftarrow \pi_{\text{titulo, preco}}(\text{PASSO1})$
* **Expressão Única Aninhada:**
  $$\pi_{\text{titulo, preco}}\left(\sigma_{\text{categoria} = '\text{Literatura}' \,\lor\, \text{preco} < 60.00}(\text{LIVRO})\right)$$
* **Tuplas Resultantes:**
  - $\langle \text{'O Pequeno Principe'}, 35.00 \rangle$
  - $\langle \text{'Dom Casmurro'}, 42.00 \rangle$
  - $\langle \text{'Quimica Organica'}, 55.00 \rangle$

---

### Exercício 2: Detecção de Ausência via Diferença de Conjuntos
**Enunciado:** Identifique os clientes (código e nome) que se cadastraram no sistema da livraria mas **nunca realizaram nenhuma compra registrada na tabela `PEDIDO`**.  
**Resolução Formal:**
1. Obter a lista com todos os códigos de clientes cadastrados:
   $$\text{TODOS\_IDS} \leftarrow \pi_{\text{id\_cli}}(\text{CLIENTE})$$
2. Obter a lista dos códigos de clientes que já compraram ao menos uma vez:
   $$\text{IDS\_COMPRADORES} \leftarrow \pi_{\text{id\_cli\_fk}}(\text{PEDIDO})$$
3. Subtrair os conjuntos compatíveis para isolar quem nunca comprou:
   $$\text{IDS\_INATIVOS} \leftarrow \text{TODOS\_IDS} - \text{IDS\_COMPRADORES}$$
   *(Valores obtidos: $\{ 102, 105 \}$)*
4. Recuperar o nome desses clientes cruzando com a relação base e projetando:
   $$\text{COMBINA} \leftarrow \text{CLIENTE} \times \text{IDS\_INATIVOS}$$
   $$\text{FILTRA} \leftarrow \sigma_{\text{CLIENTE.id\_cli} = \text{IDS\_INATIVOS.id\_cli}}(\text{COMBINA})$$
   $$\text{RESULTADO} \leftarrow \pi_{\text{id\_cli, nome}}(\text{FILTRA})$$
* **Tuplas Resultantes:**
  - $\langle 102, \text{'Maria Souza'} \rangle$
  - $\langle 105, \text{'Pedro Rocha'} \rangle$

---

### Exercício 3: Produto Cartesiano e Junção Simulado Manualmente
**Enunciado:** Sem utilizar a notação de junção ($\bowtie$), construa a expressão formal que associe cada pedido ao nome do respectivo cliente que o realizou, exibindo o `id_ped`, o `nome` do cliente e o `valor` da transação.  
**Resolução Formal:**
1. Cruzamento irrestrito de todas as combinações:
   $$\text{PROD} \leftarrow \text{CLIENTE} \times \text{PEDIDO}$$
   *(Grau: $4 + 4 = 8$ atributos; Cardinalidade: $5 \times 4 = 20$ tuplas intermediárias).*
2. Filtragem pela integridade referencial ($PK = FK$):
   $$\text{CORRETO} \leftarrow \sigma_{\text{CLIENTE.id\_cli} = \text{PEDIDO.id\_cli\_fk}}(\text{PROD})$$
   *(Redução imediata de $20 \to 4$ tuplas válidas).*
3. Projeção dos atributos de interesse:
   $$\text{RESULTADO} \leftarrow \pi_{\text{id\_ped, nome, valor}}(\text{CORRETO})$$
* **Expressão Compacta:**
  $$\pi_{\text{id\_ped, nome, valor}}\left(\sigma_{\text{CLIENTE.id\_cli} = \text{PEDIDO.id\_cli\_fk}}(\text{CLIENTE} \times \text{PEDIDO})\right)$$

---

### Exercício 4: Verificação de Compatibilidade de União
**Enunciado:** Analise os pares de relações abaixo e julgue formalmente se eles admitem a aplicação direta da operação de União ($R \cup S$):
1. $R(\text{cpf: TEXT, nome: TEXT, idade: INT})$ e $S(\text{cnpj: TEXT, razao\_social: TEXT, fundacao: INT})$
   * **Julgamento:** **Compatíveis.** Ambas possuem grau 3 e os domínios pareados são idênticos $(\text{TEXT}, \text{TEXT}, \text{INT})$. O resultado adotará o esquema $(\text{cpf}, \text{nome}, \text{idade})$.
2. $R(\text{id: INT, salario: FLOAT})$ e $S(\text{id: INT, salario: FLOAT, gratificacao: FLOAT})$
   * **Julgamento:** **Incompatíveis.** Possuem graus distintos ($\text{grau}(R) = 2 \neq \text{grau}(S) = 3$), violando o primeiro axioma da compatibilidade de união.
3. $R(\text{matricula: INT, nome: TEXT})$ e $S(\text{nome: TEXT, matricula: INT})$
   * **Julgamento:** **Incompatíveis na ordem original.** Embora possuam grau 2, na posição 1 tem-se $\text{INT}$ vs. $\text{TEXT}$. Para torná-las compatíveis, deve-se reordenar a relação $S$ através de projeção: $R \cup \pi_{\text{matricula, nome}}(S)$.

---

## 7. Referências Bibliográficas

1. **CODD, Edgar Frank.** *A Relational Model of Data for Large Shared Data Banks*. Communications of the ACM (CACM), New York, v. 13, n. 6, p. 377–387, June 1970. (Artigo canônico fundador do modelo e da álgebra relacional).
2. **ELMASRI, Ramez; NAVATHE, Shamkant B.** *Sistemas de Banco de Dados*. 7. ed. São Paulo: Pearson Education do Brasil, 2018. (Capítulo 8: Álgebra Relacional e Cálculo Relacional — Os Operadores Fundamentais de Codd).
3. **HEUSER, Carlos Alberto.** *Projeto de Banco de Dados*. 6. ed. Porto Alegre: Bookman, 2009. (Capítulo 5: A Linguagem da Álgebra Relacional e Restrições de Integridade).
4. **SILBERSCHATZ, Abraham; KORTH, Henry F.; SUDARSHAN, S.** *Sistema de Banco de Dados*. 7. ed. Rio de Janeiro: GEN/LTC, 2020. (Capítulo 6: Linguagens Formais de Consulta Relacional).
5. **DATE, Chris J.** *Introdução a Sistemas de Bancos de Dados*. 8. ed. Rio de Janeiro: Elsevier Campus, 2004. (Capítulo 6: Álgebra Relacional: Fechamento, Operadores Primitivos e Otimização).
