from sqlalchemy.sql import func


from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime,
    Enum,
)
from enum import IntEnum

from database.database import Base


class GenderEnum(IntEnum):
    male = 0
    female = 1


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    birth_date = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    gender = Column(Enum(GenderEnum), nullable=False)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), server_onupdate=func.now())
