from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from configuration.database import Base
from model.association.user_role import user_roles


class Role(Base):
    __tablename__ = "roles"

    id = Column(Integer, primary_key=True)
    name = Column(String(20), unique=True, index=True, nullable=False)

    users = relationship("User", secondary=user_roles, back_populates="roles", lazy="selectin")
