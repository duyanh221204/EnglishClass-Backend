from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

from configuration.database import Base


class UserRole(Base):
    __tablename__ = "user_role"

    user_authentication_id = Column(Integer, ForeignKey("users_authentication.id"), primary_key=True)
    role_id = Column(Integer, ForeignKey("roles.id"), primary_key=True)

    user_auth = relationship("UserAuthentication", back_populates="user_role")
    role = relationship("Role", back_populates="user_role")
