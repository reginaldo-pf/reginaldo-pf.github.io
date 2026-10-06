#!/usr/bin/env bash
# ==============================================================================
# IFCE Campus Tauá - Tecnologia em Análise e Desenvolvimento de Sistemas (ADS16)
# Disciplina: Banco de Dados Não-Relacionais
# Aula 03 (Sábado Letivo) - Prática de Terminal CLI com Redis (redis-cli)
# Docente: Prof. Me. Reginaldo Pereira Fernandes
# ==============================================================================

set -e

REDIS_HOST="${REDIS_HOST:-127.0.0.1}"
REDIS_PORT="${REDIS_PORT:-6379}"

rc() {
  redis-cli -h "$REDIS_HOST" -p "$REDIS_PORT" "$@"
}

echo "======================================================================"
echo " [IFCE TAUÁ] Laboratório CLI Redis: redis-cli"
echo " Conectando a: $REDIS_HOST:$REDIS_PORT"
echo "======================================================================"

echo -n "Testando conectividade: "
rc PING

# 1. ESCOPO DE TESTE (DB 1)
rc SELECT 1 > /dev/null

echo -e "\n>>> 2. STRINGS, TTL E CONTADORES ATÔMICOS:"
echo "[SET/GET/TTL] Sessão de usuário com expiração de 120s:"
rc SET session:ads_user_42 "token_jwt_987654321_taua" EX 120
echo -n "Valor: "; rc GET session:ads_user_42
echo -n "Tempo restante de vida (TTL em segundos): "; rc TTL session:ads_user_42

echo "[INCR] Contador atômico de visualizações de produto (Page Views):"
rc SET views:produto:NOT-DEL-01 100
rc INCR views:produto:NOT-DEL-01
rc INCRBY views:produto:NOT-DEL-01 25
echo -n "Total de views: "; rc GET views:produto:NOT-DEL-01

echo "[SETNX] Trava idempotente com SET if Not Exists:"
echo -n "1ª aquisição de trava: "; rc SETNX lock:pedido:9001 "worker_1"
echo -n "2ª aquisição de trava (deve retornar 0 - conflito): "; rc SETNX lock:pedido:9001 "worker_2"

echo -e "\n>>> 3. HASHES (Entidade Objeto Chave-Campo-Valor):"
rc HSET user:101 nome "Reginaldo Fernandes" email "reginaldo.fernandes@ifce.edu.br" campus "Taua" nivel "Docente"
rc HSET user:101 ultimo_login "2026-10-10 14:00:00"
echo -n "Campo 'nome': "; rc HGET user:101 nome
echo "Todos os campos do hash user:101:"
rc HGETALL user:101

echo "[Carrinho de Compras em Hash]"
rc HSET cart:session_taua_77 "NOT-DEL-01" 1 "MOU-LOG-02" 2
rc HINCRBY cart:session_taua_77 "MOU-LOG-02" 1
echo "Itens no carrinho (SKU -> Quantidade):"
rc HGETALL cart:session_taua_77

echo -e "\n>>> 4. LISTS (Filas FIFO e Filas de Mensagens):"
rc DEL fila:pedidos_pendentes > /dev/null
rc RPUSH fila:pedidos_pendentes "PED-1001" "PED-1002" "PED-1003"
echo -n "Tamanho da fila: "; rc LLEN fila:pedidos_pendentes
echo "Elementos atuais na fila:"
rc LRANGE fila:pedidos_pendentes 0 -1
echo -n "Consumindo primeiro da fila (LPOP - FIFO): "; rc LPOP fila:pedidos_pendentes
echo "Fila após o consumo:"
rc LRANGE fila:pedidos_pendentes 0 -1

echo -e "\n>>> 5. SETS (Conjuntos Únicos Não-Ordenados):"
rc DEL tags:tecnologia > /dev/null
rc SADD tags:tecnologia "nosql" "mongodb" "redis" "python" "docker"
rc SADD tags:tecnologia "nosql" # Ignorado automaticamente
echo "Elementos no Set:"
rc SMEMBERS tags:tecnologia
echo -n "O set contém 'mongodb'? "; rc SISMEMBER tags:tecnologia "mongodb"
echo -n "O set contém 'sql_legado'? "; rc SISMEMBER tags:tecnologia "sql_legado"

echo -e "\n>>> 6. SORTED SETS (Leaderboard e Rankings):"
rc DEL ranking:mais_vendidos > /dev/null
rc ZADD ranking:mais_vendidos 45 "MOU-LOG-02"
rc ZADD ranking:mais_vendidos 12 "NOT-DEL-01"
rc ZADD ranking:mais_vendidos 28 "TEC-MEC-03"
rc ZADD ranking:mais_vendidos 70 "CAB-USBC-05"
echo "Top 3 produtos mais vendidos (ZREVRANGE com pontuações):"
rc ZREVRANGE ranking:mais_vendidos 0 2 WITHSCORES

echo -e "\n>>> 7. METADADOS E INSPEÇÃO DE MEMÓRIA:"
echo -n "Tipo da chave user:101: "; rc TYPE user:101
echo -n "Tipo da chave fila:pedidos_pendentes: "; rc TYPE fila:pedidos_pendentes
echo -n "Tipo da chave ranking:mais_vendidos: "; rc TYPE ranking:mais_vendidos
echo -n "Uso de memória (bytes) para user:101: "; rc MEMORY USAGE user:101

echo "======================================================================"
echo " Laboratório CLI Redis concluído com 100% de sucesso!"
echo "======================================================================"
