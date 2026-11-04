# Aula 12: Álgebra Relacional (Parte 1) — Operadores Fundamentais ($\sigma, \pi, \cup, -, \times, \rho$)

Esta pasta contém o conjunto completo de recursos didáticos, plano pedagógico, portal interativo e apresentação de slides em Beamer da **Aula 12** da disciplina de **Banco de Dados** do Curso Superior de Tecnologia em Telemática (IFCE Campus Tauá).

## Resumo de Competências
* Compreender os fundamentos matemáticos e teóricos da **Álgebra Relacional formal de Edgar F. Codd (1970)** como linguagem procedural base para os Sistemas Gerenciadores de Banco de Dados Relacionais (SGBD-R).
* Aplicar a propriedade inviolável do **Fechamento Relacional (Closure)**: reconhecer que todos os operadores recebem relações como entrada e produzem obrigatoriamente uma nova relação matematicamente válida na Primeira Forma Normal (1FN), viabilizando aninhamento ilimitado.
* Dominar o **Operador de Seleção ($\sigma$)**: formular predicados booleanos de filtragem horizontal ($p$) com operadores relacionais e conectivos lógicos ($\land, \lor, \neg$), explorando a comutatividade e a decomposição conjuntiva em cascatas.
* Dominar o **Operador de Projeção ($\pi$)**: selecionar subconjuntos verticais de atributos e compreender a **eliminação mandatória de tuplas duplicadas** inerente à definição estrita de conjunto relacional (contrastando com os multiconjuntos /*bags* do SQL comercial).
* Aplicar o **Operador de Renomeação ($\rho$)**: utilizar as três notações formais para renomear relações, renomear atributos ou redefinir simultaneamente relação e esquema, resolvendo colisões de nomes e apoiando autorrelacionamentos.
* Aplicar as **Operações Tradicionais de Conjuntos ($\cup, -, \cap$)**: validar os requisitos rigorosos de **Compatibilidade de União (*Union-Compatibility*)** (mesma aridade e compatibilidade pareada de domínios), calcular uniões deduplicadas, diferenças assimétricas e provar a derivação formal da interseção ($R \cap S \equiv R - (R - S)$).
* Compreender e computar o **Produto Cartesiano ($\times$)**: deduzir a soma de graus ($\text{grau}(R) + \text{grau}(S)$) e a multiplicação de cardinalidades ($|R| \times |S|$), demonstrando como a composição com a seleção ($\sigma \circ \times$) estabelece a base teórica da Junção ($\bowtie$).
* Mapear consultas complexas em **Árvores de Expressão (Query Trees)** e entender a heurística primordial de otimização de consultas (*Query Optimizer*): a técnica de **"empurrar a seleção para baixo"** (*push-down selection*).

## Estrutura de Arquivos
* `plano_de_aula.md`: Planejamento pedagógico detalhado para 100 minutos de mentoria/aula presencial, objetivos de aprendizagem, cronograma em 5 blocos, roteiro slide a slide dos 41 slides, guia formal com definições matemáticas e 4 exercícios práticos resolvidos passo a passo em domínios cotidianos.
* `index.html`: Portal web interativo da aula com filtros interativos de operadores algébricos, simulador visual de seleção/projeção, leitor de slides embutido, plano pedagógico e quadro sinóptico de propriedades.
* `assets/img/`: Logotipos institucionais oficiais do IFCE Campus Tauá.
* `materiais/main.tex` e `materiais/secao*.tex`: Código-fonte LaTeX modularizado da apresentação de slides Beamer (tema institucional Scouts/IFCE widescreen 16:9) com árvore de consulta desenhada em TikZ nativo.
* `materiais/main.pdf`: Apresentação de slides compilada (41 páginas, formato widescreen 16:9).

## Bibliografia Base Utilizada
1. **CODD, E. F.** A Relational Model of Data for Large Shared Data Banks. *Communications of the ACM*, New York, v. 13, n. 6, p. 377–387, June 1970.
2. **ELMASRI, R.; NAVATHE, S. B.** *Sistemas de Banco de Dados*. 7. ed. São Paulo: Pearson Education do Brasil, 2018. (Capítulo 8 — Álgebra Relacional e Cálculo Relacional).
3. **HEUSER, C. A.** *Projeto de Banco de Dados*. 6. ed. Porto Alegre: Bookman, 2009. (Capítulo 5 — A Linguagem da Álgebra Relacional).
4. **SILBERSCHATZ, A.; KORTH, H. F.; SUDARSHAN, S.** *Sistema de Banco de Dados*. 7. ed. Rio de Janeiro: GEN/LTC, 2020. (Capítulo 6 — Linguagens Formais de Consulta Relacional).
5. **DATE, C. J.** *Introdução a Sistemas de Bancos de Dados*. 8. ed. Rio de Janeiro: Elsevier Campus, 2004. (Capítulo 6 — Álgebra Relacional).
