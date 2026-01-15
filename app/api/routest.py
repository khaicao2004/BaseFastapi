from fastapi import APIRouter
from app.api.v1.endpoints.user import router as user_router
from app.api.v1.endpoints.post import router as post_router
from app.core.config import configs

router = APIRouter(prefix=f"{configs.API_PREFIX}{configs.API_V1_STR}")

router.include_router(user_router, prefix="/users", tags=["Users"])
router.include_router(post_router, prefix="/posts", tags=["Posts"])