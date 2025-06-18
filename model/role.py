from sqlalchemy import Integer, String
from sqlalchemy.orm import relationship, Mapped, mapped_column

from configuration.database import Base
from model.association.user_role import user_roles


class Role(Base):
    __tablename__ = "roles"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(20), unique=True, index=True)

    users: Mapped[list["User"]] = relationship("User", secondary=user_roles, back_populates="roles", lazy="selectin")
