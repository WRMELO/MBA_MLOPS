import streamlit as st
import requests
import json

from cf_transform import gerar_payload_final, OPTIONS_MAP

API_URL = "http://localhost:8000/predict"

st.set_page_config(page_title="Classificador de Crédito - RF v1", layout="centered")
st.title("Classificador de Risco de Crédito")
st.markdown("Preencha os campos abaixo para prever o risco de crédito do cliente.")

with st.form("credit_form"):
    age = st.number_input("Age", min_value=18, max_value=100, value=35)
    annual_income = st.number_input("Annual_Income", min_value=10000, max_value=500000, value=85000)
    monthly_salary = st.number_input("Monthly_Inhand_Salary", min_value=500, max_value=30000, value=5000)

    occupation = st.selectbox("Occupation", list(OPTIONS_MAP["Occupation"].keys()))
    credit_mix = st.selectbox("Credit_Mix", list(OPTIONS_MAP["Credit_Mix"].keys()))
    payment_min_amount = st.selectbox("Payment_of_Min_Amount", list(OPTIONS_MAP["Payment_of_Min_Amount"].keys()))
    type_of_loan = st.selectbox("Type_of_Loan", list(OPTIONS_MAP["Type_of_Loan"].keys()))

    num_of_loan = st.number_input("Num_of_Loan", min_value=0, max_value=20, value=3)
    num_credit_cards = st.number_input("Num_Credit_Card", min_value=0, max_value=15, value=2)
    outstanding_debt = st.number_input("Outstanding_Debt", min_value=0.0, max_value=100000.0, value=15000.0)
    credit_util_ratio = st.number_input("Credit_Utilization_Ratio", min_value=0.0, max_value=100.0, value=42.0)
    interest_rate = st.number_input("Interest_Rate", min_value=0.0, max_value=60.0, value=12.5)
    delay_days = st.number_input("Delay_from_due_date", min_value=0, max_value=90, value=10)

    submitted = st.form_submit_button("Enviar")

    if submitted:
        raw_dict = {
            "Age": age,
            "Annual_Income": annual_income,
            "Monthly_Inhand_Salary": monthly_salary,
            "Occupation": occupation,
            "Credit_Mix": credit_mix,
            "Payment_of_Min_Amount": payment_min_amount,
            "Type_of_Loan": type_of_loan,
            "Num_of_Loan": num_of_loan,
            "Num_Credit_Card": num_credit_cards,
            "Outstanding_Debt": outstanding_debt,
            "Credit_Utilization_Ratio": credit_util_ratio,
            "Interest_Rate": interest_rate,
            "Delay_from_due_date": delay_days
        }

        try:
            payload_final = gerar_payload_final(raw_dict)
            response = requests.post(API_URL, json=payload_final)

            if response.status_code == 200:
                prediction = response.json()["prediction"]
                st.success(f"Previsão do modelo: {prediction}")
            else:
                st.error(f"Erro na API: {response.status_code} - {response.text}")
        except Exception as e:
            st.error(f"Erro ao transformar ou enviar os dados: {str(e)}")
