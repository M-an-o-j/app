from configuration.config import *
from sqlalchemy import *
from sqlalchemy.orm import relationship

class Admin(Base):
    __tablename__ = "admin"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    phone_number = Column(Integer)
    username = Column(String)
    password = Column(String)
    is_active = Column(Boolean)
    is_deleted = Column(Boolean)
    Created_at = Column(DateTime)
    Created_by = Column(Integer)
    updated_at = Column(Integer)
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
