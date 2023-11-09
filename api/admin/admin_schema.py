from pydantic import BaseModel
from datetime import datetime

class AdminResponse(BaseModel):
    id : int
    name : str
    email : str
    phone_number : str
    access_token : str
    username : str

class AdminLogin(BaseModel):
    username: str = None
    password : str = None

class TeacherResponse(BaseModel):
    id:int
    name:str
    email:str
    phone_number:str
    created_by:datetime

class TeacherSignup(BaseModel):
    name:str
    email:str
    phone_number:str
    username:str
    password:str