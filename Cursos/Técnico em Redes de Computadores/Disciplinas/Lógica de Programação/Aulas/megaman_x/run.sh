#!/usr/bin/env bash
# Script para inicializar o jogo Mega Man X
cd "$(dirname "$0")"

# Localiza o Python do ambiente virtual
if [ -f "../.venv/bin/python" ]; then
    PYTHON_EXEC="../.venv/bin/python"
elif [ -f ".venv/bin/python" ]; then
    PYTHON_EXEC=".venv/bin/python"
elif command -v python3 &> /dev/null; then
    PYTHON_EXEC="python3"
else
    echo "Erro: Python 3 não encontrado!"
    exit 1
fi

echo "Iniciando Mega Man X..."
exec "$PYTHON_EXEC" main.py
