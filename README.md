---

## ✅ **`README.md` DEFINITIVO — BASE V5.4**

````markdown
# MBA_MLOPS

# 🗂️ Projeto QuantumFinance — Score de Crédito

Este repositório contém a estrutura base para o desenvolvimento do sistema de Score de Crédito **QuantumFinance**, alinhado às práticas de **MLOps**, versionamento e reprodutibilidade.

---

## 📌 **Visão Geral**

- Estrutura organizada com **DevContainer** para garantir ambiente de desenvolvimento isolado (**Python 3.10**, SSH client incluído).
- Versionamento de dados e modelos com **DVC** integrado a **MinIO** como backend (emulando S3).
- API segura implementada com **FastAPI**, autenticação via API Key e throttling com `slowapi`.
- Frontend interativo desenvolvido com **Streamlit**.
- Rastreamento de experimentos com **MLflow**.
- Versionamento de código e infra com **Git/GitHub**.
- Gestão de ambiente via **`requirements.txt`** coerente com o `Dockerfile`.

---

## 🗺️ **Arquitetura do Projeto**

A arquitetura geral do sistema está representada no diagrama abaixo:

![Arquitetura](references/docs/arquitetura.svg)

>

---

## ⚙️ **Estrutura Recomendada**

```plaintext
📁 projeto/
 ├── .devcontainer/         # Configuração DevContainer (Dockerfile + devcontainer.json)
 ├── data/                  # Dados versionados via DVC
 ├── notebooks/             # Notebooks de EDA e pré-processamento
 ├── src/                   # Código-fonte da API e scripts auxiliares
 ├── models/                # Artefatos de modelos treinados
 ├── Streamlit/             # Interface interativa
 ├── docs/arquitetura.svg   # Diagrama de arquitetura
 ├── references/            # Documentação auxiliar (ex: PROTOCOLO_V5.4_UNIFICADO.md)
 ├── requirements.txt       # Dependências Python (coerente com Dockerfile)
 ├── README.md              # Este arquivo
 ├── .gitignore             # Exclusões rastreáveis (DVC, MinIO, .obsidian/workspace)
 └── docker-compose.yml     # (Placeholder) Orquestração local, se aplicável
````

---

## 🗂️ **Fluxo de Versionamento**

* Todos os dados, modelos e artefatos são rastreados com **DVC** e armazenados no **MinIO**.
* O `DevContainer` garante que builds locais e remotos permaneçam consistentes.
* Push e pull de código via **SSH ou HTTPS**, com chaves configuradas dentro do container.

---

## 🔒 **Rastreabilidade**

* Este repositório segue o **PROTOCOLO V5.4**, com cada ajuste versionado e documentado.
* Placeholder: *(Adicionar instruções de `dvc remote add`, `mlflow ui`, deploy FastAPI/Streamlit em produção)*

---

## ✅ **Próximos Passos**

* Finalizar configuração do **MinIO bucket** e `dvc.yaml`.
* Registrar primeiros experimentos no **MLflow**.
* Implementar o endpoint `/predict` com autenticação via API Key.
* Conectar **Streamlit** ao backend.

---

> **TODO:** Este README será expandido em blocos coerentes com o avanço das tarefas — cada novo componente será justificado, rastreável e alinhado ao plano conceitual.

---

```

`
