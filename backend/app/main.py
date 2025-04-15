from fastapi import FastAPI
from app.database import Base, engine

app = FastAPI()

@app.on_event("startup")
def startup():
    Base.metadata.create_all(bind=engine)

@app.get("/")
async def root():
    return {"message": "Welcome to KIET Digital Ecosystem"}
