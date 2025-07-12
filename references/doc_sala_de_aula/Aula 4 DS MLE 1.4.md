MACHINE LEARNING ENGINEERING

MBA EM DATA SCIENCE & IA

PIPELINES DE INTEGRAÇÃO E ENTREGA CONTÍNUA

CD/CI FLOW BLUEPRINT

AWS Lambda

Amazon ECR

Amazon CloudWatch

Amazon API Gateway

Model Product

Streamlit Cloud

Laptop Pricing

Laptop Pricing App

Laptop Pricing API

Laptop Pricing Model

Notifica nova versão

Registra nova versão

Notifica nova versão para exposição na API

Cria nova imagem, baixando o modelo mais recente

Atualiza com a nova imagem

Análise de Pull Request

Análise de Pull Request

Automatização de Fluxos de Trabalho: permite criar fluxos de trabalho automatizados para construir, testar, empacotar, liberar e implantar seu código.
Integração Contínua (CI): é possível configurar CI para construir e testar automaticamente seu código sempre que houver um push ou uma pull request no repositório.
Implantação Contínua (CD): é possível configurar implantações contínuas para enviar automaticamente seu código para ambientes de produção ou de teste após a aprovação dos testes de CI.
Eventos do GitHub: GitHub Actions responde a uma variedade de eventos do GitHub, como push, pull requests, issues, entre outros, permitindo desencadear ações específicas em resposta a esses eventos.
Reutilização de Ações: é possível compartilhar ações reutilizáveis, ou seja, pequenos trechos de código que podem ser utilizados em diferentes fluxos de trabalho, facilitando a composição de processos complexos.
Infraestrutura Escalável: é executado em infraestrutura escalável fornecida pelo GitHub, o que significa que você não precisa se preocupar com provisionamento ou gerenciamento de servidores.

https://docs.github.com/pt/actions
https://dvc.ai/blog/cml-self-hosted-runners-on-demand-with-gpus

GITHUB ACTIONS

Mesmo o os runners do GitHub Actions serem gerenciados pelo GitHub é possível instalar runners dedicados por meio de agentes. Com isso podemos ter diferentes tipos de instância até mesmo com tipos de CPU e GPU adequadas para as atividades Machine Learning.

GitHub Actions é um serviço de automação que permite automatizar fluxos de trabalho diretamente do seu repositório GitHub. Principais recursos:

ESTRATÉGIAS DE ACTIONS

Cada necessidade requer um tipo diferente de ação.
Construir um modelo, montar uma imagem de contêiner, implantar um serviço de nuvem podem diferenciar um fluxo de outro. Até mesmo o tipo de ação, um Pull Request ou atualizações em uma determinada ramificação.

MAIN

AÇÃO

DEVL

AÇÃO

AÇÃO

As ações visam garantir testes mínimos para avançar para etapas de merge e implantação do código.

PASSOS COMUNS DE ACTIONS

Cada necessidade requer um tipo diferente de ação.
Construir um modelo, montar uma imagem de contêiner, implantar um serviço de nuvem podem diferenciar um fluxo de outro. Até mesmo o tipo de ação, um Pull Request ou atualizações em uma determinada ramificação.

VERIFICAR E INSTALAR DEPENDÊNCIAS

Análise de Pull Request

EXECUTAR PIPELINE DE VALIDAÇÃO

COLETAR MÉTRICAS

TESTES DE UNIDADE

VERIFICAÇÃO DO MODELO

GOLDEN DATA

EXECUÇÃO

VALIDAÇÃO ANTES DE COMBINAR O CÓDIGO COM PRODUÇÃO

A análise de Pull Request é em outra branch que não a de produção (master).
As validações mínimas do pipeline de fluxo de dados e a análise de métricas garantem que não haja alterações que possam quebrar o modelo.
Na hipótese dos testes serem alterados, uma análise mais criteriosa precisa ser feita durante a revisão.
Após a aprovação do Pull Request o modelo segue para uma nova rodada de treinamento e registro do modelo.

ACTION PARA PULL REQUEST

Execução somente em Pull Request

Permissões para escrita de sumário do Action, modificações de Pull Request

Obtendo Python 3.10

Obtendo arquivos do repositório

Instalando dependências de produção

Realizando testes de unidade

Sistema operacional do container.

name: MLflow Model Report
on:
pull\_request:
branches: [main]
permissions:
contents: read
pull-requests: write
jobs:
report:
runs-on: ubuntu-latest
steps:
- name: Checkout code
uses: actions/checkout@v4
- name: Setup Python
uses: actions/setup-python@v5
with:
python-version: '3.10’
- name: Install dependencies
run: pip install -r requirements.txt
- name: Unit testing
run: pytest


ACTION PARA PULL REQUEST

Gerando o relatório de métricas

Exibindo o relatório no Pull Request

- name: Generate MLflow Report
run: python reports/report.py
- name: Comment on Pull Request
uses: marocchino/sticky-pull-request-comment@v2
with:
header: mlflow-report
path: mlflow\_report.md

ACTION PARA PULL REQUEST

Cada passo (step) é executado sequencialmente. Quando algum passo falha (código de status diferente de 0), a pipeline é interrompida até que uma nova execução sem erro seja realizada. Com isso nenhuma modificação é lançada em produção.

ACTION PARA PULL REQUEST

O relatório de métricas do modelo serve para revisar se o novo modelo registrado cumpre com os objetivos estabelecidos pela governança.
Integrando na tela de Pull Request podemos facilmente verificar as variações e decidir se a nova abordagem deve ser incorporada no código principal.
Caso seja incorporado, será disparado uma notificação para atualizar o modelo servido pela API.

ADICIONADO PROVEDOR OIDC PARA GITHUB

Para evitarmos salvar credenciais de acesso em secrets, a AWS permite validar credenciais de acesso utilizado OpenID Connect. Com este método, as ações das pipelines do GitHub acessam os recursos da AWS conforme liberação de política.
A configuração deste tipo de identidade é feita por essa URL de provedor:  https://token.actions.githubusercontent.com.

https://docs.github.com/en/actions/deployment/security-hardening-your-deployments/configuring-openid-connect-in-amazon-web-services

ADICIONADO PROVEDOR OIDC PARA GITHUB

Na Role de acesso pelo Github Actions, é necessário incluir a seguinte relação de confiança.

https://docs.github.com/en/actions/deployment/security-hardening-your-deployments/configuring-openid-connect-in-amazon-web-services

{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {
                "Federated": "arn:aws:iam::989944764342:oidc-provider/token.actions.githubusercontent.com"
            },
            "Action": "sts:AssumeRoleWithWebIdentity",
            "Condition": {
                "StringEquals": {
                    "token.actions.githubusercontent.com:aud": "sts.amazonaws.com"
                },
                "StringLike": {
                    "token.actions.githubusercontent.com:sub": "repo:michelpf/\*"
                }
            }
        }
    ]
}

ACTIONS PARA NOTIFICAÇÃO DE IMPLANTAÇÃO DE API

Após um Pull Request for aceito, as novas configurações estão prontas para mesclarem com o código em produção. Após isso a esteira de CI/CD vai notificar a API para implantar uma nova versão.
Como os models ficam registrados no MLFlow não é necessário nenhum passo adicional de build.

Alterações na Branch Master

VERIFICAR E INSTALAR DEPENDÊNCIAS

EXECUTAR PIPELINE DE VALIDAÇÃO

NOTIFICAR API

TESTES DE UNIDADE

VERIFICAÇÃO DO MODELO

GOLDEN DATA

EXECUÇÃO

VALIDAÇÃO ANTES DE SALVAR O CÓDIGO COM PRODUÇÃO

ACTIONS PARA TREINAMENTO DO MODELO

Execução somente quando houver atualizações na ramificação main e em pastas específicas

Instalação do Python

Sistema operacional do container.

Downloado do repositório

name: Notify API Deployment
on:
push:
branches:
- main
paths:
- 'notebooks/\*\*'
jobs:
notify\_api\_repository:
name: "Notification to API Repository"
runs-on: ubuntu-latest
steps:
- name: Checkout code
uses: actions/checkout@v4
- name: Setup Python
uses: actions/setup-python@v5
with:
python-version: '3.10'
- name: Install dependencies
run: pip install -r requirements.txt

Instalação de dependências

ACTIONS PARA TREINAMENTO DO MODELO

Notificar outro repositório para implantação.

Execução dos testes de unidade

- name: Unit testing
run: pytest
- name: Deploy Stage
uses: actions/github-script@v6
with:
github-token: ${{ secrets.ACCESS\_TOKEN }}
script: |
await github.rest.actions.createWorkflowDispatch({
owner: "michelpf",
repo: "fiap-ds-mlops-api-laptop-pricing-brl",
workflow\_id: "deploy.yml",
ref: "main"
})

ACTIONS PARA TESTES E NOTIFICAÇÃO DE IMPLANTAÇÃO

Após os testes de unidade, a pipeline avisa a outro repositório para implantar uma nova versão da API com o modelo atualizado.

ACTIONS PARA IMPLANTAÇÃO DA API

Note o “workflow dispatch”, isso indica que a pipeline foi disparada por outra pipeline.

TOKEN DE ACESSO PARTICULAR

Para ações específicas como de iniciar uma action em outro repositório é necessário permissões extras, ou seja, além da do próprio repositório da qual já é oferecida um token padrão (GITHUB\_TOKEN) sem a necessidade da criação de um novo.
Neste caso precisamos criar um token particular de acesso.

SECRET PARA USO EM UMA ACTION

Depois de criar um acesso pessoal de token, precisamos carrega-lo como secret do repositório a ser utilizado em uma action.
O nome da secret precisa ser o mesmo a ser referenciado no workflow, ou seja, o secret “ACCESS\_TOKEN” é referenciado no workflow como “secrets.ACCESS\_TOKEN”.

ACTIONS PARA IMPLANTAÇÃO DA API

Após todos os testes do modelo e treinamento estiverem concluídos, passamos a notificar o repositório da API para uma nova implantação.
O repositório da API também pode disparar novas implantações que não dependem de uma nova versão do modelo, para por exemplo, melhorar a performance do modelo e segurança.

VERIFICAR E INSTALAR DEPENDÊNCIAS

Alterações na Branch Master

BAIXAR MODELO

CRIAR ARQUIVO DE VERSÃO

TESTE DE UNIDADE

LINTER

CONSTRUIR IMAGEM

TAG DA IMAGEM (VERSIONAR)

REGISTRO DA IMAGEM

ATUALIZAR LAMBDA

Se o modelo tiver mais parâmetros do que a API, o teste de unidade vai detectar e não será lançada uma versão nova. Idem se for adicionado um parâmetro novo da API e o modelo não estiver atualizado.

ACTIONS PARA IMPLANTAÇÃO DA API

name: Build image then push to registry for deployment

on:
  workflow\_dispatch:
  push:
    branches: [ "master" ]

jobs:
  build-push-imagem-deploy:
    runs-on: ubuntu-latest

    permissions:
      id-token: write
    steps:
      - name: Checkout repo
        uses: actions/checkout@v4

      - name: Configure AWS credentials
        uses: aws-actions/configure-aws-credentials@v4
        with:
          role-to-assume: arn:aws:iam::989944764342:role/GithubActionsRole
          aws-region: us-east-1

      - name: Login to Amazon ECR
        id: login-ecr
        uses: aws-actions/amazon-ecr-login@v2
      ...

Execução somente quando houver atualizações na ramificação master

Permissão de utilizar o token para autenticação com serviços externos via OIDC com a AWS.

Ação para baixar o conteúdo do repositório (clonagem, com todos os dados).

Ação para configurar autenticação na AWS sem precisar informar chaves de segurança, utilizando OIDC (Open ID Connect) e Assume Role.

Ação para configurar credenciais de acesso no ECR.

Podemos criar uma action dedicada para Pull Request, indo até o build da imagem do container.

ACTIONS PARA IMPLANTAÇÃO DA API

...
      - name: Configure Python environment
        uses: actions/setup-python@v5
        with:
          python-version: "3.10"

      - name: Install dependencies
        run: python -m pip install -r requirements.txt

      - name: Model download
        run: python –m model\_dowloader

     
      - name: Unit testing
        run: pytest

      - name: Linting
        run: pylint src

      - name: Build image
        run: docker build --platform linux/amd64 -t laptop-pricing-api .

Ação para configurar o ambiente Python para o fluxo da pipeline.

Instalação dependências do projeto.

Baixar o último modelo disponível em produção.

Realizar testes de unidade.

Realizar análise estática (Lint)

Cria uma imagem Docker utilizando o Dockerfile.

ACTIONS PARA IMPLANTAÇÃO DA API

...
      - name: Tag to ECR
        run: docker tag laptop-pricing-api:latest 989944764342.dkr.ecr.us-east-1.amazonaws.com/laptop-pricing-api:latest

      - name: Register in ECR
        run: docker push 989944764342.dkr.ecr.us-east-1.amazonaws.com/laptop-pricing-api:latest

      - name: Update Lambda
        run: aws lambda update-function-code --function-name laptop-pricing-api --image-uri 989944764342.dkr.ecr.us-east-1.amazonaws.com/laptop-pricing-api:latest


Inclui tag na imagem criada para apontar no registro de containers.

Envia o modelo para o ECR com base na tag.

Atualiza o Lambda para a versão mais atual da imagem do contêiner.

ACTIONS PARA IMPLANTAÇÃO DA API

Passos utilizados neste workflow de implantação.
Cada um deles tem o log de das ações realizadas e o resultado das verificações.
Quando todas elas são executadas com sucesso, a pipeline por sua vez é considerada executada com sucesso como um todo.
Qualquer erro durante a implantação interrompe o processo e não é lançada uma nova versão em produção. 

FRONTEND NO STREAMLIT

A plataforma Streamlit (https://streamlit.io/) permite a implantação de aplicativos em sua cloud de forma gratuita.
Registre com sua conta do Google ou GitHub e tenha acesso ao painel de apps.

Clique em “New app” para configurar um novo aplicativo.

IMPLANTAÇÃO DO FRONTEND

Para configurar uma nova aplicação informe o nome do repositório, a ramificação, o nome do arquivo de script e por fim, defina um domínio.

UTILIZANDO SECRETS

Não podemos deixar em um repositório público as informações de endpoint de API e sua chave de acesso. Por isso definimos como Secrets.
Configuramos também a versão do Python a ser utilizada.
Para nossa aplicação que utiliza o separador de milhar e casas decimais baseado na localização, precisamos definir o arquivo packages.txt para inserir a extensão a nível de sistema operacional “locales-all”.

IMPLANTAÇÃO DO FRONTEND

Após as alterações na ramificação master, elas são replicadas para o Streamlit cloud.
Podemos acompanhar a instalação pelo próprio painel da aplicação, seja quando houver uma atualização ou seja quando a aplicação for restaurada do estado de hibernação por inatividade.

OBSERVABILIDADE E MONITORAMENTO

Acompanha continuamente métricas e KPIs.
Coleta dados em tempo real ou em intervalos regulares.
Analisa dados para detectar padrões, tendências ou anomalias.
Garante o funcionamento esperado do sistema.

Em ambientes de desenvolvimento de software, especialmente no contexto de APIs e modelos de Machine Learning, é essencial compreender a diferença entre observabilidade e monitoramento. Enquanto o monitoramento se concentra em acompanhar métricas externas e garantir o desempenho do sistema, a observabilidade visa entender o comportamento interno do sistema através da instrumentação adequada.

OBSERVABILIDADE E MONITORAMENTO

Capacidade de entender internamente o funcionamento do sistema.
Baseia-se na instrumentação adequada para geração de dados internos.
Permite identificar problemas e depurar falhas com facilidade.
Foco no entendimento do comportamento interno do sistema.

Monitoramento

Observabilidade

reativo

proativo

o quê?

quando?

por quê?

como?

Amazon CloudWatch

Todos os serviços da AWS possuem painéis dedicados para cada um deles. Tais painéis dão uma visão rápida e completa das principais métricas do serviço. O painel abaixo é da função Lambda da função de predição.
Para detalhamento de monitoração, precisamos acessar o “Visualizar logs do CloudWatch”.

PAINÉIS DE MONITORAMENTO

O painel do log do CloudWatch apresenta ferramentas para pesquisa e visualização dos logs.
Os streams de log é onde ficam armazenados todos os eventos.
Utilizamos os logs para investigações de causa raiz ou de condições específicas do comportamento de um determinado serviço.
Por tal razão deve-se ter muita cautela ao escolher quais mensagens devem ser logadas, para balancear investigações com excesso de dados e impactar o custo caso o armazenamento seja muito grande (aplicações em grande escala).

LOGS DE MONITORAMENTO

No exemplo abaixo podemos verificar como é composto um stream de logs.
São incluídos mensagens do sistema, como o “START”, “END” e “REPORT” da função Lambda e também as mensagens que a função exibe de acordo com a definição da API. Payload, Context e Prediction são exemplos de logs do serviço desenvolvido.

STREAM DE LOG

Utilizar a saída de console utilizando o comando “print” é o mais simples possível. Para controlar melhor diferentes granularidades considere utilizar o Python Logging (https://docs.python.org/pt-br/3/howto/logging.html).

As métricas customizadas que criamos e enviamos em cada requisição traz dados quantitativos dos features e assim conseguimos acompanhar eventuais grandes desvios.
Também é possível acompanhar a média de predições, caso o modelo apresente algum desvio significativo.
Estas visões são de curto prazo, para acompanhamento diário. Análises mais completas de desvios de dados sevem ser feitas num contexto estatístico mais amplo que veremos mais adiante.

PAINÉIS PERSONALIZADO DO MODELO

EXEMPLO DE PAINEL DO MODELO COMPLETO

As métricas de serviço estão associadas aos componentes da AWS utilizados.
Na nossa arquitetura, o API Gateway serve de porta de entrada das solicitações, para depois enviar ao Lambda. Com isso, é importante entender a quantidade de requisições, latência para responder o serviço, quantidade de erros, tempo de execução, etc.
O entendimento de como a topologia funciona pode ajudar na identificação de erros e gargalos no serviço.

PAINÉIS PERSONALIZADO DO SERVIÇO

EXEMPLO DE PAINEL DO SERVIÇO

DESVIO DE MODELO E DADOS

Data & Concept Drift pode impactar negativamente o desempenho do modelo, pois ele foi treinado em dados históricos que podem não mais representar com precisão a realidade atual.
Como resultado, o modelo pode produzir previsões menos precisas ou confiáveis.

Conceito

Dados

Mudança gradual ou súbita nas características dos dados de entrada em um modelo de machine learning após sua implementação. Isso pode ocorrer devido a várias razões, como mudanças nas preferências dos usuários, alterações nos padrões de comportamento, ou até mesmo falhas nos sistemas de coleta de dados.

https://blog.nimblebox.ai/machine-learning-model-drift

DESVIO DE MODELO

DESVIO DE DADOS & CONCEITO

https://kdimensions.com/
https://www.iguazio.com/questions/what-is-the-difference-between-data-drift-and-concept-drift/

Desvio de Dados: As entradas mudaram, tornando o modelo treinado irrelevante para os novos dados. Um exemplo disso é a mudança na distribuição etária dos usuários de determinado aplicativo ao longo do tempo. Assim, um modelo treinado em uma distribuição etária específica, utilizada para estratégias de marketing, precisará ser ajustado à medida que a mudança na faixa etária afetará as estratégias de marketing.
Desvio de Conceito: A distribuição dos dados permanece a mesma, mas a relação entre as entradas e saídas é diferente. Isso significa que o que estamos tentando prever mudou. Um exemplo comum é a detecção de spam: os spammers adotam novas táticas ao longo do tempo, exigindo que os filtros de spam sejam ajustados para reconhecer esses novos padrões.

https://arxiv.org/abs/2004.05785

DESVIO DE CONCEITO

Desvio sazonal. Um exemplo típico é o aumento nas vendas durante o Natal ou a Black Friday.
Um modelo de aprendizado de máquina que não leva em conta essas mudanças sazonais acabará fornecendo previsões imprecisas para essas variações sazonais.

O desvio incremental ocorre quando a relação entre a variável alvo e a entrada muda gradualmente ao longo do tempo, o que geralmente ocorre devido a mudanças no processo de geração de dados.

Desvio repentino de conceito ocorre quando a relação entre as variáveis independentes e dependentes muda de forma repentina.
Um exemplo é o surgimento repentino da pandemia de COVID-19.
A ocorrência da pandemia mudou repentinamente a relação entre a variável alvo e as características em diferentes áreas, de modo que um modelo preditivo treinado com dados prévios não será capaz de prever com precisão durante o período da pandemia.

Em um desvio gradual de conceito, a relação entre a entrada e o alvo pode mudar lentamente e de forma sutil. Isso pode resultar em uma queda gradual no desempenho de um modelo de aprendizado de máquina, à medida que o modelo se torna menos preciso ao longo do tempo.
Um exemplo de desvio gradual de conceito é o comportamento fraudulento. Os fraudadores tendem a entender como o sistema de detecção de fraudes funciona e mudam seu comportamento ao longo do tempo para escapar do sistema.
Portanto, um modelo de aprendizado de máquina treinado com dados históricos de transações fraudulentas não preverá com precisão as mudanças graduais no comportamento dos fraudadores.

As técnicas abaixo algumas ferramentas relevantes para a análise e comparação de distribuições estatísticas. Amplamente empregadas na estatística e na análise de dados, essas abordagens são essenciais para quantificar a similaridade ou disparidade entre diferentes distribuições de probabilidade.

ABORDAGENS PARA DETECÇÃO

Teste de Kolmogorov-Smirnov: é uma técnica estatística usada para determinar se duas distribuições de dados diferem significativamente uma da outra. Em termos simples, ele mede a similaridade entre duas distribuições de probabilidade. Pode ser aplicado para comparar a distribuição das previsões do modelo com a distribuição dos valores reais.
Índice de Estabilidade Populacional: é uma métrica que avalia a estabilidade das distribuições de variáveis ao longo do tempo. É comumente usados em modelos de score de crédito e outras aplicações onde é importante monitorar se a distribuição dos dados mudou significativamente entre períodos. O PSI pode ser usado para identificar desvios nos dados de treinamento e dados em tempo real.
Distância de Wasserstein: é uma métrica que quantifica a dissimilaridade entre duas distribuições de probabilidade. Ela é especialmente útil quando as distribuições têm formas diferentes ou quando há uma correspondência entre elementos das duas distribuições. Em modelos de machine learning, a distância de Wasserstein pode ser usada para comparar a distribuição das previsões do modelo com a distribuição dos valores reais.
Divergência de Kullback-Leibler: é uma medida da diferença entre duas distribuições de probabilidade. Ela quantifica o quanto uma distribuição difere de outra. A divergência de Kullback-Leibler pode ser usada para avaliar a discrepância entre a distribuição das previsões do modelo e a distribuição dos valores reais.

A biblioteca Evidently é uma biblioteca de código aberto projetada para ajudar na validação e interpretação de modelos de machine learning. Ela é usada principalmente para avaliar a performance e a interpretabilidade de modelos, incluindo os casos de desvio de dados e de modelo, dentro de monitoramento de modelos.
Principais recursos:
Análise de desempenho do modelo: fornece métricas e visualizações para avaliar a qualidade preditiva de um modelo. Isso inclui métricas comuns, como precisão, recall, F1-score, entre outras, além de gráficos que ajudam a entender como o modelo se comporta em diferentes partes do conjunto de dados.
Análise de bias e equidade: ajuda a identificar e quantificar vieses e disparidades nos resultados do modelo, permitindo uma análise mais profunda da equidade do modelo em diferentes subgrupos da população.
Interpretabilidade do modelo: oferece ferramentas para interpretar e explicar as decisões do modelo, incluindo a importância de cada feature, análise de feature interactions e visualizações que ajudam a entender como as features influenciam as previsões do modelo.
Monitoramento contínuo do modelo: pode ser usada para monitorar a performance de modelos em produção ao longo do tempo, ajudando a detectar desvios de performance e a tomar medidas corretivas quando necessário.

EVIDENTLY

Instalando a biblioteca.

UTILIZANDO EVIDENTLY

!pip install evidently==0.4.15

!git clone https://github.com/michelpf/fiap-ds-mlops-laptop-pricing-model-drift

Gerando desvio artificial em 5 desvios padrão.

df\_training = pd.read\_csv("training-data/laptop-pricing.csv")
df\_training.head()

Baixando os dados de análise.

df\_training.rename(columns={'price': 'target'}, inplace=True)
df\_training['prediction'] = df\_training['target'].values + np.random.normal(0, 5, df\_training.shape[0])

training = df\_training.sample(n=500, replace=False)
production = df\_training.sample(n=500, replace=False)

Obtendo amostras para 2 conjuntos, um de treinamento que será utilizado como referência e outro para produção que será utilizado como dado atual.

https://github.com/michelpf/fiap-ds-mlops-laptop-pricing-model-drift

Obtendo relatório visual para análise.

ANÁLISE DE DADOS

data\_quality\_report = Report(metrics=[DataQualityPreset()])
data\_quality\_report.run(reference\_data=training, current\_data=production)
data\_quality\_report

Análise para cada coluna do dataset

Análise de correlação entre os atributos.

Obtendo relatório visual para análise.

ANÁLISE DE DESVIO DE MODELO (ALVO)

report = Report(metrics=[TargetDriftPreset()])
report.run(reference\_data=training, current\_data=production)
report

Obtendo relatório visual para análise.

ANÁLISE DE DESVIO DE DADOS (CONCEITO)

report = Report(metrics=[DataDriftPreset()])
report.run(reference\_data=training, current\_data=production)
report

Os testes estatísticos são definidos automaticamente baseado no tamanho e tipo do dataset.
É possível determinar testes específicos dos diversos disponíveis.

Este relatório pode ser disponibilizado em formato JSON que facilita a integração com sistemas de monitoramento para notificações de desvios de dados relavantes.

report.json()

Tamanho do desvio que deseja detectar: dependendo do caso apenas vale investir somente em mudanças grandes. Em outros, até mesmo a uma pequena. A definição de "grande" e "pequeno" variaria com base nos seus dados e a criticidade do negócio envolvido.
Tamanho das amostras para comparação: como diferentes testes fornecem resultados diferentes dependendo do tamanho da amostra, você deve considerar isso para o tipo de teste a ser utilizado.
O custo da queda no desempenho do modelo: se cada erro for caro, você pode querer escolher um teste mais sensível, mesmo que isso resulte em alertas de falsos positivos.
Se a precisão for crucial, escolha o Teste de Kolmogorov-Smirnov (KS).
Se você deseja detectar um desvio maior, escolha o Teste de Wasserstein (WD). Você pode definir um limiar de acordo com o número de desvios padrão que você assume que a distribuição deve mudar para se qualificar como um desvio.

CONCLUSÕES SOBRE DESVIO DE MODELOS E DADOS

PARA SABER MAIS

https://www.evidentlyai.com/blog/data-drift-detection-large-datasets, artigo sobre observabilidade de modelos e desvios, da Evently AI.
https://cursos.alura.com.br/course/observabilidade-aws-utilizando-cloudwatch, curso de Observabilidade com Cloudwatch

