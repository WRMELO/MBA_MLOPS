# 📄 LEIA-ME — Detalhamento Acadêmico das Exigências

Este documento complementa o README principal com respostas detalhadas, em formato acadêmico, atendendo às exigências apresentadas. Ele descreve a estrutura do projeto, rastreamento, versionamento, documentação e validação final do sistema QuantumFinance.

---

## 1. **Estrutura do Projeto e Template Base**

O projeto foi inicialmente criado a partir de um **template Cookiecutter**, o qual foi estendido com diretórios adicionais para atender às necessidades de MLOps e integração com serviços externos. A estrutura final do projeto é organizada da seguinte forma:

```
MBA_MLOPS/
│── container_solução/        # Dockerfile, docker-compose e scripts de execução
│── src/                      # Código-fonte principal
│   └── ativos/               # API, Streamlit, transformadores
│── models/                   # Modelos treinados (v1-final)
│── data/                     # Dados de entrada e processados
│── notebooks/                # Notebooks de desenvolvimento
│── mlruns/                   # Diretório de rastreamento MLflow
│── minio_data/               # Armazenamento MinIO
│── postgres_data/            # Base de dados PostgreSQL
│── reports/                  # Relatórios e saídas de análise
│── README.md                 # Documento de uso
│── LEIA-ME.md                # Este documento acadêmico
```

📌 **Conclusão**: a formatação modular garante extensibilidade e clareza no fluxo de trabalho.

---

## 2. **Rastreamento de Experimentos (MLflow)**

O rastreamento dos experimentos foi conduzido utilizando o **MLflow**, que:

- Armazena os experimentos localmente no diretório ``.
- Permite visualização via interface web quando o serviço MLflow está ativo.
- Registra parâmetros, métricas, artefatos e versões dos modelos.

📌 **Conclusão**: todos os experimentos realizados estão disponíveis em `.mlruns`, atendendo ao requisito de rastreabilidade.

---

## 3. **Versionamento de Código e Modelos**

O versionamento foi garantido em múltiplos níveis:

- **Git**: versiona todo o código-fonte e documentos do projeto.
- **DVC (Data Version Control)**: utilizado para controle de versões de datasets e artefatos de modelo.
- **MinIO**: armazena versões consolidadas de modelos e dados em buckets específicos.
- **PostgreSQL**: mantém metadados e registros de auditoria.

📌 **Conclusão**: a solução implementa versionamento completo, alinhado com práticas modernas de MLOps.

---

## 4. **Documentação da API**

A API foi desenvolvida com **FastAPI**, que gera automaticamente documentação interativa no formato OpenAPI. Essa documentação pode ser acessada no endpoint:

- [http://localhost:8080/docs](http://localhost:8080/docs)

Além da geração automática, a descrição dos endpoints, parâmetros e exemplos foi incluída nos próprios docstrings da aplicação.

📌 **Conclusão**: a documentação está disponível de forma dinâmica e interativa via Swagger UI.

---

## 5. **Validação e Exemplo de Integração (Streamlit)**

A validação do sistema foi realizada utilizando a interface **Streamlit**, que serve como ponto de interação final com o usuário. O formulário exibido na aplicação inclui todos os 21 campos necessários, além de um exemplo pré-preenchido que pode ser utilizado como referência.

### **Exemplo de Preenchimento (Default no Formulário)**

- **Idade:** 35
- **Renda Anual:** 65.000
- **Salário Mensal:** 5.000
- **Mix de Crédito:** Standard
- **Dívida Atual:** 7.500
- **Utilização de Crédito:** 35%

Esse exemplo não apenas valida a integração com a API, como também demonstra a aplicação prática do modelo em um ambiente real.

📌 **Conclusão**: a validação via Streamlit comprova o funcionamento ponta a ponta (UI → API → Modelo), atendendo plenamente ao requisito.

---

## ✅ Conclusão Geral

A solução final do projeto QuantumFinance integra práticas acadêmicas e industriais:

- Estrutura modular baseada em template extensível.
- Rastreabilidade completa via MLflow.
- Versionamento robusto em múltiplos níveis.
- Documentação automatizada e acessível.
- Interface final validada e pronta para uso.

📌 **Status:** Exercício concluído com sucesso, cumprindo todas as exigências formais e técnicas.

