from sqlalchemy.orm import Session
from backend.models.models.student import Student
from backend.schemas.student import StudentCreate


def create_student(db: Session, student: StudentCreate):
    db_student = Student(
        name=student.name,
        email=student.email,
        degree=student.degree,
        skills=student.skills,
        interests=student.interests,
        career_goal=student.career_goal,
    )

    db.add(db_student)
    db.commit()
    db.refresh(db_student)

    return db_student


def get_students(db: Session):
    return db.query(Student).all()


def get_student(db: Session, student_id: int):
    return db.query(Student).filter(Student.id == student_id).first()


def update_student(db: Session, student_id: int, student: StudentCreate):
    db_student = db.query(Student).filter(Student.id == student_id).first()

    if db_student is None:
        return None

    db_student.name = student.name
    db_student.email = student.email
    db_student.degree = student.degree
    db_student.skills = student.skills
    db_student.interests = student.interests
    db_student.career_goal = student.career_goal

    db.commit()
    db.refresh(db_student)

    return db_student


def delete_student(db: Session, student_id: int):
    db_student = db.query(Student).filter(Student.id == student_id).first()

    if db_student is None:
        return None

    db.delete(db_student)
    db.commit()

    return db_student