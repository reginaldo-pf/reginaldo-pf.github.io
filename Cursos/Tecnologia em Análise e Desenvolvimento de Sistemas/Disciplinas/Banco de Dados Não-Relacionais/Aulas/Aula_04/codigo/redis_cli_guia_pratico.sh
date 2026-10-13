#!/usr/bin/env bash
# =============================================================================
# IFCE Campus Tauá - Tecnologia em Análise e Desenvolvimento de Sistemas (ADS)
# Disciplina: Banco de Dados Não-Relacionais (ADS16)
# Aula 04: Modelo Chave-Valor com Redis (Operações Avançadas via redis-cli)
# Docente: Prof. Me. Reginaldo Pereira Fernandes
# =============================================================================

# Cores para saída formatada no terminal
VERDE='\033[0;32m'
AZUL='\033[0;34m'
AMARELO='\033[1;33m'
VERMELHO='\033[0;31m'
CIANO='\033[0;36m'
NEGRITO='\033[1m'
NC='\033[0m' # Sem Cor

echo -e "${CIANO}${NEGRITO}"
echo "============================================================================="
echo "   IFCE CAMPUS TAUÁ - ADS | BANCO DE DADOS NÃO-RELACIONAIS"
echo "   GUIA PRÁTICO DE TERMINAL: REDIS-CLI (WSL, LINUX E DOCKER)"
echo "============================================================================="
echo -e "${NC}"

echo -e "${AMARELO}💡 DICA PARA USUÁRIOS WINDOWS:${NC}"
echo -e "O Redis foi projetado nativamente para sistemas baseados em Linux."
echo -e "No Windows 10 ou 11, execute o Redis via ${VERDE}WSL 2 (Windows Subsystem for Linux)${NC}:"
echo -e "  1. Abra o PowerShell como Administrador e execute:  ${CIANO}wsl --install -d Ubuntu${NC}"
echo -e "  2. Abra o terminal Ubuntu instalado e rode:         ${CIANO}sudo apt update && sudo apt install redis-server -y${NC}"
echo -e "  3. Inicie o daemon do Redis:                        ${CIANO}sudo service redis-server start${NC}"
echo -e "  4. Conecte-se ao terminal interativo:               ${CIANO}redis-cli${NC}"
echo -e "  (Alternativamente via Docker: ${CIANO}docker run -d --name redis-local -p 6379:6379 redis:7.4${NC})\n"

# Verifica se o redis-cli está disponível
if ! command -v redis-cli &> /dev/null; then
    echo -e "${VERMELHO}❌ Comando 'redis-cli' não encontrado no ambiente atual.${NC}"
    echo "Instale o cliente Redis ou acesse pelo container com: docker exec -it <nome_container> redis-cli"
    exit 1
fi

echo -e "${AZUL}🔍 Testando conexão com o servidor Redis (PING)...${NC}"
PONG_RESP=$(redis-cli PING)
if [ "$PONG_RESP" != "PONG" ]; then
    echo -e "${VERMELHO}❌ Não foi possível obter PONG do Redis. Verifique se o serviço está ativo!${NC}"
    exit 1
fi
echo -e "${VERDE}✅ Conexão ativa com o Redis Server! Resposta: ${PONG_RESP}${NC}\n"

# -----------------------------------------------------------------------------
echo -e "${NEGRITO}${CIANO}=============================================================================${NC}"
echo -e "${NEGRITO}${CIANO}PARTE 1: CASO REAL INICIAL - CACHE DE TERMOS DE BUSCA (E-COMMERCE TAUÁ)${NC}"
echo -e "${NEGRITO}${CIANO}=============================================================================${NC}"
echo -e "Problema: Consultas como 'notebook dell' gastam 200ms no banco em disco."
echo -e "Solução: Armazenar a resposta JSON em memória com chave-valor e TTL de 300 segundos.\n"

echo -e "${AMARELO}1.1 Gravando resultado de busca com TTL de 300 segundos (SET ... EX):${NC}"
echo "Comando: redis-cli SET busca:termo:notebook_dell '[{\"id\":101,\"nome\":\"Dell Inspiron 15\",\"preco\":3899.00}]' EX 300"
redis-cli SET busca:termo:notebook_dell '[{"id":101,"nome":"Dell Inspiron 15","preco":3899.00}]' EX 300

echo -e "\n${AMARELO}1.2 Consultando o dado em memória (GET):${NC}"
echo "Comando: redis-cli GET busca:termo:notebook_dell"
redis-cli GET busca:termo:notebook_dell

echo -e "\n${AMARELO}1.3 Inspecionando o tempo de vida restante em segundos (TTL):${NC}"
echo "Comando: redis-cli TTL busca:termo:notebook_dell"
redis-cli TTL busca:termo:notebook_dell

echo -e "\n${AMARELO}1.4 Incrementando contador de pesquisas do termo de forma atômica (INCR):${NC}"
echo "Comando: redis-cli INCR stats:buscas:notebook_dell"
redis-cli INCR stats:buscas:notebook_dell
redis-cli INCR stats:buscas:notebook_dell

# -----------------------------------------------------------------------------
echo -e "\n${NEGRITO}${CIANO}=============================================================================${NC}"
echo -e "${NEGRITO}${CIANO}PARTE 2: VARIAÇÕES AVANÇADAS DO COMANDO SET${NC}"
echo -e "${NEGRITO}${CIANO}=============================================================================${NC}"

echo -e "${AMARELO}2.1 SET com NX (Not eXists) - Trava Distribuída (Lock Concorrente):${NC}"
echo "Cenário: Processo 1 tenta travar o estoque do produto 500 por 15 segundos:"
echo "Comando: redis-cli SET lock:estoque:prod_500 \"processo_A\" NX EX 15"
redis-cli SET lock:estoque:prod_500 "processo_A" NX EX 15

echo -e "\nCenário: Processo 2 tenta a mesma trava simultaneamente (Deve retornar nil / vazio):"
echo "Comando: redis-cli SET lock:estoque:prod_500 \"processo_B\" NX EX 15"
RESP_LOCK=$(redis-cli SET lock:estoque:prod_500 "processo_B" NX EX 15)
echo -e "Retorno do Redis: [${RESP_LOCK:-'(nil)'}] -> Bloqueou concorrência com sucesso!"

echo -e "\n${AMARELO}2.2 SET com XX (Apenas se já existir):${NC}"
echo "Tentativa 1: chave inexistente (retorna nil):"
redis-cli DEL config:alerta_estoque > /dev/null
redis-cli SET config:alerta_estoque "ativo" XX
echo "Tentativa 2: criando a chave primeiro e atualizando com XX:"
redis-cli SET config:alerta_estoque "desativado"
redis-cli SET config:alerta_estoque "ativo" XX
echo "Valor atual: $(redis-cli GET config:alerta_estoque)"

echo -e "\n${AMARELO}2.3 SET com KEEPTTL (Atualiza valor preservando o TTL restante):${NC}"
redis-cli SET sessao:cliente_99 "token_jwt_v1" EX 60
echo "TTL inicial: $(redis-cli TTL sessao:cliente_99)s"
sleep 1
redis-cli SET sessao:cliente_99 "token_jwt_v2_renovado" KEEPTTL
echo "TTL após atualizar mantendo KEEPTTL: $(redis-cli TTL sessao:cliente_99)s (Não perdeu o tempo!)"

echo -e "\n${AMARELO}2.4 SET com GET (Define novo valor e devolve o valor anterior atomicamente):${NC}"
echo "Comando: redis-cli SET metrica:vendas_hoje 55 GET"
redis-cli SET metrica:vendas_hoje 55 GET

echo -e "\n${AMARELO}2.5 MSET (Múltiplas chaves atômicas em uma única viagem de rede):${NC}"
echo "Comando: redis-cli MSET cotacao:dolar 5.45 cotacao:euro 5.95 cotacao:ouro 460.00"
redis-cli MSET cotacao:dolar 5.45 cotacao:euro 5.95 cotacao:ouro 460.00

# -----------------------------------------------------------------------------
echo -e "\n${NEGRITO}${CIANO}=============================================================================${NC}"
echo -e "${NEGRITO}${CIANO}PARTE 3: VARIAÇÕES AVANÇADAS DO COMANDO GET${NC}"
echo -e "${NEGRITO}${CIANO}=============================================================================${NC}"

echo -e "${AMARELO}3.1 MGET (Recuperação de múltiplas chaves em batch):${NC}"
echo "Comando: redis-cli MGET cotacao:dolar cotacao:euro cotacao:ouro chave_inexistente"
redis-cli MGET cotacao:dolar cotacao:euro cotacao:ouro chave_inexistente

echo -e "\n${AMARELO}3.2 GETDEL (Recupera e deleta na mesma operação atômica - Token de uso único):${NC}"
redis-cli SET token:pix:transacao_101 "AUTORIZADO_R\$500" EX 60
echo "1ª Leitura com GETDEL (Consome o token):"
redis-cli GETDEL token:pix:transacao_101
echo "2ª Leitura subsequente (Deve ser nil, pois foi consumido):"
redis-cli GET token:pix:transacao_101

echo -e "\n${AMARELO}3.3 GETEX (Recupera o dado e altera o tempo de expiração na leitura):${NC}"
redis-cli SET sessao:temporaria "usuario_logado" EX 10
echo "TTL antes do GETEX: $(redis-cli TTL sessao:temporaria)s"
redis-cli GETEX sessao:temporaria EX 180
echo "TTL após GETEX com EX 180: $(redis-cli TTL sessao:temporaria)s"

echo -e "\n${AMARELO}3.4 GETRANGE e STRLEN (Substrings e Tamanho em Bytes):${NC}"
redis-cli SET anuncio:topo "SUPER PROMOÇÃO IFCE TAUÁ 2026"
echo "Texto original: $(redis-cli GET anuncio:topo)"
echo "GETRANGE anuncio:topo 0 13: $(redis-cli GETRANGE anuncio:topo 0 13)"
echo "STRLEN anuncio:topo: $(redis-cli STRLEN anuncio:topo) bytes"

# -----------------------------------------------------------------------------
echo -e "\n${NEGRITO}${CIANO}=============================================================================${NC}"
echo -e "${NEGRITO}${CIANO}PARTE 4: PERSISTÊNCIA EM DISCO (RDB SNAPSHOTTING & AOF LOG)${NC}"
echo -e "${NEGRITO}${CIANO}=============================================================================${NC}"
echo -e "A memória RAM é volátil! Se o servidor desligar, os dados na RAM evaporam."
echo -e "O Redis oferece dois mecanismos complementares para gravar no disco:\n"

echo -e "${AMARELO}4.1 Inspecionando a diretiva RDB no arquivo redis.conf (CONFIG GET save):${NC}"
redis-cli CONFIG GET save
echo -e "Explicação: Os pares 'segundos mudanças' definem quando o snapshot automático é disparado."

echo -e "\n${AMARELO}4.2 Disparando Snapshot Assíncrono com BGSAVE (Background Save via fork):${NC}"
echo -e "Atenção: NUNCA use 'SAVE' em produção, pois bloqueia todas as requisições!"
echo -e "Use SEMPRE 'BGSAVE', que cria um processo filho com Copy-on-Write no Linux."
redis-cli BGSAVE

echo -e "\n${AMARELO}4.3 Verificando o timestamp do último snapshot salvo em disco (LASTSAVE):${NC}"
LAST_TS=$(redis-cli LASTSAVE)
echo -e "Timestamp Unix: $LAST_TS ($(date -d @$LAST_TS '+%d/%m/%Y %H:%M:%S' 2>/dev/null || date))"

echo -e "\n${AMARELO}4.4 Inspecionando o status do AOF (Append-Only File):${NC}"
redis-cli CONFIG GET appendonly
redis-cli CONFIG GET appendfsync
echo -e "Dica: 'appendfsync everysec' é a recomendação padrão (perda máxima de 1s de dados sob queda súbita de energia)."

# -----------------------------------------------------------------------------
echo -e "\n${NEGRITO}${CIANO}=============================================================================${NC}"
echo -e "${NEGRITO}${CIANO}PARTE 5: ESTRUTURAS NATIVAS COMPLEMENTARES${NC}"
echo -e "${NEGRITO}${CIANO}=============================================================================${NC}"

echo -e "${AMARELO}5.1 Hashes (HSET, HGETALL, HINCRBY) - Perfil de Usuário:${NC}"
redis-cli HSET user:aluno:42 nome "Francisco" matricula "20261ADS001" pontos 80
redis-cli HINCRBY user:aluno:42 pontos 20
redis-cli HGETALL user:aluno:42

echo -e "\n${AMARELO}5.2 Lists (LPUSH, LTRIM, LRANGE) - Histórico das Últimas 3 Buscas:${NC}"
redis-cli DEL busca:historico:user_42 > /dev/null
redis-cli LPUSH busca:historico:user_42 "curso python" "docker compose" "nosql redis" "mongodb atlas"
redis-cli LTRIM busca:historico:user_42 0 2
redis-cli LRANGE busca:historico:user_42 0 -1

echo -e "\n${AMARELO}5.3 Sets (SADD, SINTER) - Tags Únicas e Filtro por Interseção:${NC}"
redis-cli DEL tags:prodA tags:prodB > /dev/null
redis-cli SADD tags:prodA "tecnologia" "portatil" "bivolt"
redis-cli SADD tags:prodB "eletro" "portatil" "bivolt"
echo "Tags em comum entre Produto A e Produto B (SINTER):"
redis-cli SINTER tags:prodA tags:prodB

echo -e "\n${AMARELO}5.4 Sorted Sets (ZADD, ZINCRBY, ZREVRANGE) - Leaderboard de Buscas:${NC}"
redis-cli DEL ranking:buscas > /dev/null
redis-cli ZADD ranking:buscas 100 "notebook" 150 "smartphone" 80 "tablet"
redis-cli ZINCRBY ranking:buscas 85 "notebook"
echo "Top 3 termos mais buscados (ZREVRANGE com pontuação):"
redis-cli ZREVRANGE ranking:buscas 0 2 WITHSCORES

echo -e "\n${VERDE}${NEGRITO}=============================================================================${NC}"
echo -e "${VERDE}${NEGRITO}🎉 PARABÉNS! TODOS OS COMANDOS ESSENCIAIS FORAM DEMONSTRADOS COM SUCESSO!${NC}"
echo -e "${VERDE}${NEGRITO}=============================================================================${NC}"
