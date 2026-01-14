from typing import Optional, Union, Annotated
from fastapi import FastAPI, Query,Path, HTTPException
from pydantic import BaseModel
from datetime import datetime
from enum import Enum
from fastapi.middleware.cors import CORSMiddleware
from fastapi_sqlalchemy import DBSessionMiddleware
from app.api.routest import router as api_router
from app.core.config import configs

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# Middleware để quản lý DB session tự động
# app.add_middleware(DBSessionMiddleware, db_url=configs.DATABASE_URI)

# Include API router
app.include_router(api_router)


@app.get('/')
def root():
    return 'Hello world'
