from pydantic import BaseModel, EmailStr


# Schema for User Registration
class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str


# Schema for User Login
class UserLogin(BaseModel):
    email: EmailStr
    password: str


# Schema for Returning User Data
class UserResponse(BaseModel):
    id: int
    username: str
    email: EmailStr

    class Config:
        from_attributes = True