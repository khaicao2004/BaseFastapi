from pydantic import BaseModel, Field
from typing import Optional

class UserCreate(BaseModel):
    username: str = Field(..., min_length=3, max_length=100)
    email: str = Field(..., min_length=3, max_length=100)
    password: str = Field(..., min_length=8, max_length=100)

class UserUpdate(BaseModel):
    username: Optional[str] = Field(None, min_length=3, max_length=100)
    email: Optional[str] = Field(None, min_length=3, max_length=100)
    password: Optional[str] = Field(None, min_length=8, max_length=100)