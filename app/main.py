from fastapi import FastAPI, Depends, HTTPException
# from sqlalchemy.orm import Session
# import services
# import models
# import schemas
# import database
import app.routes.user as users

app = FastAPI()

# Incluindo as rotas do módulo de usuários
app.include_router(users.router, prefix="/users", tags=["users"])

# Cria as tabelas no banco de dados
# models.Base.metadata.create_all(bind=database.engine)

# Dependência para obter a sessão do banco de dados
# def get_db():
#     db = database.SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()

# @app.post("/users/", response_model=schemas.User)
# def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
#     return services.create_user(db=db, user=user)

# @app.post("/transactions/", response_model=schemas.Transaction)
# def create_transaction(transaction: schemas.TransactionCreate, user_id: int, db: Session = Depends(get_db)):
#     return services.create_transaction(db=db, transaction=transaction, user_id=user_id)

# @app.get("/users/{user_id}", response_model=schemas.User)
# def get_user(user_id: int, db: Session = Depends(get_db)):
#     db_user = services.get_user(db=db, user_id=user_id)
#     if db_user is None:
#         raise HTTPException(status_code=404, detail="User not found")
#     return db_user

# @app.get("/transactions/{user_id}", response_model=List[schemas.Transaction])
# def get_transactions(user_id: int, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
#     transactions = services.get_transactions_by_user(db=db, user_id=user_id, skip=skip, limit=limit)
#     return transactions
