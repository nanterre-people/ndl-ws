import uvicorn

from fastapi import Depends
from sqlalchemy.orm import Session

from typing import List

from config import app, get_db
from models import Promotion, User, UserSchema, PromotionSchema, Question, QuestionSchema, QuestionQCM, QuestionQCMSchema



@app.get('/questions', response_model=List['QuestionSchema'])
def get_questions(db: Session = Depends(get_db)):
    questions = db.query(Question).all()
    return questions

@app.get('/questions-qcm', response_model=List['QuestionQCMSchema'])
def get_questionsQCM(db: Session = Depends(get_db)):
    questionQCM = db.query(questionQCM).all()
    return questionQCM


def main():
    uvicorn.run('main:app', host='localhost', port=8000, reload=True)

if __name__ == '__main__':
    main()