# Financial-api-with-python

Estrutura do projeto:

    financial-api-with-python/
        /app
            /core
                config.py
                security.py        # Configurações de segurança (JWT, Hashing, etc.)
            /database
                database.py        # Conexão com o banco de dados (como a criação da engine SQLAlchemy)
            /migrations
                /versions             # Arquivos de migração gerados
                alembic.ini           # Arquivo de configuração do Alembic
                env.py                # Arquivo de script para gerar migrações
            /models
                user.py            # Modelo de Usuário
                transaction.py     # Modelo de Transação
            /routes
                auth.py            # Rotas de Autenticação (Login, SignUp, etc.)
                user.py            # Rotas de Usuário
                transaction.py     # Rotas de Transação
            /schemas
                user.py            # Schemas do Usuário
                transaction.py     # Schemas da Transação
            /services
                user.py            # Logica para gerenciar dados de Usuário
                transaction.py     # Logica para gerenciar dados de Transação $$
            /tests
                test_user.py           # Testes unitários para Usuário
                test_transaction.py    # Testes unitários para Transação
            .env.dev               # Variáveis de ambiente para desenvolvimento
            .env.prod              # Variáveis de ambiente para produção
            config.py              # Configuração do projeto
            main.py                # Arquivo principal do FastAPI
        .gitignore             # Arquivos ignorados pelo Git
        docker-compose.dev.yml     # Arquivo Docker Compose para dev
        docker-compose.prod.yml    # Arquivo Docker Compose para prod
        Dockerfile.dev             # Arquivo Docker para dev
        Dockerfile.prod            # Arquivo Docker para prod
        License                # Licenças
        README.md              # Documentação
        requirements.txt       # Dependências gerais
        requirements-dev.txt   # Dependências de desenvolvimento
        requirements-prod.txt  # Dependências de produção

## Preparando o Ambiente do projeto:

DEV com Docker

1.  Construa a imagem Docker para o desenvolvimento:

        docker build -t financial-api .

2.  Execute o contêiner:

         docker run -d -p 8000:8000 financial-api

PROD

1.  Rodar a aplicação com Uvicorn em produção:

        docker-compose -f docker-compose.prod.yml up --build
        gunicorn -w 4 -k uvicorn.workers.UvicornWorker main:app
        ou
        gunicorn main:app -k uvicorn.workers.UvicornWorker --workers 4 --bind 0.0.0.0:8000

## Rodando o projeto

1.  Instale as dependências do projeto:

        py -m venv venv
        .\venv\Scripts\activate   ou   source venv/Scripts/activate
        pip install -r requirements-dev.txt

[//]: # "alembic init alembic"
[//]: # 'alembic revision --autogenerate -m "Create users table"'

2.  Rodar as migrações do banco de dados:

         python app/database/create_tables.py
         (ou com Alembic)
         alembic upgrade head

3.  rodar o Docker Compose

        docker-compose -f docker-compose.dev.yml up --build
        ou
        docker run --name mysql-db -e MYSQL_ROOT_PASSWORD=dev_password -e MYSQL_DATABASE=mysql-db -e MYSQL_USER=dev_user -e MYSQL_PASSWORD=dev_password --restart always -p 3306:3306 -d mysql:8.0 --character-set-server=utf8mb4 --collation-server=utf8mb4_bin --default-authentication-plugin=mysql_native_password

4.  Inicie o servidor local:

         uvicorn app.main:app --reload

5.  Acesse a API em http://localhost:8000/

6.  O projeto está pronto para uso!

7.  Explore as rotas e endpoints da API para criar usuários, realizar transações financeiras, etc:
    [Postman collection](https://martian-trinity-552681.postman.co/workspace/e34fa4fb-9270-4910-9be5-cdf717c76fcd/collection/11754773-7229697d-28c7-4361-a9ae-810776e7b3b9?action=share&source=email&creator=11754773&action_performed=google_login)

[//]: # "8. Acesse o painel admin em http://localhost:8000/admin/ para gerenciar models e dados do banco de dados"

## Acesso via Client (DBeaver, outros...)

1.  URL Jdbc:

        jdbc:mysql://localhost:3306/financial_db_dev?user=dev_user&password=dev_password
        ou
        jdbc:mysql://localhost:3306/financial_db_dev

## Documentação da API

1. Acesse a documentação da API pelo navegador em:
   http://localhost:8000/docs

## Testes

1.  Rodar os testes com pytest

        pytest --maxfail=1 --disable-warnings -q

## Como Desenvolver novas migrations

1.  Inicializar o Alembic para gerar novas migrações:

        alembic init migrations

2.  Criar novas migrations com Alembic:

         alembic revision --autogenerate -m "Adicionar nova tabela"

3.  Aplicar Migrações

         alembic upgrade head

## Acessando a API

    Criação de usuário: POST /users/
    Criação de transação: POST /transactions/
    Obter usuário: GET /users/{user_id}
    Obter transações de um usuário: GET /transactions/{user_id}
