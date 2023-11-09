from configuration.config import *
from fastapi import Depends
from api.admin.admin_schema import *
from api.admin.admin_controller import AdminController
from utils.auth_bearer import *

controller = AdminController()
httpbearer = AdminJWT()

@router.post("/Admin/login",response_model=AdminResponse, summary="Admin can login here",tags=["Admin"])
async def Admin_Login(admin:AdminLogin,db: Session = Depends(get_session)):
    return  controller.adminLogin_controller(db, admin)

@router.post("/Admin/logout",dependencies = [Depends(httpbearer)], summary="Admin can logout here",tags=["Admin"])
async def Admin_Logout(Auth_head:str = Depends(get_authorization_header),db: Session = Depends(get_session)):
    return controller.adminLogout_controller(db, Auth_head)

@router.post("/Admin/teacher/register",response_model=TeacherResponse,dependencies = [Depends(httpbearer)], summary="you can get Teachers list here",tags=["Admin"])
async def Admin_teacher_Register(teacher:TeacherSignup,Auth_head:str = Depends(get_authorization_header), db: Session = Depends(get_session)):
    return controller.teacherCreate_controller(db, teacher, Auth_head)

@router.post("/Admin/teacher/delete",response_model=TeacherResponse,dependencies = [Depends(httpbearer)], summary="you can get Teachers list here",tags=["Admin"])
async def Admin_teacher_Delete(teacher:TeacherSignup,Auth_head:str = Depends(get_authorization_header), db: Session = Depends(get_session)):
    return controller.teacherCreate_controller(db, teacher, Auth_head)

