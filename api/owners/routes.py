from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from api.auth.auth_bearer import JWTBearer
from ..utils.database import get_db
from .models import Owner
from .schemas import OwnerCreate, OwnerInDB, OwnerUpdate

router = APIRouter(prefix="/owners", tags=["owners"], dependencies=[Depends(JWTBearer())])


@router.post("/", response_model=OwnerInDB)
def create_owner(owner: OwnerCreate, db: Session = Depends(get_db)):
    db_owner = Owner(**owner.dict())
    db.add(db_owner)
    db.commit()
    db.refresh(db_owner)
    return db_owner


@router.get("/{owner_id}", response_model=OwnerInDB)
def read_owner(owner_id: int, db: Session = Depends(get_db)):
    db_owner = db.query(Owner).filter(Owner.id == owner_id).first()
    if not db_owner:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Owner not found",
        )
    return db_owner


@router.put("/{owner_id}", response_model=OwnerInDB)
def update_owner(
    owner_id: int, owner: OwnerUpdate, db: Session = Depends(get_db)
):
    db_owner = db.query(Owner).filter(Owner.id == owner_id).first()
    if not db_owner:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Owner not found",
        )
    for field, value in owner:
        setattr(db_owner, field, value)
    db.commit()
    db.refresh(db_owner)
    return db_owner


@router.delete("/{owner_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_owner(owner_id: int, db: Session = Depends(get_db)):
    db_owner = db.query(Owner).filter(Owner.id == owner_id).first()
    if not db_owner:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Owner not found",
        )
    db.delete(db_owner)
    db.commit()
