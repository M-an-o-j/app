from pydantic import BaseModel
from datetime import datetime

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

class TeacherSignin(BaseModel):
    username:str
    password:str