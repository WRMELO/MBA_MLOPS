# streamlit_app.py

import streamlit as st
import pandas as pd
import requests

API_URL = "http://127.0.0.1:8000/predict"

st.title("Interface de Predição - Modelo Random Forest v1-final")

st.markdown("Este app envia dados para a API FastAPI e exibe a predição retornada.")

# 1. Upload de CSV
uploaded_file = st.file_uploader("Envie um arquivo CSV com as colunas corretas", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write("Pré-visualização dos dados enviados:")
    st.dataframe(df.head())

    if st.button("Enviar à API para predição"):
        try:
            payload = {"data": df.to_dict(orient="records")}
            response = requests.post(API_URL, json=payload)

            if response.status_code == 200:
                result = response.json()
                st.success("Predição realizada com sucesso.")
                st.json(result)
            else:
                st.error(f"Erro {response.status_code}: {response.text}")
        except Exception as e:
            st.error(f"Erro ao conectar com a API: {e}")
else:
    st.info("Aguardando envio de um CSV...")
