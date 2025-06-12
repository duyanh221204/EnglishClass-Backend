from sqlalchemy import Integer, Column, String, ForeignKey
from sqlalchemy.orm import relationship

from configuration.database import Base


class UserAuthentication(Base):
    __tablename__ = "users_authentication"

    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True, index=True, nullable=False)
    password = Column(String(255), nullable=False)
    user_info_id = Column(Integer, ForeignKey("users_info.id"), index=True, nullable=False)

    user_info = relationship("UserInfo", back_populates="user_auth", uselist=False)
    user_role = relationship("UserRole", back_populates="user_auth")
