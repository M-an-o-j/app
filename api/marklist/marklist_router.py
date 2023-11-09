from configuration.config import *
from fastapi import Depends
from api.marklist.marklist_model import *
from typing import List
from api.marklist.marklist_schema import *
from api.marklist.marklist_controller import MarklistController

controller = MarklistController()

@router.get("/marklists/",response_model=List[MarklistResponse], summary="you can get all students marksheets here",tags=["Marklist"])
async def get_All_Blog(db: Session = Depends(get_session)):
    return controller.getAll_marklistController(db)

@router.get("/marklist/{id}", summary="you can get single marksheet here",tags=["Marklist"])
async def get_All_Blog(db: Session = Depends(get_session)):
    return 

@router.get("/marklist/student/{student_id}", summary="you can get all blogs here",tags=["Marklist"])
async def get_All_Blog(db: Session = Depends(get_session)):
    return 

@router.get("/marklist/teacher/{teacher_id}", summary="you can get all blogs here",tags=["Marklist"])
async def get_All_Blog(db: Session = Depends(get_session)):
    return 

@router.post("/marklist/create", summary="you can get all blogs here",tags=["Teacher","Admin"])
async def get_All_Blog(db: Session = Depends(get_session)):
    return 

@router.put("/marklist/update/{id}", summary="you can get all blogs here",tags=["Teacher","Admin"])
async def get_All_Blog(db: Session = Depends(get_session)):
    return 

@router.delete("/marklist/delete/{id}", summary="you can get all blogs here",tags=["Teacher","Admin"])
async def get_All_Blog(db: Session = Depends(get_session)):
    return 