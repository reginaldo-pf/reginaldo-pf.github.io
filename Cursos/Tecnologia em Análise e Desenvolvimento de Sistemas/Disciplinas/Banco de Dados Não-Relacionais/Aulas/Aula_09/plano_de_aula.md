# Plano de Aula: 09 - Laboratório de Fixação Intensiva e Revisão Prática Integrada (Redis + MongoDB) — Sábado Letivo

* **Curso:** Tecnologia em Análise e Desenvolvimento de Sistemas (ADS)  
* **Componente Curricular:** Banco de Dados Não-Relacionais (ADS16)  
* **Docente Responsável:** Prof. Me. Reginaldo Fernandes  
* **Semestre Letivo:** 2026.2  
* **Carga Horária:** 2 h/a (120 minutos)  
* **Data da Aula:** 14 de Novembro de 2026 (Sábado Letivo)  
* **Módulo:** Laboratório (N1) — Preparatório para Avaliação Prática 1 (AVP1) e Avaliação Teórica 1 (AVT1)  

---

## 🧭 1. Contextualização Prática e Metodologia da Aula

1. **Contextualização Prática e a Persistência Poliglota Integrada:**  
   Ao longo das Aulas 01 a 08, os estudantes exploraram os fundamentos teóricos de sistemas distribuídos e as duas principais tecnologias do ecossistema NoSQL em N1: o banco chave-valor em memória (**Redis**) e o banco orientado a documentos (**MongoDB**). Na arquitetura de software moderna, essas tecnologias raramente operam de forma isolada; elas cooperam de maneira simbiótica: o Redis assume o papel de acelerador de latência e controle de estados efêmeros (cache com TTL, controle de sessão, carrinhos e filas FIFO), enquanto o MongoDB garante a persistência confiável de documentos flexíveis com consultas analíticas e índices $B\text{-Tree}$. Este sábado letivo atua como uma oficina de consolidação e simulado integrado sem introdução de conteúdo novo, preparando os estudantes para a **AVP1** (avaliação prática em laboratório) e a **AVT1** (avaliação teórica individual).
2. **Método Teórico Clássico e Revisão Conceitual:**  
   Revisão rigorosa dos teoremas basilares: o **Teorema CAP** de Eric Brewer (a impossibilidade de garantir simultaneamente Consistência, Disponibilidade e Tolerância a Partições em redes não-confiáveis) e sua extensão pelo **Teorema PACELC** de Daniel Abadi (avaliando o trade-off de latência versus consistência em operação normal). Contraste detalhado entre as garantias transacionais relacionais **ACID** (*Atomicidade, Consistência, Isolamento, Durabilidade*) e o modelo NoSQL **BASE** (*Basically Available, Soft state, Eventual consistency*).
3. **Abordagem Computacional e Simulado em Laboratório:**  
   Execução do simulado prático integrado contendo 5 desafios progressivos que cobrem os tópicos mais cobrados na AVP1:
   - Implementação do padrão **Cache-Aside (Lazy Loading)** com hidratação automática e TTL no Redis.
   - Invalidação atômica de cache no momento de atualizações com `$inc` no MongoDB, prevenindo leituras de dados obsoletos (*Stale Reads*).
   - Manipulação de carrinhos de compras em Hashes do Redis (`HSET`, `HINCRBY`, `HGETALL`).
   - Formulação e validação da **Regra de Ouro ESR** (*Equality, Sort, Range*) com índices compostos inspecionados via `explain("executionStats")`.
   - Pipeline de agregação analítica de vendas com `$match`, `$unwind` e `$group`.
4. **Tomada de Decisão Visual e Métricas de Latência:**  
   Apresentação do benchmark comparativo de latência poliglota gerado em laboratório, contrastando a resposta em memória RAM do Redis ($\approx 0.08\text{ ms}$, ganho de velocidade $> 200\times$) com o acesso a disco indexado do MongoDB ($\approx 1.15\text{ ms}$) e a varredura desastrosa sem índice (`COLLSCAN`, $\approx 18.4\text{ ms}$).

---

## 🎯 2. Objetivos de Aprendizagem

### Objetivo Geral
Consolidar as competências teóricas e práticas do 1º Período Letivo (N1) da disciplina de Banco de Dados Não-Relacionais, capacitando os estudantes a resolver desafios práticos em laboratório integrando Redis e MongoDB e a justificar escolhas arquiteturais com base nos Teoremas CAP e PACELC.

### Objetivos Específicos
1. **Revisar a Fundamentação Distribuída:** Explicar com precisão os trade-offs do Teorema CAP (diferenciando sistemas CP de sistemas AP) e do Teorema PACELC (PC/EC vs PA/EL), além de contrastar ACID e BASE.
2. **Operar Estruturas de Dados do Redis:** Praticar comandos de Strings (`SET`, `GET`, `INCR`), Hashes (`HSET`, `HINCRBY`), Listas (`LPUSH`, `RPOP`), Sets e Sorted Sets tanto via terminal `redis-cli` quanto via Python (`redis-py`).
3. **Implementar Estratégias de Cache:** Construir o fluxo completo de *Cache Hit*, *Cache Miss* e *Invalidação Imediata* no padrão Cache-Aside, gerenciando a vida útil de chaves através de TTL (`EXPIRE`).
4. **Dominar CRUD Atômico no MongoDB:** Executar atualizações seletivas com operadores atômicos (`$set`, `$inc`, `$push`, `$addToSet`) e realizar buscas em arrays evitando falsos positivos com `$elemMatch`.
5. **Aplicar a Regra ESR e Diagnosticar Planos:** Projetar índices compostos ordenando rigorosamente Igualdade (*Equality*), Ordenação (*Sort*) e Faixa (*Range*), interpretando planos de execução com `explain()` para eliminar `COLLSCAN`.
6. **Construir Pipelines de Agregação:** Desmembrar arrays com `$unwind` e sintetizar métricas de faturamento e volume com `$group` e acumuladores no MongoDB.

---

## ⏱️ 3. Cronograma Recomendado da Aula de Revisão (120 Minutos)

| Bloco | Duração | Descrição das Atividades | Metodologia & Recursos |
| :---: | :---: | :--- | :--- |
| **1. Abertura & Teoria** | 00 – 25 min | **Revisão Conceitual e Teoremas (CAP / PACELC / BASE):** Relembrar os trade-offs de consistência eventual, tolerância a partição, persistência poliglota e limites de escala vertical. | Exposição dialogada com slides Beamer e perguntas socráticas. |
| **2. Prática Redis** | 25 – 45 min | **Revisão Prática do Redis (Estruturas e TTL):** Hashes para carrinhos, listas para filas FIFO assíncronas e estratégias de expiração de dados transientes. | Demonstração guiada no terminal redis-cli e Redis Insight. |
| **3. Prática MongoDB** | 45 – 70 min | **Revisão do MongoDB (CRUD, ESR e explain):** Atualizações atômicas sem concorrência destrutiva, filtros com `$elemMatch` e aplicação da regra ESR para Covered Queries. | Resolução pareada e prática no mongosh e Compass. |
| **4. Simulado N1** | 70 – 105 min | **Execução Assistida do Simulado Integrado AVP1:** Resolução individual ou em duplas dos 5 desafios propostos no script `simulado_n1_desafios.py`. | Laboratório prático autônomo com validação automatizada. |
| **5. Gabarito & Plantão** | 105 – 120 min | **Plantão de Dúvidas e Análise do Gabarito:** Discussão das soluções ideais em `solucao_simulado_n1.py`, erros frequentes e orientações finais para os exames AVP1 e AVT1. | Fechamento docente e alinhamento de expectativas. |

---

## 🖥️ 4. Roteiro Slide a Slide Sugerido

* **Slide 1:** Capa da Aula e Apresentação do Sábado Letivo (Revisão Integrada N1).
* **Slide 2:** Roteiro de Atividades e Matriz de Competências para AVP1 e AVT1.
* **Slide 3:** Objetivos do Sábado Letivo: Consolidação sem introdução de conteúdo novo.
* **Slide 4:** Arquitetura Integrada do Simulado: O fluxo do padrão Cache-Aside (Aplicação $\to$ Redis $\to$ MongoDB).
* **Slide 5:** Revisão do Teorema CAP (Brewer, 2000): Consistência, Disponibilidade e a inevitabilidade da Tolerância a Partições.
* **Slide 6:** O Teorema PACELC (Abadi, 2012): Comportamento sob partição (PC/PA) versus regime normal (EL/EC).
* **Slide 7:** Comparativo ACID (Transações Relacionais) vs BASE (Sistemas Distribuídos e Consistência Eventual).
* **Slide 8:** As 5 Estruturas Nativas do Redis e seus Casos de Uso (Strings, Hashes, Lists, Sets, Sorted Sets).
* **Slide 9:** Estratégias de Expiração com TTL e Modos de Persistência em Disco (RDB vs AOF).
* **Slide 10:** Modelagem BSON no MongoDB: Quando incorporar (*Embedding*) e quando referenciar (*Referencing*).
* **Slide 11:** Operadores de Atualização Atômica (`$set`, `$inc`, `$push`) e o uso seguro de `$elemMatch`.
* **Slide 12:** A Regra de Ouro ESR (*Equality, Sort, Range*): Otimização de índices compostos e diagnósticos com `explain()`.
* **Slide 13:** MongoDB Aggregation Framework: Encadeamento de estágios (`$match`, `$unwind`, `$group`).
* **Slide 14:** Evidência Empírica: Benchmark comparativo de latência entre Redis (0.08 ms), MongoDB com índice (1.15 ms) e COLLSCAN (18.4 ms).
* **Slide 15:** Instruções e Metodologia para o Simulado Prático (AVP1).
* **Slide 16:** Encerramento e Plantão de Dúvidas para as Avaliações Oficiais (Aulas 10 e 11).

---

## 🧪 5. Caderno do Simulado Integrado N1 (5 Grandes Desafios)

Os desafios a seguir compõem o simulado executado no arquivo [`simulado_n1_desafios.py`](codigo/simulado_n1_desafios.py):

1. **Desafio 1 (Cache-Aside Pattern):**  
   Implementar a função `buscar_produto_com_cache(r, db, sku, ttl=60)` que busca primeiro na chave `produto:{sku}` do Redis. Se houver falha (*Cache Miss*), recupera da coleção `produtos` do MongoDB, grava no Redis com TTL de 60 segundos e retorna o produto.
2. **Desafio 2 (Invalidação Imediata de Cache):**  
   Implementar a função `atualizar_estoque_com_invalidacao(r, db, sku, delta)` que realiza uma atualização atômica de incremento/decremento com `$inc` no MongoDB e apaga imediatamente a chave correspondente no Redis, evitando inconsistências de leitura (*Stale Reads*).
3. **Desafio 3 (Carrinho de Compras em Hashes):**  
   Implementar as funções `adicionar_ao_carrinho(r, cliente_id, sku, qtd)` e `obter_carrinho(r, cliente_id)` utilizando a estrutura de dados Hash do Redis (`HINCRBY`, `HGETALL`) com renovação de expiração de 20 minutos.
4. **Desafio 4 (Índice Composto ESR):**  
   Criar na coleção `pedidos` um índice composto otimizado para consultas que filtram por igualdade de status, ordenam cronologicamente por `data_pedido` descendente e buscam por faixas de `valor_total`, comprovando a eliminação do estágio `SORT` na memória RAM.
5. **Desafio 5 (Relatório Analítico de Agregação):**  
   Construir um pipeline analítico que filtre pedidos concluídos, desconstrua a lista de itens (`$unwind`) e sintetize a receita bruta e quantidade total de peças vendidas por categoria de produto.
