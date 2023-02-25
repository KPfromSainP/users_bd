from fastapi import FastAPI
from routes import user_router

app = FastAPI()
#database.Base.metadata.create_all(bind=engine)

app.include_router(user_router)


# @app.post('/users')
# async def create_user(new_user: schemas.UserCreate, db: Session = Depends(database.get_db)) -> schemas.UserInDB:
#     new_db_user = models.User(**new_user.dict())
#     db.add(new_db_user)
#     db.commit()
#     db.flush()
#     return new_db_user
