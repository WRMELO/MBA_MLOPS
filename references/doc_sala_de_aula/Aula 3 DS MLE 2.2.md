MACHINE LEARNING ENGINEERING

MBA EM DATA SCIENCE & IA

RASTREAMENTO DE EXPERIMENTOS

Antes de formalizar o experimento num script, ou seja, codifica-lo para que seja reproduzível em esteiras de CD/CI precisamos de um ambiente onde seja mais adequado atividades de:

EXPERIMENTOS COM NOTEBOOK

Exploração de dados
Pré-processamento de dados
Construção de features
A execução no VSCode garante que todas as bibliotecas estão condidas em dependências mapeadas.
Próximo passo é converter em scripts os passos citados anteriormente incluindo o treinamento.

Criamos uma branch nova para estas modificações

git checkout –b exploracao-inicial

Antes de começarmos a experimentar diferentes tipos de modelos, precisamos identificar e selecionar os atributos mais relevantes, ou seja, realizar o processo de feature engineering.
Após essa etapa, registraremos tanto o dataset original quanto as versões pré-processadas, garantindo organização e rastreabilidade para os próximos passos do projeto.

DESENVOLVENDO O PRÉ-PROCESSAMENTO

Este notebook fica na pasta “notebooks” identificado como data-processing.

Clicar em “Compare & pull request”.

SUBMETENDO O PULL-REQUEST

Podemos fazer as modificações na master? Sim.
Devemos? Não, pois o branch master precisa estar protegido e bem documentado quanto a qualquer alteração.
Somente trechos de código e modificações validadas e revisadas podem ser combinadas com a versão principal.
Isso se deve pois esta ramificação é que entregará o modelo em produção.

Precisamos convencer o revisor do repositório/projeto a aceitar as modificações. A depender do que se propõe modificar, valores de métricas são boas referências.

JUSTIFICANDO O PULL REQUEST

Comparações antes e depois

Referências das razões das escolhas

Utilize os recursos disponíveis como imagens e anexos

Após submeter o Pull Request, se houver alguma ação personalizada, como testes de unidade, eles poderão ser executados e automaticamente invalidar sem a revisão.
Esta automação também pode incluir informações adicionais.

VALIDAÇÕES E TESTES

Com sinal verde, ou seja, todos os testes realizados com sucesso, é possível avançar com “merge” que irá combinar a branch “exploracao-inicial” com a “master”.

Para finalizar o “Merge” confirmamos as alterações e também removemos a branch “Delete branch”.

FINALIZANDO O PULL REQUST

De volta ao nosso código local, vamos alterar a branch para a master, atualizá-la e depois remover a branch auxiliar.

ATUALIZANDO O CÓDIGO

git checkout master

Mudar a branch para master.

git pull origin master

Obter as últimas modificações depois do merge do Pull Request

git branch –d exploracao-inicial 

Remover a branch de testes

Caso as modificações não sejam sincronizadas pela main, o próprio Git informará que a branch a ser removida contém informações não sincronizadas, como um alerta.

EXPERIMENTOS COM MLFLOW

CICLO PARA CONSTRUIR UM MODELO

EXPERIMENTAÇÃO
NO NOTEBOOK

REGISTRO DE DATASET

REGISTRO DE EXPERIMENTOS

REGISTRO DE MODELO

ESTÁGIO DO MODELO

ARTEFATO PARA API

API REST

FRONTEND

Os experimentos armazenam informações importantes durante o desenvolvimento do modelo, como métricas de desempenho, metas definidas e detalhes da execução dos treinamentos. Esses registros facilitam o acompanhamento da evolução e a comparação entre diferentes abordagens.
Embora o DagsHub ofereça um painel próprio para experimentação, optaremos por utilizar a interface visual do MLflow, que oferece mais recursos, especialmente para o registro de modelos e o download de artefatos gerados durante os experimentos.

RASTREANDO EXPERIMENTOS

Na visão de gráfico podemos comparar as diferentes métricas.

COMPARAÇÃO DE MODELOS

CONFIGURAÇÃO DO RASTREAMENTO EXPERIMENTO

Para conduzir os experimentos, vamos utilizar um novo notebook. Antes de iniciar o desenvolvimento e a avaliação dos diferentes modelos, é necessário acessar o dataset já registrado. Definimos o dataset chamado processed como a base principal de features que será utilizada nos treinamentos.

ds = datasources.get('michelpf/fiap-ds-mlops-laptop-pricing-brl', 'processed')

ds.all().dataframe

res = ds.head()
for dp in res:
dataset\_url = dp.download\_url

df = pd.read\_csv(dataset\_url)

Caminho do repostório no DagsHub.

Nome do dataset

Obtendo a URL para carregar no dataframe

Dataset carregado no dataframe, pronto para uso nos modelos

CONFIGURAÇÃO DO RASTREAMENTO EXPERIMENTO

O próximo passo é iniciar o DagsHub, informando os dados do repositório e ativando o MLFlow.

dagshub.init(repo\_owner='michelpf', repo\_name='fiap-ds-mlops-laptop-pricing-brl', mlflow=True)

Para que o MLflow registre automaticamente todas as métricas durante os experimentos, podemos ativar o recurso de autolog. Essa funcionalidade é especialmente útil em modelos de deep learning, pois permite armazenar informações como o tempo de execução, a evolução da perda ao longo do treinamento e o número de épocas, facilitando a comparação entre diferentes execuções.

mlflow.autolog()

O recurso de autolog também dispara automaticamente um novo experimento no MLflow sempre que um modelo é treinado. Isso permite acompanhar a evolução em tempo real diretamente pelo portal, facilitando a análise por parte dos usuários que estiverem monitorando os experimentos.

CONFIGURAÇÃO DO RASTREAMENTO EXPERIMENTO

Apesar do autolog cobrir automaticamente todas as métricas, é boa prática definirmos explicitamente as métricas que precisamos armazenar, pois os modelos podem ter o outras métricas por padrão que nem sempre são as mesmas que são definidas como objetivo.

def evaluate\_and\_log\_model(kind, model\_name, model, X\_test, y\_test):
predictions = model.predict(X\_test)
mse = mean\_squared\_error(y\_test, predictions)
mae = mean\_absolute\_error(y\_test, predictions)
r2 = r2\_score(y\_test, predictions)
mape = mean\_absolute\_percentage\_error(y\_test, predictions)
 mlflow.log\_metric("MSE", mse)
mlflow.log\_metric("MAE", mae)
mlflow.log\_metric("R2", r2)
mlflow.log\_metric("MAPE", mape)
 # Inferir a assinatura automaticamente
signature = infer\_signature(X\_test, predictions)
 if kind == "catboost":
mlflow.catboost.log\_model(model, "model", signature=signature, input\_example=X\_test[:5])
elif kind == "xgboost":
mlflow.xgboost.log\_model(model, "model", signature=signature, input\_example=X\_test[:5])
elif kind == "lightgbm":
mlflow.lightgbm.log\_model(model, "model", signature=signature, input\_example=X\_test[:5])
else:
mlflow.sklearn.log\_model(model, "model", signature=signature, input\_example=X\_test[:5])

CONFIGURAÇÃO DO RASTREAMENTO EXPERIMENTO

Para cada treinamento realizado, seja por meio de GridSearch ou não, podemos registrar métricas específicas no MLflow. O ideal é manter um conjunto de métricas padrão, o que permite comparar de forma consistente o desempenho entre diferentes modelos e abordagens.
Por tal razão que padronizamos a função “evaluate\_and\_log\_model” para sempre rastrear as mesmas métricas.

with mlflow.start\_run(run\_name="DecisionTree\_Regressor"):
param\_grid = {
'max\_depth': [3, 5, 10, None],
'min\_samples\_split': [2, 5, 10]
}
tree = DecisionTreeRegressor(random\_state=42)
grid\_search = GridSearchCV(tree, param\_grid, scoring=make\_scorer(mean\_absolute\_percentage\_error, greater\_is\_better=False), cv=5)
grid\_search.fit(X\_train, y\_train)
best\_model = grid\_search.best\_estimator\_
mlflow.log\_param("best\_max\_depth", best\_model.max\_depth)
mlflow.log\_param("best\_min\_samples\_split", best\_model.min\_samples\_split)
evaluate\_and\_log\_model("sklearn", "Decision Tree Regressor", best\_model, X\_test, y\_test)

CONFIGURAÇÃO DO RASTREAMENTO EXPERIMENTO

Mesmo utilizando GridSearch, o MLFlow é capaz de organizar as execuções mantendo as métricas somente do modelo com melhor desempenho.

CICLO PARA CONSTRUIR UM MODELO

EXPERIMENTAÇÃO
NO NOTEBOOK

REGISTRO DE DATASET

REGISTRO DE EXPERIMENTOS

REGISTRO DE MODELO

ESTÁGIO DO MODELO

ARTEFATO PARA API

API REST

FRONTEND

REGISTRO DE MODELOS

Os modelos são registrados de acordo com as especificações do arquivo de pipeline. Com os dados do artefato, incluindo métricas e gráficos do último modelo, ele será associado quando for realizado seu registro.

Os modelos podem ser registrados diretamente pela plataforma, em “Models”, como também via linha de comando. Vamos utilizar por linha de comando pois desta forma conseguimos automatizar via esteiras de entrega contínua.

run\_id = "211650eabbba4ef2a9cf2c7aed6fc36b"
mlflow.register\_model(model\_uri=f"runs:/{run\_id}/model", name="laptop-pricing-model")

Para registarmos precisamos do “run\_id” do experimento que será promovido ao modelo.
A cada novo registro uma nova versão será gerada.

Cada versão nova é referente a uma nova etapa de treinamento que modificou o modelo. O rastreamento de versão é fundamental para o acompanhamento do modelo

Registered model 'laptop-pricing-model' already exists. Creating a new version of this model... 2025/05/15 23:46:04 INFO mlflow.store.model\_registry.abstract\_store: Waiting up to 300 seconds for model version to finish creation. Model name: laptop-pricing-model, version 3 Created version '3' of model 'laptop-pricing-model'.

REGISTRO DE MODELOS

A mesma operação também é possível fazer no plataforma do MLFlow. A limitação é que a geração de um modelo novo pelo console não permite iniciar a esteira de CD/CI para lançar uma implantação do modelo em uma API.

REGISTRO DE MODELOS

Histórico de versões para acompanhar as evoluções dos modelos juntamente com os tipos de algoritmos utilizados.

REGISTRO DE MODELOS

Detalhes sobre descrição, tags e entrada e saída de dados esperados.

Quando implantamos um modelo novo em uma API existente precisamos ter cuidado com os dados de entrada e saída. Se for incluído ou removido alguma coluna de dados pelo modelo a API precisa estar preparada para enviar os dados no mesmo padrão.

Os testes de unidade garantem que mesmo que uma implantação seja disparada, o modelo novo não é lançado em produção até que os dados de entrada da API sejam ajustado, no caso de haver alterações.

ARTEFATOS DE MODELOS

No registro de modelos temos instruções de como acessá-lo. Podemos baixar o arquivo binário do modelo ou simplesmente carregar diretamente em tempo de execução.
Como nossa API deverá ter uma ajuste nos dados de entrada vamos optar por baixar o arquivo binário (Pickle) e integrar diretamente.

Carregar diretamente em tempo de execução não é recomendável pois a API não pode estar preparada para alterações de entrada. Prefira uma arquitetura imutável para evitar surpresas em produção.

ARTEFATOS DE MODELOS

A forma mais simples de acessar o modelo registrado é via a função “load\_model”.
Indicada para uso experimental em Notebooks ou ambientes que não requer integrações com outros sistemas.

ARTEFATOS DE MODELOS

Prefira baixar diretamente o arquivo binário e incorporá-lo na API.
Procure pela última versão
Baixe o modelo padronizado (model.pkl)
Armazene os metadados do modelo para rastreamento de versão
Após isso carregue na API em produção quando for gerado uma nova imagem do container.
Este script pode ser colocado nas esteiras de CD/CI durante o registro de um modelo novo ou devido a alguma alteração no código-fonte da API.

mlflow.set\_tracking\_uri("https://dagshub.com/michelpf/fiap-ds-mlops-laptop-pricing-brl.mlflow")
# Configurações
model\_name = "laptop-pricing-model"
artifact\_relative\_path = "model/model.pkl"
client = MlflowClient()
# 1. Buscar todas as versões do modelo
versions = client.search\_model\_versions(f"name='{model\_name}'")
# 2. Obter a versão mais recente
latest = max(versions, key=lambda v: int(v.version))
# 3. Baixar o artefato
download\_path = client.download\_artifacts(
run\_id=latest.run\_id,
path=artifact\_relative\_path,
dst\_path="."
)
model\_metadata = {
"model\_name": model\_name,
"version": latest.version,
"run\_id": latest.run\_id,
"source": latest.source,
"downloaded\_at": datetime.now().isoformat()
}
with open("model/model\_metadata.json", "w") as f:
json.dump(model\_metadata, f, indent=2)

CICLO PARA CONSTRUIR UM MODELO

EXPERIMENTAÇÃO
NO NOTEBOOK

REGISTRO DE DATASET

REGISTRO DE EXPERIMENTOS

REGISTRO DE MODELO

ESTÁGIO DO MODELO

ARTEFATO PARA API

API REST

FRONTEND

API REST EM CLOUD

SERVERLESS

Antes de começar qualquer coisa: a arquitetura se adequa às capacidades tecnológicas da equipe?
Nós exploramos a capacidade de Serverless?
Quanto a estimativa do calculadora indica?

Lambda has 1 MM/month requests
always free tier

AWS Lambda

10 MM req/month

Amazon SQS

Amazon ECR

Amazon ECS

BLUEPRINT

Iniciando nossa análise para uma API REST precisamos considerar alguns pontos importantes

Armazenamento

Log de Eventos

Observabilidade

Segurança

Endpoint de Entrada

AWS Lambda

Amazon ECR

Amazon CloudWatch

Amazon API Gateway

SYSTEM DESIGN

AWS Lambda

Amazon ECR

Amazon CloudWatch

Amazon API Gateway

AWS Fargate

Amazon EKS

Model Product

XYZ Products (Backend or Batch)

Streamlit Cloud

Laptop Pricing

FUNÇÃO LAMBDA

Principais características:
Serverless: Você não precisa provisionar nem gerenciar servidores. A AWS cuida da infraestrutura, permitindo que o desenvolvedor se concentre apenas no código.
Escalabilidade Automática: As funções Lambda são dimensionadas automaticamente, o que significa que elas podem lidar com qualquer quantidade de tráfego, desde algumas chamadas por mês até milhões de chamadas por segundo.
Pagamento por Uso: Você paga apenas pelo tempo de execução das funções Lambda e pelos recursos computacionais consumidos durante a execução do código. Não há taxas mínimas nem custos fixos.
Integração com Serviços AWS: As funções Lambda podem ser facilmente integradas com outros serviços da AWS, como S3, DynamoDB, API Gateway, SNS, SQS, e muitos outros, o que permite criar aplicações complexas e altamente escaláveis.

Uma função Lambda da AWS é um tipo de serviço de computação serverless. Ela permite que você execute código sem precisar provisionar ou gerenciar servidores.
Permite executar código em resposta a eventos, como alterações em dados no Amazon S3, atualizações em tabelas do Amazon DynamoDB, chamadas de API no Amazon API Gateway, entre outros. As funções Lambda podem ser escritas em várias linguagens de programação, incluindo Python, Node.js, Java, C#, e outras.

FUNÇÃO LAMBDA

As funções Lambdas também podem ser iniciadas por outros componentes, como um API Gateway, para processamento síncrono ou outras formas assíncronas, como eventos, filas ou ações baseadas em eventos específicos do S3, como criação ou modificação de objetos, por exemplo.
Os eventos são disparados para iniciar e também há eventos de pós-processamento, seja num evento de erro ou sucesso para notificações ou ações encadeadas.

Amazon S3

Amazon SQS

Amazon API Gateway

Amazon SNS

Amazon DynamoDB

AWS Lambda

Amazon EventBridge

Amazon SNS

Amazon SQS

MODOS DE DEPLOY: CONTAINER

Uma função Lambda pode ser implantada das seguintes maneiras:
Programar diretamente no Console. Opção limita a instalação de pacotes adicionais além do Boto3.
Programar localmente (VSCode, por exemplo), depois enviar o arquivo compactado com as dependências.
Criar uma imagem de contêiner num registro e associar a imagem a uma função.
Implantações padrão (não por contêiner) tem a limitação de tamanho máximo de 250MB (descompactado, com 50MB compactado).
Por contêiner possui limite de 10GB de armazenamento.

MODOS DE DEPLOY: PADRÃO

No deploy local precisamos separar numa pasta temporária os arquivos para compactar. Note que as bibliotecas utilizadas precisam estar na raiz e não na pasta do ambiente virtualizado, por isso instalamos as dependências com o parâmetro “-t” de target.

mkdir deploy
pip install -r .\requirements.txt -t deploy
copy app.py deploy
cd deploy
zip -r function.zip .

Após compactarmos, enviamos o arquivo pela Console da AWS, em “Código”, depois “Fazer Upload” e então de arquivo local. Com a implantação terminada, a pasta deploy pode ser removida.
Ou utilizar o comando abaixo para carregar via AWS CLI.

aws lambda update-function-code --function-name detectar-face --zip-file fileb://function.zip

API GATEWAY

Principais características:
Criação de APIs RESTful e WebSocket: suporta a criação de APIs RESTful tradicionais, bem como APIs WebSocket para aplicativos que necessitam de comunicação bidirecional em tempo real.
Integração com Serviços AWS e HTTP/S: integração de APIs com serviços da AWS, como Lambda, DynamoDB, S3, entre outros, além de serviços HTTP/S externos.
Gerenciamento de Tráfego e Versões: permite controlar o tráfego para diferentes versões de suas APIs, além de oferecer suporte para testes e implantações canário.
Autenticação e Autorização: oferece recursos avançados de autenticação e autorização, incluindo integração com o AWS Identity and Access Management (IAM), tokens JWT (JSON Web Tokens), Cognito, entre outros.
Monitoramento e Logging: fornece métricas detalhadas, registros de acesso e monitoramento em tempo real, permitindo que você monitore o desempenho e a integridade de suas APIs.
Segurança: protege as APIs contra ameaças comuns, como ataques de DDoS (Distributed Denial of Service) e injeção de SQL, além de oferecer suporte para criptografia SSL/TLS.

O Amazon API Gateway é um serviço da AWS que facilita a criação, publicação, manutenção, monitoramento e proteção de APIs (Application Programming Interfaces) RESTful e WebSocket para aplicativos na nuvem.
Ele atua como uma porta de entrada para os aplicativos acessarem os dados, a lógica de negócios ou os serviços de back-end de forma segura e escalável.

ELASTIC CONTAINER REGISTRY (ECR)

Principais características:
Repositório de Imagens Docker: fornece repositórios privados para armazenar e gerenciar imagens de contêineres Docker.
Segurança e Controle de Acesso: as imagens do ECR são armazenadas de forma segura e privada. É possível controlar o acesso aos repositórios usando políticas de acesso baseadas em IAM (Identity and Access Management) da AWS, garantindo que apenas usuários autorizados possam acessar e implantar imagens de contêineres.
Integração com Serviços AWS: é totalmente integrado com outros serviços da AWS, como o Amazon ECS, o Amazon EKS e o AWS Lambda, permitindo que você implante facilmente contêineres em escala na nuvem da AWS.
Escalabilidade e Disponibilidade: é altamente escalável e oferece alta disponibilidade, permitindo armazenar e implantar imagens de contêineres em escala, mesmo para cargas de trabalho de missão crítica.
Integração com Ferramentas de Desenvolvimento: O ECR é compatível com várias ferramentas de desenvolvimento e CI/CD (Continuous Integration/Continuous Deployment), como Docker CLI, AWS CLI, Jenkins, GitLab CI, e muitas outras, facilitando a integração com seus fluxos de trabalho de desenvolvimento existentes.

O Amazon Elastic Container Registry (ECR) é um serviço gerenciado da AWS que permite armazenar, gerenciar e implantar imagens de contêineres Docker.
Fornece um repositório seguro e privado para armazenar imagens de contêineres Docker. Ele é integrado com outros serviços da AWS, como o Amazon ECS (Elastic Container Service) e o Amazon EKS (Elastic Kubernetes Service), facilitando a implantação de contêineres em escala na nuvem da AWS.

API GATEWAY

Como o próprio nome diz, o termo “Gateway” é uma porta de entrada para os serviços da AWS, garantindo segurança e flexibilidade para integrações com outros componentes.
Apesar do Lambda ser a mais comum, é possível também integrá-lo com o DynamoDB e o S3, diretamente.
Por ser um serviço público, ele pode ser acessado tanto internamente quanto externamente.

Amazon S3

AWS Lambda

Amazon DynamoDB

Usuários

Parceiro A

AWS Lambda

S3: SIMPLE STORAGE SERVICE

Principais características:
Armazenamento de Objetos: armazena dados na forma de objetos, que podem ser arquivos de qualquer tipo, desde documentos e imagens até vídeos e backups de banco de dados.
Escalabilidade e Disponibilidade: Ele é altamente escalável e pode acomodar desde alguns gigabytes até vários petabytes de dados. Além disso, o S3 é projetado para oferecer alta disponibilidade, com durabilidade de 99,999999999% (onze noves) dos objetos armazenados.
Modelo de Consistência: O S3 oferece um modelo de consistência forte para todas as operações de leitura, garantindo que os objetos recuperados sejam os mais recentes e consistentes.
Controle de Acesso: Ele fornece recursos avançados de controle de acesso, permitindo que você defina políticas granulares de permissões de acesso aos seus dados usando o IAM (Identity and Access Management) da AWS.
Segurança: O S3 oferece várias camadas de segurança para proteger seus dados, incluindo criptografia em repouso e em trânsito, controle de acesso baseado em políticas, e integração com outros serviços de segurança da AWS.
Integração com Outros Serviços: O S3 pode ser facilmente integrado com outros serviços da AWS, como Lambda, API Gateway, CloudFront, e serviços de processamento de big data, como o Amazon EMR e o Amazon Athena.

O Amazon S3 é um serviço de armazenamento de objetos da AWS que oferece escalabilidade, disponibilidade, segurança e desempenho para armazenar e recuperar dados na nuvem.
É um serviço de armazenamento de objetos altamente escalável e durável, projetado para armazenar e recuperar grandes volumes de dados de forma segura e eficiente. Ele é amplamente utilizado para uma variedade de casos de uso, como armazenamento de backups, hospedagem de arquivos estáticos para websites, distribuição de conteúdo, armazenamento de dados para aplicativos móveis e análises de big data, entre outros.

S3: SIMPLE STORAGE SERVICE

Por ser um serviço de armazenamento de objetos, ele possui classes de armazenamento associado a cada caso de uso, combinando performance e custo. A ordem das classes é para o dado armazenado mais quente (mais utilizado) para o mais frio (menos utilizado)

Intelligent-Tiering: é projetada para otimizar automaticamente os custos e o desempenho, movendo os objetos entre as camadas de armazenamento frequentemente acessadas e as camadas de armazenamento infrequentemente acessadas, com base nos padrões de acesso aos dados ao longo do tempo.
S3 Standard: classe padrão do S3, oferecendo alta disponibilidade, durabilidade e desempenho para dados frequentemente acessados.
Standard-IA: oferece os mesmos benefícios do Standard, mas com custos mais baixos para dados que são acessados com menos frequência.
One Zone-IA: oferece os mesmos benefícios do S3 Standard-IA, mas armazena os dados em apenas uma zona de disponibilidade, tornando-a mais econômica.
Glacier Flexible Retrieval: classe de armazenamento de "glacier" que oferece uma recuperação flexível dos dados, permitindo que você recupere os dados em minutos a horas.
Glacier Deep Archive: classe de armazenamento de "glacier" é projetada para dados que são acessados raramente e exigem uma recuperação ainda mais econômica do que o S3 Glacier Flexible Retrieval.
Glacier Instant Retrieval: esta é uma opção de recuperação instantânea para dados armazenados no S3 Glacier, permitindo que recuperar os dados em segundos.

S3: PRINCIPAIS COMANDOS DA API

Para realizar os comandos abaixo você precisa configurar as chaves de acesso via AWS CLI ou especificá-las no cliente. Esta última opção não é recomendada por expor as chaves em base de código.

import boto3
# Crie um cliente S3
s3\_client = boto3.client('s3')

# Listar todos os buckets
response = s3\_client.list\_buckets()
for bucket in response['Buckets']:
    print(bucket['Name'])

# Criar um novo bucket
bucket\_name = 'nome-do-seu-bucket'
s3\_client.create\_bucket(Bucket=bucket\_name)

# Enviar um arquivo para um bucket
file\_path = 'caminho/para/seu/arquivo.txt'
object\_key = 'nome-do-arquivo-no-s3.txt'
bucket\_name = 'nome-do-seu-bucket'
s3\_client.upload\_file(file\_path, bucket\_name, object\_key)

import boto3
# Defina suas chaves de acesso
ACCESS\_KEY\_ID = 'sua\_access\_key\_id'
SECRET\_ACCESS\_KEY = 'sua\_secret\_access\_key'
# Crie um cliente S3 com as chaves de acesso
s3\_client = boto3.client(
    's3',
    aws\_access\_key\_id=ACCESS\_KEY\_ID,
    aws\_secret\_access\_key=SECRET\_ACCESS\_KEY
)

Utilize com cautela esta opção de cliente.

S3: PRINCIPAIS COMANDOS DA API

Bucket é o nome reservatório dos arquivos. Object é o nome dos arquivos que podem incluir diretórios, por exemplo: “arquivo.txt” ou “arquivos/arquivo.txt” é um objeto da mesma forma.
É possível criar pastas sem objetos diretamente no console.

# Listar todos os objetos em um bucket
bucket\_name = 'nome-do-seu-bucket'
response = s3\_client.list\_objects\_v2(Bucket=bucket\_name)
for obj in response['Contents']:
    print(obj['Key'])

# Baixar um arquivo do S3
object\_key = 'nome-do-arquivo-no-s3.txt'
bucket\_name = 'nome-do-seu-bucket'
local\_file\_path = 'caminho/para/salvar/o/arquivo.txt'
s3\_client.download\_file(bucket\_name, object\_key, local\_file\_path)

# Excluir um objeto do S3
object\_key = 'nome-do-arquivo-no-s3.txt'
bucket\_name = 'nome-do-seu-bucket'
s3\_client.delete\_object(Bucket=bucket\_name, Key=object\_key)

CONTEINERIZAÇÃO

VIRTUALIZAÇÃO DE INFRAESTRUTURA

Conforme as aplicações vão crescendo e evoluindo, precisam de recursos e isolamento para trabalharem para extrair o máximo de seus recursos. Utilizando um servidor físico torna limitado essa flexibilidade pois teríamos que utilizar apenas um único sistema operacional, não podemos utilizar a mesma porta e também as versões e runtimes de interpretadores ficariam fixados em uma única versão.
Para resolver este problema as máquinas virtuais, como o EC2 da AWS foram criadas.

HARDWARE

SISTEMA OPERACIONAL (SO)

HYPERVISOR

SO VIRTUALIZADO
WINDOWS

SO VIRTUALIZADO
LINUX

SO VIRTUALIZADO
LINUX

SO VIRTUALIZADO
MACOS

PYTHON 2

PYTHON 3.7
HTTPD PORTA 80/443

PYTHON 3.8
HTTPD PORTA 80/443

PYTHON 3.10

CONTEINEIRIZAÇÃO DE APLICAÇÕES

Com a conteinerização de aplicações alcançamos os mesmos objetivos principais da virtualização, com um custo menor pois não precisamos instalar novos sistemas operacionais.
Imagens formados por camadas ainda ajudam a ser mais eficiente no espaço físico e memória ao promover maior reutilização.
Da mesma forma como nas máquinas virtuais, os contêineres alcançam os mesmos níveis de isolamento, como processos, rede, memória, rede, armazenamento, e inclusive de kernel (como se fosse outro host).

HARDWARE

SISTEMA OPERACIONAL (SO)

EXECUTANDO CONTAINERS

Uma vez instalado o Docker podemos executar containers diretamente na máquina de desenvolvimento.
Para verificação se deu tudo certo, vamos iniciar o “hello world” do Docker.

docker run hello-world

Unable to find image 'hello-world:latest' locally
latest: Pulling from library/hello-world
c1ec31eb5944: Pull complete
Digest: sha256:4bd78111b6914a99dbc560e6a20eab57ff6655aea4a80c50b0c5491968cbc2e6
Status: Downloaded newer image for hello-world:latest
Hello from Docker!
This message shows that your installation appears to be working correctly.
To generate this message, Docker took the following steps:
1. The Docker client contacted the Docker daemon.
2. The Docker daemon pulled the "hello-world" image from the Docker Hub.
(amd64)
3. The Docker daemon created a new container from that image which runs the
executable that produces the output you are currently reading.
4. The Docker daemon streamed that output to the Docker client, which sent it
to your terminal.
To try something more ambitious, you can run an Ubuntu container with:
$ docker run -it ubuntu bash
Share images, automate workflows, and more with a free Docker ID:
https://hub.docker.com/
For more examples and ideas, visit:
https://docs.docker.com/get-started/

Obtendo imagem de um registry (DockerHub)

O comando docker run automaticamente faz um pull da imagem quando ela não é encontrada no DockerHub.

CONTAINER REGISTRY: DOCKERHUB

Assim como códigos são versionados no GitHub, containers são versionados no DockerHub, um registro de containers.
Neste registro público podemos encontrar diversas imagens de containers para uso, baseado nas mais diversas necessidades, como versões de Python específicas, sistema operacional, e até mesmo imagens reduzidas para diminuir o tamanho para implantações que utilize o mínimo necessário.

https://hub.docker.com/\_/hello-world

COMANDOS PRINCIPAIS

Listar todos os containers em execução ou não.

docker container ls –a
CONTAINER ID IMAGE COMMAND CREATED STATUS PORTS NAMES
9ab4e976549c hello-world "/hello" 10 seconds ago Exited (0) 6 seconds ago musing\_gagarin
1b97f144ea22 hello-world "/hello" 7 hours ago Exited (0) 7 hours ago fervent\_pare

O container sempre vai executar um comando especificado dentro do “Dockerfile”. Após ele executar o comando ele termina a execução.
Servidores web contém comando que inicia um processo aguardando conexões, neste caso o container fica executando indefinidamente.

Executar comandos dentro da imagem do docker. Exemplo: exibir o conteúdo da pasta var dentro do container ubuntu.

docker run ubuntu ls var
backups
cache
lib
local
lock
log
mail
opt
run
spool
tmp

COMANDOS PRINCIPAIS

Mapeamento de portas. O “-d” é de detached (para não travar o console), 8080 é a porta local mapeada para a porta 80 do container.

docker run –d –p 8080:80 dockersamples/static-site
CONTAINER ID IMAGE COMMAND CREATED STATUS PORTS NAMES
331325df8538 ubuntu "sleep 1d" About a minute ago Up About a minute cool\_liskov

Exibir o mapeamento de porta

docker port 6b35c0cc8acb
80/tcp -> 0.0.0.0:8080

Com este mapeamento conseguimos acessar o conteúdo do container da máquina host.
Com todos os isolamentos existentes, o mapeamento de porta torna possível que a porta 8080 seja redirecionada para dentro do container para a porta 80.

COMANDOS PRINCIPAIS

Containers em execução.

docker ps
CONTAINER ID IMAGE COMMAND CREATED STATUS PORTS NAMES
331325df8538 ubuntu "sleep 1d" About a minute ago Up About a minute cool\_liskov

Interromper a execução.

Reiniciar a execução.

docker start 331325df8538
331325df8538

docker stop 331325df8538
331325df8538

Modo iterativo. Executar comandos dentro do container.

docker exec -it 331325df8538 bash
root@331325df8538:/# ls
bin boot dev etc home lib lib32 lib64 libx32 media mnt opt proc root run sbin srv sys tmp usr var
root@331325df8538:/#

Experimente instalar o Python (apt update | apt install python3).

Remover container (após interrompê-lo). Perderá todos os dados armazenados.

docker rm 331325df8538
331325df8538

CAMADAS DE IMAGENS

As camadas formam uma imagem. Elas podem ser reutilizadas, o que diminui consideravelmente o tamanho de arquivos que precisam ser transferidos. Uma das camadas é de escrita para operações dentro do container, as demais são somente leitura por conta do reuso.

REGISTRY (DockerHub)

Imagem A

Imagem B

Imagem A

Imagem B

Primeira imagem, é baixado todas as camadas.

Nesta imagem, há camadas já baixadas, portanto serão reutilizadas. As faltantes, serão baixadas do registro.

Imagens reutilizadas.

DOCKERFILE

O Dockerfile é como se fosse a “receita” do container. Neste arquivo é especificado a imagem, mapeamento de portas, comandos de cópia de arquivos além de processos que precisam ser executados.

DOCKERFILE

IMAGEM

CONTAINER

Build

Run

Imagem base
Cópia de arquivos (código fonte, modelo)
Instalação de dependências
Inicialização

DOCKERFILE PARA IMAGEM DE CONTAINER

O arquivo Docker file é como se fosse uma receita para montarmos uma imagem customizada, copiando arquivos necessário, baixando uma imagem de base e configurando aplicações para serem executadas ao iniciar sua execução.

# Use a imagem oficial Python como base
FROM python:3
# Copy requirements.txt
WORKDIR /app
# Install the specified packages
COPY ..
# Invoca o compando python app/app.py
CMD [ "python", "app/app.py" ]

Obtendo imagem de um registry (DockerHub)

Pasta de trabalho, onde os arquivos serão copiados

Instala as dependências

Executa o comando ao iniciar

https://docs.docker.com/engine/reference/builder/

ANATOMIA DA API

A função básica da API é retornar via interface RESTFUL a previsão de preço de um determinado modelo de laptop, utilizando a última versão do modelo em produção.

CARREGAR MODELO

CONVERTER PAYLOAD PARA FEATURES

ARMAZENAR REQUISIÇÕES

REALIZAR INFERÊNCIA

LOGAR EVENTOS E MÉTRICAS

A imagem do container deve conter a última versão do modelo.
Toda a vez que o modelo for atualizado, uma nova versão da imagem precisa ser gerada.

O uso do one-hot encoding não é trivial. Afim de manter uma boa usabilidade, utilizaremos um payload no formato JSON e faremos a conversão na própria API.

Executar o modelo, associando sua versão utilizada.

Salvar em um arquivo CSV incremental para análises de desvio de dados e modelo para acompanhamento.

Acompanhamento de métricas de infraestrutura e distribuição dos dados do modelo.
Log granular e dashboards consolidados para observabilidade.

CARREGAR O MODELO

No início do código principal (app.py) incluiremos as importações necessárias para a carga do modelo serializado, acesso a serviços da AWS como o log de eventos Cloudwatch e o componente datetime para armazenamento de timestamp dos eventos da API.
Note que como controlamos a versão do modelo por tags, não faria sentido embutir este dado como metadado do próprio modelo. Por tal razão utilizaremos um arquivo texto que informa a versão utilizada do modelo.

import boto3
import joblib
import json
model = joblib.load("model/model.pkl")
with open("model/model\_metadata.json", "r") as f:
model\_info = json.load(f)
cloudwatch = boto3.client("cloudwatch")

{
"model\_name": "laptop-pricing-model",
"version": "5",
"run\_id": "211650eabbba4ef2a9cf2c7aed6fc36b",
"source": "mlflow-artifacts:/3ef16225938f4c37b7566d2fc4480a7c/211650eabbba4ef2a9cf2c7aed6fc36b/artifacts/model",
"downloaded\_at": "2025-06-01T14:09:58.259050"
}

model\_metadata.json

CONVERTER PAYLOAD EM FEATURES

Os dados categóricos viram 0 ou 1 para cada coluna de treinamento.
Os dados numéricos permanecem como tal, porém com o tipo de dado convertido.
Ao final teremos um vetor de entrada puramente numérico, o que é esperado para interferência de um modelo.

def prepare\_payload(data):
 data\_processed = []
data\_processed.append(int(data["ram\_gb"]))
data\_processed.append(int(data["ssd"]))
data\_processed.append(int(data["hdd"]))
data\_processed.append(int(data["graphic\_card"]))
data\_processed.append(int(data["warranty"]))
data\_processed.append(1) if data["brand"] == "asus" else data\_processed.append(0)
data\_processed.append(1) if data["brand"] == "dell" else data\_processed.append(0)
data\_processed.append(1) if data["brand"] == "hp" else data\_processed.append(0)
data\_processed.append(1) if data["brand"] == "lenovo" else data\_processed.append(0)
data\_processed.append(1) if data["brand"] == "other" else data\_processed.append(0)
data\_processed.append(1) if data["processor\_brand"] == "amd" else data\_processed.append(0)
data\_processed.append(1) if data["processor\_brand"] == "intel" else data\_processed.append(0)
data\_processed.append(1) if data["processor\_brand"] == "m1" else data\_processed.append(0)
data\_processed.append(1) if data["processor\_name"] == "core i3" else data\_processed.append(0)
data\_processed.append(1) if data["processor\_name"] == "core i5" else data\_processed.append(0)
data\_processed.append(1) if data["processor\_name"] == "core i7" else data\_processed.append(0)
data\_processed.append(1) if data["processor\_name"] == "other" else data\_processed.append(0)
data\_processed.append(1) if data["processor\_name"] == "ryzen 5" else data\_processed.append(0)
data\_processed.append(1) if data["processor\_name"] == "ryzen 7" else data\_processed.append(0)
data\_processed.append(1) if data["os"] == "other" else data\_processed.append(0)
data\_processed.append(1) if data["os"] == "windows" else data\_processed.append(0)
data\_processed.append(1) if data["weight"] == "casual" else data\_processed.append(0)
data\_processed.append(1) if data["weight"] == "gaming" else data\_processed.append(0)
data\_processed.append(1) if data["weight"] == "thinnlight" else data\_processed.append(0)
data\_processed.append(1) if data["touchscreen"] == "0" else data\_processed.append(0)
data\_processed.append(1) if data["touchscreen"] == "1" else data\_processed.append(0)
data\_processed.append(1) if data["ram\_type"] == "ddr4" else data\_processed.append(0)
data\_processed.append(1) if data["ram\_type"] == "other" else data\_processed.append(0)
data\_processed.append(1) if data["os\_bit"] == "32" else data\_processed.append(0)
data\_processed.append(1) if data["os\_bit"] == "64" else data\_processed.append(0)
 return data\_processed

REALIZAR INFERÊNCIA

A parte principal da API, onde é chamado os demais módulos, carregado o modelo e executado.

def handler(event, context):
print(event)
data = event["data"]
print(data)
data\_processed = prepare\_payload(data)
prediction = model.predict([data\_processed])
print(prediction)
prediction = int(prediction[0])
write\_real\_data(data, prediction)
input\_metrics(data, prediction)
return {
'statusCode': 200,
'prediction': int(prediction),
'version': model\_version
}

As saídas em console (print) são automaticamente armazenadas como registro do Cloudwatch.
Opcionalmente podemos utilizar alguma classe de Logging já existente do Python para um controle mais flexível do que deverá ser armazenado.

CONVERTER PAYLOAD PARA FEATURES

ARMAZENAR REQUISIÇÕES

REALIZAR INFERÊNCIA

LOGAR EVENTOS E MÉTRICAS

ARMAZENAR REQUISIÇÕES

Análises de desvios de dados são essenciais depois que um modelo é colocado em produção. Por este motivo precisamos de uma forma de armazenar cada requisição em um arquivo CSV num bucket S3.

O arquivo será acumulado por dia.

def write\_real\_data(data, prediction):
 now = datetime.now()
now\_formatted = now.strftime("%d-%m-%Y %H:%M")
 file\_name = f"{now.strftime('%Y-%m-%d')}\_laptop\_prediction\_data.csv"
data["price"] = prediction
data["timestamp"] = now\_formatted
data["model\_version"] = model\_version
s3 = boto3.client("s3")
bucket\_name = "fiap-ds-mlops"
s3\_path = "laptop-prediction-real-data"
 try:
existing\_object = s3.get\_object(Bucket=bucket\_name, Key=f'{s3\_path}/{file\_name}’)
existing\_data = existing\_object['Body'].read().decode('utf-8').strip().split('\n’)
existing\_data.append(','.join(map(str, data.values())))
updated\_content = '\n'.join(existing\_data)
except s3.exceptions.NoSuchKey:
# Se o arquivo não existir, cria um novo
updated\_content = ','.join(data.keys()) + '\n' + ','.join(map(str, data.values()))
 s3.put\_object(Body=updated\_content, Bucket=bucket\_name, Key=f'{s3\_path}/{file\_name}')

Esta arquitetura pode evoluir para uma solução baseado em eventos e um processador serializar a escrita/leitura do arquivo CSV para acumular dados e evitar, apesar de raro, eventuais acessos simultâneos.

Se o arquivo não existir (novo dia), será criado um novo.
Note que estamos escrevendo as colunas dos dados como primeira linha.

Adicionando colunas além do treinamento: timestamp da execução, previsão e versão do modelo.

O S3 não contém uma função de acumular (append), por isso o arquivo é lido antes de escrever com os dados novos.

LOGAR EVENTOS E MÉTRICAS

As métricas personalizadas do Cloudwatch permite que enviemos informações das requisições e assim acompanhar a distribuição dos dados consumidos em tempo real. Já as métricas de infraestrutura já são calculadas automaticamente, sem a necessidade de enviar,.

Métrica numérica

Métrica cumulativa

def input\_metrics(data, prediction):
cloudwatch.put\_metric\_data(
MetricData = [
{
'MetricName': 'Price Prediction’,
'Value': prediction,
'Dimensions': [{'Name': "Currency", 'Value': "INR"}]
},
], Namespace='Laptop Pricing Model’)
 for key, value in data.items():
cloudwatch.put\_metric\_data(
MetricData = [
{
'MetricName': 'Latptop Feature ‘,
'Value': 1,
'Unit': 'Count’,
'Dimensions': [{'Name': key, 'Value': str(value)}]
},
], Namespace='Laptop Pricing Features')

DOCKERFILE DA API PARA SERVIR UM MODELO

A função para consumir a API e servir numa API será realizada por um Lambda. Por isso já existe uma imagem base oficial da AWS que contém tudo o que é necessário para o container funcionar nesta condição.

# Use a imagem oficial Python como base
FROM public.ecr.aws/lambda/python:3.10
# Copy requirements.txt
COPY requirements.txt ${LAMBDA\_TASK\_ROOT}
# Install the specified packages
RUN pip install -r requirements.txt
# Copy function code
COPY src/app.py ${LAMBDA\_TASK\_ROOT}
# Copy model file
COPY model/model.pkl ${LAMBDA\_TASK\_ROOT}/model/
# Copy version file
COPY model/model\_metadata.json ${LAMBDA\_TASK\_ROOT}/model
# Set the CMD to your handler (could also be done as a parameter override outside of the Dockerfile)
CMD [ "app.handler" ]

Obtendo imagem de um registry (Public ECR)

Copia arquivo de dependências local para o caminho onde a função é armazenada

Instala as dependências

Copia script Python da função

Copia modelo binário

Copia metadado do modelo

Comando padrão a ser executado ao iniciar o container. Indica o arquivo .py seguido do nome da função

https://docs.docker.com/engine/reference/builder/

EXECUTANDO CONTAINER LOCAL

Depois de criar a especificação, vamos montar a imagem, construir o container, copiar alguns arquivos para teste local e abrir o modo iterativo.

docker build --platform linux/amd64 -t laptop-pricing-api-brl .
[+] Building 889.8s (11/11) FINISHED docker:default
=> [internal] load .dockerignore 0.3s
=> => transferring context: 2B
…

docker cp test.py d23b4b71a097:/var/task
docker cp data.json d23b4b71a097:/var/task

docker exec -it d23b4b71a097 bash

yum update –y
yum install awscli -y

aws configure

python test.py

Copiar os arquivos de teste para invocar a função.

Abrir o container no modo interativo.

Instalar o AWS CLI e configurar

Finalmente executar o teste

Em produção não precisamos instalar o AWS CLI pois as permissões são concedidas no próprio Lambda.
Não será levado em produção estes arquivos adicionais, eles servem apenas para testar localmente.

docker run -d laptop-pricing-api 

Executar o container no modo detached

O Platform precisa ser o mesmo do runner escolhido ao criar uma Lambda

CRIANDO UM REGISTRY PRIVADO

Aplicações corporativas utilizam um repositório de registro privado de forma semelhante com o versionamento dos códigos.
Quando for criar um repositório, marque a opção privado e indique o nome do repositório.
Cada repositório é dedicado uma imagem de container.

OBTENDO COMANDOS DO REGISTRY

Com o respositório criado, obtemos os comandos para autenticar e enviar a imagem local para o repositório remoto.
Os comandos são obtidos ao clicar em “Visualizar comandos push” no painel do repositório.

CARREGANDO IMAGEM NO REGISTRY

Após validarmos que o container foi executado como esperado e a imagem está validada, precisamos enviar para um registro para que possa ser utilizada em novas implantações
Para aplicações corporativas utilizamos registros de imagem privados, como o Elastic Container Registry (ECR da AWS. O DockerHub é outra possibilidade, mas neste caso para imagens públicas. O ECR também tem repositórios públicos para distribuição de imagens padrão compatíveis e validadas com os serviços da AWS.

docker tag laptop-pricing-api:latest 989944764342.dkr.ecr.us-east-1.amazonaws.com/laptop-pricing-api:latest

docker push 989944764342.dkr.ecr.us-east-1.amazonaws.com/laptop-pricing-api:latest

Primeiro incluímos o tag com o nome da imagem e sua versão. É comum utilizarmos o nome “latest” para indicar que é a última versão disponível (e atualizada).

Depois iremos enviar os dados para o registro. Alguns repositórios necessitam de login e autenticação antes, como o Docker. Como estamos com o AWS CLI já autenticado com as devidas permissões, o acesso já está autorizado, mas precisamos enviar o comando para autenticar.

Existem serviços baseados em containers da qual quando há uma nova versão “latest” no repositório inicia o processo de entrega contínua atualizando automaticamente o recurso. Não é o caso das funções Lambda. É necessário atualizar via comando a nova versão da imagem mesmo que seja a mesma.

aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 989944764342.dkr.ecr.us-east-1.amazonaws.comD

CRIANDO LAMBDA CONTEINER

Para criar um Lambda baseado em contêiner selecionamos a opção “Imagem de contêiner”.
Logo depois indicamos qual a URL da imagem, buscando pelos repositórios disponíveis.
Depois selecionamos a arquitetura, recomenda-se ARM64 por ser mais eficiente computacionalmente e menos custosa.

ADICIONANDO PERMISSÕES

Após a função ter sido implantada, precisamos incluir as permissões adicionais (além do padrão) que permitirá adicionar métricas e alarmes customizados além de escrita em bucket S3.
Vamos clicar no nome da função abaixo para ir ao IAM realizar as modificações.

ADICIONANDO PERMISSÕES

Criando políticas em linha incluímos as permissões que precisamos:
No Cloudwatch: PutMetricAlarm e PutMetricData.
No S3: acesso de leitura e escrita (para simplificar adicionamos todas as permissões).

Em cloud utilizamos sempre a regra do menor privilégio. Ou seja, as permissões precisam ser exatamente as mínimas necessárias tanto de operações (o quê) e também onde (qual componente, por exemplo bucket).

TUDO PRONTO: EVENTO DE TESTE

A API está pronta para uso.
Nosso primeiro teste será na console do Lambda com um evento de teste. Será utilizado o mesmo payload que a API irá receber.

{
"data": {
"brand": "dell",
"processor\_brand": "intel",
"processor\_name": "core i5",
"os": "windows",
"weight": "casual",
"warranty": "2",
"touchscreen": "0",
"ram\_gb": "16",
"hdd": "0",
"ssd": "256",
"graphic\_card": "8",
"ram\_type": "ddr4",
"os\_bit": "64"
}
}

Payload

ANALISANDO TESTE

O contêiner quando é recém implantado pode apresentar um erro de timeout pois o padrão do tempo de execução máxima é de 3 segundos. Caso apresente esse erro, tente novamente.
Com o contêiner pronto para execução, o retorno esperado é código 200 (statusCode) e o valor da predição no JSON de resposta. 

Resposta da função (API)

Log dos últimos eventos.

ETAPA FINAL DA API: API GATEWAY

Com o Lambda funcionando (função), precisamos integrar num API Gateway para um controle mais preciso de acesso, cotas de uso e mais segurança.
O API Gateway fornecerá a URL de acesso para ser consumido pelo frontend ou outros serviços.

Amazon API Gateway

AWS Lambda

Nosso tipo de API Gateway é API REST.

CARREGANDO IMAGEM NO REGISTRY

Depois de selecionar o tipo de API para criar podemos criar uma nova (do zero) ou utilizar algum acelerador disponível, como importar da especificação OpenAPI (antigo Swagger), clonar uma existente ou utilizar uma de exemplo.
Preencher o nome da API (ela ficará exposta no endereço do endpoint, por isso use um nome identificável e sugestivo).
Utilize a descrição para informar detalhes da API, se necessário.

CRIAR UMA ROTA OU RECURSO

O primeiro passo é criar um recurso que servirá de rota para acesso.
Por exemplo, o nosso endpoint com o recurso “predict” será assim: https:///predict

CRIANDO UM MÉTODO

Com a API e o recurso criado, podemos finalmente criar o método de consumo (“Criar método”).
No método incluiremos a integração com o Lambda para sua execução.

INTEGRANDO O MÉTODO

O método pode ser integrado com os serviços da AWS ou com Lambda, que é a integração mais comum.
O método para envio de dados escolhido por padrão é o POST.
Selecionaremos o Lambda e posteriormente o ARN da função de acordo com a região selecionada (us-east-1).
Mantemos o tempo limite de 29s (padrão do API Gateway), isso significa que se a requisição levar mais do que esse tempo retornará time out.

DEFININDO MÉTODO

O API Gateway está quase terminado.
Precisamos implantar uma versão para poder associar a um plano de consumo de chaves de acesso.
Note que no momento estamos sem chave de acesso associada a API.

DEFININDO ESTÁGIO

Os estágios de uma API são como se fossem ambientes separados.
Podem ser utilizados para propósitos diferentes como desenvolvimento, produção, qualidade, etc.
No nosso caso vamos criar apenas um que será o de produção. Escolhemos o nome “prod”.
O nome do estágio vai ser incluído na definição do endereço do endpoint de acesso, portanto prefira nomes adequados para melhor identificação.

CRIANDO UM PLANO DE USO

Planos de uso definem características importantes de acesso a uma API.
Definições de:
Taxa de solicitações por segundo
Pico de acessos simultâneos
Cotas de acesso
Ajudam a controlar aspectos do uso de seu serviço, especialmente quando há solicitações de serviços custosos como os LLMs (apesar de não ser o nosso caso no momento).
Na AWS o plano de uso é associado a chaves de acesso que por sua vez é associado um estágio de API.

CRIANDO CHAVES DE ACESSO

A chave de acesso pode ser gerada automaticamente ou gerada personalizada.
Chaves de acesso garantem nível de segurança de acesso da qual quem tem direito de utilizar o serviço as utiliza para autenticação. 

Na requisição do serviço deverá ser incluída no header a chave x-api-key com o valor da senha (chave de acesso).

CRIANDO CHAVES DE ACESSO

Após criar uma chave de acesso, temos que associar ao plano de uso que criamos anteriormente.
Clicamos em “Adicionar ao plano de uso”.

CRIANDO CHAVES DE ACESSO

E então associamos ao plano de uso existente.

ADICIONANDO O PLANO DE UTILIZAÇÃO AO ESTÁGIO

Após o plano de utilização criado, com as chaves de acesso criadas e associadas, o próximo passo é associar a um estágio de API.

CARREGANDO IMAGEM NO REGISTRY

O estágio associado ao plano de uso está também associado a API da qual o estágio foi criado.
Desta forma, o plano de uso passa a ser configurado para a API que criamos no estágio selecionado.
No nosso caso a API “LaptopPricing4DTSR” do estágio “prod” foi associado ao plano de uso “PlanoUtilizacaoBasico”.

ATIVANDO USO DE CHAVES NA API

Depois que criamos o plano de uso, chaves de acesso e associamos ao estágio e API que criamos, precisamos ativar esta funcionalidade.
Por padrão as chaves de acesso não são ativadas na API.

ATIVANDO CHAVE DE ACESSO NA REQUISIÇÃO

Para ativar o uso das chaves, basta clicarmos em “Chave de API obrigatória”.

Isso fará que todas as requisições tenha a chave criada anteriormente.

DEFINIÇÃO DE ENDEREÇO DE ENDPOINT

O endereço de endpoint do método criado fica em “Estágios”, depois clicamos no método e no verbo configurado “Post”.

Endereço de acesso a ser utilizado no frontend ou serviço que fará o consumo.

TESTANDO A API NO TALEND

O Talend é uma extensão do Chrome utilizada para testes de API.
Ele realiza requests com possibilidades de configuração de cabeçalho, payload, etc. conforme cada serviço necessita.

https://chromewebstore.google.com/detail/talend-api-tester-free-ed/

Antes de liberar a API para consumo, testamos no Talend para termos certeza de que tudo está funcionando como esperado.

TESTANDO A API NO TALEND

Configuramos o endereço do endpoint. Depois o header de chave (senha) com o parâmetro “x-api-key” e o contente type JSON. Por fim, editamos o body com o mesmo valor do evento de teste no Lambda.

TESTANDO A API NO TALEND

Clicamos em “Send” e analisamos o retorno da API.
Primeiro o código de resposta, 200 sinaliza que foi processado com sucesos.
Depois o valor de retorno traz conforme o esperado: código de status, predição e a versão do modelo.
Tudo pronto para integrarmos com o frontend.

CICLO PARA CONSTRUIR UM MODELO

EXPERIMENTAÇÃO
NO NOTEBOOK

FORMALIZAÇÃO DO EXPERIMENTO EM SCRIPTS

REGISTRO DE EXPERIMENTOS

REGISTRO DE MODELO

ESTÁGIO DO MODELO

ARTEFATO PARA API

API REST

Frontend

APP DE INTERAÇÃO: FRONTEND

A aplicação de interação pode envolver diferentes formas de frontend, como uma aplicação web ou até mesmo um aplicativo móvel em smartphones.
Vamos utilizar o Streamlit que nos servirá de frontend e o serviço será consumido remotamente por meio de uma API que desenvolvemos anteriormente.

STREAMLIT

É uma biblioteca de código aberto em Python que permite a criação rápida e fácil de aplicativos da web interativos para ciência de dados e aprendizado de máquina. Com ele é possível transformar scripts Python em aplicativos da web interativos com apenas algumas linhas de código, sem a necessidade de conhecimento em desenvolvimento web.

Simplicidade de Uso: foi projetado para ser simples e intuitivo, permitindo que os desenvolvedores criem aplicativos da web interativos com apenas algumas linhas de código Python.
Reatividade em Tempo Real: os aplicativos criados são reativos em tempo real, o que significa que as atualizações nos elementos da interface do usuário são refletidas instantaneamente, sem a necessidade de recarregar a página.
Ampla Gama de Widgets: oferece uma ampla variedade de widgets interativos, como botões, caixas de seleção, barras deslizantes e gráficos, que podem ser facilmente integrados aos aplicativos para torná-los mais dinâmicos e envolventes.
Integração com Bibliotecas de Visualização: integra perfeitamente com bibliotecas populares de visualização de dados, como Matplotlib, Plotly e Altair, permitindo que os desenvolvedores criem visualizações impressionantes com apenas algumas linhas de código.
Suporte para Modelos de Machine Learning: os aplicativos podem incluir modelos de machine learning treinados e fornecer uma interface amigável para os usuários interagirem com esses modelos, inserindo dados de entrada e visualizando os resultados.

COMPOENTES: WIDGETS VISUAIS

Para coletarmos a imagem, vamos utilizar componentes de entrada do Streamlit. Eles ficam na documentação como “Input Widgets”, nesta documentação.
Vamos utilizar o componente “camera\_input” para coletar a imagem da câmera do dispositivo.

APP DE INTERAÇÃO: FRONTEND

Durante a chamada ao serviço externo, precisamos notificar o usuário que há um processamento pendente. Neste caso utilizamos o componente “spinner”.

APP DE INTERAÇÃO: FRONTEND

E finalmente para a exibição dos diferentes estados, sucesso ou erro, utilizaremos os componentes de status “success” e “error”.
Ou ainda podemos utilizar uma saída em tela no formato Markdown.

DESAFIO 1

Crie uma aplicação no Streamlit que consuma a API criada anteriormente e envie os parâmetros esperados.
Utilize “Secrets” para não expor publicamente o endpoint da API.

UTILIZAÇÃO DE SECRETS

Qualquer dado que não precise ser exposto publicamente como chaves e endpoints devem ser mantidos em variáveis de ambiente ou em ambientes com secrets.
O Streamlit possui esta área em seu ambiente de cloud e pode ser utilizado no projeto a parte. Isto é, tais informações secretas fica no seu repositório local mas não no público.
Para armazená-lo, é necessário criar uma pasta “.streamlit” e dentro dela um arquivo “secrets.toml”.
A seguir incluímos o endpoint do serviço (Lambda Function).

API-ENDPOINT = "https://u2dspwvgdq6dwi6qj26lyl5y5e0hcqzq.lambda-url.us-east-1.on.aws"

BIBLIOTECAS E DEPENDÊNCIAS

Nossas dependências são poucas pois toda a complexidade ficou na API REST.
Utilizaremos somente própria biblioteca de componentes do Streamlit e outra para acesso a APIs externas (Requests).

streamlit==1.30.0
requests==2.31.0

Cravar o versionamento evita atualizações mais recentes que podem quebrar a compatibilidade do nosso projeto.

USO DE MARKDOWN

O Streamlit permite o uso de Markdown na forma de comentário na aplicação Python. Ela renderiza como texto na aplicação.

"""
# Machine Learning Engineering
## Predição de Preço de Laptop
Este modelo é capaz de prever o preço de um laptop dada algumas características.
A aplicação é para ser utilizada em uma loja eletrônica que avalia laptops usados como parte do pagamento de um novo,
por tal razão a avaliação não é tão exaustiva e se baseia em caracteríticas comuns, como marca, processador, memória etc.
sem nenhuma outra avaliação visual, pelo menos por enquanto.
### Características do laptop
"""

FILOSOFIA PROCEDURAL

O fluxo de aplicação é sequencial e procedural. Basta incluindo os componentes e validando logo após se são válidos para o programa continuar.

brand\_option = st.selectbox(
"Qual é a marca?",
("Asus", "Dell", "HP", "Lenovo", "Outro"))
touchscreen = st.radio(
"Possui touchscreen (tela sensível ao toque)?",
["Não", "Sim"])
processor\_brand = st.radio(
"Qual a marca do processor?",
["AMD", "Intel", "M1"])
warranty = st.number\_input("Quantos anos de garantia?", step=1, placeholder="Coloque 0 se não houver garantina.")
...
weight = st.radio(
"Qual o peso estimado?",
["Casual", "Gaming", "Thinlight"],
captions = ["Peso padrão", "Pesado", "Leve"])
ram\_type = st.radio(
"Qual o tipo da memória RAM?",
["DDR4", "Outro"])

Inicialmente vamos incluindo os componentes e obtendo do usuário suas seleções.
Para dados categóricos, utilizamos caixa de seleção.

Para dados numéricos utilizamos input de dados.
Neste componente ainda podemos regular o step, ou seja, de quanto em quanto é realizado a iteração.
Valores de memória podem subir em múltiplos 8 por exemplo.

if ram\_type == "Outro":
ram\_type = "other"
if touchscreen=="Sim":
touchscreen = "1"
else:
touchscreen = "0"
payload = { "data" : {
"brand": brand\_option.lower(),
"processor\_brand": processor\_brand.lower(),
"processor\_name": brand\_option.lower(),
"os": os\_brand.lower(),
"weight": weight.lower(),
"warranty": warranty,
"touchscreen": touchscreen,
"ram\_gb": ram\_size,
"hdd": hdd\_size,
"ssd": ssd\_size,
"graphic\_card": graphic\_card\_option,
"ram\_type": ram\_type.lower(),
"os\_bit": os\_bit
}
}
if st.button("Estimar Preço"):
with st.spinner("Processando..."):
get\_prediction(payload)

FILOSOFIA PROCEDURAL

Com a entrada dos dados devemos montar o payload com as chaves conforme é esperado pela API. Note que decidimos deixar a conversão deste formato para features (one-hot encoding) a ser feito na API.

Payload em formato dicionário. Note que precisaremos converter para JSON na requisição para a API.

Neste parte iremos acionar a função que irá chamar a API remota.

def get\_prediction(data):
print(json.dumps(data))
endpoint = st.secrets["API-ENDPOINT"]
headers = {'x-api-key': st.secrets["API-KEY"], 'Content-Type': 'application/json'}
response = requests.post(endpoint, data=json.dumps(data), headers=headers)
if response.status\_code == 200:
result = (response.json())
print(result)
"""
### Preço estimado para compra
De acordo com os dados fornecidos, seu laptop poderá ser comprado pelo seguinte valor abaixo.
"""
locale.setlocale(locale.LC\_ALL, 'pt\_BR')
predicted\_value\_formatted = locale.format\_string("%d", result['prediction'], grouping=True)
st.markdown("Valor para compra: \*\*" + str(predicted\_value\_formatted) + " IND (India Rupee)\*\*.")
else:
st.markdown("Houve um problema na consulta. Revise os dados.")

FILOSOFIA PROCEDURAL

Depois da requisição for enviada, validamos se o código é de sucesso. Esta referência fornece todos os status codes. Por padrão 200 é sucesso.

Se o código for 200, tudo certo.
Do contrário, houve algum erro no processamento da API.

Afim de ter o padrão brasileiro de número inteiro e decimal, precisamos incluir o Locale. E ainda, por questões específicas da plataforma do Streamlit, se decidirmos publicar esta aplicação precisamos incluir um arquivo package.txt e nele incluir a linha locales-all para que o locale brasileiro seja ativado.

CICLO PARA CONSTRUIR UM MODELO

EXPERIMENTAÇÃO
NO NOTEBOOK

FORMALIZAÇÃO DO EXPERIMENTO EM SCRIPTS

REGISTRO DE EXPERIMENTOS

REGISTRO DE MODELO

ESTÁGIO DO MODELO

ARTEFATO PARA API

API REST

Frontend

PARA SABER MAIS

https://dvc.org/doc, documentação da DVC e de todos os produtos que utilizaremos (DVC, DVCLive, Studio e GTO)
https://youtube.com/playlist?list=PL7WG7YrwYcnDBDuCkFbcyjnZQrdskFsBz&si=rI1SrP6S06Kc\_OmS, Playlist de vídeos sobre MLOps da DVC
https://cursos.alura.com.br/course/streamlit-construindo-dashboard-interativo, Curso de Streamlit para construção de dashboards
https://www.youtube.com/watch?v=wxLvvMxzc1Q, Containers, Docker e Kubernetes com Giovanni Bassi

