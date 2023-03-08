from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from api.auth.auth_bearer import JWTBearer
from ..utils.database import get_db
from .models import Car
from .schemas import CarCreate, CarInDB, CarUpdate

router = APIRouter(prefix="/cars", tags=["cars"], dependencies=[Depends(JWTBearer())])


@router.post("/", response_model=CarInDB)
def create_car(car: CarCreate, db: Session = Depends(get_db)):
    db_car = Car(**car.dict())
    db.add(db_car)
    db.commit()
    db.refresh(db_car)
    return db_car


@router.get("/{car_id}", response_model=CarInDB)
def read_car(car_id: int, db: Session = Depends(get_db)):
    db_car = db.query(Car).filter(Car.id == car_id).first()
    if not db_car:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Car not found",
        )
    return db_car


@router.put("/{car_id}", response_model=CarInDB)
def update_car(car_id: int, car: CarUpdate, db: Session = Depends(get_db)):
    db_car = db.query(Car).filter(Car.id == car_id).first()
    if not db_car:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Car not found",
        )
    for field, value in car:
        setattr(db_car, field, value)
    db.commit()
    db.refresh(db_car)
    return db_car


@router.delete("/{car_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_car(car_id: int, db: Session = Depends(get_db)):
    db_car = db.query(Car).filter(Car.id == car_id).first()
    if not db_car:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Car not found",
        )
    db.delete(db_car)
    db.commit()
