from pydantic import BaseModel

class User(BaseModel):
    name: str
    email: str
    phone_no: int
    password: str

