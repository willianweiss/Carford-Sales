from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from api.utils.database import get_db
from api.users.models import User
from api.users.schemas import Register, Login
from api.auth.auth_handler import signJWT

router = APIRouter(tags=["users"])

@router.post("/register")
def register_user(user: Register, db: Session = Depends(get_db)):
    db_user = User(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

@router.post("/login")
def login_user(user: Login, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.name == user.name).first()
    if not db_user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found",
        )
    if db_user.password != user.password:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Incorrect password",
        )
    return {"access_token": signJWT(db_user.id), "token_type": "bearer"}
    