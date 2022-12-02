from typing import List
from pydantic import BaseModel
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Student(Base):
    __tablename__ = "students"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)


class Promotion(Base):
    __tablename__ = "promotions"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    students = relationship("Student", back_populates="promotion")


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    questions = relationship("Question", back_populates="owner")
    admin = Column(Integer, default=0)


class Question(Base):
    __tablename__ = "questions"
    id = Column(Integer, primary_key=True, index=True)
    question = Column(String)
    answer = Column(String)
    owner_id = Column(Integer, ForeignKey("users.id"))
    owner = relationship("User", back_populates="QuestionQCM")

    mapper_args = {
        "polymorphic_identity": "question",
    }


class QuestionQCM(Question):
    __tablename__ = "questions_qcm"
    id = Column(Integer, ForeignKey("questions.id"), primary_key=True)
    answer1 = Column(String)
    result1 = Column(Integer)
    answer2 = Column(String)
    result2 = Column(Integer)
    answer3 = Column(String)
    result3 = Column(Integer)
    answer4 = Column(String)
    result4 = Column(Integer)

    mapper_args = {
        "polymorphic_identity": "question_qcm",
    }

    class Config:
        orm_mode = True


class StudentSchema(BaseModel):
    name: str
    email: str
    password: str


class PromotionSchema(BaseModel):
    name: str
    students: List["StudentSchema"] = []


class QuestionSchema(BaseModel):
    question: str
    answer: str
    owner_id: int
    owner: "UserSchema"


class UserSchema(BaseModel):
    username: str
    email: str
    hashed_password: str
    questions: List["QuestionSchema"] = []
    admin: int


class QuestionQCMSchema(BaseModel):
    answer1: str
    result1: int
    answer2: str
    result2: int
    answer3: str
    result3: int
    answer4: str
    result4: int

    class Config:
        orm_mode = True
