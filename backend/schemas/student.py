from pydantic import BaseModel

class StudentCreate(BaseModel):
    name: str
    email: str
    degree: str
    skills: str
    interests: str
    career_goal: str


class StudentResponse(StudentCreate):
    id: int

    class Config:
        from_attributes = True