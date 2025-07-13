# Base Python 3.10 para DevContainer
FROM python:3.10-slim

# Instala utilitários básicos
RUN apt-get update && apt-get install -y     git openssh-client build-essential

# Copia dependências do projeto
COPY requirements.txt /workspace/requirements.txt
WORKDIR /workspace

# Instala dependências Python
RUN pip install --no-cache-dir -r requirements.txt

# Cria usuário padrão VS Code DevContainer
RUN useradd -ms /bin/bash vscode

# Permite extensões VS Code funcionarem
CMD ["sleep", "infinity"]
