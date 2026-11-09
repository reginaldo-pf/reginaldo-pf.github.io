# Aula 14: Cálculo Relacional (CRT e CRD) e Princípios de Otimização de Consultas

Esta pasta contém o conjunto completo de recursos didáticos, planejamento pedagógico, portal interativo e apresentação de slides em Beamer da **Aula 14** da disciplina de **Banco de Dados** do Curso Superior de Tecnologia em Telemática (IFCE Campus Tauá).

## Resumo de Competências
* Compreender a distinção epistemológica e de engenharia entre a abordagem **procedural** da Álgebra Relacional (*"como computar"*) e a abordagem **declarativa** do Cálculo Relacional (*"o que obter"*), fundamentada na Lógica de Predicados de Primeira Ordem.
* Dominar a sintaxe formal, variáveis de tupla, átomos e conectivos do **Cálculo Relacional de Tuplas (CRT / TRC)**, operando quantificadores existenciais ($\exists$) e universais ($\forall$) com leis de De Morgan.
* Compreender os requisitos formais de **Segurança de Expressões (*Safety*)** e a definição do **Domínio da Fórmula ($DOM(\psi)$)** para impedir consultas matematicamente válidas que gerariam relações infinitas em computadores reais.
* Formular consultas no **Cálculo Relacional de Domínios (CRD / DRC)** e compreender sua influência histórica direta na invenção da linguagem visual **QBE (Query By Example)** da IBM.
* Explicar o **Teorema da Equivalência de Edgar F. Codd (1972)** e o critério de **Completude Relacional (*Relational Completeness*)**, entendendo por que o SQL comercial adotou a interface declarativa do Cálculo e a representação interna algébrica.
* Dominar o pipeline de processamento do SGBD e aplicar as heurísticas fundamentais de **Otimização de Consultas (*Query Optimization*)**, especificamente o *Push-Down Selection* e *Push-Down Projection* em árvores de consulta (*Query Trees*), calculando ganhos drásticos de desempenho assintótico.
* Realizar a tradução conceitual e formal simultânea de consultas complexas do cotidiano (comércio eletrônico, livrarias e bibliotecas) entre **Álgebra Relacional**, **CRT**, **CRD** e **SQL**.

## Estrutura de Arquivos
* `plano_de_aula.md`: Planejamento pedagógico detalhado para 100 minutos de mentoria/aula presencial, objetivos de aprendizagem, cronograma em 5 blocos, roteiro slide a slide, definições teóricas formais e 4 exercícios práticos resolvidos passo a passo.
* `index.html`: Portal web interativo da aula com simulador comparativo de linguagens formais, analisador visual de árvores de consulta otimizadas, leitor de slides embutido, plano pedagógico e desafios formativos.
* `assets/img/`: Logotipos institucionais oficiais do IFCE Campus Tauá.
* `materiais/main.tex` e `materiais/secao*.tex`: Código-fonte LaTeX modularizado da apresentação de slides Beamer (tema institucional Scouts/IFCE widescreen 16:9) com árvores de consulta renderizadas em TikZ nativo.
* `materiais/main.pdf`: Apresentação de slides compilada em alta resolução (formato widescreen 16:9).

## Bibliografia Base Utilizada
1. **CODD, E. F.** A Relational Model of Data for Large Shared Data Banks. *Communications of the ACM*, New York, v. 13, n. 6, p. 377–387, June 1970.
2. **CODD, E. F.** Relational Completeness of Data Base Sublanguages. In: RUSTIN, R. (Ed.). *Data Base Systems*. Englewood Cliffs: Prentice-Hall, 1972. p. 65–98.
3. **ELMASRI, R.; NAVATHE, S. B.** *Sistemas de Banco de Dados*. 7. ed. São Paulo: Pearson Education do Brasil, 2018. (Capítulo 8 — Álgebra Relacional e Cálculo Relacional; Capítulo 19 — Otimização de Consultas).
4. **HEUSER, C. A.** *Projeto de Banco de Dados*. 6. ed. Porto Alegre: Bookman, 2009. (Capítulo 5 — A Linguagem da Álgebra Relacional).
5. **SILBERSCHATZ, A.; KORTH, H. F.; SUDARSHAN, S.** *Sistema de Banco de Dados*. 7. ed. Rio de Janeiro: GEN/LTC, 2020. (Capítulo 6 — Linguagens Formais; Capítulo 13 — Otimização de Consultas).
6. **DATE, C. J.** *Introdução a Sistemas de Bancos de Dados*. 8. ed. Rio de Janeiro: Elsevier Campus, 2004. (Capítulo 7 — Cálculo Relacional).