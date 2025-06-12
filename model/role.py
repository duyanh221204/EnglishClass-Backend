from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from configuration.database import Base


class Role(Base):
    __tablename__ = "roles"

    id = Column(Integer, primary_key=True)
    name = Column(String(20), unique=True, index=True, nullable=False)

    user_role = relationship("UserRole", back_populates="role")
