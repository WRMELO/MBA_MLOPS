# test_api.py

import requests
import json

# 1. Define URL da API local
url = "http://127.0.0.1:8000/predict"

# 2. Exemplo de input no mesmo formato do input_example exportado
payload = {
    "data": [
        {
            "Age": 35.0,
            "Age_Binned": "Adulto",
            "Amount_invested_monthly": 100.0,
            "Amount_invested_monthly_Binned": "Baixo",
            "Annual_Income": 40000.0,
            "Annual_Income_Binned": "Média",
            "Changed_Credit_Limit": 12.0,
            "Changed_Credit_Limit_Binned": "Moderado",
            "Credit_History_Age": "3 Years and 5 Months",
            "Credit_History_Age_Binned": "Normal",
            "Credit_History_Age_Months": 41.0,
            "Credit_Mix": "Good",
            "Credit_Utilization_Ratio": 0.35,
            "Credit_Utilization_Ratio_Binned": "Moderado",
            "Delay_from_due_date": 10,
            "Delay_from_due_date_Binned": "Curto",
            "Interest_Rate": 10,
            "Interest_Rate_Binned": "Médio",
            "Month_August": False,
            "Month_July": True,
            "Monthly_Balance": 5000.0,
            "Monthly_Balance_Binned": "Moderado",
            "Monthly_Inhand_Salary": 3000.0,
            "Monthly_Inhand_Salary_Binned": "Média",
            "Num_Bank_Accounts": 4,
            "Num_Bank_Accounts_Binned": "Média",
            "Num_Credit_Card": 2,
            "Num_Credit_Card_Binned": "Baixo",
            "Num_Credit_Inquiries": 1.0,
            "Num_Credit_Inquiries_Binned": "Baixo",
            "Num_of_Delayed_Payment": 3.0,
            "Num_of_Delayed_Payment_Binned": "Baixo",
            "Num_of_Loan": 1.0,
            "Num_of_Loan_Binned": "Baixo",
            "Occupation": "Engineer",
            "Occupation_Group_Engineer": True,
            "Occupation_Group_Other": False,
            "Outstanding_Debt": 2500.0,
            "Outstanding_Debt_Binned": "Baixo",
            "Outstanding_Debt_Binned_Low": True,
            "Payment_Behaviour_Low_spent_Medium_value_payments": True,
            "Payment_Behaviour_Other": False,
            "Payment_of_Min_Amount": "Yes",
            "Total_EMI_per_month": 700.0,
            "Total_EMI_per_month_Binned": "Moderado",
            "Type_of_Loan": "Personal Loan",
            "Type_of_Loan_Category_Personal Loan": True,
            "Type_of_Loan_Category_Other": False
        }
    ]
}

# 3. Envia requisição POST
response = requests.post(url, json=payload)

# 4. Exibe resposta
print("Status Code:", response.status_code)
print("Resposta JSON:")
print(json.dumps(response.json(), indent=4))
