# 🔧 ETAPA: API FastAPI PARA ENTREGA — COM SEGURANÇA, THROTTLING E MODELO .PKL

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

# 2️⃣ Variáveis e segurança
API_KEY = os.getenv("API_KEY", "quantum123")  # Use variável de ambiente em produção

# 3️⃣ Caminhos dos artefatos
model_path = "/workspace/models/final_model.pkl"
encoder_path = "/workspace/models/final_encoder.pkl"

# 4️⃣ Carrega modelo e encoder salvos localmente
try:
    model = joblib.load(model_path)
    encoder = joblib.load(encoder_path)
    categorical_cols = encoder.feature_names_in_.tolist()
except Exception as e:
    raise RuntimeError(f"Erro ao carregar modelo ou encoder: {e}")

# 5️⃣ Esquema da entrada
class InputData(BaseModel):
    data: dict

# 6️⃣ Endpoint de predição com throttling e autenticação
@app.post("/predict")
@limiter.limit("5/minute")
async def predict(request: Request, input_data: InputData, x_api_key: str = Header(...)):
    if x_api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Chave de API inválida.")

    try:
        df = pd.DataFrame([input_data.data])

        # Substituição de placeholders
        placeholders = ['_______', '__ __ ____', '!@9#%8']
        df.replace(placeholders, 'Unknown', inplace=True)

        # Conversão de Credit_History_Age
        if 'Credit_History_Age' in df.columns:
            years = df['Credit_History_Age'].str.extract(r'(\d+)\s+Years?')[0].astype(float)
            months = df['Credit_History_Age'].str.extract(r'(\d+)\s+Months?')[0].fillna(0).astype(float)
            df['Credit_History_Age'] = (years * 12 + months).fillna(0)

        # Conversão de colunas numéricas possíveis
        for col in df.select_dtypes(include='object').columns:
            if df[col].str.replace('.', '', 1).str.isnumeric().all():
                df[col] = pd.to_numeric(df[col], errors='coerce')

        # Aplica o encoder
        df[categorical_cols] = encoder.transform(df[categorical_cols])
        prediction = model.predict(df)[0]

        return {"prediction": prediction}

    except Exception as e:
        tb = traceback.format_exc()
        raise HTTPException(status_code=500, detail=f"Erro interno: {str(e)}\n{tb}")
