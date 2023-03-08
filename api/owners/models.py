from sqlalchemy import Column, Integer, String

from api.utils.database import Base


class Owner(Base):
    __tablename__ = "owners"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100))
    email = Column(String(100), unique=True)


class OwnerInDB(Owner):
    class Config:
        orm_mode = True
