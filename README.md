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
        docker-compose.yml     # Arquivo Docker Compose
        Dockerfile             # Arquivo Docker para dev
        License                # Licenças
        README.md              # Documentação
        requirements.txt       # Dependências gerais
        requirements-dev.txt   # Dependências de desenvolvimento
        requirements-prod.txt  # Dependências de produção


## Preparando o Ambiente do projeto:
DEV com Docker

1. Construa a imagem Docker para o desenvolvimento: 

        docker build -t financial-api .
2. Execute o contêiner:

         docker run -d -p 8000:8000 financial-api

PROD
1. Rodar a aplicação com Uvicorn em produção:
    
        uvicorn app.main:app --host 0.0.0.0 --port 8000 --workers 4 --reload

## Rodando o projeto

1. Instale as dependências do projeto:
    
        pip install -r requirements.txt

2. Rodar as migrações do banco de dados com Alembic:
    
         alembic upgrade head

3. rodar o Docker Compose
    
         docker compose up

4. Inicie o servidor local:
    
         py -m venv venv
         .\venv\Scripts\activate
         uvicorn app.main:app --reload

5. Acesse a API em http://localhost:8000/

6. O projeto está pronto para uso!

7. Explore as rotas e endpoints da API para criar usuários, realizar transações financeiras, etc:
[Postman collection](https://martian-trinity-552681.postman.co/workspace/e34fa4fb-9270-4910-9be5-cdf717c76fcd/collection/11754773-7229697d-28c7-4361-a9ae-810776e7b3b9?action=share&source=email&creator=11754773&action_performed=google_login)

[//]: # (8. Acesse o painel admin em http://localhost:8000/admin/ para gerenciar models e dados do banco de dados)

## Documentação da API

1. Acesse a documentação da API pelo navegador em:
http://localhost:8000/docs

## Testes

1. Rodar os testes com pytest

        pytest --maxfail=1 --disable-warnings -q

## Como Desenvolver novas migrations

1. Inicializar o Alembic para gerar novas migrações:
    
        alembic init migrations
2. Criar novas migrations com Alembic:
    
         alembic revision --autogenerate -m "Adicionar nova tabela"
3. Aplicar Migrações
    
         alembic upgrade head

## Acessando a API

    Criação de usuário: POST /users/
    Criação de transação: POST /transactions/
    Obter usuário: GET /users/{user_id}
    Obter transações de um usuário: GET /transactions/{user_id}