# from sqlalchemy.orm import relationship

from sqlmodel import SQLModel, Field


class User(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    name: str
    email: str
    # transactions = relationship("Transaction", back_populates="owner")