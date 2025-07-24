from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Dict, Any
import mlflow
import pandas as pd

# 1️⃣ Aponte o MLflow para o diretório .mlruns
mlflow.set_tracking_uri("file:///workspace/.mlruns")

# 2️⃣ Defina o RUN_ID congelado e carregue o modelo
RUN_ID = "7077ebfbf696487384bd5a59034170c5"
MODEL_URI = f"runs:/{RUN_ID}/model"
model = mlflow.pyfunc.load_model(MODEL_URI)

# 3️⃣ Inicialize o FastAPI
app = FastAPI(
    title="Interface de Predição – Modelo Random Forest v1-final",
    description="Envia dados para a API FastAPI e retorna as predições"
)

# 4️⃣ Defina o payload de entrada como lista de registros
class PredictionRequest(BaseModel):
    data: List[Dict[str, Any]]

# 5️⃣ Endpoint /predict
@app.post("/predict")
def predict(req: PredictionRequest):
    try:
        # converte para DataFrame e faz a predição
        df = pd.DataFrame(req.data)
        preds = model.predict(df)
        return {"predictions": preds.tolist()}
    except Exception as exc:
        # retorna erro 500 em caso de falha
        raise HTTPException(status_code=500, detail=str(exc))
