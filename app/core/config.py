import os
from dotenv import load_dotenv
from pydantic import BaseSettings

load_dotenv()

class Configs(BaseSettings):
    # base
    APP_ENV: str = os.getenv("APP_ENV", "dev")
    APP_NAME: str = os.getenv("APP_NAME")
    API_PREFIX: str = "/api"
    API_V1_STR: str = "/v1"
    APP_ROOT: str = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    DB_NAME_MAPPER: dict = {
        "prod" : "fast_prod",
        "stage" : "fast_stage",
        "dev" : "fast_dev",
    }
    DB_ENGINE_MAPPER: dict = {
        "mysql": "mysql+pymysql"
    }

    # database
    DB_CONNECTION: str = os.getenv("DB_CONNECTION", "mysql")
    DB_HOST: str = os.getenv("DB_HOST")
    DB_PORT: str = os.getenv("DB_PORT", "3306")
    DB_NAME: str = os.getenv("DB_NAME")
    DB_USER: str = os.getenv("DB_USER")
    DB_PASSWORD: str = os.getenv("DB_PASSWORD")
    DB_ENGINE: str = DB_ENGINE_MAPPER.get(DB_CONNECTION, "mysql")

    DATABASE_URI_FORMAT: str = "{db_engine}://{user}:{password}@{host}:{port}/{database}"
    DATABASE_URI = DATABASE_URI_FORMAT.format(
        db_engine=DB_ENGINE,
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT,
        database=DB_NAME_MAPPER[APP_ENV]
    )

configs = Configs()