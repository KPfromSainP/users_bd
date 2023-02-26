import uvicorn
from fastapi import FastAPI
from routes import user_router, car_router, manufacturer_router

app = FastAPI()
#database.Base.metadata.create_all(bind=engine)

app.include_router(user_router)
app.include_router(car_router)
app.include_router(manufacturer_router)

if __name__ == "__main__":
    uvicorn.run(app, port=8000, host="0.0.0.0")

# @app.post('/users')
# async def create_user(new_user: schemas.UserCreate, db: Session = Depends(database.get_db)) -> schemas.UserInDB:
#     new_db_user = models.User(**new_user.dict())
#     db.add(new_db_user)
#     db.commit()
#     db.flush()
#     return new_db_user
