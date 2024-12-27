# import os
# from dotenv import load_dotenv
#
# # Verificar o valor da variável de ambiente ENV
# environment = os.getenv('ENV', 'development')  # Padrão para 'development'
#
# # Carregar o arquivo .env apropriado com base no ambiente
# print("Ambiente ENV: ", environment)
# if environment == 'production':
#     load_dotenv('.env.prod')  # Carregar o arquivo .env.prod para produção
# else:
#     load_dotenv('.env.dev')   # Carregar o arquivo .env.dev para desenvolvimento
#
# import uvicorn
# import subprocess
#
# def run_migrations():
#     """Rodar as migrações do Alembic"""
#     subprocess.run(["alembic", "upgrade", "head"])
#
# def start_dev_server():
#     """Iniciar o servidor de desenvolvimento"""
#     uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
#
# def start_prod_server():
#     """Iniciar o servidor de produção com gunicorn"""
#     subprocess.run(["gunicorn", "-w", "4", "main:app", "--host", "0.0.0.0", "--port", "8000"])
#
# if __name__ == "__main__":
#     # Rodar migrações antes de iniciar o servidor
#     run_migrations()
#
#     # Iniciar servidor conforme o ambiente
#     if environment == 'production':
#         start_prod_server()
#     else:
#         start_dev_server()
