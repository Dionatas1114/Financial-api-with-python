from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.models.user import User
# from app.schemas import schemas


# CRUD de usuários

# Consultar todos os usuários
async def get_all_users(db: Session):
    listUser = db.query(User).all()
    if listUser is None:
        raise HTTPException(status_code=404, detail="User not found")
    return listUser

async def get_user_by_id(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()

# def create_user(db: Session, user: schemas.UserCreate):
#     db_user = User(name=user.name, email=user.email)
#     db.add(db_user)
#     db.commit()
#     db.refresh(db_user)
#     return db_user
