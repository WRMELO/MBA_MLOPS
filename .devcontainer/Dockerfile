# .devcontainer/Dockerfile

# Base oficial Python 3.10, leve, sem pacotes extras desnecessários
FROM python:3.10-slim

# Evita prompts interativos que travariam instalação no container
ENV DEBIAN_FRONTEND=noninteractive

# Diretório padrão de trabalho dentro do container
WORKDIR /workspace

# ------------------------------
# SISTEMA OPERACIONAL
# ------------------------------

# Instala pacotes do sistema necessários para git, curl, compilação de libs
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    git \
    curl \
    build-essential && \
    rm -rf /var/lib/apt/lists/*

# ------------------------------
# PYTHON E DEPENDÊNCIAS DE MLOps
# ------------------------------

# Garante pip atualizado
RUN pip install --upgrade pip

# Instala bibliotecas principais do ambiente:
# - cookiecutter: scaffold do repositório
# - mlflow: rastreamento de experimentos
# - dvc[all]: versionamento com suporte a MinIO (S3)
# - fastapi + uvicorn: API REST
# - streamlit: frontend interativo
# - slowapi: throttling da API
# - minio: cliente Python para MinIO
RUN pip install cookiecutter \
    mlflow \
    dvc[all] \
    fastapi uvicorn \
    streamlit \
    slowapi \
    minio

# ------------------------------
# COPIAR PROJETO (Opcional)
# ------------------------------
# Copia o conteúdo do repositório para dentro do container na pasta /workspace
COPY . /workspace

# ------------------------------
# PORTAS (se precisar mapear explicitamente em dev)
# ------------------------------
# Exemplo: FastAPI em 8000, Streamlit em 8501
# EXPOSE 8000
# EXPOSE 8501

# ------------------------------
# CMD padrão (opcional)
# ------------------------------
# Não define um comando fixo para não travar; VS Code gerencia o bash do container
