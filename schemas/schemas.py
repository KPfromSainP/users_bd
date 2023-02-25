from datetime import datetime
from pydantic import BaseModel, EmailStr
from models import GenderEnum
from typing import Optional
from datetime import date


class BaseUser(BaseModel):
    name: str
    email: EmailStr
    gender: GenderEnum
    birth_date: date


class UserCreate(BaseUser):
    pass


class UserUpdate(BaseModel):
    name: Optional[str]
    email: Optional[EmailStr]
    gender: Optional[GenderEnum]
    birth_date: Optional[date]


class UserInDB(BaseUser):
    id: int
    birth_date: date
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
