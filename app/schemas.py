from pydantic import BaseModel, EmailStr
from typing import Optional, Any, Dict

class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"

class UserCreate(BaseModel):
    email: EmailStr
    password: str

class UserOut(BaseModel):
    id: int
    email: EmailStr
    class Config:
        orm_mode = True

class FarmerCreate(BaseModel):
    name: str
    aadhaar: Optional[str]
    pan: Optional[str]

class ConsentCreate(BaseModel):
    farmer_id: int
    purpose: str
    scope: Optional[Dict[str, Any]]

class ApplicationCreate(BaseModel):
    farmer_id: int
    product: str

class ApplicationOut(BaseModel):
    id: int
    farmer_id: int
    product: str
    status: str
    result: Optional[Dict[str, Any]]

    class Config:
        orm_mode = True
