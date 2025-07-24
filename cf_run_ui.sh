#!/bin/bash

# cf_run_ui.sh

echo "🟢 Iniciando interface Streamlit (cf_app.py)..."

# Verifica se streamlit está instalado
if ! command -v streamlit &> /dev/null
then
    echo "❌ streamlit não encontrado. Instale com: pip install streamlit"
    exit 1
fi

# Executa a UI
streamlit run cf_app.py
