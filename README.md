# QuantumFinance

## 📌 Introdução

O projeto **QuantumFinance** implementa uma solução completa de classificação de crédito, desde o modelo treinado e versionado até a disponibilização via **API FastAPI** e **interface Streamlit**.

Todo o desenvolvimento foi conduzido em um **DevContainer** customizado (conforme descrito no histórico), que integra os serviços de MLflow, MinIO, PostgreSQL e ambiente de notebooks. Para a entrega final, a aplicação foi encapsulada em um **container exclusivo** chamado `container_solução`, responsável por rodar **API** e **Streamlit** de forma isolada.

O atendimento às exigências da entrega acadêmica podem ser visualizadas no documento LEIA-ME APÓS O README

---

## 🚀 1. Montagem do DevContainer

Para desenvolvimento, utiliza-se o `devcontainer_mba_mlops`, configurado via VS Code Remote Containers. Esse container conecta-se à rede `mba_mlops_mlops_network` e acessa MinIO, PostgreSQL e MLflow.

**Como subir:**

```bash
docker compose up -d
```

> O arquivo `docker-compose.yml` raiz já orquestra todos os serviços necessários.

---

## 🚀 2. Montagem do Container de Solução

A solução final roda isolada no container `quantumfinance_app`, localizado em `container_solução/`.

### **Passos para montar:**

1. Criar estrutura (já criada no projeto):

```bash
./setup_container_solucao.sh
```

2. Construir e subir o container:

```bash
./container_solução/run_container.sh
```

3. Verificar que está ativo:

```bash
docker ps
```

---

## 🚀 3. Iniciando API e Streamlit

Com o container ativo, inicie os serviços:

```bash
./start_services.sh
```

- **API FastAPI**: [http://localhost:8080/docs](http://localhost:8080/docs)
- **Interface Streamlit**: [http://localhost:8600](http://localhost:8600)

---

## 🔐 4. Autenticação e Limite de Requisições

- Todas as requisições à API exigem o cabeçalho `X-API-Key` (valor padrão: `quantumfinance-secret`).
- Implementado **throttling**: máximo de **5 requisições/minuto por IP**.

---

## ✅ 5. Estrutura da Solução

- `src/ativos/api_preditor_v1.py` → API FastAPI com autenticação e throttling.
- `src/ativos/interface_streamlit_v1.py` → Interface Streamlit que envia automaticamente o cabeçalho correto.
- `src/ativos/transformador_input.py` → Transformação dos 21 campos humanos para 92 features esperadas pelo modelo.
- `models/exportado_rf_v1_final/` → Modelo `v1-final` carregado via `joblib`.
- `container_solução/` → Dockerfile, requirements, compose e scripts de inicialização.

---

## ✅ 6. Conclusão

- API funcional e segura, com retorno formatado.
- Streamlit integrado, exibindo previsões `Standard`, `Good` ou `Poor`.
- Toda a solução pode ser reproduzida com os passos acima, sem ajustes adicionais.

📌 **Status:** Projeto pronto para entrega, seguindo o **PROTOCOLO V6.1**.

