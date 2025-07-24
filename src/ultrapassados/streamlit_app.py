import streamlit as st
import pandas as pd
import requests

from converter import mapeamentos, converter_dados_para_api

st.set_page_config(
    page_title="Interface de Predição – Modelo Random Forest v1-final",
    layout="wide"
)

st.title("Interface de Predição – Modelo Random Forest v1-final")
st.write("Este app envia dados para a API FastAPI e exibe a predição retornada.")

# 1️⃣ Upload do CSV
uploaded_file = st.file_uploader(
    "Envie um arquivo CSV com as colunas corretas",
    type="csv",
    help="O CSV deve conter exatamente os nomes de coluna que o modelo espera (ex: Age_Binned, Credit_Mix, etc.)"
)

if uploaded_file is not None:
    # 2️⃣ Lê e exibe as primeiras linhas
    df = pd.read_csv(uploaded_file)
    st.write("📄 Dados recebidos (primeiras linhas):")
    st.dataframe(df.head())

    # 3️⃣ Botão para executar predição
    if st.button("🚀 Executar predição"):
        # Converte cada linha via nosso conversor
        records = df.to_dict(orient="records")
        payload = {
            "data": [converter_dados_para_api(rec) for rec in records]
        }

        try:
            resp = requests.post(
                "http://localhost:8000/predict",
                json=payload,
                headers={"x-api-key": "quantum123"},
                timeout=10
            )
        except Exception as e:
            st.error(f"❌ Falha ao chamar API: {e}")
        else:
            if resp.status_code == 200:
                preds = resp.json().get("predictions", [])
                # Exibe num DataFrame lado a lado
                resultado = pd.DataFrame({
                    "input_index": list(range(len(preds))),
                    "prediction": preds
                })
                st.write("📊 Predições retornadas:")
                st.dataframe(resultado)
            else:
                st.error(f"❌ Erro {resp.status_code}: {resp.text}")

else:
    st.info("Aguardando envio de um arquivo CSV…")
