#!/usr/bin/env bash
# ==============================================================================
# Script de Inicialização do Laboratório ShopGrids (Aula 05 - BDNR)
# Exemplo Prático: Padrão Cache-Aside e Invalidação com TTL no Redis
# ==============================================================================

VERDE='\033[0;32m'
AMARELO='\033[1;33m'
VERMELHO='\033[0;31m'
AZUL='\033[0;34m'
NC='\033[0m'

echo -e "${AZUL}==============================================================================${NC}"
echo -e "${AZUL}   INICIANDO LABORATÓRIO SHOPGRIDS: CACHE-ASIDE COM REDIS (AULA 05 - IFCE)    ${NC}"
echo -e "${AZUL}==============================================================================${NC}"

# 1. Localizar o ambiente virtual Python (.venv)
VENV_PY=""
if [ -f ".venv/bin/python" ]; then
    VENV_PY=".venv/bin/python"
elif [ -f "../.venv/bin/python" ]; then
    VENV_PY="../.venv/bin/python"
elif [ -f "../../Aula_01/.venv/bin/python" ]; then
    VENV_PY="../../Aula_01/.venv/bin/python"
elif command -v python3 &> /dev/null; then
    VENV_PY="python3"
fi

if [ -z "$VENV_PY" ]; then
    echo -e "${VERMELHO}✗ Erro: Python 3 não encontrado!${NC}"
    exit 1
fi

echo -e "${VERDE}✓ Interpretador Python:${NC} $VENV_PY"

# 2. Verificar se o Redis está em execução na porta 6379
echo -ne "${AMARELO}⚙ Verificando conexão com o Redis (localhost:6379)... ${NC}"
if command -v redis-cli &> /dev/null && redis-cli ping &> /dev/null; then
    echo -e "${VERDE}ONLINE!${NC}"
else
    REDIS_TEST=$($VENV_PY -c "import redis; r=redis.Redis(); print(r.ping())" 2> /dev/null)
    if [ "$REDIS_TEST" == "True" ]; then
        echo -e "${VERDE}ONLINE!${NC}"
    else
        echo -e "${AMARELO}AVISO: Redis não detectado na porta 6379.${NC}"
        echo -e "  Para iniciar o Redis, abra outro terminal e execute:"
        echo -e "    ${AZUL}redis-server${NC} (ou ${AZUL}docker compose up -d${NC})"
    fi
fi

# 3. Executar o servidor Web Flask
echo -e "\n${VERDE}🚀 Subindo API e Painel ShopGrids em http://localhost:5000 ...${NC}"
echo -e "${AZUL}   Endpoint do vídeo: http://localhost:5000/categories/featured${NC}\n"

exec "$VENV_PY" app.py
