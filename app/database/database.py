import os
# import mysql.connector
# from dotenv import load_dotenv
from sqlalchemy.ext.declarative import declarative_base
# from contextlib import contextmanager

from sqlmodel import SQLModel, create_engine
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


# Carregar variáveis de ambiente do arquivo .env
# load_dotenv()

# # Obter as variáveis de ambiente
# DB_HOST = os.getenv('DB_HOST')
# DB_PORT = os.getenv('DB_PORT', 3306)
# DB_USER = os.getenv('DB_USER')
# DB_PASSWORD = os.getenv('DB_PASSWORD')
# DB_NAME = os.getenv('DB_NAME')

# Construir a URL de conexão com o banco de dados
# DATABASE_URL = f"mysql+mysqlconnector://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
SQLALCHEMY_DATABASE_URL  = "mysql+mysqlconnector://dev_user:dev_password@localhost:3306/financial_db_dev"
# print("SQLALCHEMY_DATABASE_URL : ", SQLALCHEMY_DATABASE_URL )

# Criar o engine e a base para os modelos
# engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True)
# engine = create_engine(SQLALCHEMY_DATABASE_URL , connect_args={"charset": "utf8mb4"})

# Base de dados onde todos os modelos serão registrados
# Base = declarative_base()

# Criar a sessão para interação com o banco de dados
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
# def init_db():
#     # Cria as tabelas no banco de dados
#     SQLModel.metadata.create_all(bind=engine, checkfirst=False)
    
# Função para obter a sessão do banco de dados
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# def get_db():
#     print("Conectando ao banco de dados...")
#     db = SessionLocal()
#     try:
#         yield db
#     except Exception as err:
#         print(f"Erro na conexão com o banco de dados: {err}")
#         return None
#     finally:
#         db.close()
    
# @contextmanager
# def get_db_session():
#     print("Conectando ao banco de dados...")
#     db = SessionLocal()
#     try:
#         yield db
#     except Exception as err:
#         print(f"Erro na conexão com o banco de dados: {err}")
#         return None
#     finally:
#         db.close()

# def init_dev_db(app):
    # # Passo 1: Conectar ao banco de dados (cria o banco se não existir)
    # conn = sqlite3.connect('meu_banco_de_dados.db')

    # # Passo 2: Criar um cursor para executar comandos SQL
    # cursor = conn.cursor()

    # # Passo 3: Criar uma tabela (caso não exista)
    # cursor.execute('''
    # CREATE TABLE IF NOT EXISTS usuarios (
    #     id INTEGER PRIMARY KEY AUTOINCREMENT,
    #     nome TEXT NOT NULL,
    #     email TEXT NOT NULL
    # )
    # ''')