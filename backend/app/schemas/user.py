from pydantic import BaseModel

# Used to show output (never includes password)
class UserOut(BaseModel):
    id: int
    email: str
    full_name: str

    class Config:
        orm_mode = True

# Used during registration
class UserCreate(BaseModel):
    email: str
    full_name: str
    password: str
