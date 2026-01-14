from app.models.base_model import BaseModel
from sqlalchemy import Column, String

class User(BaseModel):
    __tablename__ = "users"

    username = Column(String(100), unique=True, index=True)
    email = Column(String(255), unique=True, index=True)
    password = Column(String(255))