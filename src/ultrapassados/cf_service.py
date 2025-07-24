from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
import os
import pandas as pd  # ✅ Correção obrigatória

from cf_transform import transform_input

# 🔧 Inicialização da API FastAPI
app = FastAPI(title="API de Classificação de Risco", version="1.0")

# 🔧 Definição do schema esperado via Pydantic
class Payload(BaseModel):
    input_data: dict

# 🔧 Caminho fixo do modelo exportado
MODEL_PATH = "/workspace/models/exportado_rf_v1_final/pipeline_completo.pkl"

if not os.path.exists(MODEL_PATH):
    raise FileNotFoundError(f"Modelo não encontrado em: {MODEL_PATH}")

# 🔧 Carregamento do pipeline completo treinado
model = joblib.load(MODEL_PATH)

# 🔧 Rota principal de predição
@app.post("/predict")
def predict(payload: Payload):
    try:
        # Transforma input de Streamlit em lista de dicts
        X_list = transform_input(payload.input_data)

        # ✅ Conversão obrigatória para DataFrame
        X_df = pd.DataFrame(X_list)

        # Predição com modelo scikit-learn
        y_pred = model.predict(X_df)

        # Retorno como JSON
        return {"prediction": int(y_pred[0])}

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro durante inferência: {str(e)}")
