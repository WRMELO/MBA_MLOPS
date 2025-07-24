# cf_service.py

from fastapi import FastAPI, Request, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import mlflow.pyfunc
import pandas as pd
import os

# 1️⃣ Configurações
API_KEY = "quantum123"
MODEL_PATH = (
    "/workspace/.mlruns/770693764546068990/"
    "7077ebfbf696487384bd5a59034170c5/artifacts/models/"
    "m-dd39a11d77284f04bae26d274c32a483"
)

# 2️⃣ Criação da app FastAPI
app = FastAPI(title="API de Predição de Score de Crédito")

# 3️⃣ Liberação de CORS para permitir acesso do Streamlit
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["POST"],
    allow_headers=["*"],
)

# 4️⃣ Validação do caminho físico
mlmodel_path = os.path.join(MODEL_PATH, "MLmodel")
if not os.path.exists(mlmodel_path):
    raise RuntimeError(f"🚫 MLmodel não encontrado em: {MODEL_PATH}")
model = mlflow.pyfunc.load_model(MODEL_PATH)
print("✅ Modelo MLflow carregado com sucesso.")

# 5️⃣ Rota de predição
@app.post("/predict")
async def predict(request: Request):
    # Validação da chave de API
    if request.headers.get("x-api-key") != API_KEY:
        raise HTTPException(status_code=401, detail="Chave de API inválida.")

    try:
        payload = await request.json()

        # Conversão para DataFrame
        df = pd.DataFrame([payload])

        # Predição
        pred = model.predict(df)

        return {"predictions": pred.tolist()}

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro na predição: {str(e)}")
