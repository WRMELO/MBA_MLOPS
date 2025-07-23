# ETAPA: API FastAPI USANDO PIPELINE COMPLETO FINAL

from fastapi import FastAPI, HTTPException, Request, Header
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded
import pandas as pd
import joblib
import traceback
import os

# 1️⃣ Configuração geral da API
app = FastAPI(title="API Score de Crédito — QuantumFinance")
limiter = Limiter(key_func=get_remote_address)
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

# 2️⃣ Segurança
API_KEY = os.getenv("API_KEY", "quantum123")  # Use variável protegida em produção

# 3️⃣ Caminho do pipeline final completo
pipeline_path = "/workspace/models/final_pipeline_completo.pkl"

# 4️⃣ Carregamento do pipeline completo
try:
    pipeline = joblib.load(pipeline_path)
except Exception as e:
    raise RuntimeError(f"Erro ao carregar pipeline: {e}")

# 5️⃣ Esquema de entrada
class InputData(BaseModel):
    data: dict

# 6️⃣ Endpoint de predição com validações
@app.post("/predict")
@limiter.limit("5/minute")
async def predict(request: Request, input_data: InputData, x_api_key: str = Header(...)):
    if x_api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Chave de API inválida.")

    try:
        # Converte entrada para DataFrame
        df = pd.DataFrame([input_data.data])

        # Substituição preventiva de placeholders
        df.replace(['_______', '__ __ ____', '!@9#%8'], 'Unknown', inplace=True)

        # Predição direta via pipeline completo
        prediction = pipeline.predict(df)[0]
        return {"prediction": prediction}

    except Exception as e:
        erro_traceback = traceback.format_exc()
        raise HTTPException(status_code=500, detail=f"Erro interno: {str(e)}\n{erro_traceback}")


