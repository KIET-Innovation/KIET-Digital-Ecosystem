from fastapi import FastAPI
from app.database import Base, engine
from app.routers import user

app = FastAPI()

@app.on_event("startup")
def startup():
    Base.metadata.create_all(bind=engine)

app.include_router(user.router)
