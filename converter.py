# converter.py

# 1️⃣ Dicionário de mapeamentos para valores categóricos
mapeamentos = {
    "Age_Binned": {"20-30": 0, "30-40": 1, "40-50": 2, "50-60": 3, "60-70": 4, "70+": 5},
    "Amount_invested_monthly_Binned": {"0-500": 0, "500-1000": 1, "1000-1500": 2, "1500-2000": 3, "2000+": 4},
    # … inclua aqui todos os outros mapeamentos conforme definido no seu app …
    "Type_of_Loan": {
        "Home Loan": 0, "Credit-Builder Loan": 1, "Auto Loan": 2,
        "Personal Loan": 3, "Student Loan": 4, "Payday Loan": 5,
        "Mortgage Loan": 6, "Not Specified": 7
    }
}

# 2️⃣ Função que o Streamlit usará para converter a entrada da UI em dados da API
def converter_dados_para_api(dados_ui: dict) -> dict:
    dados_convertidos = {}
    for campo, valor in dados_ui.items():
        if campo in mapeamentos:
            dados_convertidos[campo] = mapeamentos[campo][valor]
        else:
            dados_convertidos[campo] = valor
    return dados_convertidos
