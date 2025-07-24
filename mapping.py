# mapping.py

# Dicionário 1: rótulos da UI (dropdowns) → nomes técnicos esperados pelo pipeline
UI_LABEL_TO_VAR = {
    "Idade": "Age",
    "Mês da Análise": "Month",
    "Ocupação": "Occupation",
    "Renda Anual": "Annual_Income_Binned",
    "Salário Mensal em Mãos": "Monthly_Inhand_Salary_Binned",
    "Saldo Mensal": "Monthly_Balance_Binned",
    "Taxa de Utilização de Crédito": "Credit_Utilization_Ratio_Binned",
    "Número de Cartões": "Num_Credit_Card_Binned",
    "Número de Contas Bancárias": "Num_Bank_Accounts_Binned",
    "Número de Consultas de Crédito": "Num_Credit_Inquiries_Binned",
    "Número de Empréstimos": "Num_of_Loan_Binned",
    "Histórico de Pagamentos Atrasados": "Num_of_Delayed_Payment_Binned",
    "Atraso após o Vencimento": "Delay_from_due_date_Binned",
    "Mudança no Limite de Crédito": "Changed_Credit_Limit_Binned",
    "Valor Investido por Mês": "Amount_invested_monthly_Binned",
    "Pagamento do Valor Mínimo": "Payment_of_Min_Amount",
    "Taxa de Juros": "Interest_Rate_Binned",
    "Mix de Crédito": "Credit_Mix",
    "Dívida em Aberto": "Outstanding_Debt_Binned",
    "EMI Total por Mês": "Total_EMI_per_month_Binned",
    "Idade do Histórico de Crédito": "Credit_History_Age_Binned"
}

# Dicionário 2: valores discretos (UI) → codificações numéricas esperadas
OPTIONS_MAP = {
    "Payment_of_Min_Amount": {
        "Yes": 1,
        "No": 0,
        "NM": 2
    },
    "Credit_Mix": {
        "Standard": 1,
        "Good": 2,
        "Bad": 0
    },
    "Occupation": {
        "Scientist": 15,
        "Teacher": 19,
        "Engineer": 6,
        "Entrepreneur": 7,
        "Lawyer": 10,
        "Doctor": 5,
        "Manager": 11,
        "Accountant": 0,
        "Writer": 20,
        "Mechanic": 12,
        "Media_Manager": 13,
        "Developer": 4,
        "Musician": 14,
        "Journalist": 9,
        "Architect": 1,
        "Pilot": 16,
        "Flight_Attendant": 8,
        "Graphic_Designer": 17,
        "Financial_Analyst": 3,
        "Interior_Designer": 18,
        "Civil_servant": 2
    }
}
