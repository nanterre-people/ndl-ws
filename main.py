import uvicorn

from fastapi import Depends
from sqlalchemy.orm import Session

from typing import List

from config import app, get_db
from models import User, Question, QuestionQCM


@app.get('/questions', response_model=List[Question])
def get_students(db: Session = Depends(get_db)):
    students = db.query(Student).all()
    return students

def main():
    uvicorn.run('main:app', host='localhost', port=8000, reload=True)

if __name__ == '__main__':
    main()
