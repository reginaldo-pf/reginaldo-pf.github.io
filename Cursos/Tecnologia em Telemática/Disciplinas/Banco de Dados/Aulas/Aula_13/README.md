# Aula 13: Álgebra Relacional (Parte 2) — Junções ($\bowtie, \bowtie_\theta, \ltimes, \rtimes, \sqsubset\bowtie, \bowtie\sqsupset, \sqsubset\bowtie\sqsupset$) e Divisão ($\div$)

Esta pasta contém o conjunto completo de recursos didáticos, planejamento pedagógico, portal interativo e apresentação de slides em Beamer da **Aula 13** da disciplina de **Banco de Dados** do Curso Superior de Tecnologia em Telemática (IFCE Campus Tauá).

## Resumo de Competências
* Compreender a motivação computacional e matemática que levou à concepção do operador de Junção, superando o custo proibitivo do produto cartesiano ingênuo ($O(|R| \times |S|)$).
* Dominar a formulação e aplicação do **Theta-Join ($\bowtie_\theta$)** com predicados de comparação gerais ($=, \neq, <, \le, >, \ge$), entendendo a variação de sua cardinalidade.
* Dominar o **Equi-Join** e a **Junção Natural ($\bowtie$)**, aplicando a eliminação automática de atributos redundantes homônimos e compreendendo as propriedades fundamentais de comutatividade e associatividade.
* Identificar o fenômeno das tuplas órfãs (*dangling tuples*) nas junções internas (*inner joins*) e aplicar o conjunto completo de **Junções Externas (*Outer Joins*)**: Left Outer Join ($\sqsubset\bowtie$), Right Outer Join ($\bowtie\sqsupset$) e Full Outer Join ($\sqsubset\bowtie\sqsupset$) com a semântica formal do valor nulo ($\text{NULL}$).
* Aplicar os operadores de **Semi-Junção ($\ltimes, \rtimes$)** e **Anti-Junção ($\triangleright$)**, reconhecendo sua importância estratégica no projeto de consultas eficientes e em arquiteturas de **Bancos de Dados Distribuídos**.
* Dominar o operador de **Divisão Relacional ($\div$)** para consultas que exigem quantificação universal ("para todo..."), compreendendo seu grau resultante e dominando sua prova formal de equivalência com os operadores fundamentais de Codd.
* Resolver desafios práticos e cotidianos envolvendo acervos de bibliotecas, sistemas de comércio eletrônico e históricos acadêmicos.

## Estrutura de Arquivos
* `plano_de_aula.md`: Planejamento pedagógico detalhado para 100 minutos de mentoria/aula presencial, objetivos de aprendizagem, cronograma em 5 blocos, roteiro slide a slide, definições conceituais formais e 4 exercícios práticos resolvidos passo a passo.
* `index.html`: Portal web interativo da aula com explorador de operadores de junção, simulador visual de divisão relacional, leitor de slides embutido, plano pedagógico e desafios interativos.
* `assets/img/`: Logotipos institucionais oficiais do IFCE Campus Tauá.
* `materiais/main.tex` e `materiais/secao*.tex`: Código-fonte LaTeX modularizado da apresentação de slides Beamer (tema institucional Scouts/IFCE widescreen 16:9).
* `materiais/main.pdf`: Apresentação de slides compilada em alta resolução.

## Bibliografia Base Utilizada
1. **CODD, E. F.** A Relational Model of Data for Large Shared Data Banks. *Communications of the ACM*, New York, v. 13, n. 6, p. 377–387, June 1970.
2. **CODD, E. F.** Relational Completeness of Data Base Sublanguages. In: RUSTIN, R. (Ed.). *Data Base Systems*. Englewood Cliffs: Prentice-Hall, 1972. p. 65–98.
3. **ELMASRI, R.; NAVATHE, S. B.** *Sistemas de Banco de Dados*. 7. ed. São Paulo: Pearson Education do Brasil, 2018. (Capítulo 8 — Álgebra Relacional e Cálculo Relacional).
4. **HEUSER, C. A.** *Projeto de Banco de Dados*. 6. ed. Porto Alegre: Bookman, 2009. (Capítulo 5 — A Linguagem da Álgebra Relacional).
5. **SILBERSCHATZ, A.; KORTH, H. F.; SUDARSHAN, S.** *Sistema de Banco de Dados*. 7. ed. Rio de Janeiro: GEN/LTC, 2020. (Capítulo 6 — Linguagens Formais de Consulta Relacional).
6. **DATE, C. J.** *Introdução a Sistemas de Bancos de Dados*. 8. ed. Rio de Janeiro: Elsevier Campus, 2004. (Capítulo 6 — Álgebra Relacional).