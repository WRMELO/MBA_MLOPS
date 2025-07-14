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

### ✅ [PLACEHOLDER] Próximas entradas

- _Exemplo: Configuração do `dvc remote` com backend MinIO finalizada._
- _Exemplo: Registro do primeiro experimento no MLflow._
- _Exemplo: Deploy do FastAPI em ambiente de homologação._

---

## 🔒 Observações

- Este histórico faz parte das **boas práticas de rastreabilidade MLOps**, complementando o versionamento do Git.
- Mantém contexto de decisões para revisões, auditorias ou reuso futuro.

---

📌 **Última atualização:** 2025-07-12

