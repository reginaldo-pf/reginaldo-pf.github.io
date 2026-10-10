# Instituto Federal de Educação, Ciência e Tecnologia do Ceará -- Campus Tauá
## Curso Superior de Tecnologia em Telemática
### Disciplina: Banco de Dados | Semestre Letivo 2026.2
**Docente:** Prof. Me. Reginaldo Pereira Fernandes  
**Discente:** __________________________________________________________________  
**Matrícula:** __________________________ **Data de Aplicação:** 10/10/2026 (Sábado Letivo)  
**Data Limite de Entrega:** 12/10/2026 (Segunda-feira)  
**Forma de Entrega:** Por escrito (Resolução manuscrita no caderno impresso ou folhas anexas)  
**Instrumento Avaliativo:** Lista de Exercícios 01 (Período N1 -- Peso: 20% da Nota N1)  
**Nota Máxima:** 10,0 pontos | **Nota Obtida:** _________ / 10,0 pontos  

---

## 📌 Orientações Gerais e Diretrizes de Submissão

1. **Objetivo:** Esta avaliação assíncrona tem por objetivo consolidar as competências teóricas, conceituais e arquiteturais abordadas nas Aulas 01, 02 e 03 da disciplina:
   - Fundamentos de Sistemas Gerenciadores de Banco de Dados (SGBD) versus Arquivos Planos;
   - Arquitetura ANSI/SPARC de Três Níveis e Independência de Dados (Lógica e Física);
   - Catálogo do Sistema (Dicionário de Metadados), Otimizador CBO e Motor de Segurança;
   - Ciclo de Vida do Projeto de Banco de Dados (4 Fases Canônicas);
   - Ontologia e Modelagem Conceitual de Entidades e Atributos no Modelo Entidade-Relacionamento (MER);
   - Elaboração gráfica rigorosa de Diagramas Entidade-Relacionamento (DER) segundo a **Notação Canônica de Peter Chen (1976)**.
2. **Abordagem Teórico-Conceitual (Sem Código SQL):** Como as aulas práticas de sintaxe e dialetos SQL serão introduzidas exclusivamente no período N2 da disciplina, **esta avaliação não exige a escrita de comandos ou scripts SQL**. As respostas fundamentam-se na semântica, integridade e modelagem estrutural de dados para infraestruturas de telecomunicações.
3. **Padrão Gráfico e Impressão:** 
   - A avaliação oficial foi diagramada em LaTeX e está compilada no arquivo [`lista_01.pdf`](file:///home/reginaldo-fernandes/Aulas/Cursos/Tecnologia%20em%20Telem%C3%A1tica/Disciplinas/Banco%20de%20Dados/Avaliacoes/lista_01.pdf) (fonte em [`lista_01.tex`](file:///home/reginaldo-fernandes/Aulas/Cursos/Tecnologia%20em%20Telem%C3%A1tica/Disciplinas/Banco%20de%20Dados/Avaliacoes/lista_01.tex)).
   - O discente deve imprimir o documento ou utilizar folhas padrão para responder às 8 questões à mão.
4. **Convenções Gráficas Formais de Peter Chen (1976):**
   - **Retângulo:** Conjunto de Entidades (*Entity Set*);
   - **Elipse Simples:** Atributo atômico monovalorado;
   - **Elipse com Nome Sublinhado:** Atributo identificador (chave primária conceitual);
   - **Elipse Ramificada:** Atributo composto (conectado às suas folhas atômicas);
   - **Elipse Dupla Concêntrica:** Atributo multivalorado;
   - **Elipse com Borda Tracejada:** Atributo derivado (calculado via regra/fórmula);
   - **Linhas Sólidas:** Arestas de ligação estrutural desenhadas com régua.
5. **Forma e Data de Entrega:** A resolução deve ser entregue obrigatoriamente **por escrito (manuscrita)** ao professor até o dia **12 de Outubro de 2026** (Segunda-feira), com respostas à caneta azul ou preta e diagramas desenhados à mão com máxima legibilidade.

---

## 📝 CADERNO DE QUESTÕES (8 QUESTÕES -- TOTAL: 10,0 PONTOS)

---

### PARTE I: Fundamentos de SGBD & Arquitetura ANSI/SPARC (3,0 Pontos)

#### Questão 1 (Valor: 1,0 ponto) -- Fundamentos de SGBD vs. Sistemas de Arquivos Planos
Em centros de operações de rede (NOC) e provedores de internet (ISPs), sistemas de monitoramento lidam com fluxos contínuos de telemetria, topologia e inventário. Compare tecnicamente a abordagem legada de persistir tais dados em arquivos gerenciados diretamente pelo sistema operacional (como arquivos `.csv` e `.json`) versus o gerenciamento por um Sistema Gerenciador de Banco de Dados (SGBD).

Sua resposta deve contrastar analiticamente os seguintes quatro pilares fundamentais:
- **a) Redundância e Inconsistência:** Como a proliferação de arquivos desincronizados propaga anomalias de atualização em comparação ao esquema centralizado de um SGBD?
- **b) Controle de Concorrência:** Explique como o controle de bloqueios (*locks*) e isolamento do SGBD evita condições de corrida (*race conditions*) e perdas de atualização (*lost updates*) quando múltiplos operadores tentam alterar ativos simultaneamente.
- **c) Propriedades ACID:** Defina formalmente Atomicidade, Consistência, Isolamento e Durabilidade, explicando por que um sistema de arquivos comum não consegue garanti-las de forma nativa.
- **d) Recuperação de Falhas:** Como o mecanismo de *Write-Ahead Logging* (WAL) e *checkpoints* de um SGBD restaura a base a um estado íntegro após um travamento do servidor do NOC?

---

#### Questão 2 (Valor: 1,0 ponto) -- Níveis de Abstração ANSI/SPARC e Independência de Dados
A arquitetura ANSI/SPARC de 3 níveis propõe uma separação estrita entre a interface do usuário e o armazenamento físico em disco.

- **a)** Explique a função e o escopo de cada um dos três níveis: **Nível Externo (Visões)**, **Nível Conceitual (Global)** e **Nível Interno (Físico)**.
- **b)** Diferencie conceitualmente **Independência Física de Dados** de **Independência Lógica de Dados**.
- **c)** Ilustre a aplicação desses conceitos com dois cenários reais do contexto de Telemática:
  - *(i)* A equipe de infraestrutura migra o armazenamento de HDDs mecânicos para um cluster SAN NVMe com particionamento de índices B-Tree (qual independência atua? Os sistemas de monitoramento precisam ser reprogramados?);
  - *(ii)* O NOC adiciona uma nova entidade `CIRCUITO_REDUNDANTE` no esquema conceitual sem interromper as aplicações legadas dos analistas de faturamento (qual independência atua?).

---

#### Questão 3 (Valor: 1,0 ponto) -- [DIAGRAMA TIKZ] Arquitetura ANSI/SPARC de Três Níveis
Construa o diagrama esquemático completo da **Arquitetura ANSI/SPARC de Três Níveis** adaptado ao ecossistema de Telemática do IFCE Campus Tauá.

O diagrama deve conter obrigatoriamente:
1. **Nível Externo:** Ao menos duas visões de usuários no domínio de redes:
   - *Visão 1 (Operador do NOC):* Alarmes críticos, status de portas e enlaces;
   - *Visão 2 (Gestor de TI):* Custos operacionais, contratos de SLA e inventário patrimonial.
2. **Nível Conceitual:** O Esquema Conceitual Global unificado mediando as regras organizacionais.
3. **Nível Interno:** O Esquema Interno representando a organização de páginas em disco, arquivos estruturados e índices de aceleração.
4. **Mapeamentos:** Setas bidirecionais indicando o *Mapeamento Externo/Conceitual* (garante Independência Lógica) e o *Mapeamento Conceitual/Interno* (garante Independência Física).
5. **Catálogo do Sistema (Dicionário de Metadados):** Repositório central conectado aos três níveis, destacando o papel do **Otimizador de Consultas (CBO)** e do **Motor de Segurança e Autorização**.

```latex
% Exemplo de Estrutura TikZ para a Questão 3:
\begin{tikzpicture}[node distance=1.8cm, font=\small]
  % Camada Externa
  \node[draw, rounded corners, fill=blue!10] (v1) {Visão 1: NOC (Alarmes)};
  \node[draw, rounded corners, fill=blue!10, right=1.5cm of v1] (v2) {Visão 2: Gestor TI (SLA)};
  % Camada Conceitual
  \node[draw, thick, fill=green!15, below=2cm of $(v1)!0.5!(v2)$, minimum width=7cm] (conc) {Esquema Conceitual Global};
  % Camada Interna
  \node[draw, fill=gray!20, below=2cm of conc, minimum width=7cm] (intern) {Esquema Interno (Storage \& B-Tree)};
  % Catálogo
  \node[draw, fill=yellow!20, right=2cm of conc] (cat) {Catálogo do Sistema (Metadados)};
  % Conectores e Mapeamentos
  \draw[<->, thick] (v1) -- (conc);
  \draw[<->, thick] (v2) -- (conc);
  \draw[<->, thick] (conc) -- (intern);
  \draw[dashed, <->] (cat) -- (conc);
\end{tikzpicture}
```

---

### PARTE II: Ciclo de Vida do Projeto & Ontologia de Atributos (2,5 Pontos)

#### Questão 4 (Valor: 1,0 ponto) -- Fases do Projeto de BD e Independência Tecnológica
O desenvolvimento de um banco de dados corporativo segue quatro etapas metodológicas bem delimitadas:
- **a)** Descreva o objetivo principal, a entrada e o artefato de saída de cada uma das quatro fases:
  1. *Análise de Requisitos*;
  2. *Projeto Conceitual*;
  3. *Projeto Lógico*;
  4. *Projeto Físico*.
- **b)** Justifique formalmente por que o Modelo Entidade-Relacionamento (MER) elaborado no Projeto Conceitual deve ser estritamente independente de software gerenciador de banco de dados (SGBD) e de comandos da linguagem SQL. Quais os riscos de se antecipar detalhes físicos ou sintáticos durante a fase conceitual?

---

#### Questão 5 (Valor: 1,5 ponto) -- Ontologia do Modelo Conceitual e Taxonomia Canônica de Atributos
- **a)** No âmbito da modelagem semântica de dados, defina com precisão epistemológica a diferença entre:
  - *(i)* **Entidade** (*Entity*);
  - *(ii)* **Conjunto de Entidades** (*Entity Set*);
  - *(iii)* **Instância de Entidade** (*Entity Instance*).
  Exemplifique cada conceito com elementos reais de infraestrutura de telecomunicações do IFCE Campus Tauá.
- **b)** Um analista de redes modelou a entidade `ROTEADOR_BORDA_BGP`. Classifique rigorosamente cada um dos atributos abaixo na taxonomia canônica de atributos (simples/composto, monovalorado/multivalorado, armazenado/derivado, chave identificadora, ou atributo com nulidade), justificando sua classificação:
  1. `tag_patrimonial_ifce`: Código alfanumérico gravado a laser no chassi do equipamento;
  2. `coordenadas_rack`: Informação estruturada composta por Bloco, Sala do Datacenter, Número do Rack e Unidade U de fixação;
  3. `prefixos_ipv6_bgp`: Lista contendo múltiplos blocos de endereçamento IPv6 roteados simultaneamente pelo equipamento;
  4. `horas_ininterruptas_uptime`: Quantidade de horas em operação contínua, computada dinamicamente pela fórmula $(t_{\text{atual}} - t_{\text{boot}})$;
  5. `motivo_ultima_falha`: Texto descritivo preenchido quando ocorre pane de hardware, permanecendo indefinido/nulo enquanto o ativo operar sem falhas.

---

### PARTE III: Produção de Diagramas Conceituais (DER Peter Chen) em LaTeX/TikZ (4,5 Pontos)

#### Questão 6 (Valor: 1,5 ponto) -- [DIAGRAMA DER TIKZ] Entidade SERVIDOR_VIRTUALIZADO
Construa o Diagrama Entidade-Relacionamento (DER) segundo a notação de Peter Chen (1976) para o conjunto de entidades `SERVIDOR_VIRTUALIZADO` do Data Center do IFCE Campus Tauá.

O diagrama deve conter rigorosamente:
- **Entidade Central:** `SERVIDOR_VIRTUALIZADO` (representada por retângulo);
- **Atributo Identificador Simples:** `uuid_maquina` (elipse sólida com texto sublinhado);
- **Atributos Simples Monovalorados:** `nome_virtual` e `memoria_ram_gb` (elipses sólidas simples);
- **Atributo Composto:** `alocacao_cluster` (elipse simples ramificada em três atributos folhas: `nome_datacenter`, `host_fisico_id` e `storage_pool`);
- **Atributo Multivalorado:** `enderecos_ip_interfaces` (elipse dupla concêntrica);
- **Atributo Derivado:** `custo_estimado_mensal` (elipse com contorno tracejado), cujo valor é obtido dinamicamente pela regra:
  $$\text{custo} = (\text{memoria\_ram\_gb} \times 15.00) + (\text{storage\_pool\_alocado\_gb} \times 0.50)$$

```latex
% Exemplo de Estrutura TikZ para a Questão 6:
\begin{tikzpicture}[
    entidade/.style={rectangle, draw=black, fill=green!15, thick, minimum width=3.2cm, minimum height=0.9cm, font=\bfseries},
    atributo/.style={ellipse, draw=black, fill=white, minimum width=2.2cm, minimum height=0.7cm, font=\scriptsize},
    identificador/.style={ellipse, draw=black, fill=blue!12, thick, minimum width=2.2cm, minimum height=0.7cm, font=\scriptsize\bfseries},
    multivalorado/.style={ellipse, draw=black, double, double distance=1.2pt, fill=pink!15, minimum width=2.4cm, minimum height=0.7cm, font=\scriptsize},
    derivado/.style={ellipse, draw=black, dashed, thick, fill=purple!10, minimum width=2.4cm, minimum height=0.7cm, font=\scriptsize}
]
  \node[entidade] (serv) {SERVIDOR\_VIRTUALIZADO};
  \node[identificador, above left=1.2cm and 1.5cm of serv] (uuid) {\underline{uuid\_maquina}};
  \node[atributo, above=1.2cm of serv] (nome) {nome\_virtual};
  \node[atributo, above right=1.2cm and 1.5cm of serv] (ram) {memoria\_ram\_gb};
  \node[multivalorado, below left=1.2cm and 1.5cm of serv] (ip) {enderecos\_ip\_interfaces};
  \node[derivado, below right=1.2cm and 1.5cm of serv] (custo) {custo\_estimado\_mensal};
  \node[atributo, below=1.4cm of serv] (cluster) {alocacao\_cluster};
  
  \node[atributo, below left=0.8cm and 0.5cm of cluster] (dc) {nome\_datacenter};
  \node[atributo, below=0.8cm of cluster] (host) {host\_fisico\_id};
  \node[atributo, below right=0.8cm and 0.5cm of cluster] (spool) {storage\_pool};

  \draw (serv) -- (uuid); \draw (serv) -- (nome); \draw (serv) -- (ram);
  \draw (serv) -- (ip); \draw (serv) -- (custo); \draw (serv) -- (cluster);
  \draw (cluster) -- (dc); \draw (cluster) -- (host); \draw (cluster) -- (spool);
\end{tikzpicture}
```

---

#### Questão 7 (Valor: 2,0 pontos) -- [DIAGRAMA DER TIKZ] Minimundo do Backbone Óptico Regional do IFCE
Considere o seguinte minimundo da infraestrutura de telecomunicações do IFCE no sertão dos Inhamuns:
> *"O IFCE opera uma rede de transmissão com Pontos de Presença (POPs) distribuídos geograficamente. Cada POP possui um código identificador único (`id_pop`), a cidade onde está situado, um endereço completo desdobrado em logradouro, bairro, número predial e CEP, uma lista com múltiplos telefones de contato de plantão técnico, e o índice de disponibilidade anual calculada percentualmente a partir dos minutos de queda registrados ao longo do ano.*  
> *Os POPs são interligados por Enlaces Ópticos metropolitanos. Cada Enlace Óptico possui um código de enlace identificador exclusivo (`codigo_enlace`), sua extensão em quilômetros (`distancia_km`), a atenuação nominal da fibra (`atenuacao_db_km`), o tipo de fibra óptica utilizada (`tipo_fibra`), e os comprimentos de onda operantes multiplexados no canal óptico (como 1310 nm, 1490 nm e 1550 nm).*  
> *Em cada POP existem Equipamentos de Transmissão (tais como multiplexadores DWDM e switches core), identificados pelo patrimônio do IFCE (`patrimonio_id`), modelo do equipamento, data de instalação em campo, e a sua localização física detalhada no rack composta pelo nome da sala do NOC, número do rack e posição da unidade U de fixação."*

Construa o diagrama conceituado em TikZ (ou desenhado em alta resolução) modelando os **três conjuntos de entidades** (`PONTO_DE_PRESENCA`, `ENLACE_OPTICO` e `EQUIPAMENTO_TRANSMISSAO`) com seus respectivos atributos canônicos (chaves primárias sublinhadas, atributos simples, compostos ramificados, multivalorados com linha dupla e derivados tracejados).

---

#### Questão 8 (Valor: 1,0 ponto) -- [DIAGRAMA DER & ANÁLISE] Engenharia Reversa de Planilha Operacional & Comparação de Notações
Um técnico do provedor de acesso à internet registrava os roteadores dos clientes corporativos em uma planilha com o seguinte leiaute tabular:
```text
[ ID_Equip | Fabricante | Modelo | Localizacao_Fisica | Servidores_DNS | Data_Compra | Anos_Operacao ]
```
Onde:
- `Localizacao_Fisica` armazena texto como `"Bloco Administrativo - Sala de Servidores 02"`;
- `Servidores_DNS` armazena múltiplos IPs separados por vírgula como `"8.8.8.8, 1.1.1.1, 208.67.222.222"`;
- `Anos_Operacao` é computado dinamicamente a partir de `Data_Compra`.

**Pede-se:**
- **a) Análise Crítica da Planilha:** Explique por que o armazenamento dessas informações no modelo em planilha viola a atomicidade de dados e as boas práticas de gerência, e como o Modelo Conceitual resolve essa inconsistência.
- **b) Construção do DER de Peter Chen:** Modele o conjunto de entidades `ROTEADOR_CLIENTE` no DER de Peter Chen em TikZ, decompondo `Localizacao_Fisica` em atributo composto, representando `Servidores_DNS` como atributo multivalorado e `Anos_Operacao` como atributo derivado.
- **c) Análise Comparativa: Notação de Peter Chen vs. Notação Pé de Galinha (*Crow's Foot*):**
  Compare as duas notações, destacando por que a Notação de Chen é mais expressiva para a modelagem conceitual pura (especialmente no tratamento de atributos compostos e multivalorados), enquanto a Notação Pé de Galinha de James Martin é mais orientada à implementação de tabelas físicas no modelo relacional.

---

## 📊 BAREMA DE CORREÇÃO OFICIAL (10,0 PONTOS)

| Questão | Categoria Temática | Habilidade / Critério Avaliado | Valor |
| :---: | :--- | :--- | :---: |
| **Q1** | Fundamentos de SGBD | Contraste técnico SGBD vs Arquivos (Redundância, Concorrência, ACID e WAL) | **1,0 pt** |
| **Q2** | Arquitetura ANSI/SPARC | Abstração em 3 Níveis e Independência Física vs Lógica em Redes | **1,0 pt** |
| **Q3** | Diagrama Arquitetural | Diagrama ANSI/SPARC em TikZ com NOC/TI, Mapeamentos e Catálogo do Sistema | **1,0 pt** |
| **Q4** | Ciclo de Vida de BD | As 4 Fases Canônicas e Justificativa da Independência Tecnológica do MER | **1,0 pt** |
| **Q5** | Ontologia de Atributos | Definição ontológica de Entidades e Taxonomia em `ROTEADOR_BORDA_BGP` | **1,5 pt** |
| **Q6** | Diagrama DER Chen | DER TikZ de `SERVIDOR_VIRTUALIZADO` (chaves, composto, multivalorado, derivado) | **1,5 pt** |
| **Q7** | Diagrama DER Chen | DER TikZ do Backbone Óptico IFCE (POP, Enlace e Equipamento com atributos) | **2,0 pts** |
| **Q8** | Diagrama DER & Análise | Normalização de planilha, DER TikZ de `ROTEADOR_CLIENTE` e Chen vs Martin | **1,0 pt** |
| **Total** | **Consolidação N1** | **Nota Máxima da Lista de Exercícios 01** | **10,0 pts** |

---

### ⚠️ Critérios de Rigor e Penalidades
- **Simbologia Geométrica de Chen Incorreta:** Desconto de 0,1 a 0,3 pt por símbolo invertido (ex: atributo derivado desenhado com borda contínua ou multivalorado com elipse simples).
- **Omissão de Identificador Chave:** Desconto de 0,2 pt por entidade cujo atributo identificador não esteja devidamente sublinhado.
- **Ausência de Justificativa Teórica:** Respostas que apenas listem itens sem argumentação conceitual sólida terão desconto proporcional de 50% na questão.
- **Legibilidade Gráfica:** Diagramas gerados em TikZ recebem pontuação integral pela clareza vetorial; diagramas desenhados manualmente devem possuir alta nitidez sob pena de anulação caso ilegíveis.
