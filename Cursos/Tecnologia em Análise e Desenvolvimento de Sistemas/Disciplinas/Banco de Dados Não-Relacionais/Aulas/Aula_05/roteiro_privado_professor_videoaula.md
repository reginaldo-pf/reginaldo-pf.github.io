# 🔒 ROTEIRO PRIVADO DO PROFESSOR (GRAVAÇÃO DA VIDEOAULA — AULA 05)
## Estudo de Caso: Padrão Cache-Aside com Redis e TTL (ShopGrids)

* **Docente:** Prof. Me. Reginaldo Fernandes (IFCE Campus Tauá)
* **Disciplina:** Banco de Dados Não-Relacionais (ADS16)
* **Uso Exclusivo:** Guia de direção, fala, comandos e explicação linha a linha para gravação da videoaula.
* **Vídeo de Inspiração:** [CACHE-ASIDE: Escalabilidade, Performance e Arquitetura de Software (Renato Augusto)](https://www.youtube.com/watch?v=vRO0UfvsbDw)

---

## 📋 Preparação Antes de Apertar "REC"

1. **Janelas recomendadas na tela:**
   * **Lado Esquerdo (ou Tela Principal):** VS Code (aberto inicialmente sem nenhuma pasta ou no terminal integrado) + Editor de código com fonte tamanho `16` ou `18` para ficar legível no vídeo.
   * **Lado Direito (ou dividido embaixo):** Dois terminais abertos (Terminal 1 para rodar o servidor Flask, Terminal 2 para rodar comandos `curl` / `redis-cli`).
2. **Garanta que o Redis esteja limpo antes de começar:**
   ```bash
   redis-cli FLUSHALL
   ```

---

## 🎬 ABERTURA: O Problema de Arquitetura (00:00 – 03:00)

### 🎙️ O que falar para a câmera:
> *"Fala, pessoal! Na aula prática de hoje nós vamos resolver na prática um dos problemas mais cobrados em entrevistas técnicas de arquitetura de software e que mais derruba sistemas reais em produção: **o excesso de consultas repetidas no banco de dados**.*
>
> *Imaginem que nós fomos contratados como desenvolvedores pelo e-commerce **ShopGrids**, que está se preparando para a **Black Friday**. Na página inicial do site existe aquela seção de **Categorias em Destaque**. O banco de dados relacional tem dezenas de categorias cadastradas, mas o pessoal de Marketing marca como `is_featured = 1` apenas as 4 ou 6 categorias que devem aparecer em destaque na semana.*
>
> *Qual é o problema? Toda vez que um cliente entra na Home, o Front-end chama a nossa rota `/categories/featured` e a API faz um `SELECT` no banco de dados. Com poucos usuários, funciona. Mas na Black Friday, com milhares de acessos simultâneos, o banco relacional — que precisa cuidar de transações ACID, índices, bloqueios e conexões em disco — é espancado com milhares de `SELECT`s idênticos para buscar sempre os mesmos dados! O banco abre o bico, forma fila, dá Timeout e o site cai.*
>
> *Como a gente resolve isso sem trocar o banco de dados e sem gastar com infraestrutura? Implementando o padrão **Cache-Aside** com **Redis**, que opera na **Memória RAM** em cerca de **100 nanossegundos** (enquanto um HD leva 10 milissegundos e um SSD leva 100 microssegundos). Bora pro código construir isso do absoluto zero!"*

---

## 🛠️ PASSO 1: Criando a Pasta, Ambiente Virtual (`venv`) e Instalando Pacotes via `pip`

### 🎥 Ação na Tela:
Abra o Terminal e digite os comandos abaixo passo a passo, comentando o que cada um faz.

### 🎙️ O que falar enquanto digita:
> *"Vamos começar do absoluto zero. Primeiro eu crio a pasta do nosso projeto `shopgrids-cache` e entro nela. Agora, como boa prática em Python, nunca instalamos pacotes soltos no sistema operacional: vamos criar um ambiente virtual isolado usando o módulo `venv` e ativá-lo. Reparem que apareceu o `(.venv)` aqui no começo do terminal. Agora atualizamos o `pip` e instalamos apenas dois pacotes: o `flask` (para criar nossa API) e o `redis` (para conversar com o servidor Redis pelo protocolo binário RESP)."*

### ⌨️ Comandos Comentados Linha a Linha:

```bash
# Cria um novo diretório chamado 'shopgrids-cache' para o projeto
mkdir shopgrids-cache

# Entra no diretório recém-criado
cd shopgrids-cache

# Executa o módulo nativo 'venv' do Python 3 para criar o ambiente virtual na pasta oculta '.venv'
python3 -m venv .venv

# Ativa o ambiente virtual no terminal atual (Linux / macOS)
# (No Windows PowerShell seria: .venv\Scripts\Activate.ps1)
source .venv/bin/activate

# Atualiza o gerenciador de pacotes pip para a versão mais recente dentro do ambiente virtual
pip install --upgrade pip

# Instala o microframework web Flask e o driver cliente oficial do Redis (redis-py)
pip install flask redis

# Salva a lista exata de pacotes e versões instaladas no arquivo requirements.txt
pip freeze > requirements.txt
```

---

## 🔌 PASSO 2: Verificando e Testando o Servidor Redis

### 🎥 Ação na Tela:
Ainda no terminal, mostre que o servidor Redis está rodando na porta `6379` e faça um teste rápido de conexão.

### 🎙️ O que falar enquanto digita:
> *"Com os pacotes instalados, vamos conferir se o nosso servidor Redis está ativo na máquina. Eu rodo `redis-cli ping` e ele me responde `PONG`. Vale lembrar para vocês: o Redis não precisa ficar na mesma máquina da API; em arquiteturas distribuídas ou microsserviços ele pode rodar em outro servidor ou container Docker, e a comunicação é ultra-rápida porque ele não usa HTTP, ele usa o protocolo RESP (Redis Serialization Protocol) direto via TCP na porta 6379."*

### ⌨️ Comandos Comentados Linha a Linha:

```bash
# Envia o comando de diagnóstico PING para o servidor Redis local (porta 6379)
# Se o servidor estiver ativo, ele responde imediatamente com a palavra PONG
redis-cli ping

# (OPCIONAL — Só execute se o Redis estiver desligado na sua máquina):
# Inicia o servidor Redis em segundo plano (daemon) ou via Docker:
# redis-server --daemonize yes
# docker run -d --name redis-aula -p 6379:6379 redis:7.4-alpine

# Executa um comando rápido em Python para provar que o pacote 'redis' instalado no .venv conecta com sucesso:
python -c "import redis; r = redis.Redis(host='localhost', port=6379, decode_responses=True); print('Redis conectado:', r.ping())"
```

---

## 🗄️ PASSO 3: Criando o Banco de Dados Relacional (`criar_banco.py`)

### 🎥 Ação na Tela:
Crie o arquivo `criar_banco.py` no VS Code, digite/cole o código abaixo explicando cada bloco e depois execute `python criar_banco.py` no terminal.

### 🎙️ O que falar enquanto digita:
> *"Agora vamos criar o nosso banco de dados relacional para simular a tabela de categorias da ShopGrids. Para ninguém precisar configurar Postgres ou MySQL pesado agora, vamos usar o `sqlite3`, que já vem embutido no Python e grava um banco SQL real no arquivo `shopgrids.db`.*
>
> *Vou criar o arquivo `criar_banco.py`. Olhem só: ele cria a tabela `categories` com `id`, `name`, `image` e a coluna booleana `is_featured` (onde `1` significa que a categoria está em destaque na Home e `0` significa que não está). Vamos cadastrar 6 categorias: deixaremos as 4 primeiras de tecnologia marcadas com `1` (em destaque) e as 2 últimas de inverno marcadas com `0`."*

### ⌨️ Código do `criar_banco.py` (Com Comentários em Cada Linha):

```python
# Importa a biblioteca nativa do Python para manipular bancos de dados SQLite em disco
import sqlite3

# Define a função responsável por criar a tabela e inserir os dados iniciais
def inicializar_banco():
    # Abre conexão com o arquivo 'shopgrids.db' (se o arquivo não existir, o SQLite cria automaticamente)
    conn = sqlite3.connect("shopgrids.db")
    
    # Cria o objeto cursor, que é quem executa os comandos SQL (CREATE, INSERT, SELECT) dentro do banco
    cursor = conn.cursor()

    # Apaga a tabela 'categories' caso ela já exista de um teste anterior, garantindo um início limpo
    cursor.execute("DROP TABLE IF EXISTS categories")

    # Executa o comando SQL DDL para criar a tabela 'categories' com 4 colunas
    cursor.execute("""
        CREATE TABLE categories (
            id INTEGER PRIMARY KEY,                 -- Identificador único da categoria (Chave Primária)
            name TEXT NOT NULL,                     -- Nome da categoria exibido na vitrine
            image TEXT NOT NULL,                    -- Nome do arquivo/ícone de imagem da categoria
            is_featured INTEGER NOT NULL DEFAULT 0  -- Flag de destaque: 1 = Em Destaque (True), 0 = Oculta (False)
        )
    """)

    # Cria uma lista de tuplas contendo as 6 categorias que serão inseridas na tabela
    # Repare no último número de cada linha: as 4 primeiras têm is_featured = 1 e as 2 últimas têm is_featured = 0
    categorias = [
        (1, "TV & Áudio", "tv-audio.png", 1),          # Em destaque (1)
        (2, "Desktop & Laptop", "laptop.png", 1),      # Em destaque (1)
        (3, "Smartphones", "smartphone.png", 1),       # Em destaque (1)
        (4, "Acessórios Gamer", "gamer.png", 1),       # Em destaque (1)
        (5, "Moda Inverno", "inverno.png", 0),         # Não está em destaque (0)
        (6, "Aquecedores", "aquecedor.png", 0),        # Não está em destaque (0)
    ]

    # Executa o INSERT em lote (executemany) substituindo os quatro '?' pelos valores de cada tupla da lista
    cursor.executemany(
        "INSERT INTO categories (id, name, image, is_featured) VALUES (?, ?, ?, ?)",
        categorias
    )

    # Confirma (persiste) a transação gravando os dados fisicamente no arquivo shopgrids.db em disco
    conn.commit()
    
    # Fecha a conexão com o banco de dados para liberar o arquivo
    conn.close()
    
    # Exibe mensagem de confirmação no terminal
    print("✓ Banco 'shopgrids.db' criado com sucesso com 6 categorias (4 em destaque)!")

# Bloco padrão do Python: executa a função inicializar_banco() quando rodamos 'python criar_banco.py'
if __name__ == "__main__":
    inicializar_banco()
```

### ⌨️ Executando no Terminal:
```bash
# Roda o script para criar o arquivo shopgrids.db
python criar_banco.py

# (Opcional — Mostrar no terminal os dados gravados na tabela SQL):
sqlite3 shopgrids.db "SELECT * FROM categories;"
```

---

## 🐢 PASSO 4: Construindo a Versão 1 do `app.py` (Sem Cache — O Gargalo no Banco)

### 🎥 Ação na Tela:
Crie o arquivo `app.py` no VS Code com a Versão 1 (sem Redis ainda). Depois rode `python app.py` no Terminal 1 e faça requisições com `curl` no Terminal 2.

### 🎙️ O que falar enquanto digita:
> *"Agora vamos criar o nosso servidor `app.py` na **Versão 1 — Sem Cache**, exatamente como o sistema estava antes de começarem os travamentos na Black Friday.*
>
> *Na função `buscar_categorias_no_banco()`, colocamos um `time.sleep(0.08)` para simular 80 milissegundos de custo de I/O de disco e concorrência no banco relacional, e fazemos o `SELECT id, name, image, is_featured FROM categories WHERE is_featured = 1`.*
>
> *Na rota `@app.route('/categories/featured')`, nós medimos o tempo de início, chamamos o banco de dados e devolvemos o JSON mostrando a origem (`BANCO_DE_DADOS (SQL)`) e quantos milissegundos demorou. Além disso, já vou deixar duas rotinhas auxiliares (`/categories/inverno` e `/categories/blackfriday`) que simulam a tela administrativa do pessoal de Produto alterando quais categorias estão em destaque lá no banco SQL."*

### ⌨️ Código Completo do `app.py` — Versão 1 (Com Comentários em Cada Linha):

```python
# Arquivo: app.py (VERSÃO 1 — SEM CACHE: TODA REQUISIÇÃO BATE NO BANCO SQL)

# Importa o módulo nativo sqlite3 para consultar o nosso banco de dados em disco
import sqlite3
# Importa o módulo time para medir a latência da requisição e simular o custo de I/O do disco
import time
# Importa a classe Flask (para criar o servidor web) e jsonify (para retornar respostas no formato JSON)
from flask import Flask, jsonify

# Instancia a aplicação Flask
app = Flask(__name__)


# Função que realiza a consulta SQL diretamente no arquivo de banco de dados 'shopgrids.db'
def buscar_categorias_no_banco():
    # Pausa a execução por 0.08 segundos (80 ms) para simular a latência real de um banco em disco sob carga
    time.sleep(0.08)

    # Abre uma conexão com o banco de dados relacional em disco
    conn = sqlite3.connect("shopgrids.db")
    
    # Configura o row_factory para sqlite3.Row, permitindo acessar as colunas pelo nome (como um dicionário)
    conn.row_factory = sqlite3.Row
    
    # Cria o cursor para executar a consulta SQL
    cursor = conn.cursor()

    # Executa o SELECT filtrando apenas as categorias onde is_featured é igual a 1 (True)
    cursor.execute("SELECT id, name, image, is_featured FROM categories WHERE is_featured = 1")
    
    # Busca todas as linhas retornadas (fetchall) e converte cada linha em um dicionário Python padrão
    categorias = [dict(row) for row in cursor.fetchall()]

    # Fecha a conexão com o banco de dados
    conn.close()
    
    # Retorna a lista de categorias encontradas no banco
    return categorias


# Define o endpoint HTTP GET /categories/featured (consultado pelo Front-end da loja)
@app.route("/categories/featured", methods=["GET"])
def get_featured_categories():
    # Registra o instante exato (timestamp) em que a requisição chegou na API
    inicio = time.time()

    # PROBLEMA DE ESCALABILIDADE: Toda requisição que chega executa um SELECT no banco de dados!
    categorias = buscar_categorias_no_banco()

    # Calcula o tempo total gasto (em milissegundos) subtraindo o tempo inicial do tempo atual
    tempo_ms = round((time.time() - inicio) * 1000, 2)
    
    # Retorna a resposta HTTP em formato JSON para o cliente (Front-end / Postman / curl)
    return jsonify({
        "origem": "BANCO_DE_DADOS (SQL)",  # Indica que os dados vieram direto do disco/SQL
        "tempo_ms": tempo_ms,              # Tempo gasto na requisição (~80 ms)
        "total": len(categorias),          # Quantidade de categorias retornadas
        "dados": categorias                # Lista com os objetos das categorias em destaque
    })


# Rota auxiliar (POST) que simula a tela administrativa do time de Produto mudando os destaques para o Inverno
@app.route("/categories/inverno", methods=["POST"])
def ativar_categorias_inverno():
    # Abre conexão com o banco de dados SQLite
    conn = sqlite3.connect("shopgrids.db")
    # Desmarca todas as categorias (define is_featured = 0 em toda a tabela)
    conn.execute("UPDATE categories SET is_featured = 0")
    # Marca apenas as 2 categorias de inverno (IDs 5 e 6) como destaque (is_featured = 1)
    conn.execute("UPDATE categories SET is_featured = 1 WHERE id IN (5, 6)")
    # Salva as alterações no disco
    conn.commit()
    # Fecha a conexão com o banco
    conn.close()
    # Retorna confirmação da alteração feita no banco SQL
    return jsonify({"mensagem": "Banco SQL atualizado: apenas 2 categorias de inverno em destaque!"})


# Rota auxiliar (POST) que simula o time de Produto colocando todas as 6 categorias em destaque na Black Friday
@app.route("/categories/blackfriday", methods=["POST"])
def ativar_todas_categorias():
    # Abre conexão com o banco de dados SQLite
    conn = sqlite3.connect("shopgrids.db")
    # Marca todas as 6 categorias da tabela com is_featured = 1
    conn.execute("UPDATE categories SET is_featured = 1")
    # Salva as alterações no disco
    conn.commit()
    # Fecha a conexão com o banco
    conn.close()
    # Retorna confirmação da alteração feita no banco SQL
    return jsonify({"mensagem": "Banco SQL atualizado: todas as 6 categorias em destaque!"})


# Inicia o servidor web Flask na porta 5000 com modo debug ativo (recarrega sozinho ao salvar alterações no código)
if __name__ == "__main__":
    app.run(port=5000, debug=True)
```

### ⌨️ Testando a Versão 1 ao Vivo:
* **No Terminal 1:**
  ```bash
  python app.py
  ```
* **No Terminal 2:**
  ```bash
  # Faz a requisição para buscar as categorias em destaque
  curl -s http://localhost:5000/categories/featured | jq .
  ```
* **🎙️ O que comentar ao mostrar a saída:**
  > *"Vejam só: retornou as **4 categorias** em destaque, vindo do `BANCO_DE_DADOS (SQL)` e levando **~81 ms**. Se eu rodar de novo, leva 81 ms de novo. Toda vez ele bate no banco!"*

---

## ⚡ PASSO 5: Evoluindo para a Versão 2 do `app.py` (Cache-Aside com `GET` e `SET`)

### 🎥 Ação na Tela:
Edite o arquivo `app.py` no VS Code para adicionar o Redis (`import json`, `import redis`, `r.get`, `r.set`). Salve o arquivo (o Flask vai recarregar sozinho no Terminal 1).

### 🎙️ O que falar enquanto edita o código:
> *"Agora vamos implementar o padrão **Cache-Aside**! O que muda no nosso código?*
> 1. *Importamos o `json` e o `redis` e criamos a conexão `r` na porta 6379.*
> 2. *Dentro da rota `/categories/featured`, criamos uma variável `cache_key = 'featured_categories'`, que é o nome da chave que vai identificar esses dados lá na memória do Redis.*
> 3. *Antes de encostar no banco de dados, fazemos `cached_categories = r.get(cache_key)`. Ou seja: 'Ô Redis, você tem as categorias em destaque aí na memória?'*
> 4. *Se o `cached_categories` existir (`if cached_categories:`), nós convertemos o texto JSON de volta para lista com `json.loads()` e já damos `return` imediatamente! O código nem chega na linha do banco de dados!*
> 5. *E se o Redis responder `None` (porque está vazio na 1ª vez)? Aí ele não entra no `if`, busca no banco de dados SQL e, antes de devolver para o front-end, salva uma cópia no Redis com `r.set(cache_key, json.dumps(categorias))`!*
>
> *Detalhe importante: por que usamos `json.dumps()`? Porque o comando `SET` do Redis guarda texto (String). Se passarmos a lista do Python direto sem converter para String JSON, o Redis dá erro!"*

### ⌨️ Código Completo do `app.py` — Versão 2 (Com Comentários em Cada Linha):

```python
# Arquivo: app.py (VERSÃO 2 — PADRÃO CACHE-ASIDE COM GET E SET SEM EXPIRAÇÃO)

# [NOVO] Importa o módulo json para serializar a lista em texto (dumps) e desserializar (loads)
import json
import sqlite3
import time
from flask import Flask, jsonify
# [NOVO] Importa o driver oficial do Redis para Python
import redis

app = Flask(__name__)

# [NOVO] Cria o cliente de conexão com o servidor Redis local na porta 6379
# O parâmetro decode_responses=True converte automaticamente as respostas de bytes (b'...') para String ('...')
r = redis.Redis(host="localhost", port=6379, db=0, decode_responses=True)


def buscar_categorias_no_banco():
    # Simula os 80ms de lentidão de I/O do banco de dados em disco
    time.sleep(0.08)
    conn = sqlite3.connect("shopgrids.db")
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, image, is_featured FROM categories WHERE is_featured = 1")
    categorias = [dict(row) for row in cursor.fetchall()]
    conn.close()
    return categorias


@app.route("/categories/featured", methods=["GET"])
def get_featured_categories():
    # Marca o tempo de início da requisição
    inicio = time.time()

    # [NOVO] Define o nome da chave (identificador único) onde guardaremos as categorias no Redis
    cache_key = "featured_categories"

    # [NOVO] PASSO 1 DO CACHE-ASIDE: Consulta o Redis primeiro para ver se o dado já está na memória RAM
    cached_categories = r.get(cache_key)

    # [NOVO] PASSO 2 (CACHE HIT): Se a chave existir no Redis, retorna imediatamente sem tocar no banco SQL!
    if cached_categories:
        # Converte a String JSON que veio do Redis de volta para uma lista de dicionários Python
        lista_categorias = json.loads(cached_categories)
        # Calcula o tempo de resposta (será menor que 1 milissegundo!)
        tempo_ms = round((time.time() - inicio) * 1000, 2)
        # Retorna os dados diretamente da memória RAM e encerra a função aqui mesmo
        return jsonify({
            "origem": "CACHE_REDIS (Memória RAM)",
            "tempo_ms": tempo_ms,
            "total": len(lista_categorias),
            "dados": lista_categorias
        })

    # PASSO 3 (CACHE MISS): Se não entrou no 'if' acima, o dado não estava no Redis.
    # Então vamos buscar no banco de dados relacional (lento: ~80 ms)
    categorias = buscar_categorias_no_banco()

    # [NOVO] PASSO 4: Salva uma cópia do resultado no Redis (convertido para String JSON com json.dumps)
    # Assim, as próximas requisições encontrarão o dado pronto na memória RAM!
    r.set(cache_key, json.dumps(categorias))

    # Calcula o tempo total desta 1ª requisição que precisou ir ao banco
    tempo_ms = round((time.time() - inicio) * 1000, 2)
    
    # Retorna os dados buscados do banco SQL
    return jsonify({
        "origem": "BANCO_DE_DADOS (SQL)",
        "tempo_ms": tempo_ms,
        "total": len(categorias),
        "dados": categorias
    })


@app.route("/categories/inverno", methods=["POST"])
def ativar_categorias_inverno():
    conn = sqlite3.connect("shopgrids.db")
    conn.execute("UPDATE categories SET is_featured = 0")
    conn.execute("UPDATE categories SET is_featured = 1 WHERE id IN (5, 6)")
    conn.commit()
    conn.close()
    return jsonify({"mensagem": "Banco SQL atualizado: apenas 2 categorias de inverno em destaque!"})


@app.route("/categories/blackfriday", methods=["POST"])
def ativar_todas_categorias():
    conn = sqlite3.connect("shopgrids.db")
    conn.execute("UPDATE categories SET is_featured = 1")
    conn.commit()
    conn.close()
    return jsonify({"mensagem": "Banco SQL atualizado: todas as 6 categorias em destaque!"})


if __name__ == "__main__":
    app.run(port=5000, debug=True)
```

### ⌨️ Testando a Versão 2 no Terminal 2:

```bash
# 1ª Chamada: O Redis está vazio -> Vai dar CACHE MISS, buscar no Banco SQL (~82 ms) e salvar no Redis:
curl -s http://localhost:5000/categories/featured | jq '{origem, tempo_ms, total}'

# 2ª Chamada: Agora já existe no Redis -> Vai dar CACHE HIT direto da RAM (< 1 ms)!
curl -s http://localhost:5000/categories/featured | jq '{origem, tempo_ms, total}'

# Mostrar para os alunos o dado salvo lá dentro do servidor Redis:
redis-cli GET featured_categories
```

---

## 🚨 PASSO 6: Demonstrando o Problema da Inconsistência (A Pegadinha!)

### 🎥 Ação na Tela:
No Terminal 2, chame a rota `/categories/inverno` para alterar o banco SQL para apenas 2 categorias e em seguida consulte `/categories/featured`.

### 🎙️ O que falar enquanto executa:
> *"Agora que nosso endpoint está respondendo em menos de 1 milissegundo vindo do Redis, parece que o trabalho acabou, certo? Calma que aqui mora o perigo!*
>
> *Imaginem que chegou o inverno e o pessoal de Produto foi lá na tela de cadastro deles — que grava direto no banco de dados SQL —, tirou TV, Laptop e Smartphone de destaque e deixou **apenas 2 categorias** em destaque: Moda Inverno e Aquecedores. Vamos rodar o comando que atualiza o banco SQL para o inverno.*
>
> *Pronto, lá no banco SQL agora só existem 2 categorias com `is_featured = 1`. Mas olhem o que acontece quando o Front-end chama `/categories/featured`: ele continua trazendo as **4 categorias antigas**! Por quê? Porque o `r.set()` que usamos não tem prazo de validade! O dado fica eterno na memória do Redis, a API sempre entra no `if cached_categories:` e nunca mais consulta o banco de dados! Como resolvemos essa inconsistência?"*

### ⌨️ Comandos para Demonstrar o Bug no Terminal 2:

```bash
# 1. Altera no Banco de Dados SQL para deixar apenas 2 categorias (Moda Inverno e Aquecedores):
curl -s -X POST http://localhost:5000/categories/inverno | jq .

# 2. (Opcional) Mostra direto no banco SQLite que realmente só as categorias 5 e 6 estão com is_featured = 1:
sqlite3 shopgrids.db "SELECT id, name, is_featured FROM categories;"

# 3. Consulta a API novamente — Veja que ela ignora a mudança do banco e devolve as 4 categorias velhas do cache!
curl -s http://localhost:5000/categories/featured | jq '{origem, tempo_ms, total, dados}'

# 4. Mostra que o tempo de vida (TTL) da chave no Redis é -1 (ou seja, infinito / nunca expira):
redis-cli TTL featured_categories
```

---

## 🏆 PASSO 7: Versão 3 Final do `app.py` — Invalidação por Tempo com TTL (`SETEX`)

### 🎥 Ação na Tela:
Volte ao `app.py` no VS Code, troque `r.set(cache_key, json.dumps(categorias))` por `r.setex(cache_key, 20, json.dumps(categorias))` e adicione o campo `"ttl_segundos": r.ttl(cache_key)` no JSON de resposta para o aluno ver a contagem regressiva na tela!

### 🎙️ O que falar enquanto edita e testa:
> *"A forma mais simples e eficaz de invalidar esse cache é definir um **TTL (Time To Live — Tempo de Vida)**. No Redis, basta trocarmos o método `r.set()` pelo **`r.setex()`**, que aceita um parâmetro a mais: o tempo em segundos! Vamos passar **20 segundos**.*
>
> *Primeiro, vamos dar um `redis-cli DEL featured_categories` para apagar aquela chave infinita que tinha ficado presa no passo anterior. Agora, quando eu consulto a API pela 1ª vez, ela não acha no cache, vai no banco SQL, traz as **2 categorias de inverno** e salva no Redis por **20 segundos**.*
>
> *Agora prestem atenção no teste ao vivo: eu vou atualizar o banco SQL para ativar todas as **6 categorias** da Black Friday e vou ficar consultando a API! Olhem o `ttl_segundos` caindo: 14, 12, 9... Enquanto os 20 segundos não acabam, ele responde rápido trazendo as 2 categorias do cache. Assim que passam os 20 segundos... Pronto! O cache expirou sozinho na memória RAM, a API foi ao banco e já atualizou para as **6 categorias** automaticamente!"*

### ⌨️ Código Completo do `app.py` — Versão 3 Final (Com Comentários em Cada Linha):

```python
# Arquivo: app.py (VERSÃO 3 FINAL — CACHE-ASIDE COM SETEX E EXPIRAÇÃO AUTOMÁTICA TTL DE 20s)

import json
import sqlite3
import time
from flask import Flask, jsonify
import redis

app = Flask(__name__)

# Conexão com o Redis local na porta 6379
r = redis.Redis(host="localhost", port=6379, db=0, decode_responses=True)


def buscar_categorias_no_banco():
    # Simula 80ms de latência de consulta no banco de dados em disco
    time.sleep(0.08)
    conn = sqlite3.connect("shopgrids.db")
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, image, is_featured FROM categories WHERE is_featured = 1")
    categorias = [dict(row) for row in cursor.fetchall()]
    conn.close()
    return categorias


@app.route("/categories/featured", methods=["GET"])
def get_featured_categories():
    inicio = time.time()
    cache_key = "featured_categories"

    # 1. Consulta primeiro o Cache no Redis
    cached_categories = r.get(cache_key)

    # 2. Se encontrou no Redis (CACHE HIT), retorna da memória RAM mostrando quantos segundos de vida restam (TTL)
    if cached_categories:
        lista_categorias = json.loads(cached_categories)
        tempo_ms = round((time.time() - inicio) * 1000, 2)
        return jsonify({
            "origem": "CACHE_REDIS (Memória RAM)",
            "tempo_ms": tempo_ms,
            "ttl_segundos": r.ttl(cache_key),  # Consulta no Redis quantos segundos faltam para a chave sumir
            "total": len(lista_categorias),
            "dados": lista_categorias
        })

    # 3. Se não encontrou no Redis (CACHE MISS), busca os dados frescos no banco SQL
    categorias = buscar_categorias_no_banco()

    # [SOLUÇÃO DEFINITIVA] 4. Usa SETEX para salvar no Redis com TTL (Time To Live) de 20 segundos!
    # Parâmetros do setex: (nome_da_chave, tempo_de_vida_em_segundos, valor_em_string_json)
    # Após 20 segundos, o próprio Redis apaga esta chave automaticamente da memória RAM!
    r.setex(cache_key, 20, json.dumps(categorias))

    tempo_ms = round((time.time() - inicio) * 1000, 2)
    return jsonify({
        "origem": "BANCO_DE_DADOS (SQL)",
        "tempo_ms": tempo_ms,
        "ttl_segundos": 20,
        "total": len(categorias),
        "dados": categorias
    })


@app.route("/categories/inverno", methods=["POST"])
def ativar_categorias_inverno():
    conn = sqlite3.connect("shopgrids.db")
    conn.execute("UPDATE categories SET is_featured = 0")
    conn.execute("UPDATE categories SET is_featured = 1 WHERE id IN (5, 6)")
    conn.commit()
    conn.close()
    return jsonify({"mensagem": "Banco SQL atualizado: apenas 2 categorias de inverno em destaque!"})


@app.route("/categories/blackfriday", methods=["POST"])
def ativar_todas_categorias():
    conn = sqlite3.connect("shopgrids.db")
    conn.execute("UPDATE categories SET is_featured = 1")
    conn.commit()
    conn.close()
    return jsonify({"mensagem": "Banco SQL atualizado: todas as 6 categorias em destaque!"})


if __name__ == "__main__":
    app.run(port=5000, debug=True)
```

### ⌨️ Sequência Exata de Comandos no Terminal 2 para o Teste Ao Vivo do TTL:

```bash
# 1. Apaga a chave antiga que tinha sido gravada sem TTL no Passo 5:
redis-cli DEL featured_categories

# 2. Faz a 1ª consulta: Vai buscar as 2 categorias de inverno no SQL e gravar no Redis por 20 segundos:
curl -s http://localhost:5000/categories/featured | jq '{origem, tempo_ms, ttl_segundos, total}'

# 3. Imediatamente atualiza o banco SQL para ter todas as 6 categorias (Black Friday):
curl -s -X POST http://localhost:5000/categories/blackfriday | jq .

# 4. Roda várias vezes seguidas para mostrar o ttl_segundos diminuindo (15, 12, 8...) e, após zerar, atualizando para 6 categorias!
curl -s http://localhost:5000/categories/featured | jq '{origem, tempo_ms, ttl_segundos, total}'
```

---

## 🎯 FECHAMENTO DA GRAVAÇÃO: Os 3 Critérios de Ouro (2 Minutos Finais)

### 🎙️ O que falar para encerrar a aula:
> *"Pessoal, para fechar com chave de ouro e vocês mandarem muito bem em qualquer entrevista de arquitetura: cuidado para não saírem colocando cache em tudo quanto é lugar! Lembrem que o cache mora na **Memória RAM** do servidor, que é um recurso limitado e onde a própria aplicação também roda.*
>
> *Antes de colocar qualquer dado no cache, verifiquem se ele tem estas **3 características obrigatórias**:*
> 1. **Ser muito requisitado:** Tem que ser um dado com altíssimo volume de leitura, como a vitrine da Home.
> 2. **Não mudar a todo segundo:** Não faz sentido cachear um dado que muda a cada segundo.
> 3. **Tolerar Consistência Eventual (consistência fraca):** Nas categorias em destaque, se o Marketing mudar no banco e demorar 20 segundos para atualizar na tela do cliente, não tem problema nenhum. Mas você **jamais** pode colocar o **saldo de uma conta bancária** no cache com TTL! Imagina você ter R$ 1.000 na conta, fazer um Pix de R$ 1.000 e o seu saldo continuar mostrando R$ 1.000 travado até o cache expirar! Dados críticos exigem consistência forte direto no banco.*
>
> *Agora é a vez de vocês: sigam o roteiro prático passo a passo no material da aula e reproduzam todo esse fluxo na máquina de vocês. Um forte abraço e até a próxima aula!"*
