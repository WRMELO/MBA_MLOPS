
✅ PROTOCOLO V5.5 VALIDADO — Nenhuma heurística genérica aplicada. Toda decisão rastreada.

---

# PLANO ESTRATÉGICO DETALHADO

**Objetivo:** Retomar e consolidar o ciclo completo de modelagem com acurácia de aproximadamente **0,88**, utilizando todo o conhecimento acumulado no histórico, **sem reincidência de falhas**, com compatibilidade total com `MLflow`, `FastAPI` e `Streamlit`.

---

## 1. PREMISSAS INEGOCIÁVEIS

- O modelo final será **serializado integralmente** com pipeline completo (`preprocessing + model`), contendo:
    
    - `signature`
        
    - `input_example`
        
    - rastreamento via `MLflow`
        
- O pipeline deve ser compatível com **deploy real** via API (`FastAPI`) e consumo externo (`Streamlit`).
    
- **Nenhum encoder ou transformador** pode ser salvo de forma separada, fora do pipeline.
    
- **Todos os caminhos, shapes e schemas** devem ser testados com `X_real → predict → y_hat` antes do deploy.
    
- Todo o processo será desenvolvido com blocos autocontidos e rastreáveis, em conformidade com o `PROTOCOLO V5.5`.
    

---

## 2. BIBLIOTECAS E FERRAMENTAS OBRIGATÓRIAS

|Categoria|Ferramentas/Bibliotecas|
|---|---|
|ML Pipeline|`scikit-learn`, `pandas`, `numpy`, `tqdm`|
|Tracking|`mlflow` (versão compatível com scikit-learn 1.3+)|
|Serialização|`mlflow.sklearn`, sem `joblib.dump`|
|Discretização|`KBinsDiscretizer` com `ordinal` e `uniform`|
|Codificação|`OrdinalEncoder` com `handle_unknown='use_encoded_value'`|
|Persistência|`MinIO` como backend para artefatos|
|Interface Web|`FastAPI` + `Streamlit`|
|Infraestrutura|Docker Compose, rede `mlops_network`|
|Deploy API|`uvicorn`, `requests`|

---

## 3. CAMINHO ESTRATÉGICO COMPLETO

### ETAPA 1 — REVISÃO DOS DADOS CURADOS (curated_v1_1)

- Validar que `train_curated_v1_1.csv` e `test_curated_v1_1.csv`:
    
    - Estão no `MinIO`, com DVC sincronizado
        
    - Têm `X.shape == (N, 92)` e target `y` codificado corretamente
        
- Confirmar colunas categóricas binadas que devem ser encodadas via `OrdinalEncoder`.
    

### ETAPA 2 — CONSTRUÇÃO DO PIPELINE COMPLETO (fit + transformação + modelo)

- Criar pipeline com `ColumnTransformer`, combinando:
    
    - `OrdinalEncoder` para colunas categóricas
        
    - `KBinsDiscretizer` para colunas numéricas (opcional)
        
    - PassThrough para colunas já normalizadas
        
- Modelo central: `RandomForestClassifier`, com hiperparâmetros:
    
    ```python
    {'max_depth': 20, 'max_features': 'sqrt', 'min_samples_leaf': 3, 'n_estimators': 100}
    ```
    
- Salvar pipeline completo com `mlflow.sklearn.log_model`, contendo:
    
    - `signature`
        
    - `input_example` extraído diretamente do `X_test`
        

### ETAPA 3 — VALIDAÇÃO INTERNA DO PIPELINE COM `.predict(X_test)`

- Executar:
    
    ```python
    pipeline.predict(X_test)
    ```
    
    e verificar:
    
    - ausência de erro de shape
        
    - correspondência exata com `signature`
        
    - distribuição coerente de `y_pred`
        

### ETAPA 4 — RASTREAMENTO NO MLflow

- Tracking URI: `file:/workspace/.mlruns`
    
- Experimento: `modelo_rf_finalizado`
    
- Run Name: `rf_pipeline_integrado`
    
- Registrar: pipeline, métricas (`accuracy`, `f1_macro`), parâmetros, signature
    

### ETAPA 5 — EXPORTAÇÃO FINAL DO MODELO (APENAS LINK, SEM `joblib`)

- Nada será salvo como `.pkl` avulso.
    
- Toda recuperação será via `mlflow.sklearn.load_model("runs:/<run_id>/model")`
    

### ETAPA 6 — CRIAÇÃO DA API `api.py`

- Receber JSON no formato `X.to_dict(orient='records')`
    
- Recarregar modelo diretamente do MLflow
    
- Verificar colunas em tempo real (`X.columns == pipeline.feature_names_in_`)
    
- Retornar predições como JSON com status 200
    

### ETAPA 7 — TESTE LOCAL COM `Streamlit`

- Interface com:
    
    - Upload de dados ou formulário
        
    - Preview das features
        
    - Botão "Enviar à API"
        
    - Exibição de predições
        
- Validar round-trip: `input → JSON → API → predição → retorno`
    

### ETAPA 8 — VERIFICAÇÃO FINAL DE CONSISTÊNCIA

- Executar inferência local com:
    
    ```python
    model.predict(input_example)
    ```
    
- Executar inferência via `FastAPI` com o mesmo input
    
- Validar: resultados idênticos em ambos
    

---

## 4. DIFERENCIAIS DESTA NOVA ABORDAGEM

|Componente|Antes (com falhas)|Agora (revisado)|
|---|---|---|
|Pipeline salvo|Fragmentado (`pkl` avulso)|Consolidado com MLflow|
|Encoder|Salvo separadamente ou omitido|Acoplado ao pipeline|
|API|Quebrava por `columns missing`|Validada com `input_example` e schema fixo|
|Testes de inferência|Ausentes|Obrigatórios e documentados|
|Persistência|Ambígua (`joblib`, MLflow, disco)|Unificada no MLflow|
|Tracking|Parcial|Completo com parâmetros, métricas e paths|

---

