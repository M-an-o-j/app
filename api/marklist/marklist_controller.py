from utils.validations import *
from api.marklist.marklist_service import MarklistService

class MarklistController(MarklistService):
    def getAll_marklistController(self,db):
        return super().getAllMarklist_service(db)
