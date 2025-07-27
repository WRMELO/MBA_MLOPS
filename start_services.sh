#!/bin/bash
# Script para iniciar API e Streamlit dentro do container quantumfinance_app
# Corrigido para definir PYTHONPATH e evitar ModuleNotFoundError

CONTAINER_NAME="quantumfinance_app"

echo "🔹 Verificando se o container $CONTAINER_NAME está ativo..."
if [ -z "$(docker ps -q -f name=$CONTAINER_NAME)" ]; then
    echo "🚫 Container $CONTAINER_NAME não está rodando. Suba-o primeiro com:"
    echo "   ./container_solução/run_container.sh"
    exit 1
fi

echo "✅ Container está ativo. Iniciando serviços com PYTHONPATH ajustado..."

# 1. Inicia API FastAPI em background dentro do container
docker exec -d $CONTAINER_NAME bash -c \
"export PYTHONPATH=/workspace && nohup uvicorn src.ativos.api_preditor_v1:app --host 0.0.0.0 --port 8000 > /workspace/api.log 2>&1 &"

echo "✅ API FastAPI iniciada em http://localhost:8080/docs"

# 2. Inicia Streamlit em background dentro do container
docker exec -d $CONTAINER_NAME bash -c \
"export PYTHONPATH=/workspace && nohup streamlit run src/ativos/interface_streamlit_v1.py --server.port 8501 --server.address 0.0.0.0 > /workspace/streamlit.log 2>&1 &"

echo "✅ Streamlit iniciado em http://localhost:8600"
echo "🔹 Logs disponíveis dentro do container em: /workspace/api.log e /workspace/streamlit.log"
