# from pydantic import BaseSettings
#
# class Settings(BaseSettings):
#     DATABASE_URL_DEV = "sqlite:///./test.db"  # SQLite para desenvolvimento
#     DATABASE_URL_PROD = "mysql://user:password@localhost/financial_db"
#
#     class Config:
#         env_file = ".env"
#
# settings = Settings()

import os

class Settings:

    def __init__(self):
        environment = os.getenv('ENV', 'development')
        if environment == 'production':
            self.DATABASE_URL = os.getenv('DATABASE_URL', 'mysql://user:password@localhost/financial_db') # MySQL para produção
        else:
            self.DATABASE_URL = 'sqlite:///./test.db'  # SQLite para dev

        database_url = self.DATABASE_URL
        print("URL do banco de dados: ", database_url)

settings = Settings()