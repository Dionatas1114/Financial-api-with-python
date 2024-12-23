# from pydantic import BaseModel
# from datetime import datetime
# from typing import List
#
#
# # Pydantic model para criação de transações (entrada)
# class TransactionCreate(BaseModel):
#     amount: float
#     description: str
#     user_id: int
#
#     class Config:
#         orm_mode = True  # Permite usar objetos SQLAlchemy diretamente
#
# # Pydantic model para resposta de transações (saída)
# class TransactionResponse(TransactionCreate):
#     id: int
#     timestamp: datetime
#
#     class Config:
#         orm_mode = True  # Permite usar objetos SQLAlchemy diretamente
#
# # Pydantic model para User (se necessário para resposta)
# class UserResponse(BaseModel):
#     id: int
#     name: str
#
#     class Config:
#         orm_mode = True  # Permite usar objetos SQLAlchemy diretamente
#
# # class TransactionBase(BaseModel):
# #     amount: float
# #     description: str
# #     timestamp: datetime
# #
# # class TransactionCreate(TransactionBase):
# #     pass
# #
# # class Transaction(TransactionBase):
# #     id: int
# #     user_id: int
# #
# #     class Config:
# #         orm_mode = True
# #
# # class TransactionList(BaseModel):
# #     transactions: List[Transaction]
# #
# #     class Config:
# #         orm_mode = True
