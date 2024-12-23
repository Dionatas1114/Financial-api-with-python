from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas import schemas


# CRUD de usuários
def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()


def create_user(db: Session, user: schemas.UserCreate):
    db_user = User(name=user.name, email=user.email)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user