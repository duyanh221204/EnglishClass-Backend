from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.ext.declarative import declarative_base

from util.constant import Constant

DB_USERNAME = Constant.DB_USERNAME
DB_PASSWORD = Constant.DB_PASSWORD
DB_HOST = Constant.DB_HOST
DB_PORT = Constant.DB_PORT
DB_DATABASE = Constant.DB_DATABASE

SQLALCHEMY_DATABASE_URL = f"postgresql+asyncpg://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_DATABASE}"

engine = create_async_engine(SQLALCHEMY_DATABASE_URL, echo=True, future=True)

AsyncSessionLocal = async_sessionmaker(
    bind=engine,
    expire_on_commit=False,
    class_=AsyncSession
)

Base = declarative_base()


async def get_db():
    async with AsyncSessionLocal() as session:
        try:
            yield session
        finally:
            await session.close()
