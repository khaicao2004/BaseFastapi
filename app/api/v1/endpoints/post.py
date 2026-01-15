from fastapi import APIRouter
from app.models.post import Post
from app.core.database import get_db
from sqlalchemy.orm import Session
from fastapi import Depends
from sqlalchemy.orm import selectinload

router = APIRouter()

@router.get("/")
def get_posts(db: Session = Depends(get_db)):
    posts = db.query(Post).options(selectinload(Post.user)).all()
    return posts