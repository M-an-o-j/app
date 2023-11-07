from pydantic import BaseModel
from datetime import datetime

class MarklistResponse(BaseModel):
    id : int
    student_id : int
    subject_id : int
    mark : int
    created_by : int
    created_at : datetime
    updated_by : int
    updated_at : datetime