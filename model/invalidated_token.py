from sqlalchemy import Column, String, DateTime

from configuration.database import Base


class InvalidatedToken(Base):
    __tablename__ = "invalidated_tokens"

    id = Column(String(36), primary_key=True)
    expired_at = Column(DateTime, nullable=False)
