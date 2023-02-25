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
