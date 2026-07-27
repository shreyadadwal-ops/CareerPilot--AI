from backend import crud
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from backend.database import SessionLocal
from backend.models.models.student import Student
from backend.schemas.student import StudentCreate, StudentResponse
from backend.services.gemini_service import generate_career_recommendation

router = APIRouter()


# Database Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Profile API
@router.get("/profile")
def get_profile():
    return {
        "message": "Student Profile API Working"
    }


# Create Student API
@router.post("/student", response_model=StudentResponse)
def create_student(student: StudentCreate, db: Session = Depends(get_db)):
    return crud.create_student(db, student)

    


# Get All Students API
@router.get("/students", response_model=list[StudentResponse])
def get_all_students(db: Session = Depends(get_db)):
    return crud.get_students(db)


# Get Student By ID API
@router.get("/student/{student_id}", response_model=StudentResponse)
def get_student(student_id: int, db: Session = Depends(get_db)):
    student = crud.get_student(db, student_id)

    if student is None:
        raise HTTPException(status_code=404, detail="Student not found")

    return student


# Update Student API
@router.put("/student/{student_id}", response_model=StudentResponse)
def update_student(student_id: int, student: StudentCreate, db: Session = Depends(get_db)):
    updated_student = crud.update_student(db, student_id, student)

    if updated_student is None:
        raise HTTPException(status_code=404, detail="Student not found")

    return updated_student


# Delete Student API
@router.delete("/student/{student_id}")
def delete_student(student_id: int, db: Session = Depends(get_db)):
    deleted_student = crud.delete_student(db, student_id)

    if deleted_student is None:
        raise HTTPException(status_code=404, detail="Student not found")

    return {
        "message": "Student deleted successfully"
    }


# AI Career Recommendation API
@router.post("/career-recommendation/{student_id}")
def career_recommendation(student_id: int, db: Session = Depends(get_db)):
    student = db.query(Student).filter(Student.id == student_id).first()

    if student is None:
        raise HTTPException(status_code=404, detail="Student not found")

    recommendation = generate_career_recommendation(student)

    return {
        "student_id": student.id,
        "student_name": student.name,
        "recommendation": recommendation
    }