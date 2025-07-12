MACHINE LEARNING ENGINEERING

MBA EM DATA SCIENCE & IA

INTRODUÇÃO A MLOPS

MACHINE LEARNING OPS

Colocar modelos de aprendizado de máquina em produção exige uma mudança de paradigma que começa no próprio ambiente de desenvolvimento. Apesar dos experimentos continuarem sendo uma etapa essencial, passaremos a utilizar o VS Code como ambiente principal, já que ele oferece um conjunto mais abrangente de recursos em comparação ao uso exclusivo de Notebooks. Entre esses recursos, destacam-se ferramentas que facilitam a construção de pipelines e a definição de processos mais estruturados, repetíveis e versionáveis, que podem ser facilmente integrados e implantados como serviços.

SOFTWARE ENGINEERING E MACHINE LEARNING OPS

Time de
Desenvolvimento

Código de aplicação

Construção

Teste

Implantação

Monitoração

Time de
Operação

Código de dados

Código de Treinamento

Execução de Treinamento

Avaliação

Código de Serviço

Testes

Implantação

Monitoração

Cientista de Dados

Engenheiro de Machine Learning

https://www.youtube.com/watch?v=N96yiqUFwEo&t=1109s

Engenharia de Software há 20 anos

Machine Learning Atualmente

A AURORA DO DEVOPS

DEVOPS
COMUNICAÇÃO
COLABORAÇÃO INTEGRAÇÃO
+
AGILIDADE

TIMES DE DESENVOLVIMENTO

TIMES DE OPERAÇÃO

https://www.youtube.com/watch?v=N96yiqUFwEo&t=1109s

DevOps representa a união de pessoas, processos e produtos com o objetivo de habilitar a entrega contínua de valor aos clientes finais. Com os times atuando de forma colaborativa e adotando um novo mindset, surgiram práticas que aproveitam o melhor de cada área, como testes automatizados, implantações contínuas e infraestrutura como código, entre outras. Essas práticas viabilizam ciclos de entrega mais ágeis, confiáveis e sustentáveis.

https://aws.amazon.com/pt/blogs/aws/acm\_queue\_inter

YOU BUILD IT, YOU RUN IT

Werner Vogels, CTO AWS

ANTES DO DEVOPS

COMUNICAÇÃO E COLABORAÇÃO

Os times apresentavam diversas dificuldades, especialmente nos seguintes domínios:

AGILIDADE E RESILIÊNCIA

ENTREGA E IMPLANTAÇÃO CONTÍNUA

GESTÃO DE INFRAESTRUTURA

MONITORAMENTO E FEEDBACK RÁPIDO

CULTURA DE MELHORIA CONTÍNUA

Divisão significativa entre as equipes de desenvolvimento e infraestrutura (operações).

Ciclos de desenvolvimento e liberação lentos, com pouca automação nos processos de entrega.

Ambientes que não conseguem se adaptar rapidamente as mudanças, resultando em sistemas menos flexíveis e resistente a falhas.

Configuração manual e propensa a erros de ambientes de infraestrutura.

Dificuldades em identificar e corrigir problemas de desempenho em tempo real.

Falta de cultura que promova a aprendizagem contínua e aprimoramento constante.

COM O DEVOPS

COMUNICAÇÃO E COLABORAÇÃO

DevOps, o começo da unificação dos times de desenvolvimento e operações.

AGILIDADE E RESILIÊNCIA

ENTREGA E IMPLANTAÇÃO CONTÍNUA

GESTÃO DE INFRAESTRUTURA

MONITORAMENTO E FEEDBACK RÁPIDO

CULTURA DE MELHORIA CONTÍNUA

Comunicação efetiva, colaboração e quebra de silos entre as equipes.

CI/CD é uma prática central do DevOps, permitindo automação de build, testes e implantação, resultando em ciclos de desenvolvimento mais curtos.

Automação e a abordagem orientada por práticas ágeis ajudam a tornar os processos mais ágeis, permitindo adaptações rápidas às mudanças.

Infraestrutura como código permitindo automação para criar e modificar ambiente, diminuindo erros humanos.

Observabilidade contínuo e feedback rápido permite a detecção precoce de problemas, facilitando a correção proativa.

Incentivo a experimentação e análise pós-implantação para impulsionar melhorias constantes.

ANTES DO MACHINE LEARNING OPS

Aplicação

Apesar de MLOps significar “Machine Learning Operations” e haver uma divisão bem definida entre a construção de modelos e sua disponibilização em produção, ainda existe uma parte, embora menor, relacionada ao desenvolvimento de aplicações. Essa parte diz respeito à forma como os modelos de aprendizado de máquina são expostos e utilizados, geralmente por meio de APIs, o que requer práticas específicas de engenharia de software para garantir eficiência, escalabilidade e segurança.

DevOps

API

Mobile App

Web App

Modelos de Machine Learning

MLOps

Predição de Vendas

Predição de Churn

Anti-fraude

API

API

API

ANTES DO MACHINE LEARNING OPS

ML Engineer é um profissional, de acordo com a AWS,
“...possui a habilidade de projetar, implementar, implantar e manter soluções de machine learning para problemas de negócio.”
Não compete com DevOps, na verdade MLOps utiliza esta importante fundação para trazer mais valor ao viabilidade ML as a Product.

Data Automation

Platform Automation

MLOps

ETL, Streaming, Big Data Processing, Feature Store, Model Registry

Object Storage, Kubernetes, Serverless, Virtual Machines, Containers

Versioning, Continous Delivery and Integration, Testing, Linting

Devops

PRINCIPÍOS DE REFERÊNCIA

Diferentemente de uma aplicação tradicional, um modelo de aprendizado de máquina precisa seguir alguns princípios específicos. No Nubank (apresentado à época por Luam Catão), por exemplo, esses princípios servem como referência para garantir qualidade, robustez e alinhamento com os objetivos de negócio. Eles orientam desde a criação e validação do modelo até sua manutenção em produção, assegurando que o comportamento do sistema seja previsível e sustentável ao longo do tempo.

https://www.youtube.com/watch?v=N96yiqUFwEo

PRINCIPÍOS DE REFERÊCIA

Reprodutibilidade

Consistência

Continuidade

Responsabilidade

Modelos precisam ser reproduzíveis para que falhas possam ser verificadas, ou seja, um novo treinamento precisa ocorrer nas mesmas condições e com os mesmos valores, visando atender a requisitos de auditoria.

O código-base deve incorporar métricas e monitoramento para promover reusabilidade e facilitar a manutenção.

Para lidar de maneira mais eficaz com a incerteza e possibilitar iterações contínuas nos modelos e decisões.

Todas as decisões precisam ser registradas, e qualquer adição ao modelo deve ser devidamente rastreada.

MLOPS FEEDBACK LOOP

Comportamentos mudam, condições socioeconômicas podem ter um impacto rápido (ex. Covid19)

TREINAR O MODELO

MONITORAMENTO

IMPLANTAR UMA NOVA VERSÃO

TRILHAS DE AUDITORIA E ARTEFATOS

Processos automatizados e testados para implantação de modelos em produção

Registros e logs sobre alterações sobre dados e modelos.

Dados desviar dos padrões do treinamento realizados. 

Monitoramento de “data drift” podem prevenir problemas de desempenho antes de gerarem problemas maiores

MODELOS EM OPERAÇÃO: NEM TUDO É API

O uso de modelos por meio de APIs é o caso mais comum na integração de soluções de machine learning. Outras plataformas também adotam essa abordagem, embora aplicadas a diferentes tipos de sistemas e contextos. Essa versatilidade permite que modelos sejam incorporados tanto em aplicações web e mobile quanto em serviços internos, mantendo consistência na entrega de previsões e facilitando a escalabilidade da solução.

MODELO

API

EDGE

BIBLIOTECA JS

MOBILE NATIVO

CONTAINER

ARQUIVO BINÁRIO

MODELOS EM OPERAÇÃO: NEM TUDO É API

MODELO

API

EDGE

BIBLIOTECA JS

MOBILE NATIVO

CONTAINER

ARQUIVO BINÁRIO

O uso de modelos por meio de APIs é o caso mais comum na integração de soluções de machine learning. Outras plataformas também adotam essa abordagem, embora aplicadas a diferentes tipos de sistemas e contextos. Essa versatilidade permite que modelos sejam incorporados tanto em aplicações web e mobile quanto em serviços internos, mantendo consistência na entrega de previsões e facilitando a escalabilidade da solução.

MODELOS EM OPERAÇÃO: NEM TUDO É API

Independentemente da aplicação, o maior desafio está em estabelecer um processo consistente e confiável para a atualização contínua dos modelos. Essa atualização pode ser necessária tanto para adaptação a novos dados quanto para a inclusão de novas funcionalidades, exigindo um fluxo bem definido que minimize riscos e preserve a qualidade do que está em produção.

MODELOS EM OPERAÇÃO SHI\* HAPPENS

Evitar intervenções manuais é primordial.
Em certas aplicações, o suporte pode levar muito tempo para corrigir uma determinada falha.
Por isso que os pacotes de atualização precisam ter inúmeros testes e serem escritos utilizando as melhores práticas para diminuir a possibilidade de termos atualizações com problemas.

www.fordraptorforum.com/threads/automatic-software-update-bricked-my-truck.96624/

DO DEVOPS: TESTE E ANÁLISE ESTÁTICA

Tanto para o serviço que utilizará o modelo quanto para o próprio modelo, é possível realizar uma série de testes antes de colocá-lo em produção. Esses testes ajudam a garantir que o comportamento esteja dentro do esperado, evitando falhas, inconsistências e impactos negativos na experiência do usuário ou nos resultados do negócio.

MODELO

SERVIÇO

DO DEVOPS: TESTE E ANÁLISE ESTÁTICA

MODELO

SERVIÇO

Número de parâmetros de entrada
Golden data (previsões já esperadas)
Validação de resultados (valores <0 por exemplo podem serem inválidos para certos tipos de regressão)
Tamanho do modelo
Tempo de resposta de predição

Parâmetros de entrada e saída
Utilização de parâmetros que minimizem potenciais problemas, por exemplo, uma biblioteca que faz uma requisição precisa ter um timeout
Validação de artefatos
Padrões de código
Padrões de desempenho em geral

Tanto para o serviço que utilizará o modelo quanto para o próprio modelo, é possível realizar uma série de testes antes de colocá-lo em produção. Esses testes ajudam a garantir que o comportamento esteja dentro do esperado, evitando falhas, inconsistências e impactos negativos na experiência do usuário ou nos resultados do negócio.

TESTES DE UNIDADE

DO DEVOPS: TESTE DE UNIDADE

Um teste de unidade é uma forma de teste de software que se concentra na verificação individual de componentes isolados de um programa. O objetivo é validar se cada unidade (módulo, função, método, etc.) do software funciona conforme o esperado. Uma unidade pode ser uma função simples, uma classe ou até mesmo um conjunto de funções relacionadas

ISOLAMENTO

AUTOMAÇÃO

RASTREABILIDADE

RAPIDEZ

FACILIDADE DE DIAGNÓSTICO

Cada unidade é testada de forma isolada, sem depender do estado ou do comportamento de outras partes do sistema.

Os testes de unidade são geralmente automatizados, o que significa que podem ser executados de forma rápida e repetida durante o desenvolvimento.

Os resultados dos testes de unidade devem ser rastreáveis até o código específico da unidade que está sendo testada.

Os testes de unidade são projetados para serem rápidos, permitindo que desenvolvedores os executem frequentemente durante o ciclo de desenvolvimento.

Caso um teste de unidade falhe, deve ser fácil identificar a causa do problema para que os desenvolvedores possam corrigi-lo rapidamente.

“Code without tests is bad code. It doesn’t matter how well written it is; it doesn’t matter how pretty or object-oriented or well encapsulated it is.”

Michael Feathers,
Working Effectively with Legacy Code, 2013.

TESTE DE UNIDADE, UM CASO PRÁTICO

A biblioteca mais utilizada no mercado é a Pytest (https://docs.pytest.org/).
Assim como qualquer teste de unidade, o objetivo é validar por meio de asserções se o resultado obtido é o esperado.

# Conteúdo do arquivo test\_soma.py
def soma(a, b):
return a + b
def test\_soma\_numeros\_positivos():
resultado = soma(2, 3)
assert resultado == 5, "A soma de 2 e 3 deveria ser 5"
def test\_soma\_numeros\_negativos():
resultado = soma(-2, -3)
assert resultado == -5, "A soma de -2 e -3 deveria ser -5"
def test\_soma\_misto\_positivo\_negativo():
resultado = soma(10, -5)
assert resultado == 5, "A soma de 10 e -5 deveria ser 5"
def test\_soma\_zero():
resultado = soma(0, 0)
assert resultado == 0, "A soma de 0 e 0 deveria ser 0"

Se um teste falhar, deverá ser realizado uma verificação até que todos eles sejam cobertos.
Uma boa cobertura de testes é ter, ao mínimo, 80% de uma determinada aplicação. Isto implica que a maioria de todas as funções precisam constar estes testes.
Como os testes sempre crescem, quando há uma nova funcionalidade implementada é possível verificar, por meio dos testes de unidade, se não há nenhuma quebra das funcionalidades já existentes.

TESTE DE UNIDADE, UM CASO PRÁTICO

Após instalar o Pytest, podemos executar o comando para realizar o teste: “pytest –v”, o parâmetro utilizado indica apresentar verbosidade padrão sobre os testes.

===================================================================== test session starts ======================================================================
platform win32 -- Python 3.7.9, pytest-7.4.4, pluggy-1.2.0 -- d:\github\_projects\fiap-ds-mlops-start\.venv\scripts\python.exe
cachedir: .pytest\_cache
rootdir: D:\
collected 2 items
tests\app\_test.py::test\_api\_return PASSED [ 50%]
tests\app\_test.py::test\_api\_price\_return PASSED [100%]
====================================================================== 2 passed in 2.69s ======================================================================= 

Quando um dos testes falha, é apresentada a mensagem negativa da asserção para investigação posterior. 

=========================================================================== FAILURES=======================================================================
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ test\_api\_price\_return \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
def test\_api\_price\_return():
result = app.get\_product\_price(1)
> assert isinstance(result, (string)), "A variável não é numérica"
E NameError: name 'string' is not defined
tests\app\_test.py:12: NameError
=================================================================== short test summary info ====================================================================
FAILED tests\app\_test.py::test\_api\_price\_return - NameError: name 'string' is not defined
================================================================= 1 failed, 1 passed in 2.75s ================================================================== 

TESTE DE UNIDADE, UM CASO PRÁTICO

Para estas funções, quais seriam bons testes de unidade?

import requests
def get\_product(id):
    results = requests.get("https://dummyjson.com/products/"+str(id))
    return results
def get\_product\_price(id):
    results = requests.get("https://dummyjson.com/products/"+str(id))
    data = results.json()
    return data["price"]

TESTE DE UNIDADE, UM CASO PRÁTICO

Os testes mais diretos do “caminho feliz”:
Teste baseado no código de sucesso 200.
Teste baseado no tipo de retorno.

def test\_api\_return():
results = app.get\_product(1)
data = results.json()
 assert results.status\_code == 200, "O retorno da conexão não foi bem sucedida"
assert "id" in data, "Não existe chave id no retorno"
assert data["id"] == 1, "Id enviado não é o mesmo recebido"
def test\_api\_price\_return():
result = app.get\_product\_price(1)
assert isinstance(result, (int, float)), "O preço não é numérico"

TESTE DE UNIDADE, UM CASO PRÁTICO

Outros testes “mocados” para condições específicas e importantes para testar:
Teste de erro baseado no status code.
Teste de erro baseado em time out.

def test\_get\_product\_http\_error\_handling(mocker):
mocker.patch("src.app.requests.get").return\_value.status\_code = 404
result = app.get\_product(2)
assert result is None, "Valor não nulo em condição de erro."
def test\_timeout\_handling(mocker):
mocker.patch("src.app.requests.get", side\_effect=requests.exceptions.Timeout)
result = app.get\_product(3)
assert result is None, "Valor não nulo em condição de erro."

DESAFIO 1

Utilizando o mesmo endpoint anterior (https://dummyjson.com/products/1), crie outro método para retornar o conteúdo da chave “images”.
Construa testes de unidade para validar a integridade deste resultado. Deve incluir as seguintes regras:
Deve retornar no mínimo uma imagem.
O formato da imagem deve ser JPG ou PNG,
O nome das imagens deve ser números, por exemplo 1.jpg, 2.jpg.

ANÁLISE ESTÁTICA (LINT)

ANÁLISE ESTÁTICA: LINT

Ferramentas de análise estática de código auxiliam os desenvolvedores na identificação e correção de problemas ainda na fase de desenvolvimento. Elas analisam o código-fonte em busca de padrões, aderência a estilos de codificação, possíveis erros e outras questões que possam comprometer a legibilidade, a manutenibilidade e a qualidade geral do software.

O termo "lint" originou-se do nome de uma ferramenta chamada "lint", desenvolvida nos anos 1970 para a linguagem de programação C. A ideia era que a ferramenta ajudaria a pentear o código em busca de problemas, assim como um "linter" de roupas remove partículas indesejadas.

ANÁLISE ESTÁTICA: LINT

CONFORMIDADE

ERROS POTENCIAIS

VARIÁVEIS NÃO DECLARADAS

COMPLEXIDADE DE CÓDIGO

Verificação se o código segue as convenções de formatação e estilo estabelecidas pela equipe de desenvolvimento ou por diretrizes específicas da linguagem.

Identificação de erros lógicos, problemas de segurança, ou outras questões que podem causar comportamento inesperado durante a execução do programa.

Detecção de variáveis que podem não ter sido declaradas ou que estão sendo usadas antes de serem inicializadas.

 Avaliação da complexidade do código-fonte, como número de linhas de código em uma função ou a profundidade de aninhamento de estruturas de controle.

PYLINT, ANÁLISE ESTÁTICA EM PYTHON

O Pylint (https://pylint.readthedocs.io) é uma ferramenta de linting para o Python. Ele é projetado para analisar o código-fonte, identificar possíveis problemas, aplicar convenções de estilo e fornecer feedback aos desenvolvedores sobre a qualidade do código. O objetivo principal do Pylint é melhorar a legibilidade, a manutenibilidade e a qualidade geral do código Python.

Verificação de Estilo de Código: verifica se o código Python segue as convenções de estilo recomendadas pelo PEP 8 (https://peps.python.org/pep-0008/), que é o guia de estilo oficial para código Python.
Identificação de Erros Potenciais: analisa o código em busca de possíveis erros lógicos, como uso incorreto de variáveis, chamadas de funções com número incorreto de argumentos, entre outros.
Métricas de Código: fornece métricas relacionadas à complexidade do código, como o número de linhas de código em uma função, a profundidade de aninhamento e outros indicadores que podem ajudar a avaliar a qualidade do código.
Suporte a Convenções Personalizadas: além das convenções do PEP 8, o Pylint para seguir convenções específicas da sua equipe ou projeto.
Integração com Editores de Código: pode ser integrado com muitos editores de código, IDEs (Ambientes de Desenvolvimento Integrado) e ambientes de desenvolvimento, proporcionando feedback em tempo real enquanto você escreve código.

PONTUAÇÃO 0-10

REFERÊNCIAS (DOC. PYLINT)

PYLINT, ANÁLISE ESTÁTICA EM PYTHON

Qual é a nota para o código abaixo?

import requestss
def get\_product(id):
    results = requests.get("https://dummyjson.com/products/"+str(product\_id), timeout=10)
    return results
def get\_product\_price(id):
    results = requests.get("https://dummyjson.com/products/"+str(product\_id), timeout=10)
    data = results.json()
    return data["price"]
get\_product(1)
get\_product\_price(1)

PYLINT, ANÁLISE ESTÁTICA EM PYTHON

 pylint app.py
\*\*\*\*\*\*\*\*\*\*\*\*\* Module app
src\app.py:14:0: C0304: Final newline missing (missing-final-newline)
src\app.py:1:0: C0114: Missing module docstring (missing-module-docstring)
src\app.py:1:0: E0401: Unable to import 'requestss' (import-error)
src\app.py:4:0: C0116: Missing function or method docstring (missing-function-docstring)
src\app.py:4:16: C0103: Argument name "id" doesn't conform to snake\_case naming style (invalid-name)
src\app.py:4:16: W0622: Redefining built-in 'id' (redefined-builtin)
src\app.py:5:14: E0602: Undefined variable 'requests' (undefined-variable)
src\app.py:5:65: E0602: Undefined variable 'product\_id' (undefined-variable)
src\app.py:4:16: W0613: Unused argument 'id' (unused-argument)
src\app.py:8:0: C0116: Missing function or method docstring (missing-function-docstring)
src\app.py:8:22: C0103: Argument name "id" doesn't conform to snake\_case naming style (invalid-name)
src\app.py:8:22: W0622: Redefining built-in 'id' (redefined-builtin)
src\app.py:9:14: E0602: Undefined variable 'requests' (undefined-variable)
src\app.py:9:65: E0602: Undefined variable 'product\_id' (undefined-variable)
src\app.py:8:22: W0613: Unused argument 'id' (unused-argument)
src\app.py:1:0: W0611: Unused import requestss (unused-import)
------------------------------------------------------------------
Your code has been rated at 0.00/10 (previous run: 0.00/10, +0.00)

PONTUAÇÃO 0!

PYLINT, ANÁLISE ESTÁTICA EM PYTHON

E agora, depois dos ajustes?

"""Module responsible to get data from produts API"""
import requests
def get\_product(product\_id):
"""Get a product by id"""
results = requests.get("https://dummyjson.com/products/"+str(product\_id), timeout=10)
return results
def get\_product\_price(product\_id):
"""Get a product price by id"""
results = requests.get("https://dummyjson.com/products/"+str(product\_id), timeout=10)
data = results.json()
return data["price"]
get\_product(1)
get\_product\_price(1)

PYLINT, ANÁLISE ESTÁTICA EM PYTHON

-------------------------------------------------------------------
Your code has been rated at 10.00/10 (previous run: 6.00/10, +4.00)

PONTUAÇÃO 10!

É comum não alcançar sempre o 10/10.
Muitas empresas adotam Linters específicos para cada time ou então flexibilizam a nota final para algo próximo a 10, sendo acima de 8 aceitável.

DESAFIO 2

No mesmo projeto utilizado no desafio anterior, crie mais um método responsável por baixar as imagens dos resultados obtidos da chave “imagem”.
Logo após execute o Lint padrão (baseado no PEP-8) e realize os ajustes necessários.

PARA SABER MAIS

https://www.youtube.com/watch?v=N96yiqUFwEo, 101 Master Class de Machine Learning Engineering do Nubank. Material indispensável para quem deseja prosseguir na área.
https://cursos.alura.com.br/course/python-tdd-explorando-testes-unitarios, Curso Python e TDD: explorando testes unitários.
https://wiki.python.org.br/GuiaDeEstilo, Guia de Estilo Python (PEP-8) em português.

