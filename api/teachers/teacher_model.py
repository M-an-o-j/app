from configuration.config import *
from sqlalchemy import *
from sqlalchemy.orm import relationship

class Teacher(Base):
    __tablename__ = "teachers"

    id = Column(Integer, primary_key=True, index=True, unique=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    phone_number = Column(String, nullable=False, unique=True)
    username = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    is_active = Column(Boolean, default=False)
    is_deleted = Column(Boolean,default=False)
    Created_at = Column(DateTime)
    Created_by = Column(Integer, ForeignKey("admin.id"))
    updated_at = Column(Integer)
    updated_by = Column(Integer)

    teacher_student = relationship("Student", back_populates="student_teacher")
    teacher_signin = relationship("Teacher_signin_logs", back_populates="teacher") # sign
    teacher_admin = relationship("Admin", back_populates="admin_teacher")
    teacher_marklist = relationship("Marklist", back_populates="marklist_teacher")

class Teacher_signin_logs(Base):
    __tablename__ = "teacher_signin_logs"

    id = Column(Integer, primary_key=True, index=True)
    teacher_id = Column(Integer, ForeignKey("teachers.id"))
    Logged_in = Column(DateTime)
    Logged_out = Column(DateTime)

    teacher = relationship("Teacher", back_populates="teacher_signin")
