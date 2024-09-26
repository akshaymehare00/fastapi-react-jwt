# backend/schemas.py
from pydantic import BaseModel

class UserCreate(BaseModel):
    username: str
    password: str

class User(BaseModel):
    username: str

    class Config:
        from_attributes = True
class UserInDB(UserCreate):
    hashed_password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: str
    
class UserResponse(BaseModel):
    username: str

    class Config:
        from_attributes = True 

