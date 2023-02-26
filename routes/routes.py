from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

import schemas
from database import get_db
from services import UserService, CarService, ManufacturerService

user_router = APIRouter(prefix="/user", tags=["user"])
car_router = APIRouter(prefix="/car", tags=["car"])
manufacturer_router = APIRouter(prefix="/man", tags=["manufacturer"])


@user_router.post("/")
def create_new_user(new_user: schemas.UserCreate, db: Session = Depends(get_db)) -> schemas.UserInDB:
    return UserService.create_user(db=db, obj_id=new_user)


@user_router.patch("/<user_id>")
def update_user(user_id: int, user: schemas.UserUpdate, db: Session = Depends(get_db)) -> schemas.UserInDB:
    return UserService.update(db=db, obj=user, obj_id=user_id)


@user_router.get("/get_user/<user_id>")
def get_user_by_id(user_id: int, db: Session = Depends(get_db)):
    return UserService.get_user(db=db, obj_id=user_id)


@user_router.delete("/delete_user/<user_id>")
def get_user_by_id(user_id: int, db: Session = Depends(get_db)):
    return UserService.delete_user(db=db, obj_id=user_id)

@car_router.post("/")
def create_new_car(
    new_car: schemas.CarCreate, db: Session = Depends(get_db)
) -> schemas.CarInDB:
    return CarService.create_car(db=db, new_car=new_car)


@car_router.patch("/<car_id>")
def update_car(
    car_id: int, car: schemas.CarUpdate, db: Session = Depends(get_db)
) -> schemas.CarInDB:
    return CarService.update(db=db, obj=car, obj_id=car_id)


@car_router.get("/get_car/<car_id>")
def get_user_by_id(car_id: int, db: Session = Depends(get_db)):
    return CarService.get_car(db=db, obj_id=car_id)


@car_router.delete("/delete_car/<car_id>")
def get_user_by_id(car_id: int, db: Session = Depends(get_db)):
    return CarService.delete_car(db=db, obj_id=car_id)


@manufacturer_router.post("/")
def create_new_manufacturer(
    new_man: schemas.ManufacturerCreate, db: Session = Depends(get_db)
) -> schemas.ManufacturerInDB:
    return ManufacturerService.create(db=db, new_man=new_man)


@manufacturer_router.patch("/<man_id>")
def update_man(
    man_id: int, man: schemas.ManufacturerUpdate, db: Session = Depends(get_db)
) -> schemas.ManufacturerInDB:
    return ManufacturerService.update(db=db, obj=man, obj_id=man_id)


@manufacturer_router.get("/get_man/<man_id>")
def get_user_by_id(man_id: int, db: Session = Depends(get_db)):
    return ManufacturerService.get(db=db, obj_id=man_id)


@manufacturer_router.delete("/delete_man/<man_id>")
def get_user_by_id(man_id: int, db: Session = Depends(get_db)):
    return ManufacturerService.delete(db=db, obj_id=man_id)