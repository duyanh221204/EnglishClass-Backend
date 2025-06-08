from typing import Annotated

from fastapi import Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from configuration.database import get_db
from model import InvalidatedToken


def get_invalidated_token_repo(db: Annotated[AsyncSession, Depends(get_db)]):
    try:
        yield InvalidatedTokenRepository(db)
    finally:
        pass


class InvalidatedTokenRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def find_by_id(self, jwt_id: str) -> InvalidatedToken | None:
        result = await self.db.execute(
            select(InvalidatedToken).where(InvalidatedToken.id == jwt_id)
        )
        return result.scalar()

    async def save(self, invalidated_token: InvalidatedToken) -> None:
        self.db.add(invalidated_token)
        await self.db.commit()
        await self.db.refresh(invalidated_token)
