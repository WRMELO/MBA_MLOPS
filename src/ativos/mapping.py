# mapping.py
# Versão integral e congelada do VARIABLE_MAP usado no transformador_input.py

import joblib
from pathlib import Path

ENCODER_DIR = Path("/workspace/models/encoders")

def load_encoder(filename):
    caminho = ENCODER_DIR / filename
    return joblib.load(caminho) if caminho.exists() else None

VARIABLE_MAP = {
    "Age": {
        "type": "int",
        "bins": [0, 25, 35, 50, 100],
        "labels": ["<=25", "26-35", "36-50", "50+"],
        "encoder": load_encoder("encoder_Age_Binned.pkl")
    },
    "Annual_Income": {
        "type": "float",
        "bins": [0, 25000, 50000, 75000, 100000, 1e6],
        "labels": ["Muito Baixa", "Baixa", "Média", "Alta", "Muito Alta"],
        "encoder": load_encoder("encoder_Annual_Income_Binned.pkl")
    },
    "Monthly_Inhand_Salary": {
        "type": "float",
        "bins": [0, 5000, 10000, 20000, 30000, 1e6],
        "labels": ["Muito Baixa", "Baixa", "Média", "Alta", "Muito Alta"],
        "encoder": load_encoder("encoder_Monthly_Inhand_Salary_Binned.pkl")
    },
    "Num_Bank_Accounts": {
        "type": "int",
        "bins": [0, 2, 5, 10, 100],
        "labels": ["1-2", "3-5", "6-10", "10+"],
        "encoder": load_encoder("encoder_Num_Bank_Accounts_Binned.pkl")
    },
    "Num_Credit_Card": {
        "type": "int",
        "bins": [0, 2, 5, 10, 100],
        "labels": ["1-2", "3-5", "6-10", "10+"],
        "encoder": load_encoder("encoder_Num_Credit_Card_Binned.pkl")
    },
    "Interest_Rate": {
        "type": "int",
        "bins": [0, 10, 20, 30, 40],
        "labels": ["0-10", "11-20", "21-30", "30+"],
        "encoder": load_encoder("encoder_Interest_Rate_Binned.pkl")
    },
    "Num_of_Loan": {
        "type": "int",
        "bins": [0, 2, 4, 6, 10],
        "labels": ["1-2", "3-4", "5-6", "6+"],
        "encoder": load_encoder("encoder_Num_of_Loan_Binned.pkl")
    },
    "Delay_from_due_date": {
        "type": "int",
        "bins": [0, 5, 10, 20, 30, 60],
        "labels": ["0-5", "6-10", "11-20", "21-30", "30+"],
        "encoder": load_encoder("encoder_Delay_from_due_date_Binned.pkl")
    },
    "Num_of_Delayed_Payment": {
        "type": "int",
        "bins": [0, 2, 5, 10, 20],
        "labels": ["0-2", "3-5", "6-10", "10+"],
        "encoder": load_encoder("encoder_Num_of_Delayed_Payment_Binned.pkl")
    },
    "Changed_Credit_Limit": {
        "type": "float",
        "bins": [-1e6, 0, 5000, 10000, 20000, 1e6],
        "labels": ["Negativo", "0-5k", "5k-10k", "10k-20k", "20k+"],
        "encoder": load_encoder("encoder_Changed_Credit_Limit_Binned.pkl")
    },
    "Num_Credit_Inquiries": {
        "type": "int",
        "bins": [0, 2, 5, 10, 20],
        "labels": ["0-2", "3-5", "6-10", "10+"],
        "encoder": load_encoder("encoder_Num_Credit_Inquiries_Binned.pkl")
    },
    "Credit_Mix": {
        "type": "str",
        "map": {
            "Bad": 0,
            "Standard": 1,
            "Good": 2
        }
    },
    "Outstanding_Debt": {
        "type": "float",
        "bins": [0, 1000, 5000, 10000, 50000, 1e6],
        "labels": ["Muito Baixa", "Baixa", "Média", "Alta", "Muito Alta"],
        "encoder": load_encoder("encoder_Outstanding_Debt_Binned.pkl")
    },
    "Credit_Utilization_Ratio": {
        "type": "float",
        "bins": [0, 20, 40, 60, 80, 100],
        "labels": ["0-20", "21-40", "41-60", "61-80", "81-100"],
        "encoder": load_encoder("encoder_Credit_Utilization_Ratio_Binned.pkl")
    },
    "Credit_History_Age": {
        "type": "int",
        "bins": [0, 12, 24, 36, 60, 120, 1000],
        "labels": ["<1a", "1-2a", "2-3a", "3-5a", "5-10a", "10+a"],
        "encoder": load_encoder("encoder_Credit_History_Age_Binned.pkl")
    },
    "Payment_of_Min_Amount": {
        "type": "str",
        "map": {
            "No": 0,
            "Yes": 1
        }
    },
    "Total_EMI_per_month": {
        "type": "float",
        "bins": [0, 1000, 5000, 10000, 20000, 1e6],
        "labels": ["Muito Baixa", "Baixa", "Média", "Alta", "Muito Alta"],
        "encoder": load_encoder("encoder_Total_EMI_per_month_Binned.pkl")
    },
    "Amount_invested_monthly": {
        "type": "float",
        "bins": [0, 500, 1000, 2000, 5000, 10000],
        "labels": ["Muito Baixa", "Baixa", "Média", "Alta", "Muito Alta"],
        "encoder": load_encoder("encoder_Amount_invested_monthly_Binned.pkl")
    },
    "Monthly_Balance": {
        "type": "float",
        "bins": [-1e6, 0, 1000, 5000, 10000, 1e6],
        "labels": ["Negativo", "Baixo", "Médio", "Alto", "Muito Alto"],
        "encoder": load_encoder("encoder_Monthly_Balance_Binned.pkl")
    },
    "Occupation": {
        "type": "str",
        "map": {
            "Scientist": 0,
            "Teacher": 1,
            "Engineer": 2,
            "Doctor": 3,
            "Lawyer": 4,
            "Entrepreneur": 5,
            "Developer": 6,
            "Other": 7
        }
    },
    "Type_of_Loan": {
        "type": "str",
        "map": {
            "Auto Loan": 0,
            "Credit-Builder Loan": 1,
            "Debt Consolidation Loan": 2,
            "Home Equity Loan": 3,
            "Mortgage Loan": 4,
            "Not Specified": 5,
            "Payday Loan": 6,
            "Personal Loan": 7,
            "Student Loan": 8
        }
    }
}
