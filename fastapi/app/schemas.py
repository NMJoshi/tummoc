from pydantic import BaseModel
from typing import List


class AddTeacher(BaseModel):
    name: str
    email: str
    password: str

    class Config():
        orm_mode = True


class Student(BaseModel):
    name: str
    email: str
    # teacher_id: int

    class Config():
        orm_mode = True


class GetTeacher(BaseModel):
    name: str
    email: str

    class Config():
        orm_mode = True


class Coordinates(BaseModel):
    latitude: float
    longitude: float


class Location(BaseModel):
    point1: Coordinates
    point2: Coordinates


class Token(BaseModel):
    access_token: str
    token_type: str


class AddUser(BaseModel):
    name: str
    email: str
    password: str

    class Config():
        orm_mode = True


class GetUser(BaseModel):
    name: str
    email: str

    class Config():
        orm_mode = True
