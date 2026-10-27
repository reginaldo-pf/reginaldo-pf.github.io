import redis

# Conexão com o redis
r = redis.Redis(host='localhost', port=6379, db=0)

# Exemplo hash
def exemplo_hash():
    # Adicionando dados ao hash
    r.hset('user:1000', 'name', 'Maria')
    r.hset('user:1000', 'age', 30)
    r.hset('user:1000', 'email', 'maria@mail.com')

    # Recuperando dados do hash
    user = r.hgetall('user:1000')
    print(f"Hash - User: {user}")

    # Atualizando um campo no hash
    r.hset('user:1000', 'age', 31)

    # Recuperando um campo específico do hash
    age = r.hget('user:1000', 'age').decode()
    print(f"Update age: {age}")

def exemplo_lista():
    # Adicionando dados a lista
    r.rpush('tasks', 'task1')
    r.rpush('tasks', 'task2')
    r.rpush('tasks', 'task3')

    # Recuperando dados da lista
    task = r.lrange('tasks', 0, -1)
    print(f"Exemplo lista - Tasks: {task}")

    # Removendo e retornando o primeiro item da lista
    task = r.lpop('tasks')
    print(f"Task removido: {task}")

    # Recuperando o tamanho da lista
    size = r.llen('tasks')
    print(f"Tamanho da lista: {size}")

def exemplo_conjunto():
    # Adicionando dados ao conjunto (set)
    r.sadd('tags', 'python')
    r.sadd('tags', 'redis')
    r.sadd('tags', 'database')

    # Recuperação de todos os membros do conjunto
    tags = r.smembers('tags')
    print(f"Exemplo de conjunto - Tags: {tags}")

    # Verificando a existência de um membro do conjunto
    is_member = r.sismember('tags', 'python')
    print(f"Phyton é um membro do conjunto tags? {is_member}")

    # Removendo um membro do conjunto
    r.srem('tags','database')
    tags = r.smembers('tags')
    print(f"Conjunto - Tags: {tags}")

# Exemplo de Conjunto ordenado (sorted set)
def exemplo_conjunto_ordenado():
    # Adicionando dados ao conjunto ordenado
    r.zadd('leaderboard', {'Maria': 100, 'Bob': 200, 'Charlie': 150})

    # Recuperando todos os membros do conjunto ordenado com suas pontuações
    leaderboard = r.zrange('leaderboard', 0, -1, withscores=True)
    print(f"Exemplo de conjunto ordenado - Leaderborder: {leaderboard}")

    # Atualizando a pontuação de um membro
    r.zincrby('leaderboard', 50, 'Maria')

    # Recuperando a pontuação de um membro
    score = r.zscore('leaderboard', 'Maria')
    print(f"Pontuação atualizada de Maria: {score}")

    # Recuperando os membros com pontuação entre um intervalo específico
    top_players = r.zrangebyscore('leaderboard', 100, 200, withscores=True)
    print(f"Top players: {top_players}")

#exemplo_hash()
#exemplo_lista()
#exemplo_conjunto()
exemplo_conjunto_ordenado()