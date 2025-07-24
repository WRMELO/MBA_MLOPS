# cf_transform.py

# 1️⃣ Imports principais
from typing import Any, Dict
import pandas as pd
import joblib
import os

# 2️⃣ Dicionários de mapeamento
from mapping import UI_LABEL_TO_VAR, OPTIONS_MAP

# 3️⃣ Função: transforma labels da UI em nomes + códigos esperados
def transform_input(human_inputs: Dict[str, Any]) -> Dict[str, Any]:
    """
    Recebe um dict com os 21 campos vindos da UI (labels → valores),
    e retorna um dict com os 21 campos nomeados conforme a API espera,
    já convertidos para o tipo/código correto.
    """
    api_payload: Dict[str, Any] = {}

    for ui_label, raw_value in human_inputs.items():
        # 1️⃣ Traduz rótulo da UI para nome de variável da API
        var_name = UI_LABEL_TO_VAR[ui_label]

        # 2️⃣ Se existir mapa de opções, converte (ex.: "20-30" → 0)
        if var_name in OPTIONS_MAP:
            try:
                api_payload[var_name] = OPTIONS_MAP[var_name][raw_value]
            except KeyError:
                raise ValueError(f"Valor inválido para '{ui_label}': {raw_value}")
        else:
            # 3️⃣ Caso contrário, assume-se valor numérico ou string livre
            api_payload[var_name] = raw_value

    return api_payload

# 4️⃣ Caminho validado para o pipeline oficial congelado
PIPELINE_PATH = "/workspace/models/exportado_rf_v1_final/pipeline_completo.pkl"

if not os.path.exists(PIPELINE_PATH):
    raise FileNotFoundError(f"🚫 Pipeline não encontrado em: {PIPELINE_PATH}")

pipeline = joblib.load(PIPELINE_PATH)
print("✅ Pipeline carregado com sucesso.")

# 5️⃣ Função: aplica pipeline para gerar os 92 campos finais
def gerar_payload_final(inputs_codificados: Dict[str, Any]) -> Dict[str, int]:
    """
    Aplica o pipeline oficial v1-final sobre os 21 campos codificados e retorna
    um dict com os 92 campos finais esperados pela API (tipados como int64).
    """
    # Cria DataFrame de entrada com uma linha
    df_input = pd.DataFrame([inputs_codificados])

    # Aplica transformação
    X_transformed = pipeline.transform(df_input)

    # Recupera nomes de colunas do pipeline (se suportado)
    if hasattr(pipeline, 'get_feature_names_out'):
        col_names = pipeline.get_feature_names_out()
    else:
        col_names = [f'feat_{i}' for i in range(X_transformed.shape[1])]

    # Gera DataFrame final e tipa como int64
    df_final = pd.DataFrame(X_transformed, columns=col_names)
    df_final = df_final.astype("int64")

    # Converte para dict linha única
    return df_final.iloc[0].to_dict()
