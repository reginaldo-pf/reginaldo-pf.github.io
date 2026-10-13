# Aula 04 -- Banco de Dados Não-Relacionais

**Disciplina:** Banco de Dados Não-Relacionais (ADS16)  
**Curso:** Tecnologia em Análise e Desenvolvimento de Sistemas (ADS) -- IFCE Campus Tauá  
**Carga Horária do Encontro:** 2 horas (120 minutos)  
**Data Prevista:** 13/10/2026 (Terça-feira)  
**Professor:** Prof. Me. Reginaldo Pereira Fernandes  

---

## 📚 Bibliografia & Referências Integradas

### Bibliografia Básica:
1. **SANFILIPPO, Salvatore (antirez).** *Redis: The Definitive Guide to In-Memory Data Structures and Real-Time Computing.* Redis Documentation, 2024. Disponível em: <https://redis.io/docs/>.
2. **SADALAGE, Pramod J.; FOWLER, Martin.** *NoSQL Essencial: Um Guia Conciso para o Mundo Emergente da Persistência Poliglota.* São Paulo: Novatec Editora, 2014. ISBN 978-8575223383.
3. **KLEPPMANN, Martin.** *Designing Data-Intensive Applications: The Big Ideas Behind Reliable, Scalable, and Maintainable Systems.* Sebastopol, CA: O'Reilly Media, 2017. 616 p.
4. **FROZZA, Angelo A.; SCHREINER, Paulo; MELLO, Ronaldo dos Santos.** *Projeto de Bancos de Dados NoSQL: Modelagem e Arquiteturas Chave-Valor e Documentos.* Livro Colaborativo de Bancos Não-Relacionais, 2022.
5. **REDIS APPLIED AI LAB.** *Context is All You Need: Data Pipelines, Context Retriever, Agent Memory and LangCache.* Mountain View: Redis AI Research, 2025.

### Bibliografia Complementar:
1. **POSTGRESQL GLOBAL DEVELOPMENT GROUP.** *Full Text Search and Query Optimization vs In-Memory Caching.* PostgreSQL 16 Documentation, 2024.
2. **GARCIA-MOLINA, Hector; ULLMAN, Jeffrey D.; WIDOM, Jennifer.** *Database Systems: The Complete Book.* 2. ed. Upper Saddle River: Pearson Prentice Hall, 2008.
3. **MICROSOFT LEARN.** *Windows Subsystem for Linux (WSL 2): Architecture, File System Performance and POSIX Compatibility.* Redmond: Microsoft Documentation, 2025.

---

## 💡 Metodologia & Filosofia Pedagógica

Esta aula foi concebida sob o método de **Construção Contextualizada em 4 Pilares**:
1. **Modelagem de Problema Real Antes do Código:** Cada comando e estrutura do Redis surge para resolver uma dor concreta de arquitetura (gargalo de busca no e-commerce, concorrência na Black Friday, estouro de memória RAM e latência em inteligência artificial).
2. **Terminal Interativo Primeiro (`redis-cli`):** Os discentes vivenciam as respostas atômicas diretamente no console antes de qualquer abstração de linguagem de alto nível.
3. **Exemplos Pareados (CLI e Python):** Toda operação de terminal possui seu equivalente direto e comentado em Python (`redis-py`), permitindo correlacionar a administração do banco com a integração de software.
4. **Comprovação Empírica da Física de Acesso:** Demonstração visual e computacional da diferença entre acesso a disco rígido/SSD (~150 a 250 ms) versus memória RAM (~0,07 ms), mensurando o ganho de aceleração (*Speedup* $> 2500\times$).

---

## 🎯 1. Objetivos de Aprendizagem

### Objetivo Geral:
Compreender os fundamentos da arquitetura em memória e do modelo Chave-Valor (*Key-Value*) utilizando o Redis, dominando a configuração de persistência em disco (RDB e AOF) para mitigar a volatilidade da memória RAM, operando com maestria as variações dos comandos `SET` e `GET`, aplicando as estruturas de dados nativas a problemas reais de negócio e implementando estratégias profissionais de caching expirável (TTL) e modernização com IA.

### Objetivos Específicos:
1. Instalar, configurar e operar o Redis no Windows via **WSL 2 (Windows Subsystem for Linux)**, Docker e Linux nativo, dominando o terminal interativo `redis-cli`.
2. Compreender a física da arquitetura **In-Memory**: por que a RAM opera em microssegundos ($\mu\text{s}$) e por que ela é intrinsecamente volátil.
3. Configurar e diferenciar os dois mecanismos de persistência durável no `redis.conf`: **RDB Snapshotting** (`save`, `BGSAVE`, `LASTSAVE`) e **AOF Log** (`appendonly yes`, `appendfsync everysec`, `BGREWRITEAOF`).
4. Modelar um sistema de **Cache de Consultas de Busca (Search Query Cache)** para resolver o gargalo de consultas lentas em catálogos de e-commerce.
5. Dominar todas as variações semânticas do comando `SET` (`EX`, `PX`, `NX` para travas distribuídas, `XX`, `KEEPTTL`, `GET`, `MSET`).
6. Dominar todas as variações semânticas do comando `GET` (`MGET`, `GETDEL` para consumo atômico de tokens, `GETEX`, `GETRANGE`, `STRLEN`).
7. Explicar por que o cache **DEVE ser expirável (TTL)**, relacionando finitude de RAM, políticas de evicção (`volatile-lru`, `allkeys-lru`) e autocura (*Self-Healing*) contra dados obsoletos (*Stale Reads*).
8. Contrastar os padrões de atualização de dados: **Cache-Aside (Lazy Loading)**, **Write-Through** e **Write-Behind (Write-Back)**, aplicando a regra de ouro de invalidação (`DEL` em vez de `SET`).
9. Operar as 5 estruturas de dados nativas do Redis: Strings, Hashes, Lists, Sets e Sorted Sets com problemas reais de modelagem.
10. Conectar o Redis à Inteligência Artificial moderna: **LangCache** (corte de 40-80% no custo de inferência de LLM) e **Agent Memory** (memória cross-session para agentes autônomos).

---

## ⏱️ 2. Cronograma da Aula (120 Minutos)

| Bloco | Duração | Descrição das Atividades Didáticas |
| :---: | :---: | :--- |
| **Bloco 1** | 00 -- 20 min | **O Modelo Chave-Valor e o Ecossistema Redis:** Conceito de chave-valor; por que a busca é $\mathcal{O}(1)$; histórico de Sanfilippo; guia de setup no Windows via WSL 2, Docker e Linux; comandos de boas-vindas no `redis-cli` (`PING`, `INFO`). |
| **Bloco 2** | 20 -- 45 min | **Arquitetura em Memória e Persistência Durável:** A volatilidade da RAM explicada; por que o Redis não perde dados; RDB Snapshotting (`save`, `BGSAVE` vs `SAVE`); AOF Log sequencial e políticas de `fsync`; Persistência Híbrida; inspeção ao vivo de status via CLI. |
| **Bloco 3** | 45 -- 75 min | **Variações Avançadas de SET e GET em Problemas Reais:** Caso Real 1: Sistema de Busca e Autocomplete de E-commerce; modelagem de termos; `SET` com `EX`, `PX`, `NX` (Locks Concorrentes), `XX`, `KEEPTTL`, `GET`, `MSET`; `GET` com `MGET`, `GETDEL` (Tokens atômicos), `GETEX`, `GETRANGE`, `STRLEN`. |
| **Bloco 4** | 75 -- 95 min | **Estratégias de Cache, TTL e Políticas de Atualização:** Por que o cache DEVE expirar; finitude da RAM e políticas de evicção LRU/LFU; os 3 padrões (Cache-Aside, Write-Through, Write-Behind); a regra crítica de invalidação (`DEL` ao atualizar no banco permanente); benchmarking visual de latência. |
| **Bloco 5** | 95 -- 120 min | **Estruturas Nativas, Modernização com IA e Hands-On:** Hashes, Lists, Sets e Sorted Sets na prática; Redis como Context Layer para IA (Data Pipelines, Context Retriever, Agent Memory e LangCache); execução dos scripts `redis_cli_guia_pratico.sh` e `demonstracao_aula04.py`. |

---

## 🛠️ 3. Guia de Ambiente no Windows (WSL 2), Docker e Linux

O Redis foi arquitetado sobre primitivas exclusivas do kernel Linux (chamadas de sistema `epoll`, `fork()` com *Copy-on-Write* e abstrações de memória POSIX). Para obter comportamento 100% idêntico à produção em ambientes Windows:

### Opção A: No Windows com WSL 2 (Windows Subsystem for Linux - Recomendado)
1. Abra o **PowerShell** ou **Terminal do Windows** como **Administrador** e instale a distribuição Ubuntu:
   ```powershell
   wsl --install -d Ubuntu
   ```
2. Após reiniciar (se solicitado), defina seu usuário e senha do Linux.
3. Dentro do terminal do Ubuntu, atualize os repositórios e instale o pacote oficial do Redis:
   ```bash
   sudo apt update
   sudo apt install redis-server -y
   ```
4. Inicie o serviço do Redis:
   ```bash
   sudo service redis-server start
   ```
5. Verifique o status e conecte-se via terminal:
   ```bash
   redis-cli ping
   # Retorno esperado: PONG
   
   redis-cli
   ```
6. **Integração com o Windows:** O WSL 2 redireciona as portas de rede automaticamente. Qualquer aplicativo rodando no Windows (como o **Redis Insight** ou extensões do VS Code) pode conectar diretamente em `localhost:6379`.

### Opção B: Via Container Docker (Multiplataforma)
Se você já utiliza Docker Desktop no Windows/macOS/Linux:
```bash
docker run -d --name redis-taua -p 6379:6379 -v redis-data:/data redis:7.4 redis-server --appendonly yes
```
Para acessar o console interativo:
```bash
docker exec -it redis-taua redis-cli
```

### Opção C: No Linux Nativo (Debian / Ubuntu / Pop!_OS)
```bash
sudo apt update && sudo apt install redis-server -y
sudo systemctl enable --now redis-server
redis-cli
```

---

## 🖼️ 4. Figuras e Elementos Visuais da Aula

A aula possui 5 diagramas vetoriais em alta resolução e 1 gráfico experimental de benchmarking:

1. **[Arquitetura em Memória vs Persistência](materiais/figuras/fig_arquitetura_memoria_persistencia.png):** Visualização em dois níveis contrastando a velocidade do motor na memória RAM com a durabilidade em disco através de snapshots RDB (`BGSAVE`) e log contínuo AOF (`appendonly`).
2. **[Ciclo de Vida do Cache de Busca](materiais/figuras/fig_ciclo_cache_busca.png):** Fluxo arquitetural do e-commerce da Tauá Tech Store, demonstrando a bifurcação entre *Cache Hit* (< 1 ms) e *Cache Miss* (200 ms), gravação serializada com TTL e contagem atômica de popularidade.
3. **[Padrões de Atualização e Sincronização](materiais/figuras/fig_padroes_atualizacao.png):** Comparativo visual lado a lado dos 3 padrões de sincronização (Cache-Aside, Write-Through e Write-Behind) e alerta didático sobre o perigo de condições de corrida.
4. **[As 5 Estruturas de Dados Nativas do Redis](materiais/figuras/fig_estruturas_redis.png):** Mapa conceitual detalhado com casos reais de uso e sintaxe CLI para Strings, Hashes, Lists, Sets e Sorted Sets.
5. **[Redis como Context Engine & LangCache para IA](materiais/figuras/fig_redis_ai_langcache.png):** Diagrama conceitual baseado na arquitetura moderna do Redis para IA (*Data Pipelines*, *Context Retriever*, *Agent Memory* e *LangCache* para economia de 40-80% em tokens de LLM).
6. **[Gráfico Experimental de Latência de Busca](codigo/grafico_latencia_busca.png):** Comprovação empírica em escala logarítmica gerada pelo script Python, demonstrando ganho de performance superior a 2500x.

---

## 📖 5. Roteiro Detalhado Slide-a-Slide

| Slide | Título do Slide | Tópicos & Pontos-Chave | Nota do Professor (Didática) | Elemento Visual |
| :---: | :--- | :--- | :--- | :--- |
| **01** | Capa Oficial | Disciplina ADS16, Título da Aula 04, Data e Docente. | Acolher os estudantes e apresentar o novo modelo NoSQL: Chave-Valor. | Identidade IFCE |
| **02** | Agenda do Encontro | 5 seções: Paradigma, Persistência, SET/GET, Cache/TTL, Estruturas & IA. | Apresentar o roteiro da aula contextualizando teoria e prática. | Sumário Beamer |
| **03** | O Paradigma Chave-Valor | Modelo conceitual, complexidade $\mathcal{O}(1)$, histórico de Salvatore Sanfilippo. | Explicar por que uma tabela hash em memória é a estrutura mais rápida da computação. | Colunas duplas |
| **04** | Setup Windows via WSL 2 | Instalação do Ubuntu no WSL 2, apt install redis-server, service start e redis-cli. | Tranquilizar os alunos de Windows mostrando que o WSL 2 roda o Linux nativo. | Bloco `lstlisting` |
| **05** | Primeiros Comandos CLI | Sintaxe do `redis-cli`, `PING`, convenção de chaves com namespaces (`entidade:id:campo`). | Ensinar a desenhar chaves organizadas como padrão de engenharia. | Bloco de código CLI |
| **06** | RAM: Velocidade vs Volatilidade | Acesso em 0,07 ms vs disco em 200 ms; o perigo da volatilidade física (queda de luz). | Provocar: "Se o servidor desligar agora, para onde vão nossos dados na RAM?" | Colunas duplas |
| **07** | Figura: Arquitetura e Persistência | Diagrama em dois níveis da RAM rápida ligada ao disco durável (RDB/AOF). | Guiar os discentes através do fluxo do processo principal e subprocessos filhos. | `fig_arquitetura_memoria_persistencia.pdf` |
| **08** | Mecanismo 1: RDB Snapshot | Dump binário `dump.rdb`, diretivas `save`, diferença crucial entre `SAVE` e `BGSAVE`. | Enfatizar: Nunca rodar `SAVE` em produção, pois ele congela o banco inteiro. | Tabela e código |
| **09** | Mecanismo 2: AOF e Híbrido | Log de escritas `appendonly.aof`, modos `everysec` vs `always`, comando `BGREWRITEAOF`. | Explicar que `everysec` é o trade-off ideal de no máximo 1 segundo de dados perdidos. | Tabela e código |
| **10** | Caso Real: Busca E-commerce | Problema de catálogo da Tauá Tech Store: buscas textuais lentas (200 ms). | Mostrar como uma query de texto em SQL derruba o servidor sob alta concorrência. | Colunas duplas |
| **11** | Figura: Ciclo do Cache de Busca | Diagrama de fluxo do Cache-Aside com Cache Hit (0,07 ms), Miss (200 ms) e TTL. | Demonstrar como a primeira busca alimenta o cache e as próximas voam em RAM. | `fig_ciclo_cache_busca.pdf` |
| **12** | Variações do SET no CLI | `SET EX`, `PX`, `NX` (Locks distribuídos / Concorrência), `XX`, `KEEPTTL`, `GET`, `MSET`. | Demonstrar como `NX` impede compra dupla na Black Friday. | Códigos comentados |
| **13** | Variações do GET no CLI | `GET`, `MGET`, `GETDEL` (Token de uso único atômico), `GETEX` (Renova sessão), `GETRANGE`. | Mostrar como `GETDEL` consome vouchers e tokens sem risco de reutilização. | Códigos comentados |
| **14** | Por que o Cache DEVE Expirar? | Finitude e custo da RAM, políticas de evicção (`volatile-lru`), autocura contra stale reads. | Alertar que memória RAM sem expiração é um vazamento de memória programado. | Colunas duplas |
| **15** | Figura: Padrões de Atualização | Visualização lado a lado de Cache-Aside, Write-Through e Write-Behind. | Contrastar os três padrões e discutir em quais projetos cada um se encaixa. | `fig_padroes_atualizacao.pdf` |
| **16** | Regra Crítica de Invalidação | Por que deletar (`DEL`) ao atualizar no SQL em vez de sobrescrever (`SET`). | Alertar contra condições de corrida (*Race Conditions*) em sistemas concorrentes. | Código explicativo |
| **17** | Figura: Benchmark Experimental | Gráfico comparativo de latência em escala logarítmica e curva de aquecimento. | Mostrar os resultados reais medidos no laboratório com ganho de 2800x. | `grafico_latencia_busca.png` |
| **18** | As 5 Estruturas Nativas | Diagrama panorâmico: Strings, Hashes, Lists, Sets e Sorted Sets. | Mostrar que o Redis não é só chave-valor simples, mas um servidor de estruturas. | `fig_estruturas_redis.pdf` |
| **19** | Hashes e Lists no Terminal | `HSET`, `HINCRBY`, `HGETALL` para perfis e `LPUSH`, `LTRIM`, `LRANGE` para históricos. | Explicar por que Hashes economizam muita memória RAM em relação a JSONs crus. | Códigos comentados |
| **20** | Sets e Sorted Sets no Terminal | `SADD`, `SINTER` para tags e `ZADD`, `ZINCRBY`, `ZREVRANGE` para termos em alta. | Mostrar a facilidade de criar leaderboards e rankings em uma única linha. | Códigos comentados |
| **21** | Figura: Redis para IA (Context Engine)| Modernização com IA: Data Pipelines, Context Retriever, Agent Memory e LangCache. | Conectar com a computação moderna de 2026 e LLMs que precisam de contexto rápido. | `fig_redis_ai_langcache.pdf` |
| **22** | Atividades Práticas e Fechamento | Guia dos scripts `redis_cli_guia_pratico.sh` e `demonstracao_aula04.py`, conexão Aula 05. | Orientar os discentes a abrir os terminais e rodar os exercícios práticos. | Roteiro final |

---

## 🎯 6. Modelagem Prática a partir de Problemas Reais

### Problema Real 1 (Inicial): Sistema de Busca e Autocomplete de E-commerce
- **Cenário de Negócio:** Na loja online **Tauá Tech Store**, quando os clientes digitam termos de busca como `"notebook dell"` ou `"fone bluetooth"`, o backend tradicional dispara consultas no PostgreSQL ou MongoDB:
  ```sql
  SELECT * FROM produtos WHERE LOWER(nome) LIKE '%notebook%' OR LOWER(descricao) LIKE '%notebook%';
  ```
  Essa consulta exige *Table Scan*, consome 100% de CPU e leva cerca de **200 ms**.
- **Modelagem Chave-Valor no Redis:**
  - **Namespace da Chave:** `busca:termo:<palavra_normalizada>` (Ex: `busca:termo:notebook_dell`).
  - **Tipo de Dado:** `String` contendo o payload serializado em JSON com a lista de produtos.
  - **Ciclo de Vida (TTL):** 300 segundos (5 minutos).
  - **Popularidade do Termo:** Contador atômico `stats:buscas:<termo>` incrementado via `INCR`.
- **Ganhos:**
  - Primeira busca (*Cache Miss*): 200 ms (alimenta o Redis com `SET ... EX 300`).
  - Próximas buscas (*Cache Hit*): **0,07 ms** (mais de $2500\times$ mais rápido).
  - Alívio total no banco de dados principal.

### Problema Real 2: Concorrência e Estoque na Black Friday (Trava Distribuída)
- **Cenário de Negócio:** Dois compradores tentam comprar a última unidade do produto `101` no mesmo milissegundo.
- **Modelagem com `SET NX EX`:**
  ```bash
  SET lock:estoque:prod_101 "worker_requisicao_A" NX EX 15
  ```
  - Se retornar `OK`, o processo obteve a posse exclusiva do recurso e prossegue com o débito no estoque.
  - Se retornar `(nil)`, o processo concorrente é informado de que outro cliente está finalizando o checkout e aguarda ou encerra.
  - O parâmetro `EX 15` garante liberação automática caso o servidor caia, prevenindo *Deadlocks*.

### Problema Real 3: Perfil de Aluno e Carrinho de Compras com Hashes
- **Cenário de Negócio:** Armazenar carrinho de compras de um aluno sem serializar e deserializar um JSON gigante a cada item adicionado.
- **Modelagem:**
  ```bash
  HSET carrinho:aluno_42 "PROD-101" 1 "PROD-202" 2
  HINCRBY carrinho:aluno_42 "PROD-101" 1
  HGETALL carrinho:aluno_42
  ```

### Problema Real 4: Fila Assíncrona de Pedidos e Histórico com Lists
- **Cenário de Negócio:** Quando um pedido é fechado, a notificação por e-mail e emissão de nota fiscal deve ser enfileirada sem travar a navegação do cliente.
- **Modelagem:**
  ```bash
  LPUSH fila:processar_pedidos "PED-9842"
  # No microservico consumidor (bloqueante):
  BRPOP fila:processar_pedidos 0
  ```

### Problema Real 5: Sistema de Tags e Recomendação por Interseção com Sets
- **Cenário de Negócio:** Encontrar tags compartilhadas entre produtos para alimentar a recomendação *"Quem viu este produto também se interessou por:"*.
- **Modelagem:**
  ```bash
  SADD tags:prod_A "computador" "dell" "bivolt"
  SADD tags:prod_B "desktop" "dell" "bivolt"
  SINTER tags:prod_A tags:prod_B
  # Retorna: "dell", "bivolt"
  ```

### Problema Real 6: Leaderboard de Tendências com Sorted Sets
- **Cenário de Negócio:** Exibir em tempo real na página inicial os 5 termos de busca mais pesquisados da semana (*Trending Searches*).
- **Modelagem:**
  ```bash
  ZINCRBY ranking:tendencias 1 "notebook dell"
  ZREVRANGE ranking:tendencias 0 4 WITHSCORES
  ```

### Problema Real 7: Modernização - Redis para IA (LangCache e Agent Memory)
- **Cenário de Negócio:** Agentes autônomos baseados em LLMs (GPT-4, Gemini, Claude) gastam de 1 a 3 segundos e dezenas de centavos por prompt. Empresas observam que 40% a 80% das perguntas de usuários são idênticas ou semanticamente similares.
- **Modelagem no Redis (LangCache):**
  - O Redis atua interceptando a chamada na inferência (*Inference Interceptor*).
  - Chave: `langcache:prompt:<hash_do_prompt>` com resposta memorizada.
  - Se existir no cache (*LangCache Hit*): Retorna em **< 1 ms**, economizando dinheiro e tempo.
  - **Agent Memory:** Como LLMs são *stateless*, o Redis preserva a memória do diálogo entre turnos e sessões.

---

## ⚡ 7. Guia Completo de Comandos no Terminal `redis-cli`

### Variações do Comando `SET`
| Sintaxe | Descrição Técnica | Exemplo no Terminal | Saída Esperada |
| :--- | :--- | :--- | :--- |
| `SET key val` | Gravação simples sem expiração | `SET app:nome "Taua Tech"` | `OK` |
| `SET key val EX seg` | Gravação com expiração em segundos | `SET token:sessao "abc" EX 60` | `OK` |
| `SET key val PX ms` | Expiração em milissegundos | `SET trava:temp "1" PX 1500` | `OK` |
| `SET key val NX` | **Not eXists:** só grava se a chave NÃO existir | `SET lock:item "w1" NX EX 10` | `OK` ou `(nil)` |
| `SET key val XX` | Só grava se a chave JÁ existir | `SET status "on" XX` | `OK` ou `(nil)` |
| `SET key val KEEPTTL`| Atualiza o valor mantendo o TTL original | `SET sessao "novo_token" KEEPTTL` | `OK` |
| `SET key val GET` | Grava novo valor e retorna o anterior de forma atômica | `SET contador 100 GET` | `"90"` |
| `MSET k1 v1 k2 v2` | Gravação múltipla em batch (1 RTT de rede) | `MSET usd 5.45 eur 5.95` | `OK` |

### Variações do Comando `GET`
| Sintaxe | Descrição Técnica | Exemplo no Terminal | Saída Esperada |
| :--- | :--- | :--- | :--- |
| `GET key` | Leitura simples | `GET app:nome` | `"Taua Tech"` |
| `MGET k1 k2 k3` | Leitura múltipla em batch (1 RTT) | `MGET usd eur inexistente` | `1) "5.45" 2) "5.95" 3) (nil)` |
| `GETDEL key` | Lê o valor e **deleta a chave atomicamente** | `GETDEL token:pix` | `"R$ 500"` (chave apagada) |
| `GETEX key EX seg` | Lê o valor e renova o tempo de expiração | `GETEX sessao EX 1800` | `"dados"` (novo TTL=1800s) |
| `GETRANGE key ini fim` | Retorna fatia da string (*Substring*) | `GETRANGE app:nome 0 3` | `"Taua"` |
| `STRLEN key` | Retorna comprimento da string em bytes | `STRLEN app:nome` | `(integer) 9` |

---

## 💾 8. Arquitetura em Memória e Persistência em Disco

### Por que a Memória RAM é Volátil?
A memória RAM dinâmica (DRAM) armazena bits em capacitores microscópicos que precisam ser recarregados milhares de vezes por segundo. Sem energia elétrica contínua, esses capacitores descarregam e os dados desaparecem. Para evitar a perda do estado do banco, o Redis implementa duas estratégias complementares:

### 1. RDB (Redis Database Snapshotting)
- **O que é:** Fotografia binária compactada de todas as chaves na memória RAM salva em disco no arquivo `dump.rdb`.
- **Configuração no `redis.conf`:**
  ```ini
  save 900 1      # Grava a cada 15 min se ao menos 1 chave mudou
  save 300 10     # Grava a cada 5 min se ao menos 10 chaves mudaram
  save 60 10000   # Grava a cada 1 min se ao menos 10.000 chaves mudaram
  dbfilename dump.rdb
  dir /var/lib/redis
  ```
- **Diferença Crucial:**
  - `SAVE`: Execução síncrona. O processo principal do Redis congela e para de responder requisições de todos os clientes até o dump terminar. **NUNCA execute em produção!**
  - `BGSAVE`: Execução assíncrona. O Redis invoca a syscall `fork()` do Linux criando um processo filho. O processo pai continua respondendo aos clientes em microssegundos com proteção de memória *Copy-on-Write (COW)* enquanto o filho escreve no disco.
- **Comandos de Terminal:**
  ```bash
  127.0.0.1:6379> BGSAVE
  Background saving started
  127.0.0.1:6379> LASTSAVE
  (integer) 1791888929
  ```

### 2. AOF (Append-Only File)
- **O que é:** Diário sequencial de log que registra cada operação de escrita recebida pelo servidor no arquivo `appendonly.aof`.
- **Configuração no `redis.conf`:**
  ```ini
  appendonly yes
  appendfilename "appendonly.aof"
  appendfsync everysec   # Recomendado: sincroniza em disco a cada 1s
  ```
- **Modos de `appendfsync`:**
  - `always`: Cada comando de escrita é descarregado para o disco antes de retornar ao cliente. Durabilidade máxima, mas reduz a vazão a taxas de disco convencional.
  - `everysec` (Padrão): Descarrega o buffer em disco 1 vez por segundo via thread dedicada. Se faltar energia, a perda máxima é de apenas 1 segundo de dados.
  - `no`: Deixa a critério do buffer do sistema operacional (mais rápido, porém imprevisível).
- **Compactação com `BGREWRITEAOF`:** Conforme o arquivo AOF cresce, ele pode acumular milhares de comandos redundantes (ex: 100 comandos `INCR contador`). O comando `BGREWRITEAOF` reescreve o arquivo no menor tamanho possível contendo apenas o estado final.

---

## 🚀 9. A Importância do Cache, TTL e Práticas de Atualização

### Por que o Cache DEVE ser Expirável (TTL)?
1. **Finitude e Custo da Memória:** Memória RAM é finita. Armazenar consultas ad infinitum esgota a memória física e aciona o *OOM Killer (Out Of Memory)* do sistema operacional.
2. **Autocura (*Self-Healing*):** Se ocorrer uma falha na invalidação ativa de cache (bug de aplicação, queda de rede), uma chave com TTL expirará naturalmente em alguns minutos, forçando o recarregamento dos dados corretos da fonte primária.
3. **Políticas de Evicção (`maxmemory-policy`):**
   - `volatile-lru`: Remove as chaves menos recentemente usadas que possuem expiração (TTL) configurada.
   - `allkeys-lru`: Remove qualquer chave sob critério LRU.
   - `noeviction`: Retorna erro em comandos de escrita quando a memória atinge o teto.

### Padrões de Atualização e Sincronização
1. **Cache-Aside (Lazy Loading - O Padrão Ouro):**
   - A aplicação tenta ler no Redis.
   - Se encontrar (*Hit*): retorna imediatamente.
   - Se não encontrar (*Miss*): busca na base permanente (SQL/Mongo), grava no Redis com TTL e retorna.
2. **Write-Through:**
   - A aplicação escreve no cache, e o cache atualiza o banco de dados síncronamente.
3. **Write-Behind (Write-Back):**
   - A escrita ocorre na memória RAM e entra em fila para gravação assíncrona posterior no banco em disco.
4. **⚠️ Regra de Ouro da Invalidação no Cache-Aside:**
   Ao atualizar um dado no banco relacional, **execute `DEL` no cache** em vez de sobrescrever com `SET`. Atualizar o cache na escrita sob concorrência cria graves condições de corrida (*Race Conditions*).

---

## 💻 10. Código Prático de Apoio e Roteiro de Execução

### Arquivos Disponíveis no Diretório `codigo/`:
1. `demonstracao_aula04.py`: Script Python modular e robusto contendo o simulador de Cache-Aside, todas as variações de SET/GET, status de persistência e geração automática do gráfico de latência.
2. `demonstracao_aula04.ipynb`: Notebook Jupyter interativo com explicações detalhadas célula a célula.
3. `redis_cli_guia_pratico.sh`: Guia de comandos em Bash para execução assistida no terminal `redis-cli`.

### Como Executar:
```bash
# 1. Executar o roteiro de comandos no terminal:
bash codigo/redis_cli_guia_pratico.sh

# 2. Executar a demonstracao em Python:
.venv/bin/python codigo/demonstracao_aula04.py
```

---

## 📝 11. Lista de Exercícios Práticos de Fixação (AV3)

### Bloco A: Operações no Terminal `redis-cli` (4,0 pontos)
1. **Exercício 1 (Cache de Busca com TTL):**
   No terminal `redis-cli`, crie uma chave `busca:termo:smartphone_5g` contendo um JSON com 2 modelos de celular, definindo expiração de 120 segundos via `SET ... EX`. Exiba o valor com `GET` e verifique o tempo restante com `TTL`.
2. **Exercício 2 (Trava Distribuída Concorrente):**
   Simule uma trava distribuída de estoque para o produto `PROD-900`. Demonstre o comando com `NX` e `EX 20` funcionando no primeiro terminal e falhando (retornando `nil`) em uma segunda tentativa simultânea.
3. **Exercício 3 (Consumo Atômico de Vouchers):**
   Grave um token promocional `voucher:desconto:user_15` com validade de 60 segundos. Em seguida, consuma e apague o token utilizando uma única instrução com `GETDEL`. Mostre a consulta subsequente comprovando a destruição da chave.
4. **Exercício 4 (Atualização Preservando TTL):**
   Crie uma chave de sessão com 45 segundos de vida. Aguarde 5 segundos e atualize o valor do token de autenticação utilizando a opção `KEEPTTL`. Demonstre com o comando `TTL` que a contagem regressiva original continuou intacta.

### Bloco B: Configuração e Persistência em Disco (3,0 pontos)
5. **Exercício 5 (Inspeção de Snapshotting RDB):**
   Execute o comando `CONFIG GET save` no `redis-cli` e transcreva os pares de valores retornados. Explique em detalhes o que significa cada par de números (segundos e alterações).
6. **Exercício 6 (Disparo de BGSAVE):**
   Execute manualmente um snapshot assíncrono com `BGSAVE`. Inspecione o timestamp retornado por `LASTSAVE` e explique a diferença física entre executar `BGSAVE` e executar `SAVE`.
7. **Exercício 7 (AOF fsync):**
   Explique qual é a consequência prática para a consistência e performance ao configurar `appendfsync always` em comparação com `appendfsync everysec`.

### Bloco C: Modelagem com Estruturas Nativas (2,0 pontos)
8. **Exercício 8 (Hashes e Sorted Sets):**
   Crie um perfil de usuário `usuario:100` usando `HSET` com os campos `nome`, `email` e `compras`. Incremente o número de compras em +1 usando `HINCRBY`. Em seguida, crie um ranking de clientes mais ativos usando `ZADD` e `ZINCRBY`, exibindo o top 3 com `ZREVRANGE ... WITHSCORES`.

### Bloco D: Questão Arquitetural de IA (1,0 ponto)
9. **Exercício 9 (LangCache e Context Layer):**
   Com base nos conceitos da imagem *"Context is all you need"*, explique por que o modelo chave-valor do Redis é amplamente adotado em arquiteturas de Inteligência Artificial para implementar **LangCache** e **Agent Memory**.
