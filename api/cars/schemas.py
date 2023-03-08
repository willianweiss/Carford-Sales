from typing import Optional

from pydantic import BaseModel


class CarBase(BaseModel):
    owner_id: int
    color: str
    model: str


class CarCreate(CarBase):
    pass


class CarUpdate(CarBase):
    pass


class Car(CarBase):
    id: int

    class Config:
        orm_mode = True


class CarInDB(Car):
    class Config:
        orm_mode = True
