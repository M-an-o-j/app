from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from fastapi import FastAPI
from sqlalchemy.ext.declarative import declarative_base

DATABASE_URL = "postgresql://postgres:12345@localhost/School_management"

engine = create_engine(DATABASE_URL)

sessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

router = FastAPI(debug=True, title="School Management")

def get_session():
    session = sessionLocal()
    try:
        yield session
    finally:
        session.close()