# cf_app.py

# 1️⃣ Imports
import streamlit as st
import requests
from cf_transform import transform_input, gerar_payload_final
from mapping import UI_LABEL_TO_VAR, OPTIONS_MAP

# 2️⃣ Configurações da API
API_URL = "http://localhost:8000/predict"
API_KEY = "quantum123"

# 3️⃣ Título e instruções
st.title("Classificador de Score de Crédito")
st.write("Preencha os campos abaixo com os dados do cliente para obter a previsão do modelo.")

# 4️⃣ Construção dinâmica dos campos da UI
user_inputs = {}

for label in UI_LABEL_TO_VAR:
    var_name = UI_LABEL_TO_VAR[label]

    # Campo com opções discretas
    if var_name in OPTIONS_MAP:
        options = list(OPTIONS_MAP[var_name].keys())
        default = options[0]
        selected = st.selectbox(label, options, index=options.index(default))
        user_inputs[label] = selected
    else:
        # Campo numérico ou texto livre
        user_inputs[label] = st.text_input(label)

# 5️⃣ Botão de predição
if st.button("Executar Predição"):
    try:
        # 🔁 Etapa 1: traduz e codifica os 21 campos
        codificados = transform_input(user_inputs)

        # 🔁 Etapa 2: aplica pipeline para gerar os 92 campos
        payload = gerar_payload_final(codificados)

        # 🔁 Etapa 3: envia para API
        headers = {"x-api-key": API_KEY}
        response = requests.post(API_URL, json=payload, headers=headers)

        # 🔁 Etapa 4: resposta
        if response.status_code == 200:
            result = response.json()
            st.success(f"Resultado da predição: {result['predictions'][0]}")
        else:
            st.error(f"Erro {response.status_code}: {response.text}")

    except Exception as e:
        st.error(f"Erro durante a predição: {e}")
