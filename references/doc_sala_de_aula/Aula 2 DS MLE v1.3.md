MACHINE LEARNING ENGINEERING

MBA EM DATA SCIENCE & IA

GERENCIAMENTO DE VERSÃO DE CÓDIGOS

CÓDIGO

Notebooks

Modelos

Features

CÓDIGO

Notebooks

Modelos

Features

VERSIONAMENTO DE CÓDIGO

O versionamento de código permite controlar as alterações em uma base comum, possibilitando sua evolução contínua e a colaboração de múltiplos times. Esse controle contribui para minimizar conflitos, garantir a integridade do histórico de mudanças e manter a padronização do desenvolvimento ao longo do tempo.

CÓDIGO

Notebooks

Modelos

Features

API

Team Member

Team Member

Team Member

master: produção

stag: staging (homologação)

devl: development (desenvolvimento)

REPOSITÓRIOS DE CÓDIGO

O repositório é o local onde são registradas as modificações e versões dos arquivos de uma determinada pasta do projeto. Após realizar as alterações necessárias, o próximo passo é enviá-las para um repositório remoto, permitindo que outras pessoas possam acessar, revisar e colaborar no mesmo código.

Notebooks

Modelos

Features

API

REPOSITÓRIO REMOTO

Notebooks

Modelos

Features

API

PUSH

PULL

REPOSITÓRIO LOCAL

CÓDIGO VERSIONÁVEL

Nem todos os arquivos de um projeto precisam ser versionados. Devem ser incluídos apenas aqueles que serão utilizados em equipe, passíveis de testes, validação e eventual publicação em produção. Arquivos de uso individual, ambientes virtuais e arquivos sensíveis, como os que contêm senhas ou variáveis de ambiente (por exemplo, arquivos .env), devem ser explicitamente ignorados. No VS Code, há uma extensão chamada Code Zombie que gera automaticamente arquivos de ignore padronizados conforme a linguagem de programação utilizada, facilitando essa configuração.

.GITIGNORE

.env

Artefatos não registrados

Pesos

Cache do Python

Cache do Python

Arquivos temporários

https://marketplace.visualstudio.com/items?itemName=codezombiech.gitignore

ADICIONANDO ARQUIVOS

Para começarmos a trabalhar com o Git precisamos instalar no sistema operacional utilizado. No Windows, instalamos a partir desta fonte (https://www.git-scm.com/downloads) e para o Mac é recomendado utilizar o Brew (https://git-scm.com/download/mac).

1. CRIA REPOSITÓRIO LOCAL

1. ADICIONA GITIGNORE (Opcional)

3. ADICIONA ARQUIVOS

git init

edite um arquivo .gitignore e adicione nele os arquivos ignorados

git add .
adiciona todos os arquivos (pode ser adicionado arquivos específicos)

CONFIRMANDO ARQUIVOS

Após concluir todas as modificações, podemos confirmá-las por meio de um commit, preparando assim o envio para um repositório remoto compartilhado. Esse processo registra oficialmente as alterações no histórico do projeto e permite que outros colaboradores as integrem de forma segura.

CONFIRMAÇÃO

git commit -m mensagem
Cada confirmação requer uma mensagem para rastrear as razões das modificações.

HASH DE MODIFICAÇÃO
ÚNICO (SHA-1)

O hash de modificação permite controlar cada uma as modificações. Assim é possível saber o que foi alterado e por qual pessoa seja para auditoria ou mesmo para sincronismo entre repositórios.

RAMIFICAÇÕES DO REPOSITÓRIO

As ramificações permitem que os membros de um time, mesmo atuando sobre a mesma base de código, possam trabalhar de forma independente, reduzindo o risco de conflitos de versão. Uma ramificação também pode ser utilizada para testes ou experimentos, sem a necessidade de que as alterações feitas nela sejam, necessariamente, integradas à versão de produção.

MAIN

DEVL

STAG

FEATURE A

EXP 1

COMMIT

COMMIT

COMMIT

COMMIT

COMMIT

COMMIT

COMMIT

COMMIT

COMMIT

COMMIT

COMMIT

RAMIFICAÇÕES E AMBIENTES

As ramificações também são utilizadas como referência para os diferentes ambientes de um sistema. Por exemplo, a ramificação principal, geralmente chamada de master ou main, costuma estar associada ao ambiente de produção. A ramificação dev, de desenvolvimento, está ligada ao ambiente onde novas funcionalidades são construídas. Já a ramificação stag, de staging ou homologação, é usada para testes finais antes da liberação. Com essa estrutura de três ambientes, é possível desenvolver uma nova funcionalidade localmente no laptop do especialista, validá-la em um ambiente de desenvolvimento com condições similares às de produção, realizar testes em homologação com dados mais atualizados e, por fim, liberar para o ambiente produtivo.

GITFLOW E MERGES

As ramificações permitem que os integrantes de um time que trabalham na mesma base de código possam desenvolver de forma independente, sem preocupações imediatas com conflitos de versão. Uma ramificação também pode ser usada para testes ou experimentos, sem que isso implique, necessariamente, a publicação das modificações no ambiente de produção.

MAIN

DEVL

STAG

MERGE

https://www.alura.com.br/artigos/git-flow-o-que-e-como-quando-utilizar

EXPERIMENT X

COMMIT

PULL REQUEST

O Pull Request (PR) pode ser opcional, pois se o desenvolvedor tiver permissões para “merge” na branch principal, ele pode consolidar as alterações. No entanto, como prática de desenvolvimento, o PR se torna uma forma de revisão e de explicação do desenvolvedor por qual razão ele quer consolidar a proposta dele de código em produção.
Membros do time mais seniores e revisores farão uma revisão detalhada para permitir a consolidação do código.
Utilizando automações de integração contínua e pipelines também é possível realizar ações ao submeter um PR, inclusive rejeitando-a quando a mesma não passar nos testes ou adicionando informações relevantes para o revisor analisar.

MAIN

STAG

MERGE

PULL REQUEST

TEMPLATES DE PROJETO

A padronização da estrutura de pastas em um projeto é essencial para facilitar o uso da base de código por toda a equipe.
Organizar o repositório com áreas específicas para Notebooks, scripts de treinamento, processamento de dados e outros componentes ajuda a manter os processos reproduzíveis e reduz o tempo de desenvolvimento em novas iniciativas.
Cada empresa ou departamento pode adotar um modelo próprio, de acordo com seus desafios e necessidades.
Uma forma prática de manter templates padronizados é com o uso do Cookiecutter, que permite criar e reutilizar estruturas de projeto de forma rápida.

SCAFFOLDING DE PROJETOS DE ML

Projeto C

Projeto A

Projeto B

TEMPLATE UTILIZANDO COOKIECUTTER

O Cookiecutter precisa ser instalado como pacote no Python (fora do ambiente virtual).
Por meio de comandos CLI passamos um template e ele constrói toda a estrutura de pastas.

https://drivendata.github.io/cookiecutter-data-science/

python -m pip install --user pipx
python -m pipx ensurepath

pipx install cookiecutter-data-science

Logo depois passamos o template a seguir. Este template é da DVC e pode ser adaptado para qualquer necessidade.

No diretório em que você quer iniciar o projeto:

ccds

ML TEMPLATE

Os dados ficam na pasta “data” separado por tipo de processamento.
Documentação ficam na pasta “docs” (readthedocs.com)
Modelos ficam na pasta “models”.
Experimentos com Notebooks ficam na pasta “notebooks”.
Manuais e referências adicionais como Papers ficam na pasta “references”.
Dentro da pasta “src” ficam os scripts para treinamento e processamento de features.

Alguns componentes ainda não precisamos utilizar e podemos remover, que é o caso do setup.py, tox.ini e Makefile. Eles são utilizados para compilar diferentes tarefas dentro do ambiente Python, e requerem um ambiente baseado em Linux.

VERSIONAR MODELOS E FEATURES ? 

O Github possui um tier especial para armazenamento de Large Files de até 2GB.
Nos repositórios não é possível versionar e armazenar arquivos maiores do que 100 MB.
Artefatos de features e modelos podem ser armazenados em outras estruturas, como por exemplo em Object Storages que é o caso do S3 da AWS.

COMO VERSIONAR EM LOCAIS DIFERENTES?

DVC FOR THE WIN!

O DVC (Data Version Control) resolve esse problema.
Utilizando a mesma estrutura de projetos do Git (seja no GitHub ou qualquer outra plataforma) ele mantem todas as modificações do projeto e adiciona outra plataforma de armazenamento de arquivos grandes, que é o caso de modelos, features ou qualquer outro artefato.

DAGSHUB TO RULE THEM ALL!

A plataforma DagsHub (dagshub.com) integra os principais serviços necessários para o gerenciamento moderno de projetos de machine learning e large language models (LLMs), oferecendo uma infraestrutura colaborativa que combina o controle de versão de dados e modelos via DVC, o versionamento de código com GitHub e o rastreamento de experimentos por meio do MLflow.
Optaremos por utilizá-la devido à sua praticidade, integração nativa com ferramentas amplamente adotadas no ecossistema de ciência de dados e por disponibilizar um plano gratuito (Community Version), adequado para fins de ensino e pesquisa acadêmica.

AWS IAM E CREDENCIAIS

Para acessar os recursos da AWS precisamos criar um usuário para acesso programático acessando o IAM.
Entre no Console, busque e entre no IAM.
Em “Usuários”, crie um usuário novo.

AWS IAM E CREDENCIAIS

Informe o nome do usuário.
Não marque acesso a console, pois esse usuário é apenas de uso programático.

AWS IAM E CREDENCIAIS

Clique em “Anexar políticas diretamente” e escolha a política “AdminstratorAccess”. E por fim, clicar em “Criar Usuário”.

Em sistemas produtivos devemos escolher exatamente quais recursos podemos ter acesso. Neste caso optamos o acesso administrador considerando o uso acadêmico e para simplificar o on-boarding.

AWS IAM E CREDENCIAIS

Volte na tela principal e clique no usuário criado.

AWS IAM E CREDENCIAIS

Agora clique em “Credenciais de segurança”.

AWS IAM E CREDENCIAIS

Vá em “Chaves de acesso” e depois “Criar chave de acesso”.

AWS IAM E CREDENCIAIS

Escolha o caso de uso adequado, neste caso é para o CLI.

AWS IAM E CREDENCIAIS

Baixe o arquivo CSV das credenciais de acesso por segurança. 

AWS CLI

Para utilizar localmente o acesso a recursos da AWS precisamos instalar o AWS CLI (Command Line Interface).
Depois que realizar a instalação precisamos configurar o CLI para acessar com as credenciais que foram criadas.

https://aws.amazon.com/pt/cli/

aws configure
AWS Access Key ID [None]: 
AWS Secret Access Key [None]: 
Default region name [None]: us-east-1
Default output format [None]:

Os dados deverão estar em um bucket de S3, como se estivesse num Data Lake.
As atividades do cientista de dados vai ser processar estes dados e construir as features,
Portanto vamos criar 1 bucket (“Criar bucket”) para armazenar os dados em uma pasta específica “dataset”. E este mesmo bucket será utilizado pelo DVC para versionar o modelo e demais arquivos.

AWS S3: CRIANDO UM BUCKET

Deixe todas as opções padrão. Informe um nome e clique em “Criar bucket”.

AWS S3: CRIANDO UM BUCKET

AWS S3: UPLOAD

Entre no bucket criado, clique em “Criar Pasta” e crie e pasta “dataset”.
Depois faça o upload do dataset que se encontra neste repositórido do Kaggle: https://www.kaggle.com/datasets/anubhavgoyal10/laptop-prices-dataset

LAPTOP PRICING PREDICITON

Temos um desafio de negócio que consiste na compra de laptops usados. Para isso, será utilizado um modelo de predição de preço.
Esse modelo considerará diferentes atributos, como marca, processador, memória, armazenamento, entre outros.
Nossa primeira meta é versionar o projeto utilizando um template de machine learning e realizar um experimento inicial com um modelo simples baseado em regressão Ridge.
Os parâmetros mínimos de sucesso definidos são: R² > 0,6 (o modelo deve explicar pelo menos 60% da variância dos dados) e MAPE < 0,15 (erro percentual médio abaixo de 15%).

IMPORTÂNCIA DO TEMPLATE

O template que utilizamos tem uma convenção de que na pasta referente e dados processados e modelos eles não serão enviados no GitHub, mas sim no S3 da AWS.
Estas configurações de ignorar arquivos são importantes para manter os arquivos certos nos locais certos.

cookiecutter https://github.com/drivendata/cookiecutter-data-science

 [1/8] project\_name (project\_name): fiap-mlops-class-laptop-pricing
[2/8] repo\_name (fiap-mlops-class-laptop-pricing):
[3/8] author\_name (Your name (or your organization/company/team)): Michel Fernandes
[4/8] description (A short description of the project.):
[5/8] Select open\_source\_license
1 - MIT
2 - BSD-3-Clause
3 - No license file
Choose from [1/2/3] (1): 3
[6/8] s3\_bucket ([OPTIONAL] your-bucket-for-syncing-data (do not include 's3://')):
[7/8] aws\_profile (default):
[8/8] Select python\_interpreter
1 - python3
2 - python
Choose from [1/2] (1): 1

VSCODE COMO IDE PADRÃO

Iremos utilizar o VS Code, pois a partir de agora trabalharemos com scripts e Notebooks que exigem controle sobre as versões dos pacotes utilizados.
O uso do Colab, por exemplo, implica em aceitar um ambiente gerenciado pelo Google, no qual não temos controle total sobre as versões do Python ou das bibliotecas instaladas, o que pode comprometer a reprodutibilidade dos experimentos.
Baixe o VSCode neste link: https://code.visualstudio.com/download 

PYENV GERENCIE VERSÕES DO PYTHON

Dependendo os projetos que trabalhamos é comum utilizarmos diferentes versões do Python, seja por compatibilidades com plataformas de Cloud ou até mesmo bibliotecas.
Gerenciar manualmente diferentes versões do Python pode dar trabalho e gerar incompatibilidades, por isso fica a recomendação de utilizar o Pyenv (https://github.com/pyenv/pyenv) .
Com o Pyenv controlamos qual a versão Global do Python e também podemos instalar por ele mesmo versões diferentes.
Oficialmente não há suporte para Windows, mas há uma versão alternativa que pode ser utilizada por meio deste link: https://github.com/pyenv-win/pyenv-win/blob/master/docs/installation.md 

pyenv install –l // Exibe as versões disponíveis para instalação
pyenv install 3.10.8 // Instala a versão 3.10.8
pyenv global 3.10.8 // Define a versão global como 3.10.8

Na disciplina vamos utilizar o Python 3.10 como padrão, portanto não há problema em baixar diretamente esta versão e utilizá-la.

VSCODE COMO IDE PADRÃO

Vamos abrir o VSCode para começarmos a trabalhar com o projeto.
Utilize a linha de comando abaixo para entrar no VSCode.

cd 
code .

Instale as seguintes extensões que ajudam no desenvolvimento:
Python
Jupyter
Docker
Gitignore
Github Actions

ARQUIVOS DE DEPENDÊNCIAS

Vamos utilizar o arquivo requirements.txt para listar as bibliotecas necessárias ao desenvolvimento do modelo, à exploração do dataset e à sincronização com repositórios locais e de experimentos.

black==25.1.0
flake8==7.2.0
isort==6.0.1
mkdocs==1.6.1
pytest==8.3.5
python-dotenv==1.1.0
notebook==7.4.2
pandas==2.2.3
numpy==2.2.5
scikit-learn==1.6.1
ipywidgets==8.1.7
ipykernel==6.29.5
dagshub==0.5.8
mlflow==2.22.0
dvc-s3==3.2.0
xgboost==3.0.0
lightgbm==4.0.0
catboost==1.2.8

Utilizar bibliotecas sem versionamento no início do projeto facilita o gerenciamento de dependências e a identificação das versões mais compatíveis entre si. No entanto, uma vez que as bibliotecas estejam estáveis e validadas, é recomendado travar suas versões no requirements.txt para evitar problemas de compatibilidade em futuras execuções ou atualizações do ambiente.

As dependências podem variar conforme a evolução do projeto, especialmente quando novas bibliotecas forem adicionadas para criação, ajuste ou avaliação de modelos.

INSTALANDO AMBIENTE VIRTUAL

Primeiro passo antes de começarmos a desenvolver nossos experimentos, será de construir um ambiente virtual que possua todos os pacotes que iremos trabalhar.

python -m venv .venv
.venv/scripts/activate

Depois de instalar o ambiente virtual você deve notar o ambiente ativo por meio da linha de comando com o nome do diretório do ambiente.

PS D:\GitHub\_Projects\fiap-ds-mlops-laptop-pricing> .\.venv\Scripts\activate
(.venv) PS D:\GitHub\_Projects\fiap-ds-mlops-laptop-pricing> 

Agora já podemos instalar as bibliotecas que iremos utilizar.
A medida que novas bibliotecas sejam necessárias, iremos adicioná-las e executar novamente o comando.

PS D:\GitHub\_Projects\fiap-ds-mlops-laptop-pricing> .\.venv\Scripts\activate
(.venv) PS D:\GitHub\_Projects\fiap-ds-mlops-laptop-pricing> pip install –r requirements.txt

CONFIGURANDO GITHUB

Primeiro vamos criar um novo repositório no GitHub.
Após isso podemos sincroniza-lo com o um repositório no DagsHub.
Por fim, sincronizaremos com o DVC utilizando o storage do DagsHub ou no S3.

CONFIGURANDO DAGSHUB

Agora com os repositórios criados, vamos carregar nosso template para depois iniciarmos o DVC.

CONFIGURANDO GIT

Na pasta local vamos iniciar o repositório.

git init

Logo após precisamos indicar o repositório remoto que é o endereço dele no GitHub.

Após isso adicionamos os arquivos e sincronizamos remotamente.

git remote add origin 

git add .

Confirmamos nossas modificações.

git commit –am “importação inicial”

E finamente sincronizamos.

git push origin main

CONFIGURANDO DVC

Agora que temos no DagsHub o repositório devidamente sincronizado, precisamos obter as credenciais do DagsHub storage que utiliza o DVC para sincronizar.

E então podemos iniciar o DVC.

dvc remote add origin s3://dvc
dvc remote modify origin endpointurl url-do-dagshub

dvc init

Adicionar o remote do DVC.

dvc remote modify origin --local access\_key\_id key
dvc remote modify origin --local secret\_access\_key secret

Adicionar credencais do DVC.

Adicionar a pasta para o controle de versões do DVC

dvc add data

A partir de agora toda a mudança na pasta data precisa ser sincronizada com o repositório.

CONFIGURANDO DVC

Mais comandos adicionais.

Adicionar o controle de mudanças no Git para associarmos as mensagens de commit no DVC

git add data.dvc

Habilitar o auto-staging no DVC, ou seja adiciona no Git qualquer novo arquivo DVC.

dvc config core.autostage true

CONFIGURANDO DVC

Para criar um repositório local, basta inicializarmos ele com o comando abaixo:

git init

Vamos criar um repositório no Github e associar como repositório remoto:

E agora inicializar o DVC.

dvc remote add -d myremote s3:///

git remote add origin 

dvc init

Logo após vamos adicionar um “remote” para os artefatos (arquivos grandes) no S3 da AWS.
Como já configuramos o AWS CLI, essa permissão será utilizada para sincronizar os arquivos com esse remote.

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

EXPLORANDO DATASET E PRÉ-PROCESSANDO

O dataset adaptado para uso em BRL está disponível neste repositório: https://github.com/michelpf/dataset-laptop-pricing.
Vamos baixá-lo e armazená-lo na pasta data/raw. A estrutura da pasta data será utilizada para organizar os dados, separando os brutos (raw) dos dados processados (processed).

Nosso primeiro desafio será realizar o pré-processamento dos dados, padronizando e preparando o conjunto para o treinamento dos modelos.
Para essa atividade, vamos criar nosso primeiro notebook, chamado data-processing.ipynb, que ficará na pasta notebooks.

ENVIANDO DADOS PARA DVC & DAGSHUB

Após os arquivos terem sido gerados nas pastas “raw” e “processed” vamos fazer o seguinte:

dvc commit

Enviar dados para o repositório remoto toda a vez que houver modificações.

dvc push 

CRIANDO UM DATASET NO DAGSHUB

Com os datasets armazenados no DagsHub conseguimos concentrar uma única versão em diversos experimentos.

UTILIZANDO UM DATASET NO DAGSHUB

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

DESAFIO 1

Crie uma primeira versão do notebook de exploração afim de alcançar ou chegar próximo dos critérios de sucesso.
Utilize um modelo de regressão Ridge.

PARA SABER MAIS

https://dvc.org/doc, documentação da DVC e de todos os produtos que utilizaremos (DVC, DVCLive, Studio e GTO)
https://youtube.com/playlist?list=PL7WG7YrwYcnDBDuCkFbcyjnZQrdskFsBz&si=rI1SrP6S06Kc\_OmS, Playlist de vídeos sobre MLOps da DVC

