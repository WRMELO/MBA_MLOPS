#!/bin/bash

# 🔧 ETAPA: Orquestração profissional da API e Streamlit com logs e separação de processos

echo "🚀 Iniciando processo..."

# 1️⃣ Verifica e encerra qualquer processo anterior na porta 8000 (API)
PID_API=$(lsof -t -i:8000)
if [ -n "$PID_API" ]; then
  echo "🔴 Encerrando processo API existente (PID $PID_API)..."
  kill -9 $PID_API
  sleep 1
fi

# 2️⃣ Inicia API com uvicorn (em segundo plano, log redirecionado)
echo "🟢 Iniciando FastAPI com uvicorn..."
cd /workspace
nohup uvicorn api:app --host 0.0.0.0 --port 8000 > api_log.txt 2>&1 &

# 3️⃣ Aguarda a subida do serviço
sleep 3

# 4️⃣ Inicia Streamlit apontando para app
echo "🟢 Iniciando Streamlit..."
nohup streamlit run /workspace/streamlit_app.py > streamlit_log.txt 2>&1 &

echo "✅ Ambos os serviços foram iniciados."
echo "🌐 Acesse o Streamlit pelo navegador (porta padrão 8501)"
