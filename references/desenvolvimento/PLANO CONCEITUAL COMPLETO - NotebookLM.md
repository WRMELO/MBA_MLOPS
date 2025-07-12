
### **Plano Conceitual de MLOps COMPLETO: Projeto Individual QuantumFinance**

As referências neste plano são indicadas por números entre colchetes, como `ou`. Esses números correspondem a pontos específicos ou seções relevantes dentro deste próprio plano, cujos conceitos e informações foram extraídos e são suportados pelas diversas fontes fornecidas sobre Machine Learning Engineering (MLOps).

Abaixo, um índice remissivo detalhado que conecta as referências numéricas do plano aos materiais de origem correspondentes:

---

### **Índice Remissivo das Referências do Plano**

- ****: Requisitos do projeto para template de repositório, rastreamento de experimentos, versionamento de modelo, API segura com autenticação e throttling, e documentação da API.
    - **Fontes**: "EXERCICIO PARA ENTREGA.md" e "Aula 0 DS MLE Apresentação V1.2.md".
- ****: Requisitos para integração com aplicação Streamlit e utilização do dataset de classificação de score de crédito do Kaggle.
    - **Fontes**: "EXERCICIO PARA ENTREGA.md" e "Aula 0 DS MLE Apresentação V1.2.md".
- ****: Utilização do Cookiecutter para template de repositório (scaffolding) com o template `cookiecutter-data-science`.
    - **Fontes**: "Aula 2 DS MLE v1.3.md" e "Aula 2 DS MLE v1.4.md".
- ****: Estrutura padronizada de pastas do projeto (data/raw, data/processed, notebooks, models, src).
    - **Fontes**: "Aula 2 DS MLE v1.3.md" e "Aula 2 DS MLE v1.4.md".
- ****: Utilização do Git como base para versionamento de código.
    - **Fontes**: "Aula 2 DS MLE v1.3.md" e "Aula 2 DS MLE v1.4.md".
- ****: Uso simplificado de branches (devl, main/master) para organização do trabalho.
    - **Fontes**: "Aula 2 DS MLE v1.3.md" e "Aula 2 DS MLE v1.4.md".
- ****: Modificações realizadas em branches de feature ou experimentação (ex: `exploracao-inicial`).
    - **Fontes**: "Aula 3 DS MLE 2.1.md" e "Aula 3 DS MLE 2.2.md".
- ****: Conceito e processo de Pull Request (PR) e merge de código.
    - **Fontes**: "Aula 2 DS MLE v1.3.md", "Aula 2 DS MLE v1.4.md", "Aula 3 DS MLE 2.1.md" e "Aula 3 DS MLE 2.2.md".
- ****: Pull Request como prática de auto-revisão e documentação pessoal, com validação automatizada.
    - **Fontes**: "Aula 3 DS MLE 2.1.md" e "Aula 3 DS MLE 2.2.md".
- ****: Importância e uso do `.gitignore` para não versionar arquivos grandes ou sensíveis.
    - **Fontes**: "Aula 2 DS MLE v1.3.md" e "Aula 2 DS MLE v1.4.md".
- ****: Utilização do Data Version Control (DVC) para versionamento de dados e modelos, superando limitações do Git para arquivos grandes.
    - **Fontes**: "Aula 2 DS MLE v1.3.md" e "Aula 2 DS MLE v1.4.md".
- ****: Configuração do MinIO como backend de armazenamento remoto compatível com S3 para o DVC.
    - **Fontes**: "Aula 2 DS MLE v1.3.md" e "Aula 2 DS MLE v1.4.md".
- ****: Utilização do MLflow para rastreamento de experimentos, incluindo métricas, parâmetros e detalhes de execução.
    - **Fontes**: "Aula 3 DS MLE 2.1.md" e "Aula 3 DS MLE 2.2.md".
- ****: Utilização do DagsHub como plataforma centralizada para integração de Git, DVC e MLflow.
    - **Fontes**: "Aula 2 DS MLE v1.3.md", "Aula 2 DS MLE v1.4.md", "Aula 3 DS MLE 2.1.md" e "Aula 3 DS MLE 2.2.md".
- ****: Ativação do `mlflow.autolog()` para registro automático de métricas.
    - **Fontes**: "Aula 3 DS MLE 2.1.md" e "Aula 3 DS MLE 2.2.md".
- ****: Definição da função padronizada `evaluate_and_log_model` para registro consistente de métricas customizadas.
    - **Fontes**: "Aula 3 DS MLE 2.1.md" e "Aula 3 DS MLE 2.2.md".
- ****: Manutenção de um conjunto padrão de métricas para comparação de modelos.
    - **Fontes**: "Aula 3 DS MLE 2.1.md" e "Aula 3 DS MLE 2.2.md".
- ****: Registro de modelos no MLflow Model Registry para acompanhamento do histórico de versões.
    - **Fontes**: "Aula 3 DS MLE 2.1.md" e "Aula 3 DS MLE 2.2.md".
- ****: Cada nova versão no MLflow Model Registry corresponde a uma nova etapa de treinamento do modelo.
    - **Fontes**: "Aula 3 DS MLE 2.1.md" e "Aula 3 DS MLE 2.2.md".
- ****: Recomendação de baixar o arquivo binário do modelo (`.pkl`) e metadados para empacotamento com a API, em vez de carregar em tempo de execução.
    - **Fontes**: "Aula 3 DS MLE 2.1.md" e "Aula 3 DS MLE 2.2.md".
- ****: Ênfase na arquitetura imutável para a API, incorporando o modelo binário diretamente.
    - **Fontes**: "Aula 3 DS MLE 2.1.md" e "Aula 3 DS MLE 2.2.md".
- ****: Desenvolvimento da API REST encapsulada em contêiner Docker para portabilidade e isolamento.
    - **Fontes**: "Aula 3 DS MLE 2.1.md" e "Aula 3 DS MLE 2.2.md".
- ****: Definição do Dockerfile para construir a imagem do contêiner, incluindo código, dependências e modelo.
    - **Fontes**: "Aula 3 DS MLE 2.1.md" e "Aula 3 DS MLE 2.2.md".
- ****: O ECR da AWS não será utilizado, optando por um registro Docker privado ou auto-hospedado.
    - **Fontes**: "Aula 3 DS MLE 2.1.md" e "Aula 3 DS MLE 2.2.md" descrevem o ECR, com a implicação de que o plano diverge dessa ferramenta.
- ****: O API Gateway da AWS não será utilizado, com a segurança implementada na própria aplicação da API.
    - **Fontes**: "Aula 3 DS MLE 2.1.md" e "Aula 3 DS MLE 2.2.md" descrevem o API Gateway, com a implicação de que o plano diverge dessa ferramenta.
- ****: Implementação de autenticação via API keys no cabeçalho da requisição.
    - **Fontes**: "Aula 3 DS MLE 2.1.md" e "Aula 3 DS MLE 2.2.md" mencionam autenticação e chaves de API.
- ****: Documentação da API com parâmetros de entrada e saída esperados pelo modelo.
    - **Fontes**: "Aula 3 DS MLE 2.1.md" e "Aula 3 DS MLE 2.2.md" abordam a importância dos dados de entrada e saída.
- ****: Criação da aplicação frontend utilizando a biblioteca Streamlit para Python.
    - **Fontes**: "Aula 3 DS MLE 2.1.md" e "Aula 3 DS MLE 2.2.md".
- ****: Consumo do endpoint da API de score de crédito pelo frontend Streamlit.
    - **Fontes**: "Aula 3 DS MLE 2.1.md" e "Aula 3 DS MLE 2.2.md".
- ****: Armazenamento de informações sensíveis (endpoint, chave de acesso) utilizando Secrets do Streamlit (`.streamlit/secrets.toml`).
    - **Fontes**: "Aula 3 DS MLE 2.1.md" e "Aula 3 DS MLE 2.2.md".
- ****: Utilização de componentes visuais (widgets) do Streamlit para coletar dados do usuário e fornecer feedback visual (spinners, mensagens de sucesso/erro).
    - **Fontes**: "Aula 3 DS MLE 2.1.md" e "Aula 3 DS MLE 2.2.md".
- ****: Uso de feedback visual durante chamadas à API, como spinners e mensagens de status.
    - **Fontes**: "Aula 3 DS MLE 2.1.md" e "Aula 3 DS MLE 2.2.md".
- ****: Automação de workflows de CI/CD com GitHub Actions, disparados por pushes para a branch principal.
    - **Fontes**: "Aula 4 DS MLE 1.3.md" e "Aula 4 DS MLE 1.4.md".
- ****: Passos comuns das GitHub Actions, incluindo instalação de dependências e execução de testes de unidade.
    - **Fontes**: "Aula 4 DS MLE 1.3.md" e "Aula 4 DS MLE 1.4.md".
- ****: Ênfase na execução de Testes de Unidade (pytest) para validação de componentes isolados e garantia do comportamento esperado do software.
    - **Fontes**: "Aula 1 DS MLE v.1.1.md" e "Aula 1 DS MLE v.1.3.md".
- ****: A importância dos testes de unidade para garantir o comportamento esperado e evitar falhas.
    - **Fontes**: "Aula 1 DS MLE v.1.1.md" e "Aula 1 DS MLE v.1.3.md".
- ****: Recomendações de cobertura mínima de testes (80%).
    - **Fontes**: "Aula 1 DS MLE v.1.1.md" e "Aula 1 DS MLE v.1.3.md".
- ****: Testes específicos para o modelo e a API, incluindo validação de parâmetros e artefatos.
    - **Fontes**: "Aula 1 DS MLE v.1.1.md", "Aula 1 DS MLE v.1.3.md", "Aula 3 DS MLE 2.1.md" e "Aula 3 DS MLE 2.2.md".
- ****: Análise Estática (Linting) com Pylint, garantindo aderência a estilos de codificação (PEP 8) e identificação de erros potenciais.
    - **Fontes**: "Aula 1 DS MLE v.1.1.md", "Aula 1 DS MLE v.1.3.md", "Aula 4 DS MLE 1.3.md" e "Aula 4 DS MLE 1.4.md".
- ****: Benefícios do Linting para melhorar a legibilidade, manutenibilidade e qualidade do código.
    - **Fontes**: "Aula 1 DS MLE v.1.1.md" e "Aula 1 DS MLE v.1.3.md".
- ****: Geração de relatório de métricas do modelo (MLflow Report) para auto-revisão do desempenho.
    - **Fontes**: "Aula 4 DS MLE 1.3.md" e "Aula 4 DS MLE 1.4.md".
- ****: Passo da pipeline para baixar o modelo mais recente do MLflow (via DVC/MinIO).
    - **Fontes**: "Aula 3 DS MLE 2.1.md", "Aula 3 DS MLE 2.2.md", "Aula 4 DS MLE 1.3.md" e "Aula 4 DS MLE 1.4.md".
- ****: Construção da imagem Docker da API com o modelo atualizado, tagueamento e registro em um repositório de contêineres privado.
    - **Fontes**: "Aula 3 DS MLE 2.1.md", "Aula 3 DS MLE 2.2.md", "Aula 4 DS MLE 1.3.md" e "Aula 4 DS MLE 1.4.md".
- ****: Utilização de Pull Requests para organização pessoal e documentação, com testes automatizados e relatórios de métricas.
    - **Fontes**: "Aula 1 DS MLE v.1.1.md", "Aula 1 DS MLE v.1.3.md", "Aula 3 DS MLE 2.1.md" e "Aula 3 DS MLE 2.2.md".
- ****: Captura de logs da API e recomendação da biblioteca `logging` do Python para maior controle.
    - **Fontes**: "Aula 3 DS MLE 2.1.md", "Aula 3 DS MLE 2.2.md", "Aula 4 DS MLE 1.3.md" e "Aula 4 DS MLE 1.4.md".
- ****: Coleta de métricas customizadas sobre as requisições da API (distribuição de features, predições).
    - **Fontes**: "Aula 3 DS MLE 2.1.md" e "Aula 3 DS MLE 2.2.md".
- ****: Conceitos de monitoramento e observabilidade, incluindo painéis de métricas e logs (mesmo que CloudWatch não seja usado diretamente no projeto individual).
    - **Fontes**: "Aula 4 DS MLE 1.3.md" e "Aula 4 DS MLE 1.4.md".
- ****: Armazenamento incremental de dados de requisições e predições em um bucket MinIO (substituindo S3) para análise de desvio.
    - **Fontes**: "Aula 3 DS MLE 2.1.md" e "Aula 3 DS MLE 2.2.md" descrevem o armazenamento em S3, com o plano especificando MinIO.
- ****: Utilização da biblioteca Evidently para detecção de _data drift_ e _concept drift_.
    - **Fontes**: "Aula 4 DS MLE 1.3.md" e "Aula 4 DS MLE 1.4.md".
- ****: Geração de relatórios visuais com Evidently para análise de desvio.
    - **Fontes**: "Aula 4 DS MLE 1.3.md" e "Aula 4 DS MLE 1.4.md".
- ****: Abordagens para detecção de desvio de dados e modelo, como Teste de Kolmogorov-Smirnov, Índice de Estabilidade Populacional, Distância de Wasserstein e Divergência de Kullback-Leibler.
    - **Fontes**: "Aula 4 DS MLE 1.3.md" e "Aula 4 DS MLE 1.4.md".

---
**PLANO DESENVOLVIDO em NotebookLM**
--
---
---

### Plano Conceitual de MLOps Simplificado para o Projeto QuantumFinance (Acadêmico/Individual)

#### 1. Estrutura e Versionamento do Projeto

Para garantir a organização e rastreabilidade mesmo em um projeto individual, manteremos uma estrutura clara e o versionamento adequado.

- **Template de Repositório (Scaffolding)**: Utilizaremos o **Cookiecutter** com o template `cookiecutter-data-science`. Essa estrutura padronizada (com `data/raw`, `data/processed`, `notebooks`, `models`, `src`) é excelente para organizar os arquivos do projeto (dataset, notebooks, scripts de treinamento e modelos), facilitando a manutenção e a reprodução, mesmo por uma única pessoa.
- **Versionamento de Código (Git)**: O Git continuará sendo a base para o controle de versões do código-fonte.
    - **Uso Simplificado de Branches**: Em vez de um Gitflow formal com múltiplos revisores, você pode usar branches para desenvolvimento (`devl`) e uma principal (`main`/`master`) para organizar seu trabalho. As modificações podem ser feitas em branches de _feature_ ou _experimentação_ (`exploracao-inicial`) e, após a validação pessoal, mescladas diretamente para a branch `main`. O conceito de Pull Request (PR) pode ser utilizado como uma _prática de auto-revisão_ e _documentação pessoal_ do que está sendo mesclado, mesmo que não haja uma equipe para aprovar.
    - **Ignorando arquivos**: O uso do `.gitignore` é fundamental para não versionar arquivos grandes (como dados brutos, modelos) ou sensíveis (`.env`), focando apenas no código que precisa ser testado e validado.
- **Versionamento de Dados e Modelos (DVC com MinIO)**: O **Data Version Control (DVC)** é a ferramenta chave para versionar dados e modelos, pois o Git tem limitações para arquivos grandes (acima de 100 MB).
    - **MinIO como Armazenamento Remoto**: Substituindo o S3 da AWS, o **MinIO** será configurado como o _backend_ de armazenamento remoto para o DVC. MinIO oferece uma API compatível com S3, o que o torna uma alternativa excelente e autogerenciável para armazenar as versões dos datasets (brutos e processados) e modelos. Você configuraria o DVC para apontar para seu servidor MinIO.

#### 2. Rastreamento e Registro de Experimentos e Modelos

Para garantir que seus experimentos e modelos sejam rastreáveis e reproduzíveis, o MLflow é a ferramenta ideal.

- **MLflow para Rastreamento de Experimentos**: O **MLflow** será utilizado para registrar métricas de desempenho (como R², MAPE, MSE, MAE), parâmetros e detalhes de execução de cada treinamento do modelo.
    - Você pode usar o **DagsHub** (dagshub.com) como uma plataforma central que integra Git, DVC e MLflow, oferecendo uma interface colaborativa e um plano gratuito adequado para fins acadêmicos. Isso centraliza tudo em um só lugar para seu projeto.
    - O `mlflow.autolog()` pode ser ativado para registrar automaticamente métricas de modelos, e uma função padronizada (`evaluate_and_log_model`) pode ser usada para registrar métricas customizadas de forma consistente, facilitando a comparação de diferentes abordagens.
- **Registro de Modelos no MLflow Model Registry**: Os modelos treinados podem ser registrados no MLflow Model Registry para acompanhar o histórico de versões. Cada versão registrada reflete uma nova etapa de treinamento.
    - Você pode baixar o arquivo binário do modelo (`.pkl`) e metadados (`model_metadata.json`) do MLflow para serem empacotados com a API. É recomendado baixar o arquivo binário do modelo e incorporá-lo na imagem Docker da API para garantir que a API utilize a versão exata do modelo com a qual foi construída.

#### 3. Disponibilização de Endpoint de API Seguro

A API servirá o modelo de score de crédito e será desenvolvida com foco em segurança e desempenho.

- **API REST com Contêineres Docker**: A API será uma aplicação **RESTful** (como Flask ou FastAPI, que não são diretamente mencionadas como ferramentas de implementação, mas são padrões Python para APIs) encapsulada em um **contêiner Docker**. Isso garante portabilidade e isolamento.
    - **Dockerfile**: Um `Dockerfile` definirá a "receita" para construir a imagem do contêiner, incluindo a imagem base Python, a cópia do código da API, a instalação de dependências e a inclusão do modelo (`model.pkl`) e seus metadados (`model_metadata.json`).
    - **Implantação em Ambiente Containerizado**: A imagem Docker da API será implantada em um ambiente que suporte contêineres, como um servidor auto-gerenciado com Docker. Como o ECR da AWS não será utilizado, você pode usar um **Docker Hub privado** ou um **registro Docker auto-hospedado** para armazenar e versionar suas imagens Docker.
- **Segurança da API (Autenticação e Throttling)**: Como o API Gateway da AWS não será usado, a segurança precisará ser implementada na própria aplicação da API.
    - **Autenticação**: A API pode implementar um mecanismo simples de autenticação, como **API keys**, onde a chave será incluída no cabeçalho da requisição (`x-api-key`).
    - **Throttling**: Para controlar o número de requisições, um mecanismo de _rate limiting_ (throttling) pode ser implementado na própria aplicação da API (usando bibliotecas Python como `Flask-Limiter` ou `FastAPI-Limiter`, que não estão nas fontes mas são comuns, ou implementando uma lógica básica de contagem de requisições por IP/chave).
- **Documentação da API**: Embora as fontes não detalhem uma ferramenta específica fora do contexto da AWS, para "Documentação da API", é fundamental descrever claramente os parâmetros de entrada e saída esperados pelo modelo. Ferramentas como **OpenAPI/Swagger UI** (frequentemente integradas em frameworks como FastAPI) geram documentação interativa e padronizada, o que é útil mesmo para um único desenvolvedor.

#### 4. Aplicação Frontend com Streamlit

Para validar a integração com parceiros, uma aplicação modelo será desenvolvida em Streamlit.

- **Streamlit**: Uma aplicação web interativa será criada usando a biblioteca **Streamlit** em Python.
    - **Consumo da API**: O frontend consumirá o endpoint da API de score de crédito.
    - **Secrets**: Informações sensíveis, como o endpoint da API e a chave de acesso, serão armazenadas usando o recurso de **Secrets do Streamlit** (no arquivo `.streamlit/secrets.toml`), evitando sua exposição pública no código.
    - **Widgets e Feedback Visual**: Serão utilizados componentes visuais do Streamlit (input widgets, radio buttons, number inputs) para coletar dados do usuário. Spinners e mensagens de sucesso/erro (usando `st.spinner`, `st.success`, `st.error` ou `st.markdown`) serão usados para feedback durante as chamadas à API.

#### 5. Automação de Pipelines (CI/CD Simplificado)

**GitHub Actions** será utilizado para automatizar os fluxos de trabalho de CI/CD, garantindo que as entregas sejam consistentes, especialmente para um projeto individual.

- **Workflow Único de Validação e Implantação (Simplificado)**:
    
    - **Gatilho**: Disparado em cada `push` para a branch `main` (ou uma branch de desenvolvimento se preferir).
    - **Passos**:
        - Instalação de dependências.
        - Execução de **Testes de Unidade** (`pytest`). A fonte enfatiza que testes de unidade validam componentes isolados e são cruciais para garantir que o comportamento do software seja o esperado. Cobrir pelo menos 80% do código com testes é uma boa prática. Testes específicos para o modelo e a API são importantes.
        - **Análise Estática (Linting)** (`pylint`). Ferramentas de linting como Pylint ajudam a identificar problemas, aderência a estilos de codificação (PEP 8) e erros potenciais ainda na fase de desenvolvimento.
        - **Geração de Relatório de Métricas do Modelo**: Um script Python pode gerar um relatório de métricas do modelo (utilizando as métricas registradas no MLflow), que pode ser anexado como um artefato da Action ou exibido diretamente no resumo da execução do GitHub Actions para sua própria revisão. Isso substitui a "análise de Pull Request" por uma "análise de desempenho do modelo para auto-revisão".
        - **Baixar o último modelo**: O pipeline baixaria o modelo mais recente do MLflow (que, por sua vez, armazena o artefato em MinIO via DVC).
        - **Construir a imagem Docker** da API com o modelo atualizado.
        - **Taggear a imagem** e **registrá-la** em seu registro de contêineres privado (e.g., Docker Hub privado).
        - **"Implantação"**: Para um projeto acadêmico individual, isso pode ser um passo conceitual. Poderia ser um script que se conecta ao seu servidor (onde o Docker está rodando) e puxa a nova imagem e reinicia o contêiner.
- **Pull Requests (PRs) no Contexto Acadêmico**: Embora você tenha mencionado que "não vai rolar" um fluxo de PRs com revisões de equipe, o conceito de PR ainda pode ser útil para **organização pessoal e documentação**. Você pode criar PRs para si mesmo, permitindo que as GitHub Actions rodem os testes e o linting automaticamente _antes_ de você mesclar o código para a branch `main`. Isso atua como um _checklist automatizado_ de qualidade do seu próprio código antes de "finalizar" uma funcionalidade. Falhas nesses testes interromperiam o merge, forçando você a corrigir os problemas.
    

#### 6. Observabilidade e Monitoramento

Para garantir o desempenho e a qualidade contínua do modelo de score de crédito em produção, a solução incluirá práticas de observabilidade e monitoramento.

- **Logging**: As saídas do contêiner da API (mensagens de `print` ou loggers Python) serão capturadas pelo Docker. Você pode visualizar esses logs com `docker logs <container_id>`. Para um controle mais flexível, o uso da biblioteca `logging` do Python é recomendado.
- **Métricas Personalizadas**: A API pode coletar métricas customizadas sobre as requisições (como distribuição de features e valores de predição). Em vez de serviços de nuvem como CloudWatch, essas métricas podem ser armazenadas em um arquivo local (e.g., CSV ou um banco de dados SQLite persistente usando um volume Docker) ou enviadas para um sistema de monitoramento auto-hospedado (como Prometheus com Grafana), se você quiser explorar essa parte mais profundamente (informação não das fontes).
- **Armazenamento de Dados de Requisições**: Cada requisição e sua predição serão armazenadas incrementalmente em um arquivo CSV em um **bucket MinIO** (substituindo S3) para futuras análises de desvio de dados e modelos. O MinIO oferece uma forma autônoma de reter esses dados para análises posteriores.
- **Detecção de Desvio de Modelo e Dados**: A biblioteca **Evidently** será utilizada para analisar e detectar _data drift_ (mudanças nas características dos dados de entrada) e _concept drift_ (mudanças na relação entre entradas e saídas). Relatórios gerados pelo Evidently podem ser executados periodicamente via um script Python (manualmente ou agendado no seu ambiente local) usando os dados armazenados no MinIO, para você acompanhar a saúde do modelo ao longo do tempo. As fontes descrevem várias abordagens para detecção de desvio, como Teste de Kolmogorov-Smirnov, Índice de Estabilidade Populacional, Distância de Wasserstein e Divergência de Kullback-Leibler.

Este plano conceitual revisado visa atender a todos os requisitos do exercício de forma mais adaptada a um projeto acadêmico individual, mantendo as práticas essenciais de MLOps de forma simplificada e focando nas suas preferências de Docker e MinIO, sem dependências de serviços AWS.