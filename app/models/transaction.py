# from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime
# from sqlalchemy.orm import relationship
# from app.database.database import SQLALCHEMY_DATABASE_URL as Base
# from sqlalchemy.ext.declarative import declarative_base
#
#
# Base = declarative_base()
#
# class Transaction(Base):
#     __tablename__ = "transactions"
#
#     id = Column(Integer, primary_key=True, index=True)
#     amount = Column(Float)
#     description = Column(String)
#     timestamp = Column(DateTime)
#     user_id = Column(Integer, ForeignKey("users.id"))
#
#     owner = relationship("User", back_populates="transactions")