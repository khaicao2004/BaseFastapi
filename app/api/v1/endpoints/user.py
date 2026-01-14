from fastapi import APIRouter, HTTPException, Depends
from app.schemas.user_schema import UserCreate, UserUpdate
from app.models.user import User
from app.core.database import get_db
from sqlalchemy.orm import Session

router = APIRouter()

@router.get("/users")
def get_users(db: Session = Depends(get_db)):
    users = db.query(User).all()
    return users

@router.get("/users/{user_id}")
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.post("/users")
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    # Check if user exists
    exist_user = db.query(User).filter(
        (User.username == user.username) | (User.email == user.email)
    ).first()
    if exist_user:
        raise HTTPException(status_code=400, detail="Username or email already exists")
    
    # Create new user
    db_user = User(
        username=user.username,
        email=user.email,
        password=user.password
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
