# Dockerfile para container QuantumFinance (API + Streamlit)
FROM python:3.10-slim

WORKDIR /workspace

# Instala dependências do sistema
RUN apt-get update && apt-get install -y build-essential && rm -rf /var/lib/apt/lists/*

# Copia requirements e instala pacotes Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia código-fonte
COPY ../src ./src

# Expõe portas para API (8000) e Streamlit (8501)
EXPOSE 8000 8501

CMD ["tail", "-f", "/dev/null"]
