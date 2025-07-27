# test_api_local.py
# Testa a API FastAPI localmente com o payload padrão do formulário

import requests
import json

URL = "http://localhost:8000/predict"

payload = {
    "Age": 35,
    "Annual_Income": 50000.0,
    "Monthly_Inhand_Salary": 4000.0,
    "Num_Bank_Accounts": 3,
    "Num_Credit_Card": 2,
    "Interest_Rate": 15,
    "Num_of_Loan": 2,
    "Delay_from_due_date": 7,
    "Num_of_Delayed_Payment": 4,
    "Changed_Credit_Limit": 5000.0,
    "Num_Credit_Inquiries": 3,
    "Credit_Mix": "Standard",
    "Outstanding_Debt": 3000.0,
    "Credit_Utilization_Ratio": 45.0,
    "Credit_History_Age": 36,
    "Payment_of_Min_Amount": "Yes",
    "Total_EMI_per_month": 1500.0,
    "Amount_invested_monthly": 800.0,
    "Monthly_Balance": 2000.0,
    "Occupation": "Engineer",
    "Type_of_Loan": "Personal Loan"
}

response = requests.post(URL, json=payload)

print("Status Code:", response.status_code)
try:
    print("Resposta JSON:", json.dumps(response.json(), indent=2))
except Exception as e:
    print("Erro ao interpretar resposta:", str(e))
    print("Conteúdo bruto:", response.text)
