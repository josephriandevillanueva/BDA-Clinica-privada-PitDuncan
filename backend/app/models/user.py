from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from enum import Enum

class RoleEnum(str, Enum):
    ADMIN = "ADMIN"
    DOCTOR = "DOCTOR"
    PATIENT = "PATIENT"

class UserBase(BaseModel):
    user: str
    activo: bool = True
    role: RoleEnum = RoleEnum.PATIENT

class UserCreate(UserBase):
    password: str

class UserDB(UserBase):
    id: str = Field(alias="_id")

class UserLogin(BaseModel):
    username: str
    password: str
