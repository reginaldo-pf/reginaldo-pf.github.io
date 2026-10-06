# Plano de Aula: 03 - Prática de Banco de Dados: MongoDB e Redis (Sábado Letivo)

**Curso:** Tecnologia em Análise e Desenvolvimento de Sistemas (ADS)  
**Disciplina:** Banco de Dados Não-Relacionais (ADS16)  
**Semestre:** 2026.2 | **Data:** 10 de Outubro de 2026 (Sábado Letivo)  
**Docente:** Prof. Me. Reginaldo Pereira Fernandes  
**Carga Horária Equivalente:** 2 horas-aula (120 minutos)  
**Modalidade:** **Não-Presencial / Remoto (Estudo e Laboratório Autônomo em Casa)**

---

## 💡 1. Filosofia Pedagógica e Metodologia

Este sábado letivo foi concebido como uma **imersão prática e ferramental** para consolidar os conceitos teóricos das Aulas 01 e 02 (descasamento de impedância, particionamento e os Teoremas CAP e PACELC). Os estudantes realizarão atividades laboratoriais em casa, explorando as duas tecnologias NoSQL mais populares do mercado: **MongoDB** (banco orientado a documentos) e **Redis** (banco chave-valor em memória).

A sequência metodológica foi organizada para eliminar abstrações desnecessárias:
1. **Interação Direta Primeiro (Sem Python):** Os alunos operam diretamente nos bancos usando ferramentas de terminal (**CLI**: `mongosh` e `redis-cli`) e interfaces gráficas profissionais (**GUI**: **MongoDB Atlas / Compass** e **Redis Insight**).
2. **Integração Complementar Segundo (Com Python):** Após dominar a sintaxe nativa dos bancos, os alunos utilizam **Python** (`pymongo` e `redis-py`) para implementar o padrão ouro da arquitetura distribuída: o **Cache-Aside Pattern (Lazy Loading)**.
3. **Comprovação Empírica de Latência:** Medição comparativa do tempo de acesso em disco (MongoDB: ~10 ms) versus em memória RAM (Redis: ~0.07 ms), visualizando o ganho de velocidade (*Speedup* $> 100\times$).

---

## 🎯 2. Objetivos de Aprendizagem

### Objetivo Geral
Capacitar o estudante a manipular, modelar e operar de forma autônoma bancos de dados MongoDB e Redis através de interfaces de linha de comando (CLI), interfaces gráficas (GUIs) e scripts Python, integrando ambas as tecnologias através do padrão arquitetural de cache distribuído.

### Objetivos Específicos
- Configurar ambientes de bancos NoSQL no computador pessoal utilizando containers Docker (`docker-compose.yml`) ou serviços em nuvem gratuitos (MongoDB Atlas e Redis Cloud).
- Executar operações de CRUD (*Create, Read, Update, Delete*) no MongoDB utilizando o terminal `mongosh` e a interface visual MongoDB Compass.
- Praticar comandos fundamentais nas cinco estruturas de dados centrais do Redis (Strings, Hashes, Lists, Sets e Sorted Sets) no terminal `redis-cli` e no Redis Insight.
- Implementar o padrão **Cache-Aside** em Python, compreendendo o ciclo de *Cache Hit*, *Cache Miss* e *Invalidação Imediata* para evitar leituras de dados obsoletos (*Stale Reads*).
- Resolver a **Lista de Exercícios Práticos Avaliativa**, documentando comandos, códigos e capturas de tela das ferramentas gráficas.

---

## ⏱️ 3. Cronograma Recomendado de Estudo Autônomo (120 min)

| Etapa | Duração Estimada | Conteúdo / Atividade |
| :--- | :---: | :--- |
| **Etapa 1** | 20 min | Leitura dos Slides Beamer e Configuração do Ambiente (Docker ou Nuvem Atlas/Redis) |
| **Etapa 2** | 30 min | Prática 1: MongoDB no Terminal (`mongosh`) e no MongoDB Compass (Criação e CRUD) |
| **Etapa 3** | 30 min | Prática 2: Redis no Terminal (`redis-cli`) e no Redis Insight (Estruturas e TTL) |
| **Etapa 4** | 20 min | Prática 3: Integração Python com `pymongo` e `redis-py` (Padrão Cache-Aside) |
| **Etapa 5** | 20 min | Resolução e Documentação da Lista de Exercícios de Fixação |

---

## 🛠️ 4. Guia de Configuração do Ambiente em Casa

Os estudantes podem escolher a opção mais conveniente para seu computador pessoal:

### Opção A: Setup Local via Docker Compose (Recomendado - 1 Comando)
Se você já tem o Docker e o Docker Compose instalados:
```bash
# Na pasta da Aula 03:
docker compose up -d
```
Serviços iniciados automaticamente:
- **MongoDB 8.0:** `localhost:27017` (Usuário: `root`, Senha: `ifce_taua_secret`)
- **Redis 7.4:** `localhost:6379`
- **Redis Insight (GUI Web):** Acesse no navegador: [http://localhost:5540](http://localhost:5540)
- **Mongo Express (GUI Web):** Acesse no navegador: [http://localhost:8081](http://localhost:8081)

Para encerrar o ambiente ao finalizar o estudo:
```bash
docker compose down
```

### Opção B: Setup em Nuvem + GUIs Desktop (Sem Instalar Servidores Pesados)
1. **MongoDB Atlas & Compass:**
   - Crie uma conta gratuita no [MongoDB Atlas](https://www.mongodb.com/cloud/atlas/register).
   - Crie um cluster gratuito **M0** (512 MB).
   - Baixe o [MongoDB Compass](https://www.mongodb.com/products/tools/compass) e cole sua Connection String.
2. **Redis Cloud & Redis Insight:**
   - Crie uma base gratuita (30 MB) no [Redis Cloud](https://redis.io/try-free/).
   - Baixe o [Redis Insight](https://redis.io/insight/) para desktop e adicione a conexão do Redis Cloud.

---

## 🍃 5. Prática 1: MongoDB sem Python (CLI e Compass)

### 5.1 Terminal mongosh
Acesse o terminal do MongoDB (`mongosh mongodb://localhost:27017`):

```javascript
// 1. Criar e alternar para a base de dados
use ecommerce_taua;

// 2. Inserir documento no catálogo de produtos (Create - insertOne)
db.produtos.insertOne({
  sku: "NOT-DEL-01",
  nome: "Notebook Dell Inspiron 15",
  categoria: "Informatica",
  preco: 4299.90,
  estoque: 14,
  especificacoes: {
    processador: "Intel Core i7 13ª Ger",
    memoria_gb: 16,
    ssd_gb: 512
  },
  tags: ["trabalho", "desenvolvimento", "bivolt"],
  ativo: true
});

// 3. Consultar produtos com projeção e filtro (Read - find)
db.produtos.find(
  { categoria: "Informatica", preco: { $lt: 5000.00 } },
  { _id: 0, sku: 1, nome: 1, preco: 1, tags: 1 }
);

// 4. Atualização atômica com $set e $inc (Update - updateOne)
db.produtos.updateOne(
  { sku: "NOT-DEL-01" },
  {
    $set: { preco: 3899.00 },
    $inc: { estoque: 5 }
  }
);

// 5. Remoção de documento (Delete - deleteOne)
db.produtos.deleteOne({ sku: "NOT-DEL-01" });
```

### 5.2 MongoDB Compass (Interface Gráfica)
1. Conecte ao banco e visualize a base `ecommerce_taua` e a coleção `produtos`.
2. Insira um novo documento clicando no botão verde **"Add Data" $\rightarrow$ "Insert Document"**.
3. Alterne entre os modos **Tree View** (árvore hierárquica) e **JSON**.
4. Teste filtros na barra superior: `{"preco": {"$gt": 1000}}`.
5. Vá na aba **"Indexes"** e crie um índice para o campo `categoria: 1`.
6. Na aba **"Explain Plan"**, execute a consulta e observe se foi utilizado um `COLLSCAN` (varredura completa) ou `IXSCAN` (busca pelo índice).

---

## ⚡ 6. Prática 2: Redis sem Python (CLI e Redis Insight)

### 6.1 Terminal redis-cli
Conecte ao Redis com `redis-cli`:

```bash
# 1. Testar conexao
PING
# Retorno: PONG

# 2. Strings e Tempo de Expiracao (TTL)
SET session:user_taua_42 "jwt_token_seguro_ifce" EX 90
GET session:user_taua_42
TTL session:user_taua_42

# 3. Contador atomico de visualizacoes
SET views:NOT-DEL-01 100
INCR views:NOT-DEL-01
INCRBY views:NOT-DEL-01 10

# 4. Hashes: Carrinho de Compras de E-commerce
HSET cart:session_77 "NOT-DEL-01" 1 "MOU-LOG-02" 2
HINCRBY cart:session_77 "MOU-LOG-02" 1
HGETALL cart:session_77

# 5. Lists: Fila FIFO de Pedidos
RPUSH fila:pedidos "PED-101" "PED-102" "PED-103"
LLEN fila:pedidos
LPOP fila:pedidos

# 6. Sorted Sets: Leaderboard de Produtos Mais Vendidos
ZADD ranking:vendas 45 "MOU-LOG-02" 12 "NOT-DEL-01" 70 "CAB-USBC-05"
ZREVRANGE ranking:vendas 0 2 WITHSCORES
```

### 6.2 Redis Insight (Interface Gráfica)
1. Abra o Redis Insight em [http://localhost:5540](http://localhost:5540) ou no aplicativo Desktop.
2. Na aba **Browser / Key Tree**, observe como as chaves são agrupadas por namespace (`session:`, `cart:`, `views:`).
3. Clique na chave `cart:session_77` e inspecione seus campos e valores no editor visual.
4. Clique no botão **Memory Usage** para verificar o consumo exato de bytes na memória RAM.

---

## 🐍 7. Prática 3: Integração Complementar com Python (Cache-Aside)

O script [`codigo/demonstracao_aula03.py`](codigo/demonstracao_aula03.py) implementa a arquitetura completa:
- MongoDB atua como **System of Record** (catálogo persistente no disco).
- Redis atua como **In-Memory Cache** (consultas instantâneas).
- Quando a aplicação consulta um produto:
  1. Primeiro verifica no Redis (**Cache Hit** $\rightarrow$ retorna em ~0.07 ms).
  2. Se não encontrar (**Cache Miss** $\rightarrow$ busca no MongoDB em ~10 ms e salva no Redis com TTL de 120s).
- Ao atualizar o preço, a aplicação invalida o cache no Redis para evitar inconsistências.

Para executar o script:
```bash
python3 codigo/demonstracao_aula03.py
```
O script gera automaticamente o gráfico de benchmarking [`codigo/grafico_latencia_cache.png`](codigo/grafico_latencia_cache.png).

---

## 📝 8. Lista de Exercícios Práticos Avaliativa (Entrega Remota)

Esta lista deve ser desenvolvida individualmente e entregue até a sexta-feira anterior à Aula 04 via SIGAA ou Google Classroom.

### Bloco A: Terminal CLI e GUI no MongoDB (4,0 pontos)
1. **Exercício 1 (Modelagem e Inserção no mongosh):**
   Crie uma coleção chamada `livros` na base `biblioteca_taua`. Insira pelo menos 4 livros contendo: `isbn`, `titulo`, `autor`, `ano`, `preco`, `tags` (array com pelo menos 2 categorias) e `dimensoes` (objeto aninhado com `altura_cm` e `paginas`). Apresente o código executado.
2. **Exercício 2 (Consultas Estruturadas):**
   Escreva comandos `find()` para:
   - Listar livros com mais de 250 páginas (`dimensoes.paginas > 250`).
   - Listar livros que contenham a tag `"tecnologia"` no array de tags.
   - Listar todos os livros projetando apenas `titulo` e `preco`, omitindo o `_id`.
3. **Exercício 3 (Índices no MongoDB Compass / Atlas):**
   Utilizando o MongoDB Compass, crie um índice para o campo `isbn`. Execute uma busca por um ISBN específico na aba **Explain Plan** e tire uma captura de tela (print) demonstrando que o estágio de execução foi `IXSCAN` (Index Scan).

### Bloco B: Terminal CLI e GUI no Redis (3,0 pontos)
4. **Exercício 4 (Sessões com TTL no redis-cli):**
   Crie 3 tokens de sessão (`session:user_1`, `session:user_2`, `session:user_3`) com tempo de expiração de 60 segundos. Demonstre a consulta com `GET` e a verificação do tempo decrescente com `TTL`.
5. **Exercício 5 (Carrinho de Compras em Hashes):**
   Crie um carrinho de compras para o usuário `cart:aluno_10` no Redis. Adicione 2 itens com quantidades iniciais. Incremente a quantidade de um dos itens em +2 usando `HINCRBY`. Exiba o carrinho completo com `HGETALL`.
6. **Exercício 6 (Inspeção Visual no Redis Insight):**
   Abra o Redis Insight, localize a chave do seu carrinho na **Key Tree** e tire um print destacando o tipo de dado (`hash`), os campos armazenados e o consumo de memória retornado pelo Redis Insight.

### Bloco C: Script de Integração em Python (2,0 pontos)
7. **Exercício 7 (Cache-Aside Pattern):**
   Implemente uma função em Python `consultar_livro(isbn)` que conecta ao MongoDB e ao Redis. A função deve:
   - Checar se o livro está no Redis. Se estiver, imprimir `[CACHE HIT]` e retornar os dados.
   - Se não estiver, imprimir `[CACHE MISS]`, buscar no MongoDB, gravar no Redis com TTL de 30 segundos e retornar os dados.
   - Execute duas consultas seguidas para o mesmo ISBN comprovando o `CACHE MISS` na primeira e o `CACHE HIT` na segunda.
8. **Exercício 8 (Invalidação Imediata):**
   Crie a função `atualizar_preco_livro(isbn, novo_preco)`. A função deve alterar o valor no MongoDB e remover (`delete`) a chave do Redis. Demonstre que a consulta seguinte resulta em um novo `CACHE MISS`.

### Bloco D: Questões Conceituais de Arquitetura (1,0 ponto)
9. **Exercício 9:** Por que não é recomendado utilizar o Redis como banco de dados principal permanente (*System of Record*) para todo o catálogo de um e-commerce em larga escala? Quais são os limites físicos de custo e durabilidade?
10. **Exercício 10:** Qual é a função do TTL (*Time to Live*) nas chaves de cache? O que ocorreria com a memória do Redis se todas as consultas do MongoDB fossem cacheadas sem nenhum TTL e sem política de expulsão (*Eviction Policy*)?

---

## 📦 9. Instruções de Submissão

- **Formato:** Relatório em PDF contendo o texto dos comandos/códigos e as capturas de tela (prints) comprobatórias das interfaces MongoDB Compass e Redis Insight, OU link de repositório no GitHub contendo os scripts `.sh`, `.py` e as imagens na pasta `prints/`.
- **Local de Envio:** Tarefa específica cadastrada no SIGAA / Classroom com o título: *"Envio Lista Prática - Aula 03 (Sábado Letivo)"*.
- **Prazo:** Até a sexta-feira anterior à Aula 04.
