# 🔧 ETAPA: Integração do dicionário de mapeamento e função de conversão no Streamlit

import streamlit as st
import requests

# 1️⃣ Dicionário de mapeamentos para valores categóricos
mapeamentos = {
    "Age_Binned": {
        "20-30": 0, "30-40": 1, "40-50": 2, "50-60": 3, "60-70": 4, "70+": 5
    },
    "Amount_invested_monthly_Binned": {
        "0-500": 0, "500-1000": 1, "1000-1500": 2, "1500-2000": 3, "2000+": 4
    },
    "Annual_Income_Binned": {
        "0-50K": 0, "50K-100K": 1, "100K-150K": 2, "150K-200K": 3, "200K+": 4
    },
    "Changed_Credit_Limit_Binned": {
        "0-2K": 0, "2K-5K": 1, "5K-10K": 2, "10K+": 3
    },
    "Credit_History_Age_Binned": {
        "0-5Y": 0, "5Y-10Y": 1, "10Y-15Y": 2, "15Y+": 3
    },
    "Credit_Mix": {
        "Bad": 0, "Standard": 1, "Good": 2
    },
    "Credit_Utilization_Ratio_Binned": {
        "0-20%": 0, "20-40%": 1, "40-60%": 2, "60-80%": 3, "80%+": 4
    },
    "Delay_from_due_date_Binned": {
        "0-10": 0, "10-20": 1, "20-30": 2, "30+": 3
    },
    "Interest_Rate_Binned": {
        "0-5%": 0, "5-10%": 1, "10-15%": 2, "15%+": 3
    },
    "Monthly_Balance_Binned": {
        "0-5K": 0, "5K-10K": 1, "10K-15K": 2, "15K+": 3
    },
    "Monthly_Inhand_Salary_Binned": {
        "0-5K": 0, "5K-10K": 1, "10K-15K": 2, "15K+": 3
    },
    "Num_Bank_Accounts_Binned": {
        "0-2": 0, "2-4": 1, "4-6": 2, "6+": 3
    },
    "Num_Credit_Card_Binned": {
        "0-1": 0, "2-3": 1, "4+": 2
    },
    "Num_Credit_Inquiries_Binned": {
        "0-1": 0, "2-3": 1, "4+": 2
    },
    "Num_of_Delayed_Payment_Binned": {
        "0": 0, "1-3": 1, "4-6": 2, "7+": 3
    },
    "Num_of_Loan_Binned": {
        "0": 0, "1-2": 1, "3-4": 2, "5+": 3
    },
    "Occupation": {
        "Scientist": 0, "Teacher": 1, "Engineer": 2, "Entrepreneur": 3,
        "Doctor": 4, "Lawyer": 5, "Artist": 6
    },
    "Outstanding_Debt_Binned": {
        "0-10K": 0, "10K-20K": 1, "20K-30K": 2, "30K+": 3
    },
    "Payment_of_Min_Amount": {
        "No": 0, "Yes": 1
    },
    "Total_EMI_per_month_Binned": {
        "0-2K": 0, "2K-4K": 1, "4K-6K": 2, "6K+": 3
    },
    "Type_of_Loan": {
        "Home Loan": 0, "Credit-Builder Loan": 1, "Auto Loan": 2,
        "Personal Loan": 3, "Student Loan": 4, "Payday Loan": 5,
        "Mortgage Loan": 6, "Not Specified": 7
    }
}

# 2️⃣ Função para converter os dados da UI para os inteiros da API
def converter_dados_para_api(dados_ui):
    dados_convertidos = {}
    for campo, valor in dados_ui.items():
        if campo in mapeamentos:
            dados_convertidos[campo] = mapeamentos[campo].get(valor)
        else:
            dados_convertidos[campo] = valor
    return dados_convertidos

# 3️⃣ Interface do Streamlit
st.title("Classificador de Crédito")

with st.form("input_form"):
    dados = {}
    dados["Age_Binned"] = st.selectbox("Idade", list(mapeamentos["Age_Binned"].keys()))
    dados["Occupation"] = st.selectbox("Ocupação", list(mapeamentos["Occupation"].keys()))
    dados["Credit_Mix"] = st.selectbox("Perfil de Crédito", list(mapeamentos["Credit_Mix"].keys()))
    dados["Payment_of_Min_Amount"] = st.selectbox("Pagamento Mínimo", list(mapeamentos["Payment_of_Min_Amount"].keys()))
    dados["Credit_History_Age"] = st.number_input("Idade do Histórico de Crédito", min_value=0)
    dados["Monthly_Inhand_Salary_Binned"] = st.selectbox("Salário Mensal", list(mapeamentos["Monthly_Inhand_Salary_Binned"].keys()))
    dados["Num_Credit_Card_Binned"] = st.selectbox("Nº de Cartões", list(mapeamentos["Num_Credit_Card_Binned"].keys()))
    dados["Num_of_Delayed_Payment_Binned"] = st.selectbox("Pagamentos Atrasados", list(mapeamentos["Num_of_Delayed_Payment_Binned"].keys()))
    dados["Annual_Income_Binned"] = st.selectbox("Renda Anual", list(mapeamentos["Annual_Income_Binned"].keys()))
    dados["Outstanding_Debt_Binned"] = st.selectbox("Dívida", list(mapeamentos["Outstanding_Debt_Binned"].keys()))
    dados["Interest_Rate_Binned"] = st.selectbox("Taxa de Juros", list(mapeamentos["Interest_Rate_Binned"].keys()))
    dados["Changed_Credit_Limit_Binned"] = st.selectbox("Mudança de Limite", list(mapeamentos["Changed_Credit_Limit_Binned"].keys()))
    dados["Credit_History_Age_Binned"] = st.selectbox("Histórico Binned", list(mapeamentos["Credit_History_Age_Binned"].keys()))
    dados["Credit_Utilization_Ratio_Binned"] = st.selectbox("Utilização de Crédito", list(mapeamentos["Credit_Utilization_Ratio_Binned"].keys()))
    dados["Delay_from_due_date_Binned"] = st.selectbox("Dias de Atraso", list(mapeamentos["Delay_from_due_date_Binned"].keys()))
    dados["Monthly_Balance_Binned"] = st.selectbox("Balanço Mensal", list(mapeamentos["Monthly_Balance_Binned"].keys()))
    dados["Num_Bank_Accounts_Binned"] = st.selectbox("Nº de Contas Bancárias", list(mapeamentos["Num_Bank_Accounts_Binned"].keys()))
    dados["Num_Credit_Inquiries_Binned"] = st.selectbox("Consultas de Crédito", list(mapeamentos["Num_Credit_Inquiries_Binned"].keys()))
    dados["Num_of_Loan_Binned"] = st.selectbox("Nº de Empréstimos", list(mapeamentos["Num_of_Loan_Binned"].keys()))
    dados["Total_EMI_per_month_Binned"] = st.selectbox("EMI Mensal", list(mapeamentos["Total_EMI_per_month_Binned"].keys()))
    dados["Type_of_Loan"] = st.selectbox("Tipo de Empréstimo", list(mapeamentos["Type_of_Loan"].keys()))
    dados["Amount_invested_monthly_Binned"] = st.selectbox("Investimento Mensal", list(mapeamentos["Amount_invested_monthly_Binned"].keys()))

    submitted = st.form_submit_button("Enviar")

# 4️⃣ Envia os dados convertidos para a API
if submitted:
    url = "http://localhost:8000/predict"
    headers = {"x-api-key": "quantum123"}
    dados_convertidos = converter_dados_para_api(dados)

    st.write("📦 Dados enviados para a API:")
    st.json(dados_convertidos)

    # Envia com a chave "data" (estrutura esperada pela API)
    response = requests.post(url, json={"data": dados_convertidos}, headers=headers)

    # Aqui dentro está tudo OK
    if response.status_code == 200:
        st.success(f"✅ Predição: {response.json()['prediction']}")
    else:
        st.error(f"❌ Erro {response.status_code}: {response.text}")
