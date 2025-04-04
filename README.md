# API pessoal


## Tópicos

- [API pessoal](#api-pessoal)
  - [Tópicos](#tópicos)
  - [Sobre o Projeto](#sobre-o-projeto)
  - [Tecnologias e Ferramentas utilizadas](#tecnologias-e-ferramentas-utilizadas)
  - [Começando](#começando)
  - [Estrutura de Arquivos](#estrutura-de-arquivos)
  - [Instalação](#instalação)
  - [Edição](#edição)
  - [Publicação](#publicação)
  - [Licença](#licença)
  - [Contato](#contato)


---
## Sobre o Projeto

Este projeto visa a criação de uma REST API para servir dados pessoais, que irão ser consumidos posteriormente por um frontend [nesse projeto](https://github.com/marcoswb/personal-api-frontend). Os dados servidos serão basicamente algumas informações pessoais(resumo pessoal, skills, experiências profissionais, formações, contatos...), além de realizar uma integração com a API do github para listar os projetos desenvolvidos e também uma integração com a API do Medium, para listagem de posts que tenho na plataforma.

A motivação para o desenvolvimento desse projeto foi o aprendizado, e também para conseguir por em prática conhecimentos que antes só tinha na teoria.


---
## Tecnologias e Ferramentas utilizadas

- **Python** -> Linguagem base para a criação da API REST e do app desktop;
- **Flask** -> Framework Python para a criação de APIs REST;
- **PostgreSQL** -> Banco de dados relacional e open source;
- **Heroku** -> Plataforma de nuvem como serviço. Utilizado no projeto para o deploy da API REST e também como servidor de banco de dados;
- **AWS Lambda** -> Serviço de computação disponibilizado na plataforma AWS que executa código em resposta a eventos. Utilizado no projeto para executar constantemente uma rotina que mantém o banco de dados atualizado.


---
## Começando

Caso deseje utilizar esse projeto como um template para criação do seu próprio, fiz ele pensando em ser totalmente configurável e poder ser reutilizado. Para isso, a seguir mostrarei um overview dos principais pontos do projeto e ao fim você deve ser capaz de configurar e poder replicá-lo em sua máquina.


---
## Estrutura de Arquivos

A estrutura de arquivos está da seguinte maneira:

```bash
├── aws_lambda_update/
│   ├── controllers/
|   |
│   ├── libs/
|   |
│   ├── models/
|   |
│   ├── psycopg2/
|   |
│   └── main.py
|
├── controllers/
├── models/
|   
├── .env
├── .gitignore
├── app.py
├── LICENSE
├── Procfile
├── README.md
└── requirements.txt
```

Serão explicados os arquivos e diretórios na seção de [Edição](#edição).


---
## Instalação

1. O processo é bem simples, basta copiar o projeto utilizando o comando:

```sh
git clone https://github.com/marcoswb/personal-api.git
```

2. Utilizar o comando a seguir para entrar dentro do projeto:
  
```sh
cd personal-api
```

3. Utilizar o comando a seguir para instalar as dependências Python:
  
```sh
python -m pip install -r requirements.txt
```

Com isso o projeto será criado com todas as dependências devidamente instaladas e linkadas.


---
## Edição

Nesta seção explicarei os diretórios e arquivos utilizados no projeto:

- **aws_lambda_update/** - Para manter o banco de dados da aplicação atualizado utilizo o serviço de lambda da AWS, que faz o update dos projetos existentes no Github e dos posts feitos no Medium periodicamente. Esse diretório é basicamente a pasta que precisa ser enviada para a AWS e que contém todo o código para o serviço lambda funcionar;
  - **controllers/** - Diretório que contém os arquivos que fazem a comunição com as APIs externas(Github e Medium) e gravam os dados retornados no banco de dados;
  - **libs/** - Diretório que contém bibliotecas externas do Python, e que o serviço da AWS lambda ainda não oferece como opção para ser importado via Python;
  - **models/** - Diretório que contém classes Python, que mapeiam tabelas do banco de dados para objetos Python;
  - **psycopg2/** - Na aplicação eu utilizo banco de dados PostgreSQL para armazenar os dados, e na AWS ainda há uma incompatibilidade com a lib psycopg2(lib para conexão com banco PostgreSQL) do python, sendo necessário importar toda a lib para dentro da AWS para que funcione corretamente;
  - **main.py** - Arquivo principal, que faz a chamada para os métodos de atualização;
  
- **controllers/** - Diretório que contém basicamente o código por trás de cada endpoint da API. Organizando os dados que serão retornados em uma chamada GET;

- **models/** - Diretório que contém classes Python, que mapeiam tabelas do banco de dados para objetos Python;
  
- **.env** - Arquivo que armazena as variáveis de ambiente da aplicação`(você deve criar esse arquivo)`, dentre elas estão:
  - `DATABASE_URL` -> URL para acessar o banco de dados PostgreSQL;
  - `DB_HOST` -> Endereço do host para acesso ao banco de dados;
  - `DB_DATABASE` -> Nome do banco de dados;
  - `DB_USER` -> Usuário de acesso ao banco de dados;
  - `DB_PASSWORD` -> Senha de acesso ao banco de dados;
  - `GITHUB_USER` -> Nome do seu usuário no Github(utilizado para fazer a request para a API do Github e trazer seus projetos);
  - `MEDIUM_USER` -> Nome do seu usuário no Medium(utilizado para fazer a request para a API do Medium e trazer seus posts);
  - `API_KEY` -> Chave de acesso fornecido pela RapidAPI(serviço de API do Medium que estou utilizando);
  - `BASE_URL` -> URL base que o serviço RapidAPI fornece;
  - `API_HOST` -> Endereço do host que o serviço RapidAPI fornece;
  - `ENDPOINT_API` -> Endereço onde sua API está hospedada(utilizada no app desktop);
  - `TOKEN` -> Token secreto utilizado para autenticação durante a comunicação entre o app desktop e API(**você deve gerar esse Token**);
  
- **.gitignore** - Arquivo padrão do GIT para ignorar diretórios e arquivos desnecessários;
  
- **app.py** - Arquivo principal que declara quais endpoints são aceitos pela API;
  
- **LICENSE** - Arquivo de licença de uso do projeto;
  
- **Procfile** - Arquivo que vai ditar o comando necessário para fazer o deploy da API na plataforma do Heroku;
  
- **README.md** - Arquivo padrão do Github com a descrição do projeto;
  
- **requirements.txt** - Arquivo padrão do Python para guardar dependências do projeto;


---
## Publicação

Como servidor de banco de dados e plataforma de deploy utilizei o [Heroku](https://dashboard.heroku.com/apps):

1. Basta criar um novo projeto no Heroku, e vincular seu projeto do Github nele. Ao vincular o projeto do Github, toda vez que você fizer um commit na branch main, automaticamente será feito um novo deploy do app pelo Heroku;

2. Depois de criado o projeto você pode ir até a aba "Resources" e adicionar o serviço **Heroku Postgres**, ao adicionar o serviço o Heroku irá fornecer as chaves de acesso ao banco de dados criado, e você pode preenche-las no arquivo .env explicado anteriormente. Para iniciar o banco de dadas está disponível o script ``init_database.sql`` que irá criar toda a estrutura de banco de dados para o projeto.

3. Por ultimo é só adicionar as mesmas variáveis do arquivo .env nas variáveis de ambiente do projeto no Heroku.

Para integração com a API do Medium, utilizei os serviços da RapidAPI, e para configurá-la é bastante simples:

1. Criar uma conta na [RapidAPI](https://rapidapi.com/hub).

2. Criar um app na plataforma e adicionar [essa API](https://rapidapi.com/nishujain199719-vgIfuFHZxVZ/api/medium2/) a ele, com isso serão disponibilizadas as chaves de acesso ao serviço e você pode configurá-las no arquivo .env e também nas variáveis de ambiente do Heroku.

Com isso o projeto já estará no ar e qualquer pessoa poderá acessá-lo. Porém como um passo opcional, você pode configurar também um serviço na AWS que irá fazer o update dos projetos e posts do medium periodicamente, para não precisar se preocupar em atualizar caso você crie um novo projeto ou faça um novo post:

1. Criar uma conta na [AWS](https://portal.aws.amazon.com/billing/signup#/start/email).
2. Acessar o console da AWS Lambda [aqui](https://sa-east-1.console.aws.amazon.com/lambda/home?region=sa-east-1#/functions);
3. Criar um nova função com o runtime do Python e subir toda a pasta "aws_lambda_update" desse projeto para a plataforma;
4. Depois basta configurar a função "start" do arquivo "main.py" como handler da função, e agendar qual o intervalo de tempo que vocẽ irá querer executar essa função.


---
## Licença

Distribuído sob a licença MIT. Veja `LICENSE` para mais informações.


---
## Contato

Marcos Warmling Berti - **marcos_wb@outlook.com**
