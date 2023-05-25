from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from .. import schemas, database, models


router = APIRouter(
    prefix="/api/v1/student",
    tags=["Student"]
)


@router.post('/add', response_model=schemas.Student)
def add_student(request: schemas.Student,
                db: Session = Depends(database.get_db)):
    new_student = models.Student(
        name=request.name, email=request.email)
    db.add(new_student)
    db.commit()
    return new_student


@router.put('/{id}/assign-teacher/{teacher_id}')
def add_student(id: int, teacher_id: int,
                db: Session = Depends(database.get_db)):
    student = db.query(models.Student).filter(models.Student.id == id).first()
    teacher = db.query(models.Teacher).filter(
        models.Teacher.id == teacher_id).first()
    if student:
        if teacher:
            student.teacher_id = teacher_id
            db.commit()
            return student
        return f"Teacher With id {teacher_id} is Not in Database!"
    return f"Student With id {id} is Not in Database!"
