from pydantic import BaseModel, EmailStr
from typing import Optional

#Datos que se envian desde el cliente para crear un usuario
class UserCreate(BaseModel):
    username: str
    email: EmailStr
    full_name: Optional[str] = None
#Datos que devuelve la API
class UserOut(BaseModel):
    id: int
    username: EmailStr
    full_name: Optional[str] = None
    
    #objetos de SQLAlchemy a Pydantic
    class Config: orn_mode = True