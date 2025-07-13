**QuantumFinance — MLOps Individual-Acadêmico**

---

## 🎯 **Objetivo**

Este projeto demonstra **na prática** como estruturar um **pipeline de MLOps rastreável**, **auditável** e **portável**, mesmo em um contexto **individual e local**.  
O caso de uso — **score de crédito** — é representativo, pois envolve dados tabulares reais, pré-processamento, treino de modelo supervisionado e consumo por API.

A meta é **provar** como um desenvolvedor **sozinho**, com recursos limitados, pode reproduzir práticas de **indústria**, como:

- Versionar código **e** dados de grande porte.
    
- Rastrear experimentos com controle de versão.
    
- Expor o modelo via **API segura**, consumida por **frontend**.
    
- Orquestrar tudo em ambiente isolado, **portável para cloud** se necessário.
    

---

## 🗂️ **1️⃣ Estrutura de Repositório**

**Decisão:** usar o template `cookiecutter-data-science` como base.

✅ **Por quê?**

- Mantém **clara separação** de dados brutos (`raw`), processados (`processed`), notebooks exploratórios (`notebooks`), scripts (`src/`), e modelos versionados (`models/`).
    
- Essa separação evita acúmulo de notebooks desorganizados, comum em projetos acadêmicos.
    
- É compatível com pipelines futuros (`dvc.yaml`), se o fluxo evoluir para CI/CD.
    

**Trade-offs:**

- Para times grandes, repositórios monorepo + mono DAG podem ser preferíveis.
    
- Para projeto individual, `cookiecutter` é minimalista e cobre bem o ciclo EDA → deploy.
    

---

## 🗃️ **2️⃣ Versionamento de Código e Dados**

**Decisão:** Git para código + DVC para datasets/modelos, com backend remoto **MinIO**.

✅ **Por quê?**

- **Git** não é projetado para rastrear artefatos pesados (datasets brutos ou modelos `.pkl`).
    
- O **DVC** cria ponte: rastreia hashes no repositório, mas empurra os arquivos grandes para um **bucket remoto** — aqui, o MinIO.
    
- **MinIO** emula um **S3** real, sem custos ou dependência de nuvem pública.  
    → Isso permite migração futura para AWS S3, GCS ou Azure Blob **sem reescrever scripts**.
    

**Alternativas consideradas:**

- **Só Git LFS:** Não tão eficiente para pipelines complexos; storage pode sair caro.
    
- **Repositório S3 real:** Custo operacional desnecessário em ambiente local.
    
- **Sem DVC:** Aumenta risco de sobrescrever datasets, impossível auditar experimentos antigos.
    

---

## 🗄️ **3️⃣ Rastreamento de Experimentos**

**Decisão:** usar **MLflow Tracking Server** com:

- **Backend-store:** PostgreSQL em container.
    
- **Artifact-store:** MinIO.
    

✅ **Por quê?**

- O **MLflow** é padrão de facto para rastrear **runs, métricas, hiperparâmetros e artefatos** de experimento.
    
- SQLite é frágil para múltiplos workers (trava fácil, não suporta transações complexas).
    
- **PostgreSQL** oferece **ACID**, concorrência real, e fácil migração para cloud (RDS, CloudSQL).
    
- Com o **MinIO** plugado como artifact-store, separa o “meta” do “volume”, seguindo boas práticas.
    

**Alternativas consideradas:**

- **MySQL:** similar, mas PostgreSQL tem comunidade maior no ecossistema MLOps.
    
- **Databricks MLflow Hosted:** overkill para uso individual.
    
- **Sem MLflow:** rastrear tudo manualmente → inviável para auditoria ou rollback.
    

**Limitação:**

- Usar PostgreSQL local exige orquestração Docker, mas isso reforça boas práticas de rede isolada.
    

---

## 🚀 **4️⃣ API de Predição**

**Decisão:** **FastAPI**.

✅ **Por quê?**

- É leve, **Python-native**, com Swagger docs automáticas (`/docs`).
    
- Suporta validação de payloads, headers (`x-api-key`), e integração fácil com modelos `.pkl`.
    
- Alternativas como Flask precisariam de mais boilerplate para validação e docs.
    

**Segurança:**

- Autenticação via header `x-api-key`.
    
- `slowapi` implementa **throttling mínimo**, simulando políticas reais de rate limit.
    

**Alternativas consideradas:**

- **Flask:** menos estruturado.
    
- **Django Rest Framework:** overkill para uma rota `/predict`.
    
- **Gradio:** ótimo para demos, mas não separa backend de frontend.
    

---

## 💻 **5️⃣ Frontend com Streamlit**

**Decisão:** **Streamlit** para o frontend.

✅ **Por quê?**

- É **extremamente rápido** para prototipar formulário → request → resposta.
    
- Ótimo para **demo interativo**, ideal em ambiente de protótipo ou POC.
    
- Manter chaves sensíveis em `.streamlit/secrets.toml` impede vazamentos acidentais.
    

**Alternativas consideradas:**

- **Dash:** mais flexível para dashboards complexos, mas Streamlit é mais plug-and-play.
    
- **React/Next.js:** maior poder de customização, mas exige stack JS e hosting separado.
    

**Limitação:**

- Streamlit não é ideal para produção B2C; é POC.
    

---

## ☁️ **6️⃣ Uso do MinIO como Emulador S3**

**Decisão:** usar MinIO como storage de datasets e modelos.

✅ **Por quê?**

- **Emula S3**, mas roda local → Sem custo de banda/nuvem.
    
- Permite usar **DVC remote add** com `endpointurl` e chaves `AWS_ACCESS_KEY_ID`.
    
- Tudo orquestrado na mesma **rede Docker** (`mlops_network`).
    

**Alternativas consideradas:**

- S3 real: dependência externa.
    
- GCS/Azure: similar, mas MinIO cobre dev local sem lock-in.
    

---

## 🐳 **7️⃣ DevContainer**

**Decisão:** usar **DevContainer** (`.devcontainer/Dockerfile` + `devcontainer.json`).

✅ **Por quê?**

- Garante **ambiente reprodutível**, inclusive extensões do VS Code.
    
- `Python 3.10` + dependências fixas (`requirements.txt`).
    
- Container conecta a **PostgreSQL** e **MinIO** via `mlops_network`.
    

**Alternativas consideradas:**

- Venv local: arriscado — “works on my machine”.
    
- Conda: possível, mas Docker resolve de forma mais geral.
    

---

## 🏁 **8️⃣ Justificativa para Exclusões**

✅ **Sem CI/CD automatizado:**

- Overhead injustificável para escopo individual.
    
- Fluxo manual já é rastreável via Git commits, DVC pushes, MLflow UI.
    

✅ **Sem monitoramento de drift:**

- Fora de escopo. Requer jobs cron, data pipeline online.
    

✅ **Sem orquestração de jobs:**

- Para real-time scoring, precisa de escalabilidade, que foge ao protótipo local.
    

---

## 🔗 **9️⃣ Estrutura Final**

```
/data/
  ├── raw/
  ├── processed/
/notebooks/
/models/
/src/
  ├── api/
  └── frontend/
/.devcontainer/
/.pgdata/           # Volume PostgreSQL
/.dvc/
/README.md
/requirements.txt
```

---

## 🔒 **10️⃣ Compromisso PROTOCOLO V5.4**

✅ Cada decisão é **rastreável** no `HISTÓRICO DE DESENVOLVIMENTO`.  
✅ Cada bloco de código é autocontido, validado isoladamente.  
✅ Fluxo garante rollback total de datasets, modelos, runs.  
✅ Naming, rede Docker, buckets e containers padronizados.  
✅ Toda heurística anulada é registrada.

---

## 🚩 **Resumo Final**

**Este plano não é só técnico — é uma defesa de arquitetura:**

- **Minimalista**, mas realista.
    
- Sem vendor lock-in.
    
- Pronto para migrar para cloud com PostgreSQL managed + S3 real.
    
- 100% rastreável para auditoria, POC acadêmica ou migração para time.
    

---

**Fim do Plano Conceitual — Versão de Desenvolvimento V5.5**

🔒 **Pronto para commit, auditável, sem lacunas.**  
**Quer que eu atualize agora o _Plano de Atividades_ na mesma pegada — ou aprova o Conceitual antes?**