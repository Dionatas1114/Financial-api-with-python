import uvicorn
from fastapi import FastAPI
import app.routes.auth as auth
import app.routes.user as users

# from .database.database import init_db
app = FastAPI()

# Inicializa o banco de dados
# init_db()

@app.get("/health-check") # Rota de health-check
def health_check():
    return {"status": "OK"}

app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(users.router, prefix="/users", tags=["users"])

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", reload=True, port=8000)

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
