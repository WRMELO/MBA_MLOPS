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

📌 **Última atualização:** 2025-07-12


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

