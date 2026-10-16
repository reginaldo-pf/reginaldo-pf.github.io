#!/usr/bin/env bash
# ==============================================================================
# Script de Inicialização do Worker de Pedidos FastCommerce (Aula 05 - BDNR)
# ==============================================================================

VERDE='\033[0;32m'
AMARELO='\033[1;33m'
VERMELHO='\033[0;31m'
AZUL='\033[0;34m'
NC='\033[0m'

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

exec "$VENV_PY" worker_pedidos.py
