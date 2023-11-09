from utils.auth_handler import *
from .teacher_model import *
import datetime
from fastapi.responses import JSONResponse

expiry_del = ACCESS_TOKEN_EXPIRY_MINUTES

class TeacherService:

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

    def teacherSignin_service(self,db, teacher):
        db_teacher = authenticate_user(db,teacher.username, teacher.password, Teacher)
        db_teacher.is_active = True
        access_token = create_access_token(data={"sub": str(db_teacher.id), "teacher":True}, expires_delta=expiry_del)
        db.commit()

        return JSONResponse({
            "name":db_teacher.name,
            "username":db_teacher.username,
            "email":db_teacher.email,
            "access_token":access_token,
            "phone Number":db_teacher.phone_number
        })
