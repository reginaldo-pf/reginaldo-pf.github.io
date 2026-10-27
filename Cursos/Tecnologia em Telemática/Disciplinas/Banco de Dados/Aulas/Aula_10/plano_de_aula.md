# Plano de Aula 10: Mapeamento Lógico Relacional (Parte 1) — Entidades Fortes, Fracas e Relacionamentos 1:1 e 1:N

## 1. Identificação
* **Instituição:** Instituto Federal de Educação, Ciência e Tecnologia do Ceará (IFCE) — Campus Tauá
* **Curso:** Tecnologia em Telemática
* **Disciplina:** Banco de Dados
* **Professor:** Prof. Reginaldo
* **Unidade Temática:** Unidade IV — Projeto Lógico de Banco de Dados Relacional (Parte 1)
* **Data Prevista:** 27/10/2026
* **Carga Horária:** 2 horas-aula (100 minutos)

---

## 2. Objetivos de Aprendizagem
Ao final desta aula, o estudante deverá ser capaz de:
1. **Compreender a Natureza Algorítmica do Mapeamento Lógico:** Entender como um Diagrama Entidade-Relacionamento (DER) validado nas Aulas 04 a 08 é convertido de forma determinística em um Esquema Lógico Relacional formal fundamentado no Modelo de Codd (Aula 09).
2. **Aplicar o Passo 1 (Entidades Fortes e Atributos):** Converter entidades regulares em relações base na **Primeira Forma Normal (1FN)**, realizando o **achatamento (*flattening*)** de atributos compostos em subatributos atômicos e omitindo atributos derivados do esquema armazenado.
3. **Aplicar o Passo 2 (Entidades Fracas):** Transformar entidades fracas propagando a Chave Primária ($PK$) da entidade forte proprietária como Chave Estrangeira ($FK$) e compondo a Chave Primária da entidade fraca como a união da $FK$ com o discriminador parcial ($\underline{PK_W} = \underline{FK_E + \text{Discriminador}}$).
4. **Aplicar o Passo 3 (Relacionamentos Binários $1:1$):** Distinguir e escolher tecnicamente entre as 3 estratégias de mapeamento $1:1$ (**Abordagem A — Chave Estrangeira no lado de Participação Total $(1,1)$ com restrição de Chave Alternativa `AK`**; **Abordagem B — Fusão em Relação Única** quando ambos os lados possuem participação total $(1,1)$; e **Abordagem C — Relação de Referência Cruzada** quando ambos os lados são $(0,1)$ e o vínculo é altamente esparso).
5. **Aplicar o Passo 4 (Relacionamentos Binários $1:N$ e Recursivos $1:N$):** Propagar sempre a $PK$ do lado de cardinalidade máxima $1$ como $FK$ na relação do lado de cardinalidade máxima $N$, demonstrando por que a inversão violaria a **1FN**, e mapear auto-relacionamentos recursivos $1:N$ em uma única relação com arco referencial interno.

---

## 3. Cronograma Pedagógico (100 Minutos — 5 Blocos)

| Bloco | Tempo | Etapa Didática | Tópicos e Atividades | Recursos |
| :--- | :--- | :--- | :--- | :--- |
| **Bloco 1** | 15 min | **Ponte Conceitual $\to$ Lógico** | Revisão da anatomia formal do Modelo Relacional (Aula 09) e apresentação da visão geral do Algoritmo de 7 Passos de Elmasri & Navathe (foco hoje nos Passos 1 a 4). | Slides 1 a 7 |
| **Bloco 2** | 25 min | **Passos 1 e 2: Entidades Fortes e Fracas** | Transformação visual **ANTES (DER) $\Longrightarrow$ DEPOIS (Relacional)**: achatamento de atributos compostos, omissão de derivados e formação da chave primária composta em entidades fracas. | Slides 8 a 14 |
| **Bloco 3** | 25 min | **Passo 3: Relacionamentos Binários $1:1$** | Análise comparativa das 3 abordagens (FK no lado total com `AK`, Fusão em relação única e Relação de referência cruzada) com auditoria da densidade de valores `NULL`. | Slides 15 a 18 |
| **Bloco 4** | 20 min | **Passo 4: Relacionamentos $1:N$ e Recursivos** | Regra de ouro do $1:N$ ($PK_{\text{lado } 1} \to FK_{\text{lado } N}$), prova visual da violação da 1FN no sentido inverso, migração de atributos do losango e auto-relacionamento $1:N$. | Slides 19 a 23 |
| **Bloco 5** | 15 min | **Estudo de Caso Integrado e Desafios** | Transformação ponta a ponta do DER da Operadora de Telecomunicações **TeleTauá** (Passos 1 a 4) com matriz de rastreabilidade e resolução guiada de desafios em sala. | Slides 24 a 28 |

---

## 4. Roteiro Detalhado dos 28 Slides (`materiais/main.pdf`)

1. **Capa:** Aula 10 — Mapeamento Lógico Relacional (Parte 1): Entidades Fortes, Fracas e Relacionamentos $1:1$ e $1:N$.
2. **Roteiro da Aula (Agenda):** Estrutura da aula em 8 seções temáticas.
3. **Onde Estamos na Jornada de Projeto de BD?** Diagrama de fases: Mini-Mundo $\to$ Modelo Conceitual (Aulas 04–08) $\to$ Modelo Lógico Relacional (Aulas 09–11).
4. **Por que Precisamos de um Algoritmo Sistemático?** Riscos da conversão *ad-hoc* vs. garantias do algoritmo formal de Elmasri & Navathe / Heuser.
5. **O Algoritmo de 7 Passos de Elmasri & Navathe:** Visão panorâmica dos Passos 1 a 4 (Aula 10) e Passos 5 a 7 (Aula 11).
6. **Convenções Gráficas de Transformação (Antes $\to$ Depois):** Notação de sublinhado contínuo ($\underline{PK}$), tracejado ($\dashuline{\text{ Discriminador }}$), destaque de $FK$, chave alternativa (`AK`) e arcos referenciais dirigidos.
7. **Divisor de Seção:** Passo 1 — Mapeamento de Entidades Regulares (Fortes).
8. **Passo 1: Regra Formal para Entidades Fortes:** Algoritmo passo a passo para entidades regulares e escolha entre chaves candidatas.
9. **Passo 1: O que Acontece com Atributos Compostos e Derivados?** Achatamento (*flattening*) para preservar a 1FN e omissão de atributos derivados.
10. **Transformação Visual do Passo 1: Entidade Forte:** Diagrama completo **ANTES (DER de `PACIENTE`) $\Longrightarrow$ DEPOIS (Esquema de Relação + Instância Tabular na 1FN)**.
11. **Divisor de Seção:** Passo 2 — Mapeamento de Entidades Fracas.
12. **Passo 2: Regra Formal para Entidades Fracas:** Propagação da $PK$ proprietária e formação da Chave Primária Composta ($\underline{PK_W} = \underline{FK_E + \text{Chave Parcial}}$).
13. **Transformação Visual do Passo 2: Entidade Fraca:** Diagrama completo **ANTES (DER de `OLT` e `PORTA_PON`) $\Longrightarrow$ DEPOIS (Esquema Relacional com Arco Referencial + Instância Tabular)**.
14. **Divisor de Seção:** Passo 3 — Relacionamentos Binários $1:1$.
15. **Passo 3: As 3 Opções para Relacionamentos Binários $1:1$:** Apresentação das Abordagens A (FK no lado Total), B (Fusão em Tabela Única) e C (Relação de Referência Cruzada).
16. **Transformação Visual do Passo 3 (Abordagem A — FK):** Comparativo visual no DER `(0,1):(1,1)` (`TECNICO` — `GERENCIA` — `ESTACAO_ERB`) demonstrando a escolha correta sem `NULL` vs. escolha incorreta com alta taxa de `NULL`.
17. **Passo 3: Abordagens B (Fusão) e C (Referência Cruzada) + Matriz:** Diagrama de fusão para `(1,1):(1,1)` e tabela de decisão técnica das 3 estratégias $1:1$.
18. **Divisor de Seção:** Passo 4 — Relacionamentos Binários $1:N$.
19. **Passo 4: A Regra de Ouro dos Relacionamentos $1:N$:** Por que a $PK$ do lado $1$ vai sempre para o lado $N$ e prova de que o sentido inverso viola a 1FN.
20. **Transformação Visual do Passo 4: Relacionamento $1:N$ Regular:** Diagrama completo **ANTES (`POP_REGIONAL` $1:N$ `ROTEADOR_BORDA`) $\Longrightarrow$ DEPOIS (Esquema Relacional + Instância Tabular)**.
21. **Passo 4 (Variação): Auto-Relacionamento (Recursivo) $1:N$:** Transformação de relacionamento unário (`TECNICO` — `SUPERVISIONA` — `TECNICO`) em uma única relação com arco referencial interno.
22. **Divisor de Seção:** Matriz Resumo de Decisão (Passos 1 a 4).
23. **Quadro Sinóptico de Mapeamento (Passos 1 a 4):** Tabela de referência completa com construto MER, cardinalidade, regra de transformação, destino dos atributos e restrição de `NULL` na $FK$.
24. **Divisor de Seção:** Estudo de Caso Completo — Rede FTTH **TeleTauá**.
25. **Estudo de Caso: ANTES (DER Conceitual) $\to$ DEPOIS (Relacional):** Transformação integrada de 4 entidades (`ESTACAO_CENTRAL`, `TECNICO`, `OLT`, `PORTA_PON`) e 4 relacionamentos (`GERENCIA` $1:1$, `ABRIGA` $1:N$, `SUPERVISIONA` $1:N$ recursivo, `CONTEM_PORTA` $1:N$ identificador).
26. **Rastreabilidade Completa da Transformação "TeleTauá":** Auditoria passo a passo das 4 relações geradas, suas chaves primárias, chaves estrangeiras, chaves alternativas e regras de nulidade.
27. **Desafios Práticos de Mapeamento em Sala:** 3 problemas de transformação lógica para resolução imediata.
28. **Referências Bibliográficas e Próxima Aula:** Leituras recomendadas e prévia da Aula 11 (Passos 5 a 7: $N:M$, multivalorados, $n$-ários e especialização EER).

---

## 5. Guia de Referência: Passos 1 a 4 do Algoritmo de Mapeamento

> **Importante:** Nesta etapa da disciplina, todas as transformações são expressas exclusivamente por meio de **notação de esquemas relacionais formais**, **diagramas de esquema relacional com arcos referenciais** e **instâncias tabulares**, sem uso de linguagens de programação ou scripts físicos.

### Passo 1 — Entidades Regulares (Fortes)
Para cada entidade regular (forte) $E$ do DER, cria-se uma relação base $R$:
1. **Atributos Simples:** Todos os atributos simples de $E$ tornam-se atributos atômicos de $R$.
2. **Atributos Compostos (Achatamento / *Flattening*):** O atributo composto agrupador desaparece e apenas seus **subatributos simples folhas** são incluídos como colunas atômicas de $R$ (preservando a **1FN**).
3. **Atributos Derivados (Omissão):** Atributos tracejados no DER (calculáveis a partir de outros dados, como `idade` ou `total_portas`) **não são incluídos** na relação base armazenada para evitar anomalias de atualização.
4. **Chaves:** O identificador principal torna-se a **Chave Primária ($\underline{PK}$)**; outros identificadores candidatos são documentados como **Chaves Alternativas (`AK`)**.

### Passo 2 — Entidades Fracas e Relacionamentos Identificadores
Para cada entidade fraca $W$ que depende de uma entidade proprietária $E$ por meio de um relacionamento identificador $1:N$:
1. Cria-se uma relação $R_W$ contendo todos os atributos simples (ou subatributos achatados) de $W$.
2. Inclui-se em $R_W$, como **Chave Estrangeira ($FK$)**, a chave primária $\underline{PK_E}$ da relação proprietária $R_E$.
3. A **Chave Primária de $R_W$** é obrigatoriamente **composta**:
   $$\underline{PK_{R_W}} = \underline{FK_{R_E} + \text{Discriminador Parcial de } W}$$
4. O próprio relacionamento identificador (losango duplo) já fica representado por essa chave estrangeira e **não gera tabela adicional**.

### Passo 3 — Relacionamentos Binários $1:1$
Para cada relacionamento binário $1:1$ entre as relações $S$ e $T$, analisa-se a **cardinalidade mínima (participação)**:
* **Abordagem A — Chave Estrangeira (Padrão para $(0,1) : (1,1)$):** Escolhe-se a relação que possui **participação total $(1,1)$** (ex: $T$) para receber a chave primária da outra relação ($S$) como Chave Estrangeira ($FK$). Assim, a $FK$ em $T$ **nunca será `NULL`**. Além disso, impõe-se uma restrição de **Chave Alternativa (`AK` / Unicidade)** sobre essa $FK$ para garantir a proporção $1:1$. Atributos do relacionamento migram junto com a $FK$ para $T$.
* **Abordagem B — Fusão em Relação Única (Exclusiva para $(1,1) : (1,1)$):** Quando **ambas** as entidades participam totalmente $(1,1)$ do relacionamento e não participam de outros vínculos conflitantes, fundem-se $S$ e $T$ em uma única relação $R_{ST}$, escolhendo uma das chaves como $\underline{PK}$ e mantendo a outra como `AK`.
* **Abordagem C — Relação de Referência Cruzada (Para $(0,1) : (0,1)$ muito esparso):** Quando ambas as participações são opcionais $(0,1)$ e raríssimas tuplas se relacionam, cria-se uma terceira relação $R_{\text{rel}}(\underline{FK_S}, FK_T\text{ [AK]}, \text{atributos})$ para eliminar completamente valores `NULL` nas tabelas principais.

### Passo 4 — Relacionamentos Binários $1:N$ (Regulares e Recursivos)
* **Relacionamento Binário $1:N$ Regular:** Identifica-se a relação $S$ no **lado $1$** e a relação $T$ no **lado $N$**. Propaga-se a chave primária $\underline{PK_S}$ do lado $1$ como **Chave Estrangeira ($FK$)** dentro da relação $T$ do **lado $N$** ($FK \longrightarrow PK_S$). Quaisquer atributos próprios do losango migram para a relação do lado $N$.
  * *Participação de $T$ no lado $N$:* Se a participação de $T$ for total $(1,1)$, a $FK$ **não aceita `NULL`**. Se for parcial $(0,1)$, a $FK$ **aceita `NULL`**.
* **Auto-Relacionamento (Recursivo) $1:N$:** Quando uma entidade $E$ relaciona-se consigo mesma na proporção $1:N$ (ex: `SUPERVISIONA`), **nenhuma nova relação é criada**. Adiciona-se na própria relação $R_E$ uma Chave Estrangeira com nome semântico do papel de cardinalidade máxima $1$ (ex: `mat_supervisor_fk`) apontando para a própria $\underline{PK}$ de $R_E$.

---

## 6. Lista de Exercícios de Fixação (Modelagem e Transformação Lógica)

### Exercício 1 — Passo 1: Entidade Forte, Achatamento e Derivados
No DER de uma operadora de telecomunicações, a entidade regular **`ASSINANTE`** possui os seguintes atributos:
* `id_assinante` (identificador principal);
* `cpf` (identificador alternativo único);
* `nome_completo` (composto por `primeiro_nome` e `sobrenome`);
* `endereco_instalacao` (composto por `logradouro`, `numero`, `bairro` e `cep`);
* `data_adesao` (simples);
* `tempo_fidelidade_meses` (derivado, calculado a partir de `data_adesao`).

**Pede-se:**
1. Escreva a **intensão formal** do esquema de relação resultante da aplicação do **Passo 1**, indicando a Chave Primária ($\underline{PK}$) e a Chave Alternativa (`AK`).
2. Justifique formalmente por que os agrupadores `nome_completo` e `endereco_instalacao` e o atributo `tempo_fidelidade_meses` não aparecem como colunas da relação base.
3. Desenhe uma **instância tabular** válida com 2 tuplas para essa relação.

### Exercício 2 — Passo 2: Cadeia de Entidades Fracas (2 Níveis)
Em um datacenter regional, existe a entidade forte **`PREDIO`** ($\underline{\text{cod\_predio}}$, `nome_predio`). Dentro de cada prédio, as salas de equipamentos são numeradas sequencialmente a partir de `1` (Sala 1, Sala 2...) apenas dentro daquele prédio, constituindo a entidade fraca **`SALA_TECNICA`** (discriminador $\dashuline{\text{num\_sala}}$, atributo `area_m2`). Por sua vez, dentro de cada sala técnica, os bastidores (racks) também são numerados a partir de `1` (Rack 1, Rack 2...) apenas dentro daquela sala específica, formando a entidade fraca **`RACK`** (discriminador $\dashuline{\text{num\_rack}}$, atributo `altura_u`).

**Pede-se:**
1. Aplique os **Passos 1 e 2** para derivar os esquemas relacionais formais de `PREDIO`, `SALA_TECNICA` e `RACK`, sublinhando todas as Chaves Primárias e destacando as Chaves Estrangeiras.
2. Quantos atributos compõem a Chave Primária da relação `RACK`? Desenhe o **Diagrama de Esquema Relacional** com os arcos de integridade referencial ($FK \longrightarrow PK$) entre as três relações.

### Exercício 3 — Passo 3: Decisão Técnica em Relacionamentos $1:1$
Analise três relacionamentos binários $1:1$ distintos em uma empresa de logística de redes:
* **Caso 1:** `TECNICO_CAMPO` $(0, 1)$ — `DIRIGE` (atributo `data_entrega`) — $(1, 1)$ `VEICULO_FROTA` (todo veículo da frota está obrigatoriamente sob responsabilidade de um técnico, mas apenas 25% dos técnicos possuem veículo).
* **Caso 2:** `ORDEM_SERVICO` $(1, 1)$ — `GERA` — $(1, 1)$ `LAUDO_ENCERRAMENTO` (toda ordem de serviço possui exatamente um laudo obrigatório criado simultaneamente, e vice-versa).
* **Caso 3:** `FUNCIONARIO` $(0, 1)$ — `OCUPA` (atributo `andar`) — $(0, 1)$ `VAGA_GARAGEM_VIP` (apenas 2% dos funcionários possuem vaga VIP, e algumas vagas VIP estão temporariamente desocupadas).

**Pede-se:**
Para cada um dos três casos, indique qual abordagem do **Passo 3** (**Abordagem A — FK**, **Abordagem B — Fusão** ou **Abordagem C — Relação de Referência Cruzada**) deve ser utilizada, escreva os esquemas relacionais resultantes e explique como sua escolha evita valores `NULL`.

### Exercício 4 — Passo 4: Relacionamento $1:N$ Regular vs. Recursivo
Considere o DER de uma central de atendimento técnico onde:
* Uma **`EQUIPE_MANUTENCAO`** ($\underline{\text{cod\_equipe}}$, `nome_equipe`, `turno`) agrupa vários **`AGENTE_SUPORTE`** ($\underline{\text{matricula}}$, `nome_agente`, `nivel_certificacao`) por meio do relacionamento **`LOTADO_EM`** (com atributo `data_lotacao`), sendo que cada agente pertence obrigatoriamente a uma única equipe $(1,1)$ e uma equipe possui vários agentes $(1,N)$.
* Além disso, existe um auto-relacionamento **`COORDENA`** sobre **`AGENTE_SUPORTE`**, no qual um agente sênior coordena vários agentes juniores $(0,N)$, e cada agente possui no máximo um coordenador imediato $(0,1)$.

**Pede-se:**
1. Aplique os **Passos 1 e 4** para gerar o esquema relacional completo. Quantas relações são criadas ao todo?
2. Explique por que propagar a chave `matricula` de `AGENTE_SUPORTE` para dentro de `EQUIPE_MANUTENCAO` violaria a **Primeira Forma Normal (1FN)**.
3. Preencha uma **instância tabular** de `AGENTE_SUPORTE` com 3 tuplas (1 coordenador sênior e 2 agentes coordenados por ele).

### Exercício 5 — Desafio Integrador (Passos 1 a 4 Completos)
A partir do seguinte enunciado de requisitos de um **Sistema de Monitoramento de Enlaces de Rádio Micro-ondas**, construa a solução completa:
* Cada **TORRE** possui `id_torre` (PK), `nome_torre` e `coordenada_geografica` (composta por `latitude`, `longitude` e `altitude_m`).
* Cada torre possui uma **LICENCA_ANATEL** exclusiva ($\underline{\text{num\_licenca}}$, `data_vencimento`), sendo que toda torre homologada possui no máximo uma licença $(0,1)$, mas toda licença emitida pertence obrigatoriamente a uma única torre $(1,1)$ através do vínculo **HOMOLOGA** (com atributo `orgao_emissor`).
* Uma torre abriga várias **ANTENA_PARABOLICA** $(0,N)$, e cada antena está instalada obrigatoriamente em uma única torre $(1,1)$ através do relacionamento **INSTALADA_EM** (com atributo `azimute_graus`). As antenas não possuem número de série global único; elas são identificadas apenas por um `num_sequencial_antena` ($1, 2, 3\dots$) dentro de sua respectiva torre, possuindo ainda `diametro_m` e `frequencia_ghz`.

**Pede-se:**
1. Desenhe o **DER Conceitual** indicando cardinalidades $(min, max)$ e tipos de atributos.
2. Aplique sistematicamente os **Passos 1, 2, 3 e 4** para derivar o **Diagrama de Esquema Lógico Relacional** com arcos referenciais dirigidos ($FK \longrightarrow PK$).
3. Elabore a **Matriz de Rastreabilidade** especificando, para cada relação gerada, sua $\underline{PK}$, suas $FK\text{s}$, suas `AK`s e se as $FK\text{s}$ aceitam ou proíbem `NULL`.
