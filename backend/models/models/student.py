from sqlalchemy import Column, Integer, String
from backend.database import Base

class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    degree = Column(String)
    skills = Column(String)
    interests = Column(String)
    career_goal = Column(String)