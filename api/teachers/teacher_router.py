from configuration.config import *
from fastapi import Depends
from api.teachers.teacher_model import *
from api.teachers.teacher_schema import *
from .teacher_controller import *
from typing import List
from utils.auth_bearer import *

controller = TeacherController()
httpbearer = AdminJWT()

# @router.post("Admin/teacher/register",response_model=TeacherResponse,dependencies = [Depends(httpbearer)], summary="you can get Teachers list here",tags=["Admin"])
# async def get_All_Teacher(teacher:TeacherSignup,Auth_head:str = Depends(get_authorization_header), db: Session = Depends(get_session)):
#     return controller.teacherCreate_controller(db, teacher, Auth_head)

@router.post("/teacher/login",response_model=TeacherResponse,summary="teacher can signin here",tags=["Teacher"])
async def teacher_signin(teacher:TeacherSignin, db: Session = Depends(get_session)):
    return controller.teacherSignin_controller(db, teacher)

@router.post("/teacher/update",response_model=TeacherResponse,dependencies = [Depends(httpbearer)], summary="you can get Teachers list here",tags=["Teacher"])
async def Admin_teacher_Update(teacher:TeacherSignup,Auth_head:str = Depends(get_authorization_header), db: Session = Depends(get_session)):
    return controller.teacherCreate_controller(db, teacher, Auth_head)