#!/bin/bash

# cf_run_api.sh

echo "🔧 Iniciando API FastAPI (cf_service.py)..."

# Verifica se uvicorn está instalado
if ! command -v uvicorn &> /dev/null
then
    echo "❌ uvicorn não encontrado. Instale com: pip install uvicorn[standard]"
    exit 1
fi

# Executa a API
uvicorn cf_service:app --host 0.0.0.0 --port 8000 --reload
