from app.models.base_model import BaseModel as BareBaseModel
from sqlalchemy import Column, String
from datetime import datetime
from pydantic import BaseModel

class User(BareBaseModel):
    __tablename__ = "users"

    username = Column(String(100), unique=True, index=True)
    email = Column(String(255), unique=True, index=True)
    password = Column(String(255))

class UserResponse(BaseModel):
    id: int
    username: str
    email: str
    created_at: datetime
    updated_at: datetime