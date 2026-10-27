# Aula 10: Mapeamento Lógico Relacional (Parte 1) — Entidades Fortes, Fracas e Relacionamentos 1:1 e 1:N

Esta pasta contém o conjunto completo de recursos didáticos, plano pedagógico, portal interativo e apresentação de slides em Beamer da **Aula 10** da disciplina de **Banco de Dados** do Curso Superior de Tecnologia em Telemática (IFCE Campus Tauá).

## Resumo de Competências
* Aplicar sistematicamente o **Algoritmo de Mapeamento Lógico Relacional de Elmasri & Navathe (Passos 1 a 4)** combinado às regras de transformação de **Heuser** para converter um Diagrama Entidade-Relacionamento (DER) conceitual em um **Esquema Lógico Relacional** formal.
* Executar o **Passo 1 (Entidades Regulares/Fortes)**: criar relações base na **Primeira Forma Normal (1FN)**, aplicando o **achatamento (*flattening*)** de atributos compostos nos seus subatributos atômicos e omitindo atributos derivados.
* Executar o **Passo 2 (Entidades Fracas e Relacionamentos Identificadores)**: propagar a chave primária da entidade proprietária como chave estrangeira e combiná-la ao discriminador parcial para formar uma **Chave Primária Composta** ($\underline{PK_W} = \underline{FK_E + \text{Discriminador}}$).
* Executar o **Passo 3 (Relacionamentos Binários $1:1$)**: selecionar entre as 3 abordagens de mapeamento (**Abordagem A — Chave Estrangeira na Participação Total $(1,1)$ com restrição de unicidade `AK`**, **Abordagem B — Fusão em Relação Única** quando ambos os lados têm participação total $(1,1)$, ou **Abordagem C — Relação de Referência Cruzada** quando ambos os lados são $(0,1)$ e o relacionamento é esparso) para minimizar valores `NULL`.
* Executar o **Passo 4 (Relacionamentos Binários $1:N$ e Auto-Relacionamentos Recursivos $1:N$)**: propagar sempre a chave primária do lado $1$ como chave estrangeira na relação do lado $N$ ($FK_{\text{lado } N} \longrightarrow PK_{\text{lado } 1}$), incluindo a migração de atributos de relacionamento e o renomeio semântico de papéis em relacionamentos recursivos.
* **Nota Metodológica:** Todo o conteúdo utiliza exclusivamente **modelagem conceitual e lógica relacional** (diagramas DER de Chen e Heuser, esquemas textuais formais $R(\underline{PK}, A_1, \dots)$, diagramas de esquema relacional com arcos referenciais dirigidos e instâncias tabulares), sem qualquer código em linguagens de programação ou scripts físicos.

## Estrutura de Arquivos
* `plano_de_aula.md`: Planejamento pedagógico de 100 minutos, objetivos de aprendizagem, roteiro detalhado dos 28 slides, guia passo a passo de transformação **ANTES (DER) $\Longrightarrow$ DEPOIS (Relacional)** e 5 exercícios de modelagem e transformação lógica.
* `index.html`: Portal web interativo da aula com quadros comparativos visuais SVG (DER Conceitual $\to$ Esquema Lógico Relacional e Instância Tabular) para os Passos 1 a 4, matriz de decisão completa, leitor de slides embutido, cronograma e exercícios.
* `assets/img/`: Logotipos institucionais do IFCE Campus Tauá e ícones do tema Beamer.
* `materiais/main.tex` e `materiais/secao*.tex`: Código-fonte modularizado dos slides em LaTeX Beamer (tema institucional Scouts/IFCE) com diagramas nativos em TikZ ilustrando todas as transformações antes e depois.
* `materiais/main.pdf`: Apresentação de slides compilada (28 páginas em formato widescreen 16:9).

## Bibliografia Base Utilizada
1. **ELMASRI, R.; NAVATHE, S. B.** *Sistemas de Banco de Dados*. 7. ed. São Paulo: Pearson Addison Wesley, 2019. (Capítulo 9 — Mapeamento de Banco de Dados Relacional por Modelagem ER e EER).
2. **HEUSER, C. A.** *Projeto de Banco de Dados*. 6. ed. Porto Alegre: Bookman, 2009. (Capítulo 4 — Transformação entre Modelos: Do Modelo Conceitual ao Modelo Relacional).
3. **SILBERSCHATZ, A.; KORTH, H. F.; SUDARSHAN, S.** *Sistema de Banco de Dados*. 7. ed. Rio de Janeiro: GEN/LTC, 2020. (Capítulo 6 — Redução para Esquemas Relacionais).
4. **CODD, E. F.** A Relational Model of Data for Large Shared Data Banks. *Communications of the ACM*, v. 13, n. 6, p. 377–387, 1970.
5. **CHEN, P. P.** The Entity-Relationship Model — Toward a Unified View of Data. *ACM Transactions on Database Systems (TODS)*, v. 1, n. 1, p. 9–36, 1976.
