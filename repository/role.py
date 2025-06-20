from typing import Annotated

from fastapi import Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from configuration.database import get_db
from model import Role


def get_role_repo(db: Annotated[AsyncSession, Depends(get_db)]):
    try:
        yield RoleRepository(db)
    finally:
        pass


class RoleRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def find_all(self) -> list[Role]:
        roles = await self.db.execute(select(Role))
        return list(roles.scalars().all())

    async def save_all(self, roles: list[Role]) -> None:
        self.db.add_all(roles)
        await self.db.flush()
