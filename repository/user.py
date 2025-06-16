from typing import Annotated

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from configuration.database import get_db
from model import User


def get_user_repo(db: Annotated[AsyncSession, Depends(get_db)]):
    try:
        yield UserRepository(db)
    finally:
        pass


class UserRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def save(self, user: User) -> None:
        self.db.add(user)
        await self.db.commit()
        await self.db.refresh(user)
