from configuration.config import *
from sqlalchemy import *
from sqlalchemy.orm import relationship

class Admin(Base):
    __tablename__ = "admin"

    id = Column(Integer, primary_key=True, index=True, nullable=False)
    name = Column(String,nullable=False)
    email = Column(String,nullable=False, unique=True)
    phone_number = Column(String,nullable=False, unique=True)
    username = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    is_active = Column(Boolean, default=False)
    is_deleted = Column(Boolean, default=False)
    Created_at = Column(DateTime)
    Created_by = Column(Integer)
    updated_at = Column(DateTime)
    updated_by = Column(Integer)

    admin_teacher = relationship("Teacher", back_populates="teacher_admin")
    signin_admin = relationship("Admin_signin_logs", back_populates="admin_signin")

class Admin_signin_logs(Base):
    __tablename__ = "admin_signin_logs"

    id = Column(Integer, primary_key=True, index=True)
    admin_id = Column(Integer, ForeignKey("admin.id"))
    Logged_in = Column(DateTime)
    Logged_out = Column(DateTime)

    admin_signin = relationship("Admin", back_populates="signin_admin")
