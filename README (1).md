# 📌 QuantumFinance — Score de Crédito | Pipeline MLOps

Este repositório consolida o desenvolvimento do pipeline de **Ingestão, Curadoria, Versionamento e Tracking de Experimentos** para o sistema **QuantumFinance**, alinhado ao **PROTOCOLO V5.4** documentado no **HISTÓRICO DE DESENVOLVIMENTO**.

---

## 🗂️ Visão Geral

- **Problema:** Análise e predição de Score de Crédito com datasets extensos (100k linhas, ~6k features após `get_dummies`).
- **Objetivo:** Construir um pipeline auditável, 100% versionado, capaz de suportar escalabilidade para experimentos com rastreabilidade total.

---

## 🖼️ Estrutura Arquitetural

> ![Pipeline Arquitetural — QuantumFinance](caminho/para/sua/imagem.png)

- **Camadas:** `Raw ➜ Processed ➜ Curated`
- **Containers:** PostgreSQL, MinIO, MLflow Tracking Server, DevContainer Jupyter.
- **Rede:** `mlops_network` isolada, credenciais e endpoints definidos por variável de ambiente.

---

## ✅ Status do Pipeline

### 🔹 Ingestão e Curadoria

- Ingestão e limpeza na camada **`Processed`**, coerção de tipos, imputação de valores ausentes.
- Diagnóstico de **alta cardinalidade** executado com `tqdm` para monitorar colunas críticas.
- **Feature Engineering**: `binning` aplicado em variáveis com distribuição distorcida; mapeamento `Month` categórico ➜ numérico.

### 🔹 Camada `Curated`

- Datasets `train_curated.csv` (~3.6 GiB) e `test_curated.csv` (~1.8 GiB) salvos em `data/curated/`.
- Versionamento **DVC** auditado, push incremental validado no terminal externo.
- Remote duplicado removido (`minio-remote`), mantendo `storage` como default único.

---

## 🔹 Tracking de Experimentos

- **MLflow Tracking URI interno:** `http://mlflow:5000` para containers.
- **Links externos:** `http://127.0.0.1:5000` para navegador local.
- Credenciais MinIO (`wrm` / `senha_segura`) exportadas explicitamente dentro do notebook.
- **`MLFLOW_S3_ENDPOINT_URL` fixo:** `http://minio:9000` para evitar `InvalidAccessKeyId`.
- Experimento baseline rodado com **Árvore de Decisão (`max_depth=5`)**, barra de progresso `tqdm` no fitting.
- Artefato salvo no MinIO, push auditado.

---

## 🗄️ Status do PostgreSQL

- Container **`postgres_mlflow`** já provisionado para atuar como backend store do MLflow.
- **Próximo passo:** migrar `mlruns/` local para PostgreSQL, permitindo rastreabilidade dos metadados de runs, grid search e auditoria de pipelines.

---

## 🔑 Compromissos — PROTOCOLO V5.4

- `tqdm` obrigatório em loops de fitting ou validação.
- Nenhuma heurística improvisada para push — sempre incremental, auditável.
- Tracking URI coerente para rede interna, links amigáveis fixos para `127.0.0.1`.

---

## 🔗 Links de Acesso

- MLflow UI: [http://127.0.0.1:5000](http://127.0.0.1:5000)
- MinIO: [http://127.0.0.1:9000](http://127.0.0.1:9000)

---

## ✅ Histórico Consolidado

Para detalhes, consulte o documento **HISTÓRICO DE DESENVOLVIMENTO — QuantumFinance.md**, com toda a trilha de decisões, diagnósticos e auditoria de cada etapa.

---

**QuantumFinance | Julho 2025 | MLOps Baseline**
