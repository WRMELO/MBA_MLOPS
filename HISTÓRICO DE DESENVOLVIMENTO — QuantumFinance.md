# 📜 Objetivo

Este documento complementa o `README.md` e registra **decisões técnicas**, **mudanças importantes**, **erros e correções**, seguindo o **PROTOCOLO V5.4**.  

Cada entrada tem data, descrição clara e vínculo com o fluxo de versionamento.

Desenvolvido e atualizado pelo Obsidian

---

## 📌 Estrutura

- Cada bloco é datado no padrão `YYYY-MM-DD`.
- Use marcadores curtos e claros.
- Cada decisão deve ter justificativa quando aplicável.

---

## 📅 Histórico

---

### ✅ 2025-07-12

- Estrutura inicial do **DevContainer** criada com **Python 3.10**.
- **Cliente SSH (`openssh-client`) adicionado** ao `Dockerfile` para suportar `git push` via SSH.
- **Fluxo de push ajustado:** troca para HTTPS validada quando chave SSH não estava presente.
- **`Makefile` removido:** definido que não será usado neste protótipo, pois não faz parte do fluxo real.
- **`requirements.txt` revisado:** alinhado ao `Dockerfile`, cobrindo `mlflow`, `dvc[all]`, `fastapi`, `streamlit` e libs auxiliares.
- **Vault duplicado detectado:** `cofre_remoto_mba_mlops/` removido para evitar ruído.
- **Pasta `.obsidian/workspace.json` ignorada no Git:** não rastrear estado de janelas.
  
  ### ✅ 2025-07-12 — Continuação

- **Rede Docker `mlops_network` criada:** DevContainer e MinIO orquestrados no mesmo `docker-compose.yml`.
- **MinIO container rodando:** configurado com `wrm` / `senha_segura`, bucket `mba-mlops-bucket` criado via `mc` (CLI).
- **`dvc init` concluído:** repositório DVC inicializado e versionado no Git.
- **`dvc remote add` configurado:** backend MinIO definido como remoto padrão com `endpointurl: http://minio:9000`.
- **`dvc push` testado:** arquivo dummy versionado com sucesso, rastreável no bucket.
- **Infra validada end-to-end:** Compose, rede, bucket, push coerente.

---
### ✅ 2025-07-12 — Infra Compose Unificado: Windows + Linux

- Consolidado o diretório de trabalho em `C:\Users\wilso\MBA_MLOPS` montado em `/mnt/c/Users/wilso/MBA_MLOPS` no WSL.
- Definido bind mount persistente do volume PostgreSQL em `/home/wrm/pgdata` (FS Linux), evitando conflito NTFS.
- Validado subida de `postgres_mlflow` com `docker-compose up -d` rodando no FS montado.
- Conexão testada com `psql` → `mlflow_db` disponível.




📌 **Última atualização:** 2025-07-12



---

### ✅ 2025-07-12 — Continuação: Decisão de Migração Windows ➝ Linux

- Após validar a infraestrutura com **DevContainer**, **MinIO**, **DVC** e **docker-compose** rodando no ambiente Windows/WSL, detectou-se **confusão estrutural recorrente** entre:
  - Bind mounts entre **NTFS (Windows)** e **FS Linux (WSL)**.
  - Caminhos misturados (`/mnt/c/...` vs `/home/wrm/...`), gerando **inconsistências em push/pull** de artefatos pesados.
  - Problemas para renderizar imagens no `README.md` devido a divergências de versionamento local vs. GitHub.

- Identificado também ruído na montagem do **Vault Obsidian**:
  - Configuração do Vault duplicada entre host Windows e WSL.
  - Estado do `.obsidian/` nem sempre coerente com o repositório Git.

- **Ambiente Windows/WSL** exigia Docker Desktop para orquestração, mas:
  - O `docker compose` V2 rodava em NTFS, sofrendo permissões inconsistentes em volumes persistentes.
  - A rede `mlops_network` ficava sujeita a travamentos se paths não estivessem 100% alinhados.

- Para eliminar todos os riscos de permissões cruzadas, foi decidido:
  1️⃣ **Zerar o repositório WSL**, re-clonar o master `MBA_MLOPS` no **notebook Linux nativo**.
  2️⃣ Configurar o **Docker Engine CE** diretamente via `apt` (sem Snap), garantindo compatibilidade total com Compose V2.
  3️⃣ Recriar o ambiente de chaves SSH, vinculando `id_ed25519` ao GitHub com `noreply` para push rastreável.
  4️⃣ Tornar o ambiente **rootless** para `docker`, adicionando `wrm` ao grupo `docker`.

- A partir desta etapa:
  - **Infraestrutura**: `docker.sh` criado na pasta pessoal (`/home/wrm/`) para orquestrar Compose por CLI puro, sem Docker Desktop.
  - **Vault Obsidian**: Consolidado no mesmo clone, garantido em `/home/wrm/MBA_MLOPS`.
  - **DevContainer**: Mantido na mesma rede `mlops_network`, agora 100% Linux-native, sem bind mount de NTFS.
  - **Navegador recomendado**: Brave ou Chromium, para evitar lentidão no render do ChatGPT.

✅ Essa decisão **encerra o uso híbrido Windows/WSL** e garante rastreabilidade total:
  - Repositório Git unificado.
  - Backend MinIO coerente.
  - Rede Docker e containers rodando sem bloqueio de permissão.

---

📌 **Última atualização:** 2025-07-12

---
---

### ✅ 2025-07-13

- **DevContainer orquestrado como serviço Compose**, anexado à `mlops_network`, validado com `docker inspect` e `VS Code Remote Containers`.  
- **Push do DVC validado dentro do DevContainer**, usando `endpointurl: minio:9000`, sem conflito `localhost`/`minio`.  
- **Imagem `mlflow` customizada criada** (`Dockerfile.mlflow`), com `psycopg2-binary` instalado para backend PostgreSQL (`postgres_mlflow`).  
- **Problema de sintaxe do `command` no Compose V2 identificado:** strings com `\` falharam, causando loop `Restarting (1)`. Corrigido com `command:` no formato **lista YAML**, garantindo compatibilidade Compose V2 (`docker compose`).  
- **Registro de falhas PROTOCOLO:**  
  - `#2025-07-13-008`: Instrução solta para edição manual de Compose — violação do passo-a-passo único.  
  - `#2025-07-13-009`: Reincidência da heurística de “atalho de edição trivial” — bloqueio de heurística aplicado.  
- **Checklist final:** todos os containers (`postgres_mlflow`, `minio`, `mlflow`, `devcontainer_mba_mlops`) na rede única, com bind mounts coerentes, fluxo `Git ➜ DVC ➜ MinIO ➜ MLflow` validado end-to-end.

---
### ✅ 2025-07-14 — Ingestão Final e Versionamento dos Dados Reais

- **Download real executado via `kagglehub`**, dataset `credit-score-classification` baixado dentro do DevContainer, seguindo rede Compose única.
- **Diretório `data/raw/` estruturado** na raiz `/workspace`, corrigindo conflitos com `notebooks/data`.
- **Movimentação do dataset validada** usando `path` real sem heurísticas, garantindo que `train.csv` (~30 MiB) e `test.csv` (~15 MiB) estão presentes.
- **Pipeline de versionamento revisado:** 
  - `git rm --cached` aplicado para garantir que `data/raw/` não estivesse rastreado diretamente pelo Git.
  - `dvc add` executado corretamente a partir do nível `/workspace/notebooks` com path relativo `../data/raw`.
  - Cache `.dvc/cache/files/md5/` gerado com 4 blobs: 2 para os CSVs reais, 1 `.dir` e 1 bloco de controle.
- **`dvc push` realizado no terminal do container**, empurrando chunks para `mba-mlops-bucket/files/md5` no MinIO.
- **Verificação do backend MinIO feita via `mc`:**
  - `mc alias set` configurado dentro do container.
  - Blobs listados via `mc ls --recursive` confirmaram presença real dos hashes MD5 no bucket remoto.
- **Correção de heurísticas:**  
  - Registro da falha de working dir causado por Kernel em `/workspace/notebooks` versus terminal em `/workspace`.
  - Registro da anulação de qualquer inferência automática de path até o fim do projeto.
- **Pronto para EDA:** dados reais versionados, cache local e remoto coerentes, rastreio Git pendente de commit final.

### ✅ 2025-07-14 — EDA, Pré-processamento e Consolidação dos Datasets Finalizados

- **Notebook de EDA revisitado:** executado dentro do DevContainer com Kernel validado em `/workspace` para coerência de paths.
- **Pipeline de pré-processamento concluído:** 
  - Conversão de tipos numéricos (`Age`, `Outstanding_Debt`, etc.) com coerção `pd.to_numeric(errors='coerce')`.
  - Imputação de valores ausentes em colunas numéricas com mediana calculada no treino.
  - Substituição de placeholders (`_______`, `!@9#%8`, etc.) por `Unknown` em colunas categóricas.
  - Exclusão de colunas puramente identificadoras (`ID`, `Customer_ID`, `Name`, `SSN`).
  - Codificação de variáveis categóricas (`Month`, `Occupation`, `Credit_Mix`, `Payment_Behaviour`) com `pd.get_dummies()`, garantindo consistência.
- **`train_clean.csv` salvo em `data/processed/`** na raiz do repositório `/workspace`, versionado com `DVC` e push realizado com sucesso para o backend MinIO.
- **Consolidação do conjunto de teste:** 
  - Aplicação do **mesmo pipeline** do treino (`train_clean.csv`) ao `test.csv`, garantindo coerência de features.
  - `test_clean.csv` salvo em `data/processed/` com **path coerente**, corrigindo tentativas anteriores que geraram diretórios `data/` abaixo de `notebooks/`.
  - Versão final do `test_clean.csv` registrada com `DVC`, push para MinIO validado e commit no Git coerente.
- **Decisão estratégica:** camada `curated/` mantida como **fase posterior**, pois toda codificação e limpeza final permanecem dentro de `processed/` por ora, alinhado ao escopo do exercício.
- **Registro de falha evitada:** identificado que rodar `dvc add` com `CWD` incorreto (`/workspace/notebooks`) causava erros de `working_dir`. Adotada conferência obrigatória de `CWD` antes de versionamento.
- **Pronto para fase de modelagem com MLflow:** `train_clean.csv` e `test_clean.csv` auditáveis, versionados, push confirmados no bucket `mba-mlops-bucket`, preparados para rastreamento de experimentos.


### ✅ 2025-07-14 — Curated Layer Finalizada, Diagnóstico de Cardinalidade e Experimento Baseline no MLflow

- **Camada `curated/` criada:** consolidou `train_curated.csv` (~3,6 GiB) e `test_curated.csv` (~1,8 GiB), 100% numerificados e prontos para aprendizado supervisionado.
- **Diagnóstico de alta cardinalidade:** executado com `tqdm` para mapeamento de colunas não numéricas — identificados casos críticos (`ID`, `Customer_ID`, `Type_of_Loan`).
- **Feature engineering aplicado:** `binning` de `Num_of_Loan` e mapeamento de `Month` para valores numéricos, revisado dentro de notebook.
- **Processo de versionamento revisado:** push incremental `dvc push` executado no terminal externo, remote duplicado removido para manter `storage` como default único.
- **Credenciais MinIO (`wrm` / `senha_segura`) exportadas dentro do container e kernel Python — evitada falha `NoCredentialsError`.
- **`MLFLOW_S3_ENDPOINT_URL` configurado explicitamente:** apontando para `http://minio:9000` para garantir que `boto3` não busque AWS real.
- **Experimento baseline rodado:** Árvore de Decisão (`max_depth=5`), tracking `mlflow` validado com `tqdm` no loop de fitting.
- **Tracking URI interno mantido como `http://mlflow:5000`**, com links finais padronizados para `http://127.0.0.1:5000` para entrega acadêmica.
- **Output final rastreável:** Accuracy e F1 Score registrados, artefato salvo no backend MinIO/S3.
- **Pronto para expandir:** próximo passo é escalar para `GridSearchCV` e múltiplos runs rastreados com `mlflow`.

📌 **Decisão fixada:** todos os blocos técnicos devem manter barra de progresso `tqdm` para fitting e splits mais demorados, com credenciais e endpoints explicitamente declarados dentro do notebook.


### ✅ 2025-07-14 — Kernel interrompido por alta cardinalidade e decisão de reabrir Feature Engineering

- **Situação:** Durante o pipeline `Curated`, o kernel Jupyter foi interrompido repetidas vezes por estouro de memória (OOM Killer). Diagnóstico preliminar indicou que o dataset final atingiu ~6.300 colunas, geradas por `get_dummies()` indiscriminado, inviabilizando fitting local mesmo em ambiente i9 com 32 GB RAM.
- **Decisão:** Foi suspenso o push final desta versão. Optou-se por **reabrir o notebook `feature_engineering_curadoria.ipynb`** para executar uma nova abordagem de Feature Engineering focada em **reduzir cardinalidade**, com binning, agrupamento de categorias raras e encoding controlado.
- **Próximo passo registrado:** A nova camada `Curated` só será consolidada e versionada no DVC após passar por validação de footprint de memória, garantindo fitting viável em ambiente local, em aderência ao **PROTOCOLO V5.4**.

### ✅ 2025-07-15 — Consolidação Final do STAGED e Versionamento Rastreável

- **Pipeline `STAGED V1 FINAL` concluído:** unificou coerção numérica por `Occupation`, variáveis textuais limpas (`Occupation`, `Type_of_Loan_Category`), binning interpretável (`Amount_invested_monthly`, `Monthly_Balance`, `Outstanding_Debt`, `Credit_Utilization_Ratio`) e One-Hot Encoding com `CategoricalDtype` fixo.
- **Kernel interrompido anteriormente por inconsistências em `working_dir`:** detectada divergência entre `/workspace/notebooks` e `/workspace/data/` no root Git. Ponto fixo: todos os comandos `dvc add` e `git add` passam a usar caminho absoluto `/workspace/data/` dentro do notebook.
- **Bloco técnico unificado criado em Python puro (`subprocess`):** sem `!`, rodando `dvc add`, `git add`, `git commit` e `dvc push` coerente. Falha do `git add .gitignore` registrada — corrigido com verificação `os.path.exists()`.
- **Verificação de shape final:** `TRAIN` com 46 colunas, `TEST` com 45, mantendo `Credit_Score` somente no treino (target).
- **Checklist final do `STAGED`:**
  - `train_staged_v1_final.csv` e `test_staged_v1_final.csv` versionados com DVC.
  - Push concluído para o backend MinIO (`mba-mlops-bucket`).
  - Commit Git coerente, sem rastrear dados brutos.
- **Pronto para promoção ao `CURATED`:** consolidar numéricos coeridos + texto + binning/OHE como snapshot baseline rastreável.

📌 **Decisão fixada no PROTOCOLO V5.4:**  
- Todos os blocos de versionamento devem usar verificação de `CWD` e `os.path.exists()` para evitar conflitos de path.
- Versionamento deve ser atômico: coerção numérica e categórica não mais separadas em blocos múltiplos.

### ✅ [PLACEHOLDER] Próximas entradas

- _Exemplo: Configuração do `dvc remote` com backend MinIO finalizada._
- _Exemplo: Registro do primeiro experimento no MLflow._
- _Exemplo: Deploy do FastAPI em ambiente de homologação._

---

## 🔒 Observações

- Este histórico faz parte das **boas práticas de rastreabilidade MLOps**, complementando o versionamento do Git.
- Mantém contexto de decisões para revisões, auditorias ou reuso futuro.

---


