from utils.validations import *
from utils.handlers import *
from .teacher_service import *
from utils.auth_handler import *

class TeacherController(Validations, TeacherService):
    def teacherCreate_controller(self,db,teacher,Auth_head):
        id = decode_token_admin(Auth_head)
        if id != True:
            errorhandler(403,"Admin can only create teacher")
        if not super().None_validation(teacher.name, teacher.email, teacher.phone_number, teacher.username, teacher.password):
            errorhandler(400, "All field is required")
        if super().empty_validation(teacher):
            errorhandler(400,"Field's shouldn't be empty")
        if not super().email_validations(teacher.email):
            errorhandler(400,"Invalid email")
        if not super().password_validation(teacher.password):
            errorhandler(400,"Invalid password")

        return super().teacherCreate_service(db, teacher)
    
    def teacherSignin_controller(self, db, teacher):
        if super().None_validation(teacher.username, teacher.password):
                  return errorhandler(400,"All field is required")
        db_teacher = filter_items(db,Teacher,Teacher.username, teacher.username).first()
            # if user object exist
        if db_teacher:
                  # Validate the user is deleted or not
                if super().User_delete_validation(db_teacher):
                        errorhandler(404, "User not found")
            # validate the empty field
        if super().empty_validation(teacher) == False:
                  errorhandler(400, "Username and password is required")
        return super().teacherSignin_service(db,teacher)