from api.marklist.marklist_model import Marklist
from utils.handlers import *

class MarklistService:
    def getAllMarklist_service(self,db):
        try:
            db_mklist = db.query(Marklist).all()
            return db_mklist
        except Exception as e:
            errorhandler(400, f"{e}")