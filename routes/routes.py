from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

import schemas
from database import get_db
from services import UserService

user_router = APIRouter(prefix="/user", tags=["user"])


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
