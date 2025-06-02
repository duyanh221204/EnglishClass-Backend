from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

from util.constant import Constant

DB_USERNAME = Constant.DB_USERNAME
DB_PASSWORD = Constant.DB_PASSWORD
DB_HOST = Constant.DB_HOST
DB_PORT = Constant.DB_PORT
DB_DATABASE = Constant.DB_DATABASE

SQLALCHEMY_DATABASE_URL = f"postgresql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_DATABASE}"

engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
