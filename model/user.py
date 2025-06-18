from datetime import date

from sqlalchemy import Integer, String, Date
from sqlalchemy.orm import relationship, Mapped, mapped_column

from configuration.database import Base
from model.association.user_role import user_roles


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    first_name: Mapped[str] = mapped_column(String(50))
    last_name: Mapped[str] = mapped_column(String(50))
    email: Mapped[str] = mapped_column(String(100), unique=True, index=True)
    phone: Mapped[str] = mapped_column(String(12), index=True)
    dob: Mapped[date] = mapped_column(Date)
    avatar: Mapped[str] = mapped_column(String(255), nullable=True)
    username: Mapped[str] = mapped_column(String(50), unique=True, index=True)
    password: Mapped[str] = mapped_column(String(255))

    roles: Mapped[list["Role"]] = relationship("Role", secondary=user_roles, back_populates="users", lazy="selectin")
