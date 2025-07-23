# api.py

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Dict, Any
import pandas as pd
import mlflow.pyfunc
import uvicorn
from datetime import datetime

# 1. Carrega modelo
model_path = "/workspace/models/exportado_rf_v1_final/pipeline"
try:
    model = mlflow.pyfunc.load_model(model_path)
except Exception as e:
    raise RuntimeError(f"Erro ao carregar o modelo em {model_path}") from e

# 2. Define estrutura do input
class Item(BaseModel):
    data: List[Dict[str, Any]]  # espera uma lista de dicionários (X em JSON)

# 3. Instancia API
app = FastAPI(title="API de Inferência - Random Forest v1-final")

# 4. Endpoint de predição
@app.post("/predict")
def predict(item: Item):
    try:
        X = pd.DataFrame(item.data)
        y_pred = model.predict(X)
        return {
            "timestamp": datetime.now().isoformat(),
            "status": "ok",
            "predictions": y_pred.tolist(),
            "num_rows": len(X)
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
