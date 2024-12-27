from fastapi import FastAPI, Depends, HTTPException, APIRouter
from typing import List
from app.schemas.user import UserBase, UserCreate, UserUpdate
from app.database.database import get_db
import app.services.user as userService

from sqlalchemy.orm import Session
from app.models import user


fake_db = {} # Simulação de um banco de dados em memória

router = APIRouter()

# router.on_event("startup")
# def on_startup():
#     print("create_db_and_tables()")


# Endpoint para obter todos os usuários
@router.get("/", response_model=List[UserBase])
async def get_users(db: Session = Depends(get_db)):
    return userService.get_all_users(db)

# Endpoint para obter um usuário específico
@router.get("/{user_id}", response_model=UserBase)
async def get_users(user_id: int):
    user = fake_db.get(user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

# Endpoint para criar um novo usuário
@router.post("/", response_model=UserBase)
async def create_user(user: UserCreate):
    if user.id in fake_db:
        raise HTTPException(status_code=400, detail="User already registered")
    fake_db[user.id] = user
    return user

# @router.post("/", response_model=schemas.User)
# def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
#     return services.create_user(db=db, user=user)