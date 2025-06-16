from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from configuration.database import Base
from model.association.user_role import user_roles


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    email = Column(String(100), unique=True, index=True, nullable=False)
    phone = Column(String(12), index=True, nullable=False)
    dob_day = Column(Integer, nullable=False)
    dob_month = Column(Integer, nullable=False)
    dob_year = Column(Integer, nullable=False)
    avatar = Column(String(255))
    username = Column(String(50), unique=True, index=True, nullable=False)
    password = Column(String(255), nullable=False)

    roles = relationship("Role", secondary=user_roles, back_populates="users", lazy="selectin")
