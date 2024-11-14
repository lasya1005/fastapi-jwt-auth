from pydantic import BaseModel, Field, EmailStr

class UserModel(BaseModel):
    email: EmailStr
    username: str
    password: str
    role: str = "user"

class TokenData(BaseModel):
    username: str
    role: str
