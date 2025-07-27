# api_preditor_v1.py
# API FastAPI que consome a função transform_input e executa predição com o modelo v1-final
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import mlflow.pyfunc
from transformador_input import transform_input

# Carrega o modelo MLflow
MODEL_PATH = "/workspace/models/exportado_rf_v1_final/pipeline"
model = mlflow.pyfunc.load_model(MODEL_PATH)

# Mapeamento opcional das classes numéricas → textuais
CLASS_MAP = {0: "Poor", 1: "Standard", 2: "Good"}

app = FastAPI(
    title="API Classificador de Crédito",
    description="Recebe 21 variáveis humanas, transforma em 92 features e retorna classe prevista",
    version="1.0",
)

# Define os 21 campos de entrada
class InputPayload(BaseModel):
    Age: int
    Annual_Income: float
    Monthly_Inhand_Salary: float
    Num_Bank_Accounts: int
    Num_Credit_Card: int
    Interest_Rate: float
    Delay_from_due_date: int
    Num_of_Delayed_Payment: int
    Changed_Credit_Limit: float
    Num_Credit_Inquiries: int
    Credit_History_Age: str
    Total_EMI_per_month: float
    Amount_invested_monthly: float
    Monthly_Balance: float
    Occupation: str
    Credit_Mix: str
    Payment_of_Min_Amount: str
    Payment_Behaviour: str
    Type_of_Loan: str
    Num_of_Loan: int
    Outstanding_Debt: float
    Credit_Utilization_Ratio: float

@app.post("/predict")
def predict(payload: InputPayload):
    try:
        # Converte input para dict
        payload_dict = payload.dict()

        # Transforma dados para as 92 features
        df_transformed = transform_input(payload_dict)

        # Predição
        prediction = model.predict(df_transformed)

        # Mapeia resultado numérico para textual (se aplicável)
        predicted_class = CLASS_MAP.get(int(prediction[0]), str(prediction[0]))

        return {"classe_prevista": predicted_class}

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro durante a inferência: {str(e)}")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("api_preditor_v1:app", host="0.0.0.0", port=8000, reload=False)
