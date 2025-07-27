# transformador_input.py
# Versão consolidada da célula validada – não modificar sem revalidação no notebook
import pandas as pd
import mlflow.pyfunc

# Caminho fixo para o modelo e leitura de colunas esperadas
MODEL_PATH = "/workspace/models/exportado_rf_v1_final/pipeline"
modelo = mlflow.pyfunc.load_model(MODEL_PATH)
colunas_esperadas = modelo.metadata.get_input_schema().input_names()

def transform_input(payload_dict: dict) -> pd.DataFrame:
    """
    Transforma os 21 campos humanos em um DataFrame com 92 features
    exatamente no formato esperado pelo modelo v1-final.
    """
    # 1. Cria DataFrame a partir do dicionário
    df_input = pd.DataFrame([payload_dict])

    # Remove coluna "Month" caso venha do formulário
    if "Month" in df_input.columns:
        df_input.drop(columns=["Month"], inplace=True)

    # 2. Garante presença de todas as 92 colunas
    for col in colunas_esperadas:
        if col not in df_input.columns:
            df_input[col] = 0

    # 3. Conversão explícita de tipos
    colunas_long = [
        "Delay_from_due_date", "Interest_Rate", "Num_Bank_Accounts", "Num_Credit_Card",
        "Month_August", "Month_February", "Month_January", "Month_July",
        "Month_June", "Month_March", "Month_May"
    ]
    colunas_month_bool = ["Month_November", "Month_October", "Month_September"]
    colunas_categoricas = [
        "Credit_History_Age", "Credit_Mix", "Occupation",
        "Type_of_Loan", "Payment_of_Min_Amount", "Payment_Behaviour"
    ]

    for col in df_input.columns:
        if col in colunas_categoricas or "Binned" in col:
            df_input[col] = df_input[col].astype(str)
        elif col in colunas_long:
            df_input[col] = df_input[col].astype("int64")
        elif col in colunas_month_bool:
            df_input[col] = df_input[col].astype(bool)
        elif col.startswith(("Occupation_Group_", "Payment_Behaviour_", "Type_of_Loan_Category_")):
            df_input[col] = df_input[col].astype(bool)
        else:
            df_input[col] = df_input[col].astype("float64")

    # 4. Reordena as colunas
    df_input = df_input[colunas_esperadas]

    return df_input
