from sqlalchemy.orm import Session
import schemas
import models
from exceptions import ItemNotFound


class UserService:
    @staticmethod
    def create_user(db: Session, obj_id: schemas.UserCreate):
        new_user = models.User(**obj_id.dict())
        db.add(new_user)
        db.commit()
        return new_user

    @staticmethod
    def update(db: Session, obj: schemas.UserUpdate, obj_id: int) -> models.User:
        db_obj = db.query(models.User).get(obj_id)
        if not db_obj:
            raise ItemNotFound

        for k, v in obj.dict().items():
            if v is not None:
                setattr(db_obj, k, v)

        db.commit()
        return db_obj

    @staticmethod
    def get_user(db: Session, obj_id: int) -> models.User:
        db_obj = db.query(models.User).get(obj_id)
        if not db_obj:
            raise ItemNotFound
        return db_obj

    @staticmethod
    def delete_user(db: Session, obj_id: int):
        db_user = db.query(models.User).get(obj_id)
        if db_user:
            db.delete(db_user)
            db.commit()
            return {"detail": "ok"}
        else:
            raise ItemNotFound


class CarService:
    @staticmethod
    def create_car(db: Session, new_car: schemas.CarCreate) -> models.Car:
        new_car = models.Car(**new_car.dict())
        db.add(new_car)
        db.commit()
        return new_car

    @staticmethod
    def update(db: Session, obj: schemas.CarUpdate, obj_id: int) -> models.Car:
        db_obj = db.query(models.Car).get(obj_id)
        if not db_obj:
            raise ItemNotFound

        for k, v in obj.dict().items():
            if v is not None:
                setattr(db_obj, k, v)

        db.commit()
        return db_obj

    @staticmethod
    def get_car(db: Session, obj_id: int) -> models.Car:
        db_obj = db.query(models.Car).get(obj_id)
        if not db_obj:
            raise ItemNotFound
        return db_obj

    @staticmethod
    def delete_car(db: Session, obj_id: int):
        db_car = db.query(models.Car).get(obj_id)
        if db_car:
            db.delete(db_car)
            db.commit()
            return {"detail": "ok"}
        else:
            raise ItemNotFound


class ManufacturerService:
    @staticmethod
    def create(db: Session, new_man: schemas.ManufacturerCreate):
        new_man = models.Manufacturer(**new_man.dict())
        db.add(new_man)
        db.commit()
        return new_man

    @staticmethod
    def get(db: Session, obj_id: int) -> models.Manufacturer:
        db_obj = db.query(models.Manufacturer).get(obj_id)
        if not db_obj:
            raise ItemNotFound
        return db_obj

    @staticmethod
    def update(db: Session, obj: schemas.ManufacturerUpdate, obj_id: int) -> models.Manufacturer:
        db_obj = db.query(models.Manufacturer).get(obj_id)
        if not db_obj:
            raise ItemNotFound

        for k, v in obj.dict().items():
            if v is not None:
                setattr(db_obj, k, v)

        db.commit()
        return db_obj

    @staticmethod
    def delete(db: Session, obj_id: int):
        db_manufacturer = db.query(models.Manufacturer).get(obj_id)
        if db_manufacturer:
            db.delete(db_manufacturer)
            db.commit()
            return {"detail": "ok"}
        else:
            raise ItemNotFound
