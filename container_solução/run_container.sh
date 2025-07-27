#!/bin/bash
# Script para build e execução do container QuantumFinance

cd "$(dirname "$0")/.."

IMAGE_NAME="quantumfinance:latest"
CONTAINER_NAME="quantumfinance_app"

echo "🔹 Buildando imagem..."
docker build -t $IMAGE_NAME -f container_solução/Dockerfile .

if [ "$(docker ps -aq -f name=$CONTAINER_NAME)" ]; then
    echo "🔹 Removendo container antigo..."
    docker rm -f $CONTAINER_NAME
fi

echo "🔹 Subindo container..."
docker compose -f container_solução/docker-compose.yml up -d

echo "✅ Container $CONTAINER_NAME rodando!"
echo "👉 API: http://localhost:8000/docs"
echo "👉 Streamlit: será executado manualmente com: streamlit run src/ativos/interface_streamlit_v1.py"
