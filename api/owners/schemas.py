from pydantic import BaseModel


class OwnerBase(BaseModel):
    name: str
    email: str


class OwnerCreate(OwnerBase):
    pass


class OwnerUpdate(OwnerBase):
    pass


class Owner(OwnerBase):
    id: int

    class Config:
        orm_mode = True


class OwnerInDB(Owner):
    class Config:
        orm_mode = True
