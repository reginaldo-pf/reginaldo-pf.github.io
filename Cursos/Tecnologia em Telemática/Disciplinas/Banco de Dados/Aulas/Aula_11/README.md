# Aula 11: Mapeamento Lógico Relacional (Parte 2) — Tabelas Associativas para N:M, Atributos Multivalorados, Relacionamentos Ternários e Especialização EER

Esta pasta contém o conjunto completo de recursos didáticos, plano pedagógico, portal interativo e apresentação de slides em Beamer da **Aula 11** da disciplina de **Banco de Dados** do Curso Superior de Tecnologia em Telemática (IFCE Campus Tauá).

> [!IMPORTANT]
> **Diretriz Pedagógica Obrigatória:** Para garantir o foco irrestrito na teoria matemática de Codd e no algoritmo de mapeamento de Elmasri & Navathe e Heuser, todos os exemplos, diagramas visuais e exercícios utilizam **exclusivamente entidades de domínios comuns e cotidianos** (escolas, alunos, disciplinas, clientes, salas e frotas de veículos), eliminando qualquer barreira cognitiva por jargões técnicos.

## Resumo de Competências
* Aplicar sistematicamente os passos avançados do **Algoritmo de Mapeamento Lógico Relacional de Elmasri & Navathe (Passos 5 a 8)** combinado às regras canônicas de **Heuser** para converter Diagramas Entidade-Relacionamento complexos em **Esquemas Lógicos Relacionais** na **Primeira Forma Normal (1FN)**.
* Executar o **Passo 5 (Relacionamentos Binários $N:M$)**: criar a **Tabela Associativa** (relação de junção), definir a Chave Primária Composta formada pela união das Chaves Estrangeiras que apontam para as entidades participantes ($\underline{PK} = \underline{\{FK_1, FK_2\}}$), alocar os atributos descritivos do relacionamento (matrícula de alunos) e mapear auto-relacionamentos recursivos $N:M$ (ex: disciplinas e seus pré-requisitos acadêmicos).
* Executar o **Passo 6 (Atributos Multivalorados)**: isolar coleções e listas em uma relação autônoma $R_A$, propagando a chave da entidade proprietária como Chave Estrangeira e compondo a Chave Primária por $\underline{PK} = \underline{\{FK_E, \text{Atributo}\}}$ com integridade referencial em cascata (`ON DELETE CASCADE`) para telefones e e-mails de clientes.
* Executar o **Passo 7 (Relacionamentos de Grau Superior / Ternários)**: mapear relacionamentos $n$-ários ($n \ge 3$) em tabelas de ligação especializadas (ex: alocação de professor, turma e sala), deduzindo rigorosamente a Chave Primária conforme as restrições de cardinalidade máxima ($N:M:P$ vs. $1:N:M$).
* Executar o **Passo 8 (Especialização e Generalização no Modelo EER)**: selecionar entre as 4 opções clássicas de mapeamento de hierarquias de herança (veículo, carro e caminhão), dominando a **Opção 8A (Múltiplas relações com Chave Primária e Estrangeira compartilhada $\underline{PK/FK}$)** para preservar a atomicidade e integridade sem colunas com `NULL`.
* **Nota Metodológica:** Todo o conteúdo apoia-se estritamente na **teoria formal do Modelo Relacional de Codd**: esquemas textuais intensionais, diagramas de esquemas relacionais com grafos dirigidos de integridade referencial e instâncias tabulares, sem necessidade de códigos em linguagens de programação ou dialetos proprietários.

## Estrutura de Arquivos
* `plano_de_aula.md`: Planejamento pedagógico detalhado de 100 minutos, objetivos de aprendizagem, cronograma em 5 blocos, roteiro slide a slide dos 36 slides, guia formal dos Passos 5 a 8 e 5 exercícios práticos contextualizados em domínios cotidianos (escolas, clientes, alocação de salas e veículos).
* `index.html`: Portal web interativo da aula com quadros comparativos visuais interativos, leitor de slides embutido, plano pedagógico, quadro sinóptico de decisão, exercícios e central de downloads.
* `assets/img/`: Logotipos institucionais do IFCE Campus Tauá e ícones visuais.
* `materiais/main.tex` e `materiais/secao*.tex`: Código-fonte modularizado da apresentação de slides em LaTeX Beamer (tema institucional Scouts/IFCE widescreen 16:9) com diagramas nativos em TikZ.
* `materiais/main.pdf`: Apresentação de slides compilada (36 páginas).

## Bibliografia Base Utilizada
1. **ELMASRI, R.; NAVATHE, S. B.** *Sistemas de Banco de Dados*. 7. ed. São Paulo: Pearson Addison Wesley, 2019. (Capítulo 9 — Mapeamento de Banco de Dados Relacional por Modelagem ER e EER: Passos 5, 6, 7 e 8).
2. **HEUSER, C. A.** *Projeto de Banco de Dados*. 6. ed. Porto Alegre: Bookman, 2009. (Capítulo 4 — Transformação entre Modelos: Do Modelo Conceitual ao Modelo Relacional).
3. **SILBERSCHATZ, A.; KORTH, H. F.; SUDARSHAN, S.** *Sistema de Banco de Dados*. 7. ed. Rio de Janeiro: GEN/LTC, 2020. (Capítulo 6 — Redução para Esquemas Relacionais).
4. **CODD, E. F.** A Relational Model of Data for Large Shared Data Banks. *Communications of the ACM*, v. 13, n. 6, p. 377–387, 1970.
5. **CHEN, P. P.** The Entity-Relationship Model — Toward a Unified View of Data. *ACM Transactions on Database Systems (TODS)*, v. 1, n. 1, p. 9–36, 1976.
