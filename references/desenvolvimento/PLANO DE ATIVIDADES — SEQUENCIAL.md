
---
## Contexto

Este Plano de Atividades traduz o **Plano Conceitual** em uma sequência lógica de passos técnicos, considerando a ordem natural para:

- Reduzir retrabalho,
    
- Garantir versionamento desde o início,
    
- Rastrear tudo no Git, DVC e MLflow,
    
- Manter a camada de API e frontend consistente com o modelo versionado no MinIO.
    

Cada atividade está descrita com **justificativa técnica**, em linha com **práticas reais de MLOps**, mas dimensionada para projeto **individual-acadêmico**.

---

## 1. Preparar o repositório base

**Por que primeiro?**  
Define a estrutura `cookiecutter-data-science`, cria `.gitignore` e organiza pastas (`data/raw`, `notebooks`, `src/`, `.devcontainer/`). Assim, evita perder tempo migrando scripts depois.

---

## 2. Configurar o DevContainer

**Por que antes de mexer em código?**  
Garante ambiente controlado com Python 3.10, extensões VS Code, Dockerfile e `devcontainer.json`. Assim, qualquer EDA ou API criada já roda no mesmo ambiente, sem “works on my machine”.

---

## 3. Conectar o MinIO

**Por que nesta fase?**  
Antes de iniciar DVC e MLflow, o backend remoto deve estar funcional. Cria bucket(s) para datasets brutos, processados e artefatos de modelo, emulando S3. Assim, garante versionamento real.

---

## 4. Coletar e armazenar o dataset

Baixar o dataset do Kaggle (`credit-score-classification`), guardar em `data/raw/` e subir a primeira versão no MinIO via DVC.

**Por que não rodar EDA antes?**  
Porque dados brutos devem ser versionados na forma original. Isso é a base para auditoria.

---

## 5. Rodar EDA e pré-processamento

Cria notebooks exploratórios:

- Verifica dados faltantes,
    
- Faz split treino/teste,
    
- Salva `data/processed/`.
    

**Por que aqui?**  
Só depois de versionar os brutos é que faz sentido processar. O artefato limpo também é enviado para o bucket MinIO, gerando nova versão no DVC.

---

## 6. Treinar o modelo e rastrear com MLflow

Executa script ou notebook para:

- Treinar o modelo,
    
- Registrar parâmetros, métricas no MLflow,
    
- Gerar `.pkl` local.
    

**Por que MLflow aqui?**  
Sem dados limpos, não há como treinar. E o rastreamento de experimentos começa já atrelado ao commit e à versão do dataset no MinIO.

---

## 7. Registrar o modelo e salvar no MinIO

Depois de treinar, o modelo `.pkl` e os metadados são versionados:

- `mlflow register model` localmente,
    
- Upload para MinIO via DVC.
    

**Justificativa:**  
Isso garante que a API vai consumir **exatamente a versão aprovada**, sem risco de usar um arquivo fora do fluxo.

---

## 8. Desenvolver a API FastAPI

Cria endpoint `/predict`:

- Carrega modelo `.pkl` da versão correta,
    
- Implementa autenticação API Key,
    
- Adiciona throttling básico com `slowapi`.
    

**Por que agora?**  
A API precisa do modelo final já registrado, para estar 100% coerente.

---

## 9. Desenvolver o frontend Streamlit

Monta app Streamlit:

- Coleta input do usuário,
    
- Chama a API,
    
- Mostra resposta.
    

**Por que depois da API?**  
Sem endpoint funcional e autenticado, o frontend não pode validar nada.

---

## 10. Teste end-to-end no DevContainer

Valida tudo:

- Notebook → MLflow → modelo versionado → API → frontend → chamada real.
    
- Registra logs e printa status.
    

**Por que fechar assim?**  
É o checkpoint para entregar o pipeline rastreável e auditável, em linha com o PROTOCOLO V5.4.

---

## Compromisso

Cada etapa será rastreada por:

- Bloco Markdown explicativo,
    
- Código autocontido,
    
- Registro incremental no Git/DVC/MinIO/MLflow.
    

**Fim do Plano de Atividades Sequencial (V5.4)**