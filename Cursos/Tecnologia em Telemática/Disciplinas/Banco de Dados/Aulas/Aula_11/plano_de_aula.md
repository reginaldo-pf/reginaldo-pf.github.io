# Plano de Aula 11: Mapeamento Lógico Relacional (Parte 2) — Tabelas Associativas para N:M, Atributos Multivalorados, Relacionamentos Ternários e Especialização EER

## 1. Identificação
* **Instituição:** Instituto Federal de Educação, Ciência e Tecnologia do Ceará (IFCE) — Campus Tauá
* **Curso:** Tecnologia em Telemática
* **Disciplina:** Banco de Dados
* **Professor:** Prof. Me. Reginaldo Fernandes
* **Unidade Temática:** Unidade IV — Projeto Lógico de Banco de Dados Relacional (Parte 2)
* **Data Prevista:** 03/11/2026 (Terça-feira)
* **Carga Horária:** 2 horas-aula (100 minutos)
* **Regime Didático:** Mentoria Individual / PBL (Aprendizagem Baseada em Projetos)

> [!IMPORTANT]
> **Diretriz Didática Fundamental: Uso Exclusivo de Domínios Comuns e Cotidianos**  
> Fica expressamente estabelecido que **não devem ser utilizadas entidades ou cenários restritos à área técnica de telemática ou redes de computadores** (tais como roteadores, OLTs, switches, pacotes, interfaces de rede, enlaces ópticos DWDM, BGP ou ASNs) nos exemplos de sala de aula e nas listas de fixação. Toda a fundamentação, demonstrações em slides, diagramas e exercícios devem adotar estritamente **domínios universais e comuns do cotidiano** (gestão acadêmica/escolar, comércio/lojas, veículos, pessoas e bibliotecas). Esta diretriz assegura que o discente concentre sua carga cognitiva exclusivamente nas regras matemáticas e lógicas do Modelo Relacional e da 1ª Forma Normal (1FN), eliminando ruídos causados por jargões técnicos.

---

## 2. Objetivos de Aprendizagem
Ao final desta aula, o estudante deverá ser capaz de:
1. **Compreender a Limitação Estrutural dos Passos 1 a 4:** Demonstrar matematicamente por que relacionamentos $N:M$ e atributos multivalorados **não podem** ser representados por simples colunas de Chave Estrangeira em relações existentes sem violar a **Primeira Forma Normal (1FN)** (exigiria listas em células) ou provocar duplicação aberrante de tuplas (quebra da Chave Primária).
2. **Aplicar o Passo 5 (Relacionamentos Binários $N:M$):** Criar uma **Tabela Associativa** (relação de ligação / junção), definir sua **Chave Primária Composta** como a união das Chaves Estrangeiras que apontam para as relações participantes ($\underline{PK} = \underline{\{FK_1, FK_2\}}$), migrar atributos próprios do losango e mapear auto-relacionamentos recursivos $N:M$ (ex: pré-requisitos entre matérias).
3. **Aplicar o Passo 6 (Atributos Multivalorados):** Isolar atributos multivalorados em uma relação autônoma $R_A$, propagando a Chave Primária da relação proprietária como $FK$ e compondo a Chave Primária por $\underline{PK} = \underline{\{FK_E, \text{Atributo}\}}$, assegurando atomicidade na 1FN e política de exclusão em cascata (`ON DELETE CASCADE`).
4. **Aplicar o Passo 7 (Relacionamentos $n$-ários e Ternários):** Mapear vínculos de grau superior a 2 criando relações associativas com as $FK\text{s}$ de todas as entidades participantes, deduzindo rigorosamente a constituição da Chave Primária com base nas cardinalidades máximas ($N:M:P$ vs. $1:N:M$).
5. **Aplicar o Passo 8 (Especialização e Generalização no Modelo EER):** Selecionar e implementar as 4 opções formais de mapeamento de hierarquias de herança (com ênfase na **Opção 8A: Relações Múltiplas com Chave Primária/Estrangeira Compartilhada** $\underline{PK/FK}$).
6. **Consolidar o Esquema Lógico Relacional do Projeto Prático (AVP1):** Integrar todos os 8 passos do algoritmo sobre o minimundo de negócio escolhido, gerando a especificação relacional completa com arcos dirigidos de integridade referencial.

---

## 3. Cronograma Pedagógico (100 Minutos — 5 Blocos)

| Bloco | Tempo | Etapa Didática | Tópicos e Atividades | Recursos |
| :--- | :--- | :--- | :--- | :--- |
| **Bloco 1** | 15 min | **Ponte Conceitual & A Prova da 1FN** | Revisão rápida dos Passos 1 a 4 (Aula 10). Demonstração visual de por que $N:M$ e atributos multivalorados quebram a 1FN caso forçados em tabelas já existentes (ex: aluno e disciplinas cursadas). Apresentação do roadmap da Aula 11 (Passos 5 a 8). | Slides 1 a 7 |
| **Bloco 2** | 25 min | **Passo 5: Tabelas Associativas para $N:M$** | Regra algorítmica da Tabela Associativa. Definição da Chave Primária Composta ($\underline{PK} = \underline{\{FK_1, FK_2\}}$). Migração de atributos descritivos do relacionamento (ex: matrícula em matérias). Caso especial: auto-relacionamento recursivo $N:M$ de pré-requisitos. | Slides 8 a 11 |
| **Bloco 3** | 20 min | **Passo 6: Atributos Multivalorados** | Eliminação de vetores/listas. Criação da relação independente. Composição da chave primária ($\underline{PK} = \underline{\{FK_E, \text{Atributo}\}}$). Regras de integridade referencial e deleção em cascata (`CASCADE`). | Slides 12 a 14 |
| **Bloco 4** | 20 min | **Passos 7 e 8: Ternários e Especialização EER** | Relacionamentos $n$-ários / ternários: como as restrições de cardinalidade máxima determinam o tamanho da $PK$ associativa (ex: professor, turma e sala). Mapeamento de herança EER: as 4 opções de Elmasri & Navathe (foco na Opção 8A com $\underline{PK/FK}$ em veículos). | Slides 15 a 21 |
| **Bloco 5** | 20 min | **Estudo de Caso Integrado "EducaPlus" & Mentoria** | Transformação lógica completa dos requisitos integrados do sistema escolar **EducaPlus**. Construção do Esquema com arcos referenciais e resolução guiada de desafios práticos para a AVP1. | Slides 22 a 28 |

---

## 4. Roteiro Detalhado dos Slides (`materiais/main.pdf`)

1. **Capa:** Aula 11 — Mapeamento Lógico Relacional (Parte 2): Tabelas Associativas para $N:M$, Atributos Multivalorados, Relacionamentos Ternários e Especialização EER.
2. **Roteiro da Aula (Agenda):** Estrutura da apresentação em 9 seções lógicas.
3. **Ponte Pedagógica: O que Aprendemos na Aula 10?** Síntese dos Passos 1 a 4 (entidades fortes, entidades fracas, $1:1$ e $1:N$).
4. **O Dilema dos Vínculos Complexos: Por que Não Usar Simples FK?** A prova formal: listas em células quebram a atomicidade da 1FN; duplicação de tuplas viola a unicidade da Chave Primária.
5. **Visão Panorâmica do Algoritmo Completo (Passos 5 a 8):** O papel dos passos finais na conversão de estruturas ricas de dados para tabelas puras em 1FN.
6. **Divisor de Seção:** Passo 5 — Mapeamento de Relacionamentos Binários $N:M$.
7. **Passo 5: A Regra da Tabela Associativa:** Criação da relação de junção $R_{AB}$, propagação das chaves primárias como Chaves Estrangeiras e formação da Chave Primária Composta.
8. **Passo 5: Atributos Próprios do Relacionamento:** Alocação de atributos do losango (semestre, nota, quantidade) dentro da tabela associativa.
9. **Transformação Visual do Passo 5 ($N:M$ Regular):** Diagrama ANTES (`ALUNO` $N:M$ `DISCIPLINA`) $\Longrightarrow$ DEPOIS (Esquema Relacional com 2 arcos de FK dirigidos + Instância Tabular).
10. **Passo 5 (Variação Avançada): Auto-Relacionamento Recursivo $N:M$:** Como mapear estruturas de dependência mútua (`DISCIPLINA` que exige `DISCIPLINA` como pré-requisito) gerando duas FKs na mesma tabela associativa.
11. **Transformação Visual do Recursivo $N:M$:** Diagrama ANTES (`DISCIPLINA` recursivo) $\Longrightarrow$ DEPOIS (Relação `PRE_REQUISITO` com `cod_disc_fk` e `cod_prereq_fk`).
12. **Divisor de Seção:** Passo 6 — Mapeamento de Atributos Multivalorados.
13. **Passo 6: Regra Formal para Atributos Multivalorados:** Por que colunas fixas repetidas (`fone1`, `fone2`) violam o projeto relacional limpo; criação de relação separada e $\underline{PK} = \underline{\{FK_E, \text{Atributo}\}}$.
14. **Transformação Visual do Passo 6:** Diagrama ANTES (DER com elipse dupla `telefone` e `email`) $\Longrightarrow$ DEPOIS (Esquema Relacional + Instância Tabular com integridade referencial).
15. **Divisor de Seção:** Passo 7 — Mapeamento de Relacionamentos $n$-ários (Ternários).
16. **Passo 7: Regra Formal para Relacionamentos Ternários:** Criação de relação de ligação de grau superior contendo as chaves estrangeiras de todas as entidades participantes.
17. **Passo 7: A Determinação Crítica da Chave Primária:** Análise de cardinalidades ($N:M:P$ com PK de 3 atributos vs. $1:N:M$ com PK de 2 atributos e a terceira atuando como FK simples).
18. **Transformação Visual do Passo 7:** Diagrama ANTES (`PROFESSOR`, `TURMA` e `SALA`) $\Longrightarrow$ DEPOIS (Esquema Relacional com 3 arcos referenciais).
19. **Divisor de Seção:** Passo 8 — Mapeamento de Especialização e Generalização (EER).
20. **Passo 8: As 4 Opções Canônicas de Elmasri & Navathe:** Comparativo entre as Opções 8A (relações múltiplas com PK/FK compartilhada), 8B (apenas subclasses), 8C (relação única com tipo) e 8D (relação única com booleanos).
21. **Transformação Visual do Passo 8 (Opção 8A):** Diagrama ANTES (`VEICULO` especializa-se em `CARRO` e `CAMINHAO`) $\Longrightarrow$ DEPOIS (Superclasse + Subclasses com chave primária e estrangeira simultânea $\underline{PK/FK}$).
22. **Divisor de Seção:** Estudo de Caso Integrado — Sistema Escolar **EducaPlus**.
23. **Estudo de Caso "EducaPlus": DER Conceitual Integrado:** Apresentação do DER com $N:M$, multivalorados, recursivo e especialização EER.
24. **Transformação Relacional Completa "EducaPlus":** Esquema formal gerado contendo todas as relações, chaves primárias sublinhadas, chaves estrangeiras e atributos.
25. **Diagrama de Esquema Lógico com Arcos Referenciais:** Grafo relacional visual exibindo a teia de integridade referencial entre as tabelas do sistema.
26. **Quadro Sinóptico de Decisão para os Passos 5 a 8:** Tabela em largura total comparando construto DER, criação de relação, formação de PK e destino dos atributos.
27. **Checklist de Validação & Próxima Aula:** 5 perguntas de checagem do esquema lógico e introdução à **Álgebra Relacional (Aula 12)**.
28. **Referências Bibliográficas:** Obras clássicas de Elmasri & Navathe, Heuser, Silberschatz, Codd e Chen.

---

## 5. Guia de Referência: Passos 5 a 8 do Algoritmo de Mapeamento

> **Importante:** Todo o conteúdo é expresso através da **linguagem formal do Modelo Relacional de Codd**: esquemas textuais intensionais $R(\underline{PK}, A_1, FK \dots)$, diagramas de esquemas relacionais com arcos referenciais dirigidos e instâncias tabulares extensionais na Primeira Forma Normal (1FN).

### Passo 5 — Mapeamento de Tipos de Relacionamentos Binários $N:M$ (M:N)
Para cada tipo de relacionamento binário $N:M$ (M:N) $R$ entre duas entidades $S$ e $T$:
1. **Criação da Tabela Associativa:** Cria-se obrigatoriamente uma nova relação $R_{ST}$ (relação de junção ou tabela associativa).
2. **Propagação das Chaves:** Incluem-se como **Chaves Estrangeiras ($FK$)** as chaves primárias $\underline{PK_S}$ de $S$ e $\underline{PK_T}$ de $T$.
3. **Formação da Chave Primária Composta:** A Chave Primária de $R_{ST}$ é formada pela **união das duas chaves estrangeiras**:
   $$\underline{PK(R_{ST})} = \underline{\{FK_S, FK_T\}}$$
4. **Migração de Atributos:** Todos os atributos simples pertencentes ao relacionamento (desenhados no losango no DER) migram diretamente como colunas da relação $R_{ST}$.
5. **Nulidade:** As colunas que compõem a Chave Primária Composta são estritamente `NOT NULL`, satisfazendo a Regra de Integridade de Entidade.
6. **Auto-Relacionamento Recursivo $N:M$:** Quando uma entidade $E$ possui um relacionamento $N:M$ consigo mesma (ex: `PRE_REQUISITO` entre disciplinas), a tabela associativa $R_{\text{rec}}$ conterá **duas Chaves Estrangeiras distintas**, ambas apontando para a Chave Primária de $E$, devendo receber nomes semânticos que esclareçam os papéis desempenhados (ex: `cod_disc_fk` e `cod_prereq_fk`). A chave primária é composta pelas duas $FK\text{s}$.

### Passo 6 — Mapeamento de Atributos Multivalorados
Para cada atributo multivalorado $A$ de uma entidade proprietária $E$:
1. **Criação de Relação Independente:** Cria-se uma nova relação $R_A$.
2. **Propagação da Chave Proprietária:** Inclui-se como **Chave Estrangeira ($FK$)** a Chave Primária $\underline{PK_E}$ da relação proprietária $R_E$.
3. **Inclusão do Atributo:** Adiciona-se o próprio atributo $A$ como coluna de $R_A$ (se $A$ for composto, desmembra-se em seus componentes atômicos).
4. **Formação da Chave Primária Composta:** A Chave Primária de $R_A$ é a combinação da Chave Estrangeira com o próprio valor do atributo multivalorado:
   $$\underline{PK(R_A)} = \underline{\{FK_E, A\}}$$
   Isso garante que um mesmo valor não se repita para a mesma entidade e assegura a unicidade na 1FN.
5. **Ação Referencial:** Define-se integridade referencial com remoção em cascata (`ON DELETE CASCADE`), pois instâncias de atributos multivalorados perdem o sentido se a entidade principal for excluída.

### Passo 7 — Mapeamento de Relacionamentos de Grau Superior ($n$-ários / Ternários)
Para cada tipo de relacionamento $R$ de grau $n > 2$ associando as entidades $E_1, E_2, \dots, E_n$:
1. **Criação da Relação Associativa:** Cria-se uma nova relação $R_{\text{ass}}$.
2. **Inclusão de Chaves Estrangeiras:** Incluem-se as chaves primárias de todas as $n$ entidades participantes como Chaves Estrangeiras ($FK_1, FK_2, \dots, FK_n$) em $R_{\text{ass}}$.
3. **Inclusão de Atributos Próprios:** Quaisquer atributos pertencentes ao relacionamento são alocados em $R_{\text{ass}}$.
4. **Regra de Dedução da Chave Primária ($\underline{PK}$):**
   * **Caso Geral ($N:M:P$):** Se todas as cardinalidades máximas forem $N$ (nenhuma entidade está restrita a no máximo 1 ocorrência), a $\underline{PK}$ é a combinação de **todas as $n$ chaves estrangeiras**:
     $$\underline{PK} = \underline{\{FK_1, FK_2, \dots, FK_n\}}$$
   * **Caso com Cardinalidade Máxima 1 (ex: $1:N:M$):** Se a cardinalidade máxima de uma das entidades (ex: $E_1$) associada ao par das outras duas $(E_2, E_3)$ for igual a $1$, a Chave Primária de $R_{\text{ass}}$ é formada **apenas pelas chaves de $E_2$ e $E_3$**:
     $$\underline{PK} = \underline{\{FK_2, FK_3\}}$$
     A chave $FK_1$ entra em $R_{\text{ass}}$ apenas como Chave Estrangeira simples, pois para cada par de ocorrências de $(E_2, E_3)$ existe no máximo um único $E_1$ correspondente!

### Passo 8 — Mapeamento de Especialização / Generalização (Modelo EER)
Para mapear uma hierarquia de herança com superclasse $C$ (com chave primária $k$) e subclasses $\{S_1, S_2, \dots, S_m\}$, utilizam-se as opções canônicas de Elmasri & Navathe:
* **Opção 8A (Múltiplas Relações com Chave Compartilhada $\underline{PK/FK}$ — Padrão Recomendado):**
  * Cria-se uma relação para a superclasse $C$ com sua chave primária $\underline{k}$ e todos os atributos genéricos comuns.
  * Cria-se uma relação para cada subclasse $S_i$ contendo os atributos específicos daquela subclasse mais a chave $\underline{k}$.
  * A chave $\underline{k}$ em cada relação de subclasse $S_i$ atua simultaneamente como **Chave Primária e Chave Estrangeira** apontando para $C$ ($\underline{PK/FK} \longrightarrow C.k$).
  * *Vantagem:* Funciona universalmente para qualquer restrição de disjunção (disjunta ou sobreposta) e participação (total ou parcial), eliminando valores `NULL`.
* **Opção 8B (Relações Apenas para as Subclasses):**
  * Cria-se uma relação para cada subclasse, duplicando os atributos da superclasse em todas elas.
  * *Condição estrita:* Aplicável apenas se a especialização for **Total e Disjunta**.
* **Opção 8C (Relação Única com Atributo Discriminador de Tipo):**
  * Funde-se toda a hierarquia em uma única relação com todos os atributos comuns e específicos, acrescentando uma coluna discriminadora (ex: `tipo_veiculo`).
  * *Restrição:* Só é aplicável se a especialização for **Disjunta** e aceita valores `NULL` nas colunas de atributos específicos de outras subclasses.
* **Opção 8D (Relação Única com Indicadores Booleanos Múltiplos):**
  * Cria-se uma única relação com colunas booleanas (`eh_carro`, `eh_caminhao`), indicada para especializações **Sobrepostas**.

---

## 6. Lista de Exercícios de Fixação (Modelagem e Transformação Lógica)

### Exercício 1 — Passo 5: Tabela Associativa $N:M$ e Atributos de Vínculo
No sistema de gestão acadêmica de uma instituição de ensino, alunos matriculam-se em diversas disciplinas a cada semestre, e cada disciplina possui múltiplos alunos matriculados:
* Entidade Forte **`ALUNO`**: $\underline{\text{matricula}}$, `nome_aluno`, `curso`, `data_ingresso`.
* Entidade Forte **`DISCIPLINA`**: $\underline{\text{cod\_disc}}$, `nome_disciplina`, `carga_horaria`, `ementa`.
* Relacionamento **`MATRICULA`**: cardinalidade `ALUNO` $(0, N)$ --- $\langle\text{MATRICULA}\rangle$ --- $(1, N)$ `DISCIPLINA`. O vínculo possui os seguintes atributos próprios: `semestre_letivo`, `nota_final` e `frequencia_pct`.

**Pede-se:**
1. Escreva o esquema relacional resultante da aplicação do **Passo 5**, explicitando a criação da tabela associativa, sublinhando sua Chave Primária Composta e indicando as Chaves Estrangeiras ($FK\text{s}$).
2. Explique formalmente o que aconteceria se tentássemos registrar a matrícula colocando a chave `cod_disc` da disciplina diretamente na tabela `ALUNO`. Por que isso violaria a **1FN**?
3. Construa uma **instância tabular** consistente com 3 matrículas, mostrando um mesmo aluno cursando 2 disciplinas distintas no mesmo semestre.

### Exercício 2 — Passo 5 Avançado: Auto-Relacionamento Recursivo $N:M$ (Grade Curricular)
Na estrutura do plano pedagógico de um curso, uma matéria pode exigir outras disciplinas como pré-requisitos antes de ser cursada, e uma mesma disciplina introdutória pode servir de pré-requisito para várias outras matérias avançadas:
* Entidade Forte **`DISCIPLINA`**: $\underline{\text{cod\_disc}}$, `nome_disciplina`, `carga_horaria`.
* Relacionamento Recursivo $N:M$ **`EXIGE_PRE_REQUISITO`**: cada disciplina pode ter de $0$ a $N$ disciplinas pré-requisito, e cada matéria pode ser pré-requisito de $0$ a $N$ outras disciplinas. O relacionamento possui o atributo próprio `tipo_exigencia` (com valores como 'Obrigatório' ou 'Recomendado').

**Pede-se:**
1. Derive o esquema relacional completo aplicando o **Passo 5 para auto-relacionamento recursivo**. Dê nomes semânticos claros às duas Chaves Estrangeiras na tabela de ligação.
2. Como a Chave Primária da tabela de ligação deve ser configurada? O par $(\text{MAT2}, \text{MAT1})$ tem o mesmo significado que $(\text{MAT1}, \text{MAT2})$?
3. Desenhe o **Diagrama de Esquema Relacional** com os arcos referenciais dirigidos apontando para a tabela principal.

### Exercício 3 — Passo 6: Atributos Multivalorados e Eliminação de Vetores
No cadastro de clientes de uma livraria comercial, a entidade forte **`CLIENTE`** possui os seguintes dados no DER:
* `id_cliente` (identificador principal);
* `cpf` (chave candidata única);
* `nome_completo` (simples);
* `{telefone_contato}` (atributo multivalorado: residencial, celular pessoal, recado);
* `{email_adicional}` (atributo multivalorado: e-mail principal, e-mail corporativo).

**Pede-se:**
1. Apresente duas abordagens ingênuas (antipatterns) frequentemente tentadas por projetistas inexperientes para armazenar `{telefone_contato}` na tabela principal e demonstre as deficiências graves de cada uma (violação da 1FN ou proliferação de `NULL`s com limite arbitrário de colunas `fone1`, `fone2`).
2. Aplique rigorosamente o **Passo 6** do Algoritmo de Mapeamento para `{telefone_contato}` e `{email_adicional}`. Escreva os esquemas relacionais de todas as tabelas geradas.
3. Demonstre por que a cláusula `ON DELETE CASCADE` é imprescindível nas Chaves Estrangeiras geradas a partir do Passo 6.

### Exercício 4 — Passo 7: Relacionamento Ternário e Determinação da Chave Primária
Considere o gerenciamento de alocação de aulas em uma escola:
* Um **`PROFESSOR`** ($\underline{\text{id\_prof}}$, `nome_professor`) ministra aula para uma **`TURMA`** ($\underline{\text{cod\_turma}}$, `ano_semestre`) em uma determinada **`SALA`** ($\underline{\text{num\_sala}}$, `bloco`).
* As três entidades participam do relacionamento ternário **`ALOCACAO_AULA`** com os atributos `dia_semana` e `horario`.
* **Regra de Negócio:** Para cada par constituído por um professor e uma turma, a aula ocorre em **no máximo uma única sala** de aula no mesmo horário (cardinalidade máxima de `SALA` associada ao par professor-turma é igual a $1$).

**Pede-se:**
1. Escreva o esquema relacional da tabela associativa resultante, indicando os atributos que compõem a Chave Primária Composta.
2. Justifique formalmente por que a chave `num_sala_fk` entra na tabela associativa apenas como **Chave Estrangeira simples** e não pode fazer parte da $\underline{PK}$.
3. Desenhe o Diagrama de Esquema Relacional com os três arcos dirigidos de integridade referencial.

### Exercício 5 — Passo 8: Especialização/Generalização EER (Frotas e Veículos)
Em uma concessionária de transportes, todos os veículos automotores compartilham atributos comuns, mas possuem propriedades específicas de sua categoria:
* Superclasse **`VEICULO`**: $\underline{\text{placa}}$, `renavam` (AK), `marca`, `modelo`, `ano_fab`, `valor_aquisicao`.
* Subclasse **`CARRO`**: `qtd_portas`, `tipo_cambio`, `volume_porta_malas_litros`.
* Subclasse **`CAMINHAO`**: `num_eixos`, `capacidade_carga_ton`, `tipo_carroceria`.
* **Restrição EER:** Especialização **Total e Disjunta** (todo veículo é de exatamente uma dessas categorias).

**Pede-se:**
1. Mapeie essa hierarquia utilizando a **Opção 8A (Múltiplas relações com chave compartilhada $\underline{PK/FK}$)**. Escreva os esquemas formais das 3 relações resultantes e explique por que a chave nas subclasses desempenha duplo papel.
2. Mapeie a mesma hierarquia utilizando a **Opção 8C (Relação única com tipo)**. Escreva o esquema relacional resultante e comente o impacto sobre o armazenamento de valores `NULL`.
3. Qual dessas duas abordagens é mais segura para preservar a integridade do banco de dados quando novas subclasses de veículos forem adicionadas no futuro? Justifique tecnicamente.
