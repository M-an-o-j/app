from api.admin.admin_router import *
from api.teachers.teacher_router import *
from api.students.student_router import *
from api.marklist.marklist_router import *
from configuration.config import *
import uvicorn

Base.metadata.create_all(bind=engine)
router.mount('/api/v1', router )

if __name__ == '__main__':
    uvicorn.run("main:router", host="localhost",port=5003, reload=True)