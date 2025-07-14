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



### ✅ [PLACEHOLDER] Próximas entradas

- _Exemplo: Configuração do `dvc remote` com backend MinIO finalizada._
- _Exemplo: Registro do primeiro experimento no MLflow._
- _Exemplo: Deploy do FastAPI em ambiente de homologação._

---

## 🔒 Observações

- Este histórico faz parte das **boas práticas de rastreabilidade MLOps**, complementando o versionamento do Git.
- Mantém contexto de decisões para revisões, auditorias ou reuso futuro.

---


