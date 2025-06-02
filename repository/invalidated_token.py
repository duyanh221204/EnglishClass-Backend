from fastapi import Depends
from sqlalchemy.orm import Session

from configuration.database import get_db
from model import InvalidatedToken


def get_invalidated_token_repo(db=Depends(get_db)):
    try:
        yield InvalidatedTokenRepository(db)
    finally:
        pass


class InvalidatedTokenRepository:
    def __init__(self, db: Session):
        self.db = db

    def find_by_token_id(self, token_id: str) -> InvalidatedToken | None:
        return self.db.query(InvalidatedToken).filter(InvalidatedToken.id == token_id).first()

    def save(self, invalidated_token: InvalidatedToken) -> None:
        self.db.add(invalidated_token)
        self.db.commit()
        self.db.refresh(invalidated_token)
