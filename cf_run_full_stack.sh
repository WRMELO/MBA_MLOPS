#!/bin/bash

# cf_run_full_stack.sh

echo "🚀 Iniciando stack FastAPI + Streamlit..."

# 1️⃣ Libera a porta 8000 se estiver ocupada (FastAPI)
PID_API=$(lsof -t -i:8000)
if [ -n "$PID_API" ]; then
  echo "🔴 Encerrando processo anterior na porta 8000 (PID: $PID_API)..."
  kill -9 $PID_API
  sleep 1
fi

# 2️⃣ Verifica dependências
if ! command -v uvicorn &> /dev/null; then
  echo "❌ uvicorn não encontrado. Instale com: pip install uvicorn[standard]"
  exit 1
fi

if ! command -v streamlit &> /dev/null; then
  echo "❌ streamlit não encontrado. Instale com: pip install streamlit"
  exit 1
fi

# 3️⃣ Inicia API FastAPI em segundo plano
echo "🟢 Iniciando FastAPI com uvicorn..."
nohup uvicorn cf_service:app --host 0.0.0.0 --port 8000 > api_log.txt 2>&1 &
API_PID=$!

# 4️⃣ Aguarda subida da API
sleep 2

# 5️⃣ Inicia Streamlit
echo "🟢 Iniciando Streamlit..."
streamlit run cf_app.py

# 6️⃣ Finaliza API ao sair do Streamlit
echo "🛑 Encerrando API FastAPI (PID: $API_PID)..."
kill $API_PID
