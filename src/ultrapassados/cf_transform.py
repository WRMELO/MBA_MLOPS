# cf_transform.py

"""
Este módulo contém:
1. O dicionário OPTIONS_MAP com os valores válidos esperados pela interface Streamlit;
2. A função transform_input() que mapeia os campos da UI para os nomes usados no modelo;
3. A função gerar_payload_final() que embala os dados em formato compatível com a API.
"""

# 🔧 ETAPA: DEFINIÇÃO DOS VALORES ACEITOS PELA INTERFACE

OPTIONS_MAP = {
    "Occupation": {
        "Scientist": 0,
        "Teacher": 1,
        "Engineer": 2,
        "Lawyer": 3,
        "Entrepreneur": 4
    },
    "Credit_Mix": {
        "Good": 1,
        "Standard": 0,
        "Bad": -1
    },
    "Payment_of_Min_Amount": {
        "Yes": 1,
        "No": 0
    },
    "Type_of_Loan": {
        "Auto Loan": 0,
        "Personal Loan": 1,
        "Mortgage": 2
    }
}

# 🔧 ETAPA: TRANSFORMAÇÃO DOS CAMPOS DE UI PARA INPUT DO MODELO

def transform_input(dicionario_ui: dict) -> list:
    """
    Converte os nomes e valores da interface Streamlit para os nomes exigidos pelo modelo.
    """
    convertido = {
        "Age": dicionario_ui["Age"],
        "Annual_Income": dicionario_ui["Annual_Income"],
        "Monthly_Inhand_Salary": dicionario_ui["Monthly_Inhand_Salary"],
        "Occupation": OPTIONS_MAP["Occupation"][dicionario_ui["Occupation"]],
        "Credit_Mix": OPTIONS_MAP["Credit_Mix"][dicionario_ui["Credit_Mix"]],
        "Payment_of_Min_Amount": OPTIONS_MAP["Payment_of_Min_Amount"][dicionario_ui["Payment_of_Min_Amount"]],
        "Type_of_Loan": OPTIONS_MAP["Type_of_Loan"][dicionario_ui["Type_of_Loan"]],
        "Num_of_Loan": dicionario_ui["Num_of_Loan"],
        "Num_Credit_Card": dicionario_ui["Num_Credit_Card"],
        "Outstanding_Debt": dicionario_ui["Outstanding_Debt"],
        "Credit_Utilization_Ratio": dicionario_ui["Credit_Utilization_Ratio"],
        "Interest_Rate": dicionario_ui["Interest_Rate"],
        "Delay_from_due_date": dicionario_ui["Delay_from_due_date"]
    }

    # O modelo espera um dataframe-like, então retorna como lista de dicionários
    return [convertido]

# 🔧 ETAPA: EMBALAGEM DO PAYLOAD PARA FASTAPI

def gerar_payload_final(formulario_dict: dict) -> dict:
    """
    Gera o payload final no formato esperado pela API:
    {
        "input_data": { ... campos preenchidos pelo usuário ... }
    }
    """
    return {"input_data": formulario_dict}
