from typing import Optional, Union, Annotated
import uvicorn
from fastapi import FastAPI, Query,Path, HTTPException

from fastapi.middleware.cors import CORSMiddleware
from fastapi_sqlalchemy import DBSessionMiddleware
from app.api.routest import router as api_router
from app.models import Base
from app.core.database import engine
from app.core.config import configs

Base.metadata.create_all(bind=engine)

def get_application() -> FastAPI:
    application = FastAPI(
        title=configs.APP_NAME, docs_url="/docs", redoc_url="/redoc",
        openapi_url=f"{configs.API_PREFIX}{configs.API_V1_STR}/openapi.json",
    )
    application.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    application.add_middleware(DBSessionMiddleware, db_url=configs.DATABASE_URI)
    application.include_router(api_router)
    return application

app = get_application()

# if __name__ == "__main__":
#     uvicorn.run(app, host="0.0.0.0", port=8000)
