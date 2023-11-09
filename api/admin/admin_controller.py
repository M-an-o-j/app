from utils.validations import Validations
from api.admin.admin_service import AdminService
from utils.handlers import *
from utils.auth_handler import *
from api.admin.admin_model import *

class AdminController(Validations, AdminService):

    def adminLogin_controller(self,db, admin):

        if super().None_validation(admin):
            errorhandler(400,"All field is required")
        if super().empty_validation(admin):
            errorhandler(400,"Field's shoudn't be empty")

        return super().AdminLogin_service(db,admin)
    
    def adminLogout_controller(self,db, Auth_head):
        id = decode_token_id(Auth_head)
        db_admin = filter_items(db,Admin,Admin.id,id).first()
        
        if not super().login_validation(db_admin):
            errorhandler(400,"You have to login first")
        
        return super().AdminLogout_service(db,db_admin)
    
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
    
    def teacherUpdate_controller(self,db,teacher,Auth_head):

        if not super().None_validation(teacher.name, teacher.email, teacher.phone_number, teacher.username, teacher.password):
            errorhandler(400, "All field is required")
        if super().empty_validation(teacher):
            errorhandler(400,"Field's shouldn't be empty")
        if not super().email_validations(teacher.email):
            errorhandler(400,"Invalid email")
        if not super().password_validation(teacher.password):
            errorhandler(400,"Invalid password")

        return super().teacherCreate_service(db, teacher)
        