from pydantic import BaseModel


class Register(BaseModel):
    name: str
    email: str
    password: str

class Login(BaseModel):
    name: str
    password: str
