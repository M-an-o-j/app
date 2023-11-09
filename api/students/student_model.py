from configuration.config import *
from sqlalchemy import *
from sqlalchemy.orm import relationship

class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True, unique=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    phone_number = Column(String, nullable=False, unique=True)
    username = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    Roll_no = Column(Integer, primary_key=True, index=True, nullable=False,unique=True)
    class_teacher_id = Column(Integer, ForeignKey("teachers.id"), nullable=False)
    is_active = Column(Boolean, default=False)
    is_deleted = Column(Boolean,default=False)
    Created_at = Column(DateTime)
    Created_by = Column(Integer)
    updated_at = Column(Integer)
    updated_by = Column(Integer)

    marklist = relationship("Marklist", back_populates="studentId")
    studentSignin = relationship("Student_signin_logs", back_populates="student_Id")
    student_teacher = relationship("Teacher", back_populates="teacher_student")

class Student_signin_logs(Base):
    __tablename__ = "student_signin_logs"

    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, ForeignKey("students.id"))
    Logged_in = Column(DateTime)
    Logged_out = Column(DateTime)

    student_Id = relationship("Student", back_populates="studentSignin")

