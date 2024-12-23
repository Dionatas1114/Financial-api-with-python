# from sqlalchemy.orm import Session
# from app.models.transaction import Transaction
# from app.schemas import schemas
#
# # CRUD de transações
# def create_transaction(db: Session, transaction: schemas.TransactionCreate, user_id: int):
#     db_transaction = Transaction(**transaction.dict(), user_id=user_id)
#     db.add(db_transaction)
#     db.commit()
#     db.refresh(db_transaction)
#     return db_transaction
#
# def get_transactions_by_user(db: Session, user_id: int, skip: int = 0, limit: int = 100):
#     return db.query(Transaction).filter(Transaction.user_id == user_id).offset(skip).limit(limit).all()
