from pydantic import BaseModel, Field, EmailStr
from typing import List, Optional

class Item(BaseModel):
    item_id: str = Field(...)
    quantity: int = Field(...,gt=0)
    price: float = Field(...,gt=0)

class User(BaseModel):
    user_id: str = Field(...)
    email: EmailStr = Field(examples=['marcelo@mail.com'])
    timestamp: str = Field(...)
    items: List[Item]

class Users(BaseModel):
    List[User]
