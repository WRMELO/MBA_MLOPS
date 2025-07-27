# interface_streamlit_v1.py
# Interface Streamlit que envia dados para a API e exibe a resposta
import streamlit as st
import requests

API_URL = "http://localhost:8000/predict"

st.title("Classificador de Crédito – QuantumFinance")
st.write("Preencha as informações abaixo para obter a previsão:")

with st.form("formulario_credit_score"):
    Age = st.number_input("Idade (Age)", min_value=18, max_value=100, value=35)
    Annual_Income = st.number_input("Renda Anual", value=65000.0)
    Monthly_Inhand_Salary = st.number_input("Salário Mensal Líquido", value=5000.0)
    Num_Bank_Accounts = st.number_input("Nº Contas Bancárias", min_value=0, value=3)
    Num_Credit_Card = st.number_input("Nº Cartões de Crédito", min_value=0, value=2)
    Interest_Rate = st.number_input("Taxa de Juros (%)", value=13.0)
    Delay_from_due_date = st.number_input("Dias Médio de Atraso", value=5)
    Num_of_Delayed_Payment = st.number_input("Nº Pagamentos Atrasados", value=1)
    Changed_Credit_Limit = st.number_input("Alteração Limite Crédito", value=15000.0)
    Num_Credit_Inquiries = st.number_input("Nº Consultas de Crédito", value=2.0)
    Credit_History_Age = st.text_input("Histórico de Crédito (ex: '8 Years and 2 Months')", value="8 Years and 2 Months")
    Total_EMI_per_month = st.number_input("EMI Mensal Total", value=300.0)
    Amount_invested_monthly = st.number_input("Valor Investido Mensal", value=200.0)
    Monthly_Balance = st.number_input("Saldo Mensal Médio", value=1500.0)
    Occupation = st.selectbox("Ocupação", ["Scientist","Teacher","Engineer","Entrepreneur","Developer","Lawyer","Mechanic","Media_Manager","Doctor","Manager","Journalist","Musician","Writer","Architect","Other"])
    Credit_Mix = st.selectbox("Mix de Crédito", ["Standard","Good","Bad"])
    Payment_of_Min_Amount = st.selectbox("Pagamento Mínimo", ["Yes","No","NM"])
    Payment_Behaviour = st.selectbox("Comportamento de Pagamento", ["High_spent_Medium_value_payments","Low_spent_Small_value_payments","Other"])
    Type_of_Loan = st.selectbox("Tipo de Empréstimo", ["Auto Loan","Credit-Builder Loan","Debt Consolidation Loan","Home Equity Loan","Mortgage Loan","Not Specified","Payday Loan","Personal Loan","Student Loan"])
    Num_of_Loan = st.number_input("Nº de Empréstimos", value=1)
    Outstanding_Debt = st.number_input("Dívida Atual", value=7500.0)
    Credit_Utilization_Ratio = st.number_input("Utilização de Crédito (%)", value=35.0)

    submitted = st.form_submit_button("Enviar e Obter Previsão")

    if submitted:
        payload = {
            "Age": Age,
            "Annual_Income": Annual_Income,
            "Monthly_Inhand_Salary": Monthly_Inhand_Salary,
            "Num_Bank_Accounts": Num_Bank_Accounts,
            "Num_Credit_Card": Num_Credit_Card,
            "Interest_Rate": Interest_Rate,
            "Delay_from_due_date": Delay_from_due_date,
            "Num_of_Delayed_Payment": Num_of_Delayed_Payment,
            "Changed_Credit_Limit": Changed_Credit_Limit,
            "Num_Credit_Inquiries": Num_Credit_Inquiries,
            "Credit_History_Age": Credit_History_Age,
            "Total_EMI_per_month": Total_EMI_per_month,
            "Amount_invested_monthly": Amount_invested_monthly,
            "Monthly_Balance": Monthly_Balance,
            "Occupation": Occupation,
            "Credit_Mix": Credit_Mix,
            "Payment_of_Min_Amount": Payment_of_Min_Amount,
            "Payment_Behaviour": Payment_Behaviour,
            "Type_of_Loan": Type_of_Loan,
            "Num_of_Loan": Num_of_Loan,
            "Outstanding_Debt": Outstanding_Debt,
            "Credit_Utilization_Ratio": Credit_Utilization_Ratio
        }

        try:
            response = requests.post(API_URL, json=payload)
            if response.status_code == 200:
                resultado = response.json()
                st.success(f"Classe prevista: {resultado['classe_prevista']}")
            else:
                st.error(f"Erro na previsão: {response.text}")
        except Exception as e:
            st.error(f"Erro ao conectar à API: {e}")
