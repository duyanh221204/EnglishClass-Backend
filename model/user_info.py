from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from configuration.database import Base


class UserInfo(Base):
    __tablename__ = "users_info"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    email = Column(String(100), unique=True, index=True, nullable=False)

    user_auth = relationship("UserAuthentication", back_populates="user_info", uselist=False)
