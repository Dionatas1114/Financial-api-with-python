# from app.models.transaction import Transaction
from typing import List
from pydantic import BaseModel


class UserBase(BaseModel):
    id: int
    name: str
    email: str

class UserCreate(UserBase):
    pass

class UserUpdate(UserBase):
    pass

class User(UserBase):
    id: int
    # transactions: List[Transaction]

    class Config:
        orm_mode = True
