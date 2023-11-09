from configuration.config import *
from sqlalchemy import Integer, DateTime, Column, ForeignKey
from sqlalchemy.orm import relationship

class Marklist(Base):
    __tablename__ = "marklist"

    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, ForeignKey("students.id"), nullable=False)
    subject_id = Column(Integer, nullable=False)
    mark = Column(Integer, nullable=False)
    created_by = Column(Integer, ForeignKey("teachers.id"))
    created_at = Column(DateTime)
    updated_by = Column(Integer)
    updated_at = Column(DateTime)

    studentId = relationship("Student", back_populates="marklist")
    marklist_teacher = relationship("Teacher", back_populates="teacher_marklist")