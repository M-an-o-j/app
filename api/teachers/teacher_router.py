from configuration.config import *
from fastapi import Depends
from api.teachers.teacher_model import *

@router.get("/blogs/", summary="you can get all blogs here",tags=["Blogs"])
async def get_All_Blog(db: Session = Depends(get_session)):
    return 