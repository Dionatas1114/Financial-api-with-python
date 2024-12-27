from database import engine, Base

# Criação das tabelas no banco
Base.metadata.create_all(bind=engine)

print("Tabelas criadas com sucesso!")