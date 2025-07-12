
---
## Objetivo

Este projeto estabelece uma aplicação de práticas de MLOps mínimas porém realistas em um contexto acadêmico-individual. O modelo de score de crédito será rastreável, versionado e disponibilizado via API segura, validando integração com um frontend simples. O uso do MinIO emula um bucket S3, garantindo versionamento de datasets e modelos fora do Git, prática essencial em pipelines de dados reais.

---

## 1 Estrutura de Repositório

O template `cookiecutter-data-science` organiza as pastas em `data/`, `notebooks/`, `models/` e `src/`. Essa estrutura padrão facilita a separação de dados brutos, processados, scripts e notebooks, e se encaixa bem com o versionamento adicional no MinIO.

O diretório `.devcontainer/` conterá o Dockerfile e o `devcontainer.json`, padronizando o ambiente com Python 3.10, bibliotecas mínimas, e extensões do VS Code necessárias para desenvolvimento. Isso garante que todo o pipeline seja reproduzível, do EDA até a API.

---

## 2 Versionamento de Código e Dados

Para o código, o Git cobre rastreamento de scripts, notebooks e configurações. Os dados e modelos são versionados usando DVC configurado com backend remoto apontando para um bucket MinIO, que replica a estrutura de um S3 privado. Isso resolve a limitação do Git para arquivos grandes e simula um fluxo MLOps real.

Branches simplificados (`main`, `dev`) mantêm separação entre produção e desenvolvimento. Pull Requests servem como auto-revisão de mudanças, mesmo sem equipe.

---

## 3 Rastreamento de Experimentos

Os experimentos de treino serão rastreados localmente com MLflow, armazenando métricas, parâmetros e artefatos. O MLflow Registry é integrado com DVC para vincular as versões dos modelos no bucket MinIO. O `mlflow.autolog()` será ativado para garantir que todos os parâmetros e métricas sejam registrados automaticamente.

Essa configuração combina rastreio local de execução com versionamento de artefatos grande porte via MinIO.

---

## 4 API de Predição

A API será construída com FastAPI. O framework é leve, suporta documentação automática (Swagger UI) e é de fácil integração com o modelo salvo. Para segurança, o endpoint `/predict` exigirá autenticação via chave API no header `x-api-key`. A biblioteca `slowapi` fará o controle de requisições por IP/chave, simulando throttling mínimo de governança.

A imagem Docker incluirá o modelo `.pkl` versionado, baixado do MinIO, para garantir que a versão consumida seja a mesma registrada no pipeline.

---

## 5 Frontend com Streamlit

Um app Streamlit consumirá o endpoint da API para validação prática da predição. É uma solução leve e rápida para exibir inputs, fazer requisições POST para a API e mostrar resultados. As chaves de acesso (endpoint, chave API) serão mantidas em `.streamlit/secrets.toml` para não expor credenciais em código.

---

## 6 Uso do MinIO como Emulador S3

O MinIO será configurado como backend remoto do DVC. Os arquivos versionados (datasets brutos, limpos, modelos `.pkl`) são armazenados nos buckets do MinIO. Isso simula o padrão de produção com AWS S3, mas sem custos ou dependências de nuvem pública. A integração local simplifica testes de fluxo de dados real e treino incremental.

Essa camada aumenta a aderência ao conceito de pipelines reprodutíveis com rastreio de versões de datasets, sem depender apenas do Git.

---

## 7 DevContainer

A aplicação completa (API FastAPI e Streamlit) roda dentro de um único container definido no Dockerfile. Esse container se conecta ao MinIO localmente via credenciais configuradas em variáveis de ambiente. O ambiente base usa Python 3.10, evitando inconsistências de dependências na máquina host.

---

## 8 Justificativa para Exclusões

A estrutura não prevê monitoramento de drift ou CI/CD automatizado, pois o foco é demonstrar versionamento e rastreamento mínimos sem custos de infraestrutura extra. O modelo é academicamente válido para entrega como exercício de MLOps simplificado.

---

## 9 Estrutura Final

/  
├── data/  
│ ├── raw/  
│ ├── processed/  
├── notebooks/  
├── models/  
├── src/  
│ ├── api/  
│ └── frontend/  
├── .devcontainer/  
│ ├── Dockerfile  
│ └── devcontainer.json  
├── .dvc/  
├── README.md  
├── dvc.yaml  
├── .streamlit/  
│ └── secrets.toml  
└── requirements.txt

---

## Compromisso Final

Todo o pipeline segue o PROTOCOLO V5.4. Todas as escolhas são justificadas, cada bloco de execução será autocontido e rastreável, e o versionamento de datasets/modelos será auditável via MinIO, emulando práticas reais de armazenamento em nuvem.

Fim do Plano Conceitual.