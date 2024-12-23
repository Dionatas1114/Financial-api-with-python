from fastapi import FastAPI, Depends, HTTPException, APIRouter
# from pydantic import BaseModel
# from sqlalchemy.orm import Session
from typing import List
from app.schemas.user import UserBase, UserCreate, UserUpdate
# from app.services import services
# import app.database.database as database


fake_db = {} # Simulação de um banco de dados em memória

router = APIRouter()

@router.post("/", response_model=UserBase)
def create_user(user: UserCreate):
    if user.id in fake_db:
        raise HTTPException(status_code=400, detail="User already registered")
    fake_db[user.id] = user
    return user

# Endpoint para obter todos os usuários
@router.get("/", response_model=List[UserBase])
def get_users():
    return list(fake_db.values())

# Endpoint para obter um usuário específico
@router.get("/{user_id}", response_model=UserBase)
def get_users(user_id: int):
    user = fake_db.get(user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

# @router.post("/", response_model=schemas.User)
# def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
#     return services.create_user(db=db, user=user)