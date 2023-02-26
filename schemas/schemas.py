from datetime import datetime
from pydantic import BaseModel, EmailStr
from models import GenderEnum
from typing import Optional
from datetime import date


class BaseUser(BaseModel):
    full_name: str
    email: EmailStr
    gender: GenderEnum
    birth_date: date


class UserCreate(BaseUser):
    pass


class UserUpdate(BaseModel):
    full_name: Optional[str]
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


class BaseCar(BaseModel):
    manufacturer_id: int
    issued: int
    user_id: int


class CarCreate(BaseCar):
    model: Optional[str]


class CarUpdate(BaseModel):
    manufacturer_id: Optional[int]
    issued: Optional[int]
    user_id: Optional[int]
    model: Optional[str]


class CarInDB(CarCreate):
    id: int

    class Config:
        orm_mode = True


class ManufacturerBase(BaseModel):
    name: str


class ManufacturerCreate(ManufacturerBase):
    pass


class ManufacturerUpdate(ManufacturerBase):
    pass


class ManufacturerInDB(ManufacturerBase):
    id: int

    class Config:
        orm_mode = True
