# ETAPA: APP STREAMLIT SINCRONIZADO COM PIPELINE FINAL

import streamlit as st
import requests

st.title("Classificador de Crédito — QuantumFinance")

# 1️⃣ Coleta dos dados brutos
dados = {
    "Age_Binned": st.selectbox("Faixa Etária", ["Jovem", "Adulto", "Idoso", "Desconhecido"]),
    "Amount_invested_monthly_Binned": st.selectbox("Investimento Mensal (Binned)", ["Baixo", "Moderado", "Alto", "Desconhecido"]),
    "Annual_Income_Binned": st.selectbox("Renda Anual (Binned)", ["Baixo", "Moderado", "Alto", "Desconhecido"]),
    "Changed_Credit_Limit_Binned": st.selectbox("Alteração de Limite (Binned)", ["Pequena", "Moderada", "Alta", "Desconhecida"]),
    "Credit_History_Age_Binned": st.selectbox("Tempo de Crédito (Binned)", ["Curto", "Médio", "Longo"]),
    "Credit_History_Age_Months": st.number_input("Histórico de Crédito (em meses)", min_value=0.0),
    "Credit_Mix": st.selectbox("Perfil de Crédito", ["Bad", "Standard", "Good", "Unknown"]),
    "Credit_Utilization_Ratio_Binned": st.selectbox("Utilização de Crédito", ["Baixo", "Moderado", "Alto"]),
    "Delay_from_due_date_Binned": st.selectbox("Dias de Atraso", ["0-5", "6-10", "11-20", "21-30", "Acima de 30"]),
    "Interest_Rate_Binned": st.selectbox("Taxa de Juros", ["Baixa", "Média", "Alta"]),
    "Monthly_Balance_Binned": st.selectbox("Balanço Mensal", ["Negativo", "Estável", "Positivo"]),
    "Monthly_Inhand_Salary_Binned": st.selectbox("Salário na Mão", ["Baixo", "Médio", "Alto"]),
    "Num_Bank_Accounts_Binned": st.selectbox("Contas Bancárias", ["1-2", "3-5", "6-8", "9+"]),
    "Num_Credit_Card_Binned": st.selectbox("Cartões de Crédito", ["1-2", "3-4", "5-6", "7+"]),
    "Num_Credit_Inquiries_Binned": st.selectbox("Consultas de Crédito", ["0-2", "3-5", "6-8", "9+"]),
    "Num_of_Delayed_Payment_Binned": st.selectbox("Pagamentos Atrasados", ["Nenhum", "Poucos", "Muitos", "Extremo"]),
    "Num_of_Loan_Binned": st.selectbox("Número de Empréstimos", ["1-2", "3-4", "5-6", "7+"]),
    "Occupation": st.selectbox("Ocupação", ["Scientist", "Teacher", "Engineer", "Entrepreneur", "Doctor", "Lawyer", "Artist", "Manager", "Writer", "Mechanic", "Journalist", "Musician", "Architect", "Developer", "Media_Manager", "Other"]),
    "Outstanding_Debt_Binned": st.selectbox("Dívida Atual", ["Baixa", "Moderada", "Alta", "Muito Alta"]),
    "Payment_of_Min_Amount": st.selectbox("Pagou o mínimo?", ["Yes", "No", "Unknown"]),
    "Total_EMI_per_month_Binned": st.selectbox("EMI Total por Mês", ["Baixo", "Moderado", "Alto"]),
    "Type_of_Loan": st.text_input("Tipo(s) de Empréstimo (string completa)", "Student Loan, Personal Loan")
}

# 2️⃣ Envio para API
if st.button("Classificar"):
    st.markdown("**📤 Dados enviados para a API:**")
    st.json(dados)

    try:
        response = requests.post(
            "http://localhost:8000/predict",
            json={"data": dados},
            headers={"x-api-key": "quantum123"}
        )
        if response.status_code == 200:
            st.success(f"🎯 Predição: {response.json()['prediction']}")
        else:
            st.error(f"❌ Erro da API: {response.text}")
    except Exception as e:
        st.error(f"❌ Erro de conexão com a API: {e}")
