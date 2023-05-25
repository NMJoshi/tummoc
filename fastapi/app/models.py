'''For Creating Database Table'''

from sqlalchemy import Column, Integer, String, ForeignKey
from .database import Base
from sqlalchemy.orm import relationship

# Creating DB Models using Base Declarative


class Teacher(Base):
    __tablename__ = 'teacher'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)

    # teacher=relationship("Student",back_populates="student")


class Student(Base):
    __tablename__ = 'student'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    teacher_id = Column(Integer, ForeignKey('teacher.id'))

    student = relationship("Teacher")


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)
