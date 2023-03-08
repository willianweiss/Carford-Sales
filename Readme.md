# Carford-Sales

Este projeto é uma API construída em Python usando o framework FastAPI, e foi projetado para ser escalável, modular e fácil de manter.

## Requisitos

-   Python 3.9 ou superior
-   Docker e Docker Compose

## Configuração

Antes de iniciar a API, é necessário mudar o nome do arquivo `.env-example` para `.env`

## Arquitetura do projeto

O projeto está estruturado em vários pacotes e módulos, cada um responsável por uma parte específica da aplicação. 

```
`📦api
 ┣ 📂auth
 ┃ ┣ 📜auth_bearer.py
 ┃ ┗ 📜auth_handler.py
 ┣ 📂cars
 ┃ ┣ 📜models.py
 ┃ ┣ 📜routes.py
 ┃ ┗ 📜schemas.py
 ┣ 📂owners
 ┃ ┣ 📜models.py
 ┃ ┣ 📜routes.py
 ┃ ┗ 📜schemas.py
 ┣ 📂users
 ┃ ┣ 📜models.py
 ┃ ┣ 📜routes.py
 ┃ ┗ 📜schemas.py
 ┣ 📂utils
 ┃ ┣ 📜database.py
 ┃ ┗ 📜database_utils.py
 ┣ 📜__init__.py
 ┣ 📜main.py
 ┗ 📜settings.py` 
 ```

-   O pacote `auth` contém os módulos responsáveis pela autenticação e autorização dos usuários na API.
-   O pacote `cars` contém os modelos, rotas e esquemas relacionados aos carros.
-   O pacote `owners` contém os modelos, rotas e esquemas relacionados aos proprietários de carros.
-   O pacote `users` contém os modelos e rotas relacionados aos usuários da API.
-   O pacote `utils` contém módulos auxiliares, como a configuração do banco de dados.

O arquivo `main.py` é o ponto de entrada da aplicação e define as rotas e middlewares usados pela API.

## Uso

Para executar a API localmente, basta executar o comando `uvicorn api.main:app --reload` na raiz do projeto. Você também pode usar o Docker Compose para executar a API em um container, usando o comando `docker-compose up --build`.

Após iniciar a API, você pode acessar a documentação interativa da API em `http://localhost:8000/docs`. A partir daí, você pode explorar as rotas disponíveis e testar as diferentes funcionalidades da API.

## Comandos

O arquivo `Makefile` contém alguns comandos úteis para facilitar o desenvolvimento da API. Alguns dos comandos disponíveis incluem:

-   `make lint`: Executa o linting do código usando o Black e o isort.
-   `make test`: Executa os testes da API usando o Pytest.
-   `make build`: Compila a API em um container usando o Docker Compose.
-   `make up`: Inicia a API em um container usando o Docker Compose.
-   `make down`: Para e remove