#!/bin/bash
# cf_run_api.sh
# Executa o serviço FastAPI apontando para o app correto

echo "🚀 Iniciando API FastAPI em: src.ativos.api_preditor_v1"

uvicorn src.ativos.api_preditor_v1:app \
  --host 0.0.0.0 \
  --port 8000 \
  --reload
