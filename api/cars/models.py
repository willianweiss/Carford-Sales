# models.py
from sqlalchemy import Column, Integer, String

from api.utils.database import Base


class Car(Base):
    __tablename__ = "cars"

    id = Column(Integer, primary_key=True, index=True)
    owner_id = Column(Integer, index=True)
    color = Column(String(50))
    model = Column(String(50))

    class Config:
        orm_mode = True
