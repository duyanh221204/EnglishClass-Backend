from datetime import datetime

from sqlalchemy import String, DateTime
from sqlalchemy.orm import Mapped, mapped_column

from configuration.database import Base


class InvalidatedToken(Base):
    __tablename__ = "invalidated_tokens"

    id: Mapped[str] = mapped_column(String(36), primary_key=True)
    expired_at: Mapped[datetime] = mapped_column(DateTime)
