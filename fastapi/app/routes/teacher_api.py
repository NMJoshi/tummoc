from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from .. import schemas, database, models


router = APIRouter(
    prefix="/api/v1/teacher",
    tags=["Teacher"]
)

# Create


@router.post('/add', response_model=schemas.GetTeacher, status_code=status.HTTP_201_CREATED)
def add_teacher(request: schemas.AddTeacher,
                db: Session = Depends(database.get_db)):
    new_teacher = models.Teacher(
        name=request.name, email=request.email, password=request.password)
    db.add(new_teacher)
    db.commit()
    return new_teacher

# Read


@router.get('/{id}', response_model=schemas.GetTeacher, status_code=status.HTTP_200_OK)
def get_teacher(id: int, db: Session = Depends(database.get_db)):
    teacher = db.query(models.Teacher).filter(models.Teacher.id == id).first()
    if teacher:
        return teacher
    return f"Teacher With id {id} is Not in Database!"

# Update


@router.put('/update/{id}', status_code=status.HTTP_202_ACCEPTED)
def update_teacher(id: int,
                   request: schemas.AddTeacher,
                   db: Session = Depends(database.get_db)):
    teacher = db.query(models.Teacher).filter(models.Teacher.id == id).first()
    if teacher:
        teacher.update(
            {
                'name': request.name,
                'email': request.email,
                'password': request.password
            }
        )
        db.commit()
        return f"Data of id {id} Updated!"
    return f"Blog With id {id} is Not in Database!"

# Delete


@router.delete('/delete/{id}', status_code=status.HTTP_202_ACCEPTED)
def remove_teacher(id: int, db: Session = Depends(database.get_db)):
    teacher = db.query(models.Teacher).filter(models.Teacher.id == id).first()
    if not teacher:
        return f"Blog With id {id} is Not in Database!"
    db.delete(teacher)
    db.commit()
    return f"Teacher with {id} Deleted!"
