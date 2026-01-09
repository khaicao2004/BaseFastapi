from typing import Generator
from app.core.config import configs
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine(configs.DATABASE_URI)