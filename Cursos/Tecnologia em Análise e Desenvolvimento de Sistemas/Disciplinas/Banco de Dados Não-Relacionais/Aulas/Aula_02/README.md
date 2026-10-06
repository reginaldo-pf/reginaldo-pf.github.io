# Aula 02 -- Banco de Dados Não-Relacionais

**Disciplina:** Banco de Dados Não-Relacionais (ADS16)  
**Curso:** Tecnologia em Análise e Desenvolvimento de Sistemas (ADS) -- IFCE Campus Tauá  
**Carga Horária do Encontro:** 2 horas (120 minutos)  
**Data Prevista:** 06/10/2026 (Terça-feira)  
**Professor:** Prof. Me. Reginaldo Pereira Fernandes  

---

## 📚 Bibliografia & Referências Integradas

### Bibliografia Básica:
1. **BREWER, Eric.** *CAP twelve years later: How the 'rules' have changed.* Computer, IEEE, v. 45, n. 2, p. 23-29, 2012. DOI: 10.1109/MC.2012.37.
2. **ABADI, Daniel J.** *Consistency tradeoffs in modern distributed database system design: CAP is only part of the story.* Computer, IEEE, v. 45, n. 2, p. 37-42, 2012. DOI: 10.1109/MC.2012.33. (Definição formal do Teorema PACELC).
3. **VOGELS, Werner.** *Eventually Consistent.* Communications of the ACM, v. 52, n. 1, p. 40-44, 2008. DOI: 10.1145/1435417.1435432.
4. **SADALAGE, Pramod J.; FOWLER, Martin.** *NoSQL Essencial: Um Guia Conciso para o Mundo Emergente da Persistência Poliglota.* São Paulo: Novatec Editora, 2014. ISBN 978-8575223383.
5. **GRAY, Jim.** *The Transaction Concept: Virtues and Limitations.* In: Proceedings of the 7th International Conference on Very Large Data Bases (VLDB), p. 144-154, 1981.

### Bibliografia Complementar:
1. **GILBERT, Seth; LYNCH, Nancy.** *Brewer's conjecture and the feasibility of consistent, available, partition-tolerant web services.* ACM SIGACT News, v. 33, n. 2, p. 51-59, 2002.
2. **PRITCHETT, Dan.** *BASE: An Acid Alternative.* ACM Queue, v. 6, n. 3, p. 48-55, 2008.
3. **KLEPPMANN, Martin.** *Designing Data-Intensive Applications: The Big Ideas Behind Reliable, Scalable, and Maintainable Systems.* Sebastopol, CA: O'Reilly Media, 2017. 616 p.

---

## 🎯 1. Objetivos de Aprendizagem

### Objetivo Geral:
Compreender os fundamentos físico-arquiteturais que governam os bancos de dados modernos sob distribuição horizontal, dominando a formulação formal e as implicações práticas do Teorema CAP e do Teorema PACELC, contrastando as propriedades estritas de ACID com as propriedades otimistas de BASE e capacitando o estudante a configurar níveis de garantia de escrita (*Write Concern*) e isolamento de leitura (*Read Concern*) no MongoDB e em clusters simulados.

### Objetivos Específicos:
1. Compreender as 8 Falácias da Computação Distribuída (*Deutsch & Gosling, 1994*) e por que falhas parciais de rede são uma fatalidade física inegociável em clusters.
2. Desmistificar o Triângulo CAP tradicional, compreendendo que a Tolerância a Partições de Rede ($P$) não é uma opção configurável, mas uma imposição do meio físico (*Brewer, 2012*).
3. Calcular analiticamente a regra de Quórum da maioria absoluta em clusters de $N$ nós ($Q = \lfloor N/2 \rfloor + 1$) e justificar a necessidade de nós ímpares para prevenir cenários de *Split-Brain*.
4. Analisar o Teorema PACELC (*Abadi, 2012*) como a extensão necessária do CAP para os 99,99% do tempo em que o cluster opera em estado de normalidade (*Else*), avaliando o trade-off entre Latência ($L$) e Consistência ($C$).
5. Delinear as diferenças conceituais e operacionais entre o paradigma pessimista ACID (*Atomicity, Consistency, Isolation, Durability*) e o paradigma otimista BASE (*Basically Available, Soft state, Eventual consistency*).
6. Analisar o mecanismo de convergência da Consistência Eventual, contrastando o algoritmo *Last-Write-Wins* (LWW) com Relógios Lógicos / Vetores de Versão (*Vector Clocks*).
7. Mapear os 4 modelos NoSQL (Chave-Valor, Documentos, Família de Colunas, Grafos) e Bancos Vetoriais dentro da matriz arquitetural CAP/PACELC.
8. Executar simulações computacionais interativas com injeção de rompimento de link de rede e mensuração de latência via script Python (`codigo/demonstracao_aula02.py`).
9. Configurar e testar na prática parâmetros de *Write Concern* (`w: 1` vs `w: "majority"`, `j: true`) e *Read Concern* (`local`, `majority`, `linearizable`) no MongoDB.

---

## ⏱️ 2. Cronograma da Aula (120 Minutos)

| Bloco | Duração | Descrição das Atividades Didáticas |
| :---: | :---: | :--- |
| **Bloco 1** | 00 -- 25 min | **O Dilema dos Sistemas Distribuídos:** Da máquina única aos clusters (revisão da Aula 01); as 8 falácias da computação distribuída; o drama da Black Friday e o risco de gasto duplo (*Double-Spending*); definição formal de linearizabilidade. |
| **Bloco 2** | 25 -- 55 min | **O Teorema CAP (Brewer, 2000/2012):** Definição rigorosa de $C$, $A$ e $P$; a prova de Gilbert \& Lynch (2002); o mito do triângulo desfeito; quórum de maioria ($Q = \lfloor N/2 \rfloor + 1$) e topologia de 3 nós; sistemas CP vs AP na prática. |
| **Bloco 3** | 55 -- 80 min | **O Teorema PACELC (Abadi, 2012):** Por que o CAP é incompleto para 99,99% do tempo de operação normal; a árvore de decisão PACELC; trade-off de Latência ($L$) vs Consistência ($C$); exemplo pareado analítico e computacional em Python. |
| **Bloco 4** | 80 -- 100 min | **Duelo de Paradigmas: ACID vs BASE:** Travas pessimistas e 2PC (*Jim Gray, 1981*) vs resiliência otimista (*Werner Vogels, 2008*); consistência eventual na prática; Last-Write-Wins (LWW) e Vector Clocks; matriz decisória de mercado (PIX vs TikTok vs Carrinho Amazon). |
| **Bloco 5** | 100 -- 120 min | **Laboratório Hands-On Interativo:** Execução do simulador de cluster `demonstracao_aula02.py` (injeção de falha de rede ao vivo e cura); comandos reais de Write Concern e Read Concern no MongoDB; orientações para o Sábado Letivo (Oficina Docker 10/10) e Lista 1. |

---

## 🖼️ 3. Figuras e Elementos Visuais da Aula

A apresentação é enriquecida com 5 diagramas vetoriais gerados em TikZ em alta resolução:

1. **[O Teorema CAP: Mito vs Realidade](file:///home/reginaldo-fernandes/Aulas/Cursos/Tecnologia%20em%20An%C3%A1lise%20e%20Desenvolvimento%20de%20Sistemas/Disciplinas/Banco%20de%20Dados%20N%C3%A3o-Relacionais/Aulas/Aula_02/materiais/figuras/fig_cap_realidade.png):** Desmistifica o triângulo popular demonstrando a bifurcação real durante uma partição de rede inevitável ($P \implies C \lor A$).
2. **[A Árvore Decisória do Teorema PACELC](file:///home/reginaldo-fernandes/Aulas/Cursos/Tecnologia%20em%20An%C3%A1lise%20e%20Desenvolvimento%20de%20Sistemas/Disciplinas/Banco%20de%20Dados%20N%C3%A3o-Relacionais/Aulas/Aula_02/materiais/figuras/fig_pacelc_arvore.png):** Fluxo decisório completo de Daniel Abadi, classificando bancos de dados tanto sob falha ($P$) quanto sob operação normal ($E$).
3. **[Anatomia do Quórum e Partição de Rede](file:///home/reginaldo-fernandes/Aulas/Cursos/Tecnologia%20em%20An%C3%A1lise%20e%20Desenvolvimento%20de%20Sistemas/Disciplinas/Banco%20de%20Dados%20N%C3%A3o-Relacionais/Aulas/Aula_02/materiais/figuras/fig_cluster_split_brain.png):** Visualização de um cluster com 3 nós, o corte de comunicação isolando o Nó C e o funcionamento do quórum de maioria.
4. **[Duelo de Paradigmas: ACID vs BASE](file:///home/reginaldo-fernandes/Aulas/Cursos/Tecnologia%20em%20An%C3%A1lise%20e%20Desenvolvimento%20de%20Sistemas/Disciplinas/Banco%20de%20Dados%20N%C3%A3o-Relacionais/Aulas/Aula_02/materiais/figuras/fig_acid_vs_base.png):** Cartão de batalha lado a lado contrastando a filosofia pessimista de travas (RDBMS) com a filosofia otimista de consistência eventual (NoSQL).
5. **[Taxonomia NoSQL na Matriz PACELC / CAP](file:///home/reginaldo-fernandes/Aulas/Cursos/Tecnologia%20em%20An%C3%A1lise%20e%20Desenvolvimento%20de%20Sistemas/Disciplinas/Banco%20de%20Dados%20N%C3%A3o-Relacionais/Aulas/Aula_02/materiais/figuras/fig_taxonomia_4_modelos.png):** Mapeamento dos 4 modelos NoSQL (Chave-Valor, Documentos, Família de Colunas, Grafos) e Bancos Vetoriais frente aos trade-offs arquiteturais.

---

## 📖 4. Roteiro Detalhado Slide-a-Slide

| Slide | Título do Slide | Tópicos & Pontos-Chave | Nota do Professor (Didática) | Elemento Visual |
| :---: | :--- | :--- | :--- | :--- |
| **01** | Capa Oficial | Disciplina ADS16, Título da Aula 02, Data e Docente. | Acolher os estudantes e conectar com o encerramento prático da Aula 01. | Identidade visual IFCE |
| **02** | Agenda do Encontro | 5 seções estruturadas: Contexto, CAP, PACELC, ACID vs BASE, Prática. | Apresentar o roteiro cronológico para contextualizar a aula. | Sumário dinâmico Beamer |
| **03** | De Um Servidor a Múltiplos Nós | Centralização única vs Nós distribuídos; o surgimento de falhas parciais. | Relembrar que Scale-Out resolve o teto de hardware, mas cria o problema da rede. | Colunas comparativas |
| **04** | As 8 Falácias da Rede | Deutsch & Gosling (1994); Rede confiável, latência zero, largura infinita. | Enfatizar que a física impõe limites e a internet não é perfeita. | Lista com ícones de alerta |
| **05** | Cenário: Black Friday e Saldo | 100k req/s, cabo rompido entre SP e Fortaleza; dilema: travar ou duplicar? | Estimular o debate em sala: Você prefere errar 503 ou perder R$ 500? | Caixa de destaque de negócio |
| **06** | Linearizabilidade (Consistência) | Definição de Herlihy & Wing (1990); Leitura subsequente sempre vê dado novo. | Esclarecer que Consistência no CAP não é a mesma coisa que integridade relacional. | Bloco formal |
| **07** | Origem e Teorema CAP | Eric Brewer (2000), prova de Gilbert & Lynch (2002); Impossibilidade simultânea. | Destacar a importância histórica do teorema para o movimento NoSQL. | Citação bibliográfica |
| **08** | As 3 Propriedades do CAP | C (Linearizabilidade), A (Disponibilidade sem erro), P (Tolerância a Partição). | Definir cada letra com rigor matemático. | Lista em duas colunas |
| **09** | Desmistificando o Triângulo | O erro do "escolha 2 de 3"; Brewer (2012): Partição é lei da física inegociável. | Destacar que "sistemas CA" não existem na internet. | Caixa de alerta metodológica |
| **10** | Figura: O CAP na Realidade | Diagrama vetorial comparando o mito do triângulo com a árvore de decisão real. | Pausar e guiar os alunos através do fluxo: Se há partição, escolha CP ou AP. | `fig_cap_realidade.pdf` |
| **11** | A Regra de Quórum ($N$ Nós) | Quórum $Q = \lfloor N/2 \rfloor + 1$; Por que o número de nós deve ser ímpar ($3, 5, 7$). | Demonstrar na lousa por que 4 nós é pior que 3 nós em caso de partição binária. | Fórmulas matemáticas |
| **12** | Figura: Anatomia do Quórum | Cluster com Nós A, B (Quórum 2/3) e Nó C isolado pela fibra rompida. | Mostrar visualmente como o nó isolado detecta a perda de maioria. | `fig_cluster_split_brain.pdf` |
| **13** | Classificação CAP Real | Bancos CP (MongoDB, HBase, Raft) vs Bancos AP (Cassandra, DynamoDB, CouchDB). | Dar exemplos de bancos consagrados que os estudantes usarão no mercado. | Tabela contrastada |
| **14** | Insuficiência do CAP | Daniel Abadi (2012); Redes passam 99,99% do tempo sem partição de rede. | Provocar: Se a rede está funcionando perfeitamente, o CAP diz o quê? Nada! | Citação de artigo IEEE |
| **15** | A Mnemônica do PACELC | If P $\implies$ A or C; Else $\implies$ L or C; As 4 categorias: PA/EL, PC/EC, PC/EL. | Ensinar a sigla PACELC de forma mnemônica e intuitiva. | Equação arquitetural |
| **16** | Figura: Árvore do PACELC | Diagrama em árvore completo classificando bancos nos ramos P e E. | Mostrar onde MongoDB, Cassandra, DynamoDB e PostgreSQL se encaixam. | `fig_pacelc_arvore.pdf` |
| **17** | Exemplo Analítico: Latência | RTT local (1,5 ms) vs RTT interestadual (45 ms e 58 ms); Cálculo de $T_{\text{EL}}$ e $T_{\text{EC}}$. | Resolver passo a passo na lousa demonstrando o atraso de 33,3x da consistência. | Exemplo numérico analítico |
| **18** | Demonstração Pareada Python | Código Python simulando o cálculo analítico exato do Slide 17. | Demonstrar como a computação valida a teoria analítica de forma imediata. | `lstlisting` Python |
| **19** | Paradigma ACID (RDBMS) | Jim Gray (1981); Atomicidade, Consistência, Isolamento, Durabilidade; Travas e 2PC. | Explicar por que travas pessimistas não escalam para milhões de acessos simultâneos. | Cartão conceitual |
| **20** | Paradigma BASE (NoSQL) | Werner Vogels (2008); Basically Available, Soft State, Eventual Consistency. | Conectar com o case da Amazon: Nunca derrubar o checkout. | Cartão conceitual |
| **21** | Figura: ACID vs BASE | Duelo de paradigmas lado a lado com características fundamentais. | Contrastar a filosofia pessimista com a filosofia otimista. | `fig_acid_vs_base.pdf` |
| **22** | Mecanismos de Consistência | Last-Write-Wins (LWW) e riscos de Clock Drift vs Vetores de Versão (Vector Clocks). | Explicar como réplicas assíncronas detectam quem escreveu primeiro. | Diagrama conceitual |
| **23** | Matriz Decisória de Negócio | Tabela de domínios: PIX (ACID/CP), TikTok (BASE/AP), Carrinho (BASE/AP), SISU (ACID/CP). | Fazer os alunos analisarem e justificarem cada escolha para a carreira técnica. | Tabela comparativa |
| **24** | Os 4 Modelos NoSQL | Chave-Valor, Documentos, Família de Colunas, Grafos e Bancos Vetoriais (RAG). | Explicar que cada modelo possui afinidade com uma escolha PACELC. | Resumo estrutural |
| **25** | Figura: Taxonomia na Matriz | Posicionamento dos 4 modelos NoSQL frente ao CAP e PACELC. | Mostrar a visão holística da disciplina que será aprofundada nas próximas aulas. | `fig_taxonomia_4_modelos.pdf` |
| **26** | MongoDB: Write Concern | Código `db.collection.insertOne` com `w: 1` vs `w: "majority"` e `j: true`. | Mostrar que no código o engenheiro escolhe se quer PA/EL ou PC/EC. | `lstlisting` MongoDB |
| **27** | MongoDB: Read Concern | Níveis de leitura: `local`, `majority` e `linearizable`. | Alertar sobre leituras defasadas (*Stale Reads*) e garantias de quórum. | `lstlisting` MongoDB |
| **28** | Roteiro Laboratório Terminal | Guia de execução de `demonstracao_aula02.py` e simulação de corte de rede. | Orientar os estudantes a abrir o terminal e rodar os testes práticos. | Instruções práticas |
| **29** | Sábado Letivo \& Atividades | Aula 03 (10/10) - Oficina Docker e Compose; Questões 7 a 12 da Lista 1. | Reforçar que sábado letivo não tem conteúdo novo e serve para nivelamento DevOps. | Cronograma e Lista |
| **30** | Encerramento \& Dúvidas | Contatos, e-mail institucional e encerramento. | Abrir espaço para perguntas e feedback dos discentes. | Slide final IFCE |

---

## 🔢 5. Associação Teórico-Computacional (Exemplos Pareados)

Seguindo o padrão metodológico do curso, apresentamos o cálculo analítico formal e sua imediata validação computacional em Python:

### Exemplo Analítico Passo a Passo (Cálculo do RTT e Latência PACELC)
Considere uma aplicação bancária distribuída com réplica primária em **São Paulo**, secundária em **Fortaleza** e terciária em **Tauá**:
- $RTT_1$ (*Round-Trip Time* Local / São Paulo): $1{,}5 \text{ ms}$
- $RTT_2$ (*Round-Trip Time* Regional / Fortaleza): $45{,}0 \text{ ms}$
- $RTT_3$ (*Round-Trip Time* Interior / Tauá): $58{,}0 \text{ ms}$
- $\delta$ (Sobrecarga de processamento e gravação em disco local): $0{,}3 \text{ ms}$

**1. Estratégia PA/EL (Confirmação Imediata Local $W=1$):**
$$T_{\text{EL}} = RTT_1 + \delta = 1{,}5 + 0{,}3 = \mathbf{1{,}8\text{ ms}}$$

**2. Estratégia PC/EC (Confirmação Síncrona com Todas as Réplicas):**
$$T_{\text{EC}} = \max(RTT_1, RTT_2, RTT_3) + \delta_{\text{quorum}} = 58{,}0 + 2{,}0 = \mathbf{60{,}0\text{ ms}}$$

**3. Razão de Trade-off:**
$$\text{Fator de Aceleração} = \frac{T_{\text{EC}}}{T_{\text{EL}}} = \frac{60{,}0}{1{,}8} \approx \mathbf{33{,}3\times}$$
*Conclusão da Engenharia:* Para garantir linearizabilidade em réplicas geodistribuídas sem inconsistência, a aplicação paga uma penalidade de $33{,}3\times$ no tempo de resposta percebido pelo cliente.

### Demonstração Equivalente em Código Python
```python
# Demonstracao computacional pareada do calculo analitico de latencia PACELC
rtt_local = 1.5       # No 1 (rack local)
rtt_fortaleza = 45.0  # No 2 (Fortaleza)
rtt_taua = 58.0       # No 3 (Taua)

# PA/EL: Confirmacao imediata no primario local (W=1)
tempo_el = rtt_local + 0.3

# PC/EC: Confirmacao sincrona aguardando quorum
tempo_ec = max(rtt_local, rtt_fortaleza, rtt_taua) + 2.0

fator = tempo_ec / tempo_el

print(f"Latencia PC/EC (Consistencia Estrita) : {tempo_ec:.1f} ms")
print(f"Latencia PA/EL (Baixa Latencia W=1)   : {tempo_el:.1f} ms")
print(f"Ganho de desempenho no modelo EL     : {fator:.1f}x mais veloz!")
```

---

## 🍃 6. Guia Prático MongoDB: Configurando Write Concern e Read Concern

No MongoDB, o desenvolvedor ajusta o trade-off do PACELC diretamente nos métodos de consulta e escrita:

### 1. Níveis de Confirmação de Escrita (Write Concern)
```javascript
// A) Foco em Velocidade e Latência Ultrabaixa (Modo PA/EL):
// O driver confirma assim que a gravação chega na memória do primário
db.metricas_iot.insertOne(
  { sensor: "ESTACAO-01", umidade: 62.4, leitura: new Date() },
  { writeConcern: { w: 1, wtimeout: 1000 } }
);

// B) Foco em Consistência Estrita e Durabilidade Bancária (Modo PC/EC):
// Aguarda a confirmação da maioria dos nós votantes e escrita física no journal
db.lancamentos_contabeis.insertOne(
  { id_transacao: "PIX-9942", valor: 350.00, status: "confirmado" },
  { writeConcern: { w: "majority", j: true, wtimeout: 5000 } }
);
```

### 2. Níveis de Isolamento de Leitura (Read Concern)
```javascript
// A) Leitura Local (Rápida, sem verificação de consenso):
db.pedidos.find({ status: "aberto" }).readConcern("local");

// B) Leitura de Quórum (Apenas dados confirmados pela maioria do cluster):
// Previne ler dados que poderiam sofrer rollback em caso de queda do líder
db.pedidos.find({ id_pedido: "PED-10" }).readConcern("majority");

// C) Leitura Linearizável (Mais rigorosa, checa o líder em tempo real):
db.saldos.find({ conta: "8842-1" }).readConcern("linearizable");
```

---

## 💻 7. Como Executar as Demonstrações Interativas

### Modo Terminal Interativo (CLI)
```bash
# Acessar a pasta da Aula 02
cd "Aulas/Aula_02"

# Executar o simulador didático com menu completo
python3 codigo/demonstracao_aula02.py

# Ou rodar todos os testes de benchmark automaticamente
python3 codigo/demonstracao_aula02.py --all
```

### Modo Caderno Interativo (Jupyter Notebook)
Abra o arquivo [`codigo/demonstracao_aula02.ipynb`](file:///home/reginaldo-fernandes/Aulas/Cursos/Tecnologia%20em%20An%C3%A1lise%20e%20Desenvolvimento%20de%20Sistemas/Disciplinas/Banco%20de%20Dados%20N%C3%A3o-Relacionais/Aulas/Aula_02/codigo/demonstracao_aula02.ipynb) no VS Code, JupyterLab ou Google Colab para executar as células passo a passo.

---

## 📝 8. Exercícios de Fixação (Lista 1 -- Bloco 2)

1. Por que a afirmação popular *"Basta escolher 2 dentre Consistência, Disponibilidade e Tolerância a Partições no Teorema CAP"* é considerada conceitualmente incorreta na engenharia de sistemas modernos segundo Eric Brewer (2012)?
2. Explique detalhadamente por que um cluster distribuído com $N = 4$ nós votantes é mais vulnerável a paradas operacionais (*downtime*) do que um cluster com $N = 3$ nós sob a ocorrência de uma partição de rede binária estrita.
3. Defina a equação mnemônica do Teorema PACELC de Daniel Abadi (2012). Qual é a limitação central do Teorema CAP que o PACELC visa solucionar?
4. Contrastando os paradigmas ACID e BASE, diferencie o conceito de *Isolamento Pessimista baseado em Travas* do conceito de *Consistência Eventual Otimista*.
5. Considere o algoritmo *Last-Write-Wins* (LWW) utilizado para resolução de conflitos em sistemas AP. Qual é a fragilidade física desse método quando há desvio de relógio (*Clock Drift*) entre os servidores de um cluster? Como os *Relógios Lógicos / Vetores de Versão* contornam essa limitação?
6. No MongoDB, qual é a diferença operacional entre executar uma gravação com `{ writeConcern: { w: 1 } }` e executar a mesma gravação com `{ writeConcern: { w: "majority", j: true } }`? Em qual quadrante do Teorema PACELC cada uma se posiciona?
