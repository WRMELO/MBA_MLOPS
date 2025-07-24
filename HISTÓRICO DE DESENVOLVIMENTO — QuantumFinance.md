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

### ✅ 2025-07-15 — Consolidação FINAL CURATED V1.1 + Fitting supervisionado rastreado

- **Nova camada `CURATED V1.1` criada:** binning supervisionado revisado, agrupamento de categorias raras e OHE restrito aplicado apenas em variáveis com sentido de negócio (`Month`, `Occupation_Group`, `Payment_Behaviour`).
- **Diagnóstico de footprint:** shape reduzido de ~6.300 colunas para apenas 93, validando fitting local sem OOM Killer.
- **Versionamento atômico:** `train_curated_v1_1.csv` e `test_curated_v1_1.csv` adicionados via `dvc add`, `dvc push` realizado com sucesso para o bucket `mba-mlops-bucket` no MinIO.
- **Fitting supervisionado baseline rodado:** `DecisionTreeClassifier` (`max_depth=5`), com `LabelEncoder` aplicado para eliminar colunas `object` remanescentes (`_Binned`, `Credit_History_Age`).
- **Endpoint S3 dentro do container corrigido:** troca de `127.0.0.1` para `minio:9000` garantiu persistência do modelo no backend MinIO sem erro `ConnectionClosedError`.
- **Tracking MLflow validado:** servidor `mlflow` na mesma rede Compose, exposto via `127.0.0.1:5000` para acesso local, com artefato salvo no bucket remoto.
- **Resultados do baseline:** Accuracy **0.6881**, F1 Macro **0.6519** — coerente com os parâmetros supervisionados.
- **Decisão fixada:** 
  - `127.0.0.1` jamais usado como endpoint interno para persistência de artefatos.
  - Todos os blocos de fitting devem manter export explícito de `MLFLOW_S3_ENDPOINT_URL` com nome de serviço Docker.
  - Prints de acesso ao `127.0.0.1:5000` ficam apenas para acesso do UI fora do container.

📌 Pronto para Grid Search supervisionado, tuning de hiperparâmetros ou pipeline de stacking, mantendo rastreabilidade integral conforme **PROTOCOLO V5.4**.

### ✅ 2025-07-22 — Inferência Final Random Forest Tuned com Tracking MLflow

- **Problema identificado:** tentativa de carregar modelo via `mlflow.sklearn.load_model("runs:/...")` resultou em `MlflowException: Run not found`, mesmo com artefatos salvos no bucket MinIO.
- **Diagnóstico resolvido:** diretório `.mlruns` estava presente e válido, mas o MLflow não estava apontando corretamente para ele.
- **Correção aplicada:** inserido `mlflow.set_tracking_uri("file:/workspace/.mlruns")` explicitamente no notebook, evitando heurísticas.
- **Inferência executada com sucesso:** 
  - Recarregou o modelo da execução `"4e56a5afe29a4a26b962c220fef03f5d"`;
  - Reaplicou `OrdinalEncoder` usando as colunas categóricas do treino;
  - Removeu a coluna `Credit_Score` do conjunto de teste;
  - Realizou predição final no `test_curated_v1_1.csv`;
  - Salvou o resultado em `/workspace/data/predictions/random_forest_final_test_predictions.csv`;
  - As predições apresentaram coerência com distribuição prevista.

---

### ✅ 2025-07-22 — Preparação para Versionamento Final das Predições com DVC

- **Bloco de `dvc add` executado**, mas resultou em erro de `dubious ownership` no Git (`exit status 128`) ao tentar adicionar o `.dvc`.
- **Motivo do erro:** Git recusou-se a operar dentro do diretório `/workspace` por não considerá-lo seguro, conforme política de segurança interna.
- **Solução registrada e aplicada:** inserido comando:

  git config --global --add safe.directory /workspace
---

### ❌ 2025-07-22 — Falha Crítica de Persistência para Consumo pela API (Erro #2025-07-22-014)

- **Erro detectado:** O pipeline de modelagem supervisionada seguiu corretamente o rastreamento com MLflow, mas **não salvou externamente o modelo final nem o encoder**, inviabilizando o uso da API `api.py`.
- **Causa raiz:** O modelo foi rastreado via MLflow (`run_id: 4e56a5afe29a4a26b962c220fef03f5d`), mas o `OrdinalEncoder`, essencial para transformar os dados de entrada, **foi recriado dinamicamente no notebook e não serializado**.
- **Impacto:** A API não consegue realizar predições, pois não possui os arquivos `.pkl` necessários. Tentativas de inferência geraram `MlflowException` ou `KeyError` ao aplicar transformações.
- **Gravidade:** ALTA — falha estrutural, rompe rastreabilidade, viola o Plano de Atividades (etapa 7) e o PROTOCOLO V5.4, item 2.3 e 3.1.
- **Correção aplicada:** Criação imediata de bloco técnico para:
  - Recarregar modelo com `mlflow.sklearn.load_model(...)`;
  - Recriar e persistir `OrdinalEncoder`;
  - Salvar ambos em `/workspace/models/final_model.pkl` e `/workspace/models/final_encoder.pkl`.
- **Ação preventiva:** A partir deste ponto, **toda etapa de fitting será obrigatoriamente acompanhada de bloco de persistência externa** para garantir compatibilidade com API e deploy.

### ✅ 2025-07-22 — Substituição do Modelo Base por Random Forest Otimizado + Registro no MLflow

- **Motivação:** O modelo anterior (`DecisionTreeClassifier(max_depth=5)`) apresentou acurácia limitada (~0.689), inferior à performance registrada em execuções anteriores (~0.79).
- **Decisão técnica:** Substituir completamente a etapa `RECONSTRUÇÃO FINAL DO MODELO COM TRATAMENTO COMPLETO CONFORME CURATED V1.1`, adotando `RandomForestClassifier` com `GridSearchCV` (5 folds) e parâmetros realistas.
- **Tratamento replicado:** Reaplicação total do pipeline `curated_v1_1`, incluindo substituição de placeholders, conversão de `Credit_History_Age`, coerção de tipos e `OrdinalEncoder` supervisionado com controle para desconhecidos.
- **Resultado final:** Melhor configuração:  
  `{'max_depth': 20, 'max_features': 'sqrt', 'min_samples_leaf': 3, 'n_estimators': 100}`  
  Acurácia no conjunto de treino: **0.8803**
- **Persistência:** 
  - Modelo salvo localmente em: `/workspace/models/final_model.pkl`
  - Encoder salvo localmente em: `/workspace/models/final_encoder.pkl`
- **Registro MLflow:**
  - Tracking URI: `file:/workspace/.mlruns`
  - Experimento: `modelo_otimizado_rf`
  - Run name: `random_forest_otimizado`
  - Parâmetros, métrica e artefato registrados com sucesso.

📌 Pronto para inferência via `api.py` com artefatos rastreáveis e performance validada.


---

### ❌ 2025-07-23 — Falha crítica no consumo da API e reinício do desenvolvimento

- **Problema identificado:** Durante a tentativa de consumo do modelo via interface `Streamlit`, foi gerado erro do tipo `ValueError: columns are missing`, indicando que os dados enviados não eram compatíveis com o pipeline de predição salvo.
    
- **Causa raiz:** O pipeline treinado com `OrdinalEncoder` e `KBinsDiscretizer` foi construído sobre um subconjunto reduzido das colunas reais do `curated_v1_1`, mas a aplicação `Streamlit` preparava os dados com um conjunto muito maior de colunas (inclusive as já transformadas, como `Occupation_Group_*`, `*_Binned_*`, etc.).
    
- **Impacto:** A tentativa de inferência gera um `diff` entre as colunas esperadas pelo pipeline salvo e as fornecidas pelo formulário JSON da API, causando exceção em tempo de execução.
    
- **Gravidade:** ALTA — impossibilita o deploy da aplicação, mesmo com modelo funcional e encoder salvo.
    
- **Tentativas de correção realizadas:**
    
    - Verificação do pipeline `pipeline_completo.pkl` com `.named_steps['preprocessor']` para mapear as colunas esperadas.
        
    - Teste local de inferência manual com os mesmos dados — erro persistiu.
        
    - Print do erro completo via interface Streamlit confirmou **incompatibilidade estrutural entre `X` esperado e `X` enviado**.
        
- **Decisão final:**
    
    1. **Arquivar o pipeline atual como falho para consumo em produção.**
        
    2. **Reiniciar todo o desenvolvimento, do zero, agora de forma completa, integrando os seguintes pontos desde o início:**
        
        - Pré-processamento único e rastreável;
            
        - Encoding supervisionado com controle de cardinalidade;
            
        - Persistência acoplada ao pipeline (`joblib`) com schema fixo;
            
        - Compatibilidade garantida com API externa (`FastAPI`, `Streamlit`, etc.);
            
        - Teste de inferência ao final do fitting para validar shape e ordem das colunas.
            



---

### 🔁 2025-07-23 — Decisão de refazer o notebook `runs_desenvolvimento` com MLflow pleno

- **Problema identificado:** A tentativa de integração entre o pipeline treinado (`pipeline_completo.pkl`) e a interface de consumo via API (FastAPI + Streamlit) falhou por inconsistência estrutural entre os dados esperados pelo modelo e os dados enviados pela aplicação.
    
- **Evidência:** Erro do tipo `ValueError: columns are missing` foi registrado, evidenciando descompasso entre o vetor de entrada gerado pelo frontend e o que o pipeline espera após transformação (`OrdinalEncoder` + `KBinsDiscretizer`).
    
- **Causa raiz:** O pipeline foi construído e salvo separadamente, sem garantir consistência plena com o fluxo de ingestão e serialização usado no momento da predição. O ciclo de ML não estava fechado corretamente.
    
- **Impacto:** A aplicação completa (modelo + API + UI) tornou-se não funcional, inviabilizando o deploy e os testes de inferência em produção.
    

#### ✅ Decisão estratégica

A partir deste ponto, todo o desenvolvimento será **refeito a partir do notebook `runs_desenvolvimento.ipynb`**, com as seguintes diretrizes fixas:

1. **Utilização plena do MLflow desde o início do ciclo**, incluindo:
    
    - Registro de modelos com hiperparâmetros, métricas e artefatos;
        
    - Salvamento versionado com `run_id` rastreável;
        
    - Log estruturado de pipelines e transformações;
        
    - Validação completa do modelo com `signature` e `input_example`.
        
2. **Eliminação de serializações manuais (`joblib.dump`) avulsas**, substituindo por persistência estruturada via MLflow.
    
3. **Reformulação do ciclo de experimentação**, com:
    
    - Separação clara entre etapas de pré-processamento, treino, avaliação e exportação;
        
    - Conformidade entre os dados de treino e os dados esperados no deploy;
        
    - Versionamento automático e rastreável de cada execução.
        

📌 Esta redefinição é mandatória e segue o **PROTOCOLO V5.4**, encerrando oficialmente a fase anterior de prototipação e iniciando a etapa de **desenvolvimento consolidado e pronto para produção**.


---

### 🔎 2025-07-23 — Discussão sobre persistência do pipeline e rastreabilidade com MLflow

- **Contexto atual:** Após a etapa de treinamento e tuning com `GridSearchCV` usando `RandomForestClassifier`, obteve-se desempenho superior ao baseline (Acurácia **0.7770**, F1 Macro **0.7611**), registrado e rastreado via MLflow.
    
- **Discussão técnica em andamento:**
    
    - Debate sobre **momento correto para persistência** do pipeline final.
        
    - Avaliação se o encoder (`OrdinalEncoder`, `KBinsDiscretizer`) está sendo salvo **dentro do pipeline** rastreado, ou se é necessário salvar como artefato adicional.
        
    - Verificação se o pipeline final (`sklearn.pipeline.Pipeline`) inclui todas as etapas de transformação necessárias para consumo direto na API.
        
    - Conclusão parcial: embora o modelo esteja sendo corretamente salvo com `mlflow.sklearn.log_model(...)`, é necessário garantir que:
        
        - O **schema do input (`signature`)** seja registrado corretamente;
            
        - O **`input_example`** reflita a estrutura real de predição (com colunas transformadas);
            
        - As etapas de transformação estejam acopladas ao `Pipeline` para **evitar perda de contexto na inferência**.
            
- **Risco identificado:** Se o pipeline final não estiver completo (com encoder embutido), **a API falhará novamente** como no ciclo anterior.
    
- **Ação determinada:**
    
    1. Garantir que o pipeline final contenha o encoder treinado e seja **único artefato serializado**;
        
    2. **Evitar múltiplos `.pkl` avulsos**, preferindo a serialização única do `Pipeline` completo via MLflow;
        
    3. Confirmar a compatibilidade do modelo via `mlflow.pyfunc.load_model()` e teste manual de inferência antes do deploy;
        
    4. Incluir bloco de verificação de `.signature` e `.input_example` no experimento antes da exportação final.
        

### ✅ 2025-07-23 — Etapas 2, 3 e 4 reexecutadas e modelo congelado oficialmente como versão `v1-final`

Após a detecção de inconsistências técnicas nos registros anteriores (run_id `79e0f222...` e `aea76868...`), foi refeito todo o processo de modelagem, validação e registro para garantir integridade completa e conformidade com o PROTOCOLO V5.5.

#### Etapa 2 (Reexecutada)

- O modelo Random Forest foi treinado diretamente com os melhores hiperparâmetros já conhecidos, sem GridSearch adicional:
  - `max_depth = 20`
  - `max_features = 'sqrt'`
  - `min_samples_leaf = 3`
  - `n_estimators = 200`
- O pipeline foi construído com `OrdinalEncoder` acoplado e serializado integralmente via `mlflow.sklearn.log_model(...)`;
- Foi salvo com `input_example` coerente, forçado para `object`, garantindo integridade de tipos;
- O run final foi salvo sob:
  - `run_id = 7077ebfbf696487384bd5a59034170c5`
  - `experimento = modelo_rf_otimizado_final`

#### Etapa 3 (Validação Completa)

- O modelo foi carregado via `pyfunc.load_model()` e testado com `X_test` real;
- A inferência foi realizada com sucesso, sem erros de shape ou tipo;
- A `signature` foi recuperada e validada estruturalmente contra as colunas reais;
- O `input_example.json` original, embora corrompido para leitura via Pandas, foi substituído por uma exportação rastreável:
  - `input_example_rf_v1.csv` salvo em `/workspace/data/examples/`
  - Estrutura auditável e versionável, compatível com API REST, documentação externa e deploys automatizados.

#### Etapa 4 (Congelamento Oficial)

- O modelo foi oficialmente promovido à versão `v1-final`;
- Foi gerado e salvo o manifesto JSON contendo os metadados da versão congelada:
  - Local: `/workspace/models/congelados/manifesto_modelo_rf_v1.json`
- Este modelo é agora a base canônica para as etapas seguintes: exportação de pipeline, deploy da API FastAPI e interface via Streamlit.

📌 A partir deste ponto, qualquer nova alteração deve ser registrada como nova versão (`v2`, `v3`, etc.), mantendo o `v1-final` imutável para rastreabilidade de produção.

#### Etapa 5 (Exportação física, testes de API e tratamento de erros críticos)

Com o congelamento oficial do modelo `v1-final`, iniciou-se a etapa de exportação física e integração com as aplicações externas (API FastAPI e interface Streamlit). No entanto, esta fase revelou uma série de erros operacionais, estruturais e conceituais, que exigiram diagnóstico profundo, correções e ajustes de protocolo.

**5.1 Exportação física do modelo**

- O pipeline completo foi exportado a partir do MLflow com sucesso para:
  - `/workspace/models/exportado_rf_v1_final/pipeline`
- O manifesto auxiliar foi criado no formato `.json`, contendo `run_id`, `timestamp`, caminho do modelo e instrução `mlflow.pyfunc.load_model(...)` para uso futuro:
  - `/workspace/models/exportado_rf_v1_final/manifesto_rf_v1.json`

**5.2 Teste inicial com FastAPI**

- O script `test_api.py` foi criado para simular chamadas à API utilizando o exemplo salvo `input_example_rf_v1.csv`.
- Ao rodar o teste, ocorreu **erro 500**, com mensagem clara de **incompatibilidade com o schema MLflow**.
- A mensagem indicava, por exemplo: `Incompatible input types for column Month_August. Can not safely convert bool to int64`.

**5.3 Diagnóstico e causa raiz**

- Descobriu-se que os dados utilizados como input foram criados manualmente, desrespeitando o tipo inferido durante o registro do modelo.
- Apesar de todos os dados estarem disponíveis e versionados, a inferência do schema havia sido feita com tipos específicos (`int64`, `float64`, `string`), e não permitia `bool` mesmo quando semanticamente equivalentes.
- Isso gerou **erros de schema enforcement rígido** do MLflow, mesmo com estrutura de colunas correta.

**5.4 Correção com pipeline oficial**

- A partir do pipeline oficial registrado, foi feita uma aplicação real sobre os dados `train_curated_v1_final.csv` para gerar um `input_example` compatível:
  - O DataFrame de entrada foi transformado com o pipeline salvo;
  - As colunas foram renomeadas e os tipos ajustados conforme o schema oficial (evitando booleanos);
  - Esse input corrigido foi usado tanto no teste da API quanto na interface Streamlit.

**5.5 Problemas com caminhos e versionamento**

- Houve falhas repetidas ao localizar os arquivos versionados, como `train_curated_v1_final.csv`;
- Isso ocorreu por **uso incorreto de caminhos antigos (`/data/staged`)**, **erros de digitação**, e **tentativa de uso de arquivos não rastreados pelo DVC**;
- Como correção, os caminhos foram restabelecidos com base nos notebooks anteriores (ex: `adequacao_desenvolvimento.ipynb`), e a recuperação via DVC foi explicitamente exigida antes de qualquer uso.

**5.6 Testes finais da API e da interface Streamlit**

- Após validações, o modelo `v1-final` foi corretamente carregado pela API FastAPI;
- A interface Streamlit foi conectada à API usando o novo input;
- As predições foram recebidas com sucesso e exibidas corretamente.

**Conclusão da Etapa 5:**

- Apesar de o modelo estar congelado corretamente, a integração revelou falhas importantes na consistência entre input de inferência e schema inferido;
- Os erros foram solucionados com reconstrução baseada no pipeline real;
- Foram bloqueadas heurísticas de inferência automática de tipos ou nomes, passando-se a exigir input gerado diretamente pelo pipeline e versão oficial.

