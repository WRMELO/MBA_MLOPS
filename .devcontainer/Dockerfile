# .devcontainer/Dockerfile

# Base oficial Python 3.10, leve, mas completa para MLOps
FROM python:3.10-slim

# Evita prompts interativos que travariam o build
ENV DEBIAN_FRONTEND=noninteractive

# Diretório de trabalho dentro do container
WORKDIR /workspace

# ------------------------------
# SISTEMA OPERACIONAL
# ------------------------------

# Instala pacotes essenciais:
# - git: versionamento de código
# - curl: testes de conexão HTTP
# - openssh-client: push/pull via SSH
# - build-essential: compila dependências Python nativas
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    git \
    curl \
    openssh-client \
    build-essential && \
    rm -rf /var/lib/apt/lists/*

# ------------------------------
# PYTHON E DEPENDÊNCIAS DE MLOps
# ------------------------------

# Atualiza o pip para a versão mais recente
RUN pip install --upgrade pip

# Instala bibliotecas principais:
# - cookiecutter: scaffold do projeto
# - mlflow: rastreamento de experimentos
# - dvc[all]: versionamento de dados com backend MinIO (S3)
# - fastapi + uvicorn: API RESTful
# - streamlit: frontend interativo para visualizações
# - slowapi: controle de throttling na API
# - minio: cliente Python para integração MinIO
RUN pip install \
    cookiecutter \
    mlflow \
    dvc[all] \
    fastapi uvicorn \
    streamlit \
    slowapi \
    minio

# ------------------------------
# COPIA O CÓDIGO-FONTE DO HOST (opcional)
# ------------------------------
COPY . /workspace

# ------------------------------
# PORTAS (opcional)
# ------------------------------
# EXPOSE 8000   # FastAPI
# EXPOSE 8501   # Streamlit

# ------------------------------
# CMD padrão
# ------------------------------
# O DevContainer não define ENTRYPOINT fixo; o VS Code gerencia o shell interativo
