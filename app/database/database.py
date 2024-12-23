from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.config import settings


# Verifica qual URL de banco usar, dependendo do ambiente
DATABASE_URL = settings.DATABASE_URL_DEV if settings.DATABASE_URL_DEV else settings.DATABASE_URL_PROD

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False} if "sqlite" in DATABASE_URL else {})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

SQLALCHEMY_DATABASE_URL = declarative_base()
