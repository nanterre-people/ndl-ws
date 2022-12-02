from typing import List
from pydantic import BaseModel
from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

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

    __mapper_args__ = {
        "polymorphic_identity": "question",
    }

class QuestionQCM(Question):
    __tablename__ = "questions_qcm"
    id = Column(Integer, ForeignKey("questions.id"), primary_key=True)
    answer1 = Column(String)
    result1 = Column(Boolean)
    answer2 = Column(String)
    result2 = Column(Boolean)
    answer3 = Column(String)
    result3 = Column(Boolean)
    answer4 = Column(String)
    result4 = Column(Boolean)

    __mapper_args__ = {
        "polymorphic_identity": "question_qcm",
    }
