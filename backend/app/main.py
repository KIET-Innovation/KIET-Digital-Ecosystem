from fastapi import FastAPI
from pydantic_settings import BaseSettings
from app.database import Base, engine
from app.routers import user, auth

app = FastAPI()

@app.on_event("startup")
def startup():
    Base.metadata.create_all(bind=engine)

app.include_router(user.router, prefix="/api", tags=["Users"])
app.include_router(auth.router, prefix="/api", tags=["Auth"])

@app.get("/")
def read_root():
    return {"message": "Welcome to KIET Digital Ecosystem API 🚀"}
