from configuration.config import *
from fastapi import Depends
from api.students.student_model import *
from utils.auth_bearer import *

httpbearer = AdminJWT()

@router.post("/student/register",dependencies = [Depends(httpbearer)], summary="you can get Teachers list here",tags=["Student"])
async def Admin_student_Register(Auth_head:str = Depends(get_authorization_header), db: Session = Depends(get_session)):
    return 

@router.post("/student/update",dependencies = [Depends(httpbearer)], summary="you can get Teachers list here",tags=["Student"])
async def Admin_Student_Update(Auth_head:str = Depends(get_authorization_header), db: Session = Depends(get_session)):
    return 

@router.post("/student/delete",dependencies = [Depends(httpbearer)], summary="you can get Teachers list here",tags=["Teacher","Admin"])
async def Admin_Student_Delete(Auth_head:str = Depends(get_authorization_header), db: Session = Depends(get_session)):
    return 