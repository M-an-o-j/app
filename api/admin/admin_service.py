from api.admin.admin_model import *
from api.teachers.teacher_model import *
from utils.auth_handler import *
from fastapi.responses import JSONResponse

expiry_del = ACCESS_TOKEN_EXPIRY_MINUTES

class AdminService:

    def AdminLogin_service(self,db, admin):
        db_admin = authenticate_user(db, admin.username, admin.password, Admin)
        db_admin.is_active = True
        access_token = create_access_token(data={"sub": str(db_admin.id), "admin":True}, expires_delta=expiry_del)
        db.add(db_admin)
        db.commit()
        print(db_admin.is_active)
        return JSONResponse({
            "name":db_admin.name,
            "username":db_admin.username,
            "email":db_admin.email,
            "access_token":access_token,
            "phone Number":db_admin.phone_number
        })

    def AdminLogout_service(self,db,db_admin):
        db_admin.is_active = False
        db.commit()
        return JSONResponse({
            "message":"You're logged out succesfully"
        })
    
    def teacherCreate_service(self,db,teacher):
        hashed_password = hash_password(teacher.password)
        teacher.password = hashed_password
        db_teacher = Teacher(**teacher.dict(), Created_at = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        print(db_teacher)
        db.add(db_teacher)
        db.commit()
        db.refresh(db_teacher)
        return JSONResponse({
            "message":"created successfully"
        })