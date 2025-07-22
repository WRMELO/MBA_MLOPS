# api.py

import os
import pandas as pd
import mlflow
import mlflow.sklearn
from fastapi import FastAPI, Header, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from sklearn.preprocessing import OrdinalEncoder

# Configuração do MLflow Tracking URI
mlflow.set_tracking_uri("file:/workspace/.mlruns")

# Identificação do modelo salvo no MLflow
MODEL_RUN_ID = "4e56a5afe29a4a26b962c220fef03f5d"
MODEL_URI = f"runs:/{MODEL_RUN_ID}/random_forest_tuned_model"
TRAIN_CSV = "/workspace/data/curated/train_curated_v1_1.csv"

# Carregamento do modelo treinado
model = mlflow.sklearn.load_model(MODEL_URI)

# Carregamento e treinamento do encoder
df_train = pd.read_csv(TRAIN_CSV)
X_train = df_train.drop(columns=["Credit_Score"])
object_cols = X_train.select_dtypes(include="object").columns.tolist()

encoder = OrdinalEncoder(handle_unknown="use_encoded_value", unknown_value=-1)
encoder.fit(X_train[object_cols])

# Mapeamento de labels
label_map = {0: "Poor", 1: "Standard", 2: "Good"}

# Carregamento da chave de autenticação
API_KEY = os.environ.get("API_KEY", "default_secret")

# Definição do schema de entrada
class InputData(BaseModel):
    Age_Binned: int
    Amount_invested_monthly_Binned: int
    Annual_Income_Binned: int
    Changed_Credit_Limit_Binned: int
    Credit_History_Age: float
    Credit_History_Age_Binned: int
    Credit_Mix: int
    Credit_Utilization_Ratio_Binned: int
    Delay_from_due_date_Binned: int
    Interest_Rate_Binned: int
    Monthly_Balance_Binned: int
    Monthly_Inhand_Salary_Binned: int
    Num_Bank_Accounts_Binned: int
    Num_Credit_Card_Binned: int
    Num_Credit_Inquiries_Binned: int
    Num_of_Delayed_Payment_Binned: int
    Num_of_Loan_Binned: int
    Occupation: int
    Outstanding_Debt_Binned: int
    Payment_of_Min_Amount: int
    Total_EMI_per_month_Binned: int
    Type_of_Loan: int

# Criação do app FastAPI
app = FastAPI()

# Middleware para CORS (caso haja frontend separado)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Endpoint de predição
@app.post("/predict")
def predict(data: InputData, x_api_key: str = Header(...)):

    if x_api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API Key")

    # Conversão para DataFrame
    input_df = pd.DataFrame([data.dict()])

    # Aplicação do encoding
    input_df[object_cols] = encoder.transform(input_df[object_cols])

    # Inferência
    prediction = model.predict(input_df)[0]
    label = label_map.get(prediction, "Unknown")

    return {"prediction": label}
