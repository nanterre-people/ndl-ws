import uvicorn

from fastapi import Depends
from sqlalchemy.orm import Session

from typing import List

from config import app, get_db
from models import User, UserSchema, Question, QuestionSchema, QuestionQCM, QuestionQCMSchema



@app.get('/questions', response_model=List[QuestionSchema])
def get_questions(db: Session = Depends(get_db)):
    """Get all questions

    Args:
        db (Session, optional): Database session. Defaults to Depends(get_db).

    Returns:
        List[QuestionSchema]: List of questions
    """

    questions = db.query(Question).all()
    return questions

@app.get('/questions-qcm', response_model=List[QuestionQCMSchema])
def get_questionsQCM(db: Session = Depends(get_db)):
    """Get all questions QCM

    Args:
        db (Session, optional): Database session. Defaults to Depends(get_db).

    Returns:
        List[QuestionSchema]: List of questions
    """

    questionQCM = db.query(QuestionQCM).all()
    return questionQCM

#crud types for Question
@app.post('/questions', response_model=QuestionSchema)
def create_question(question: QuestionSchema, db: Session = Depends(get_db)):
    """Create a question

    Args:
        question (QuestionSchema): Question to create
        db (Session, optional): Database session. Defaults to Depends(get_db).

    Returns:
        QuestionSchema: Created question

    How to use:
        curl -X POST -H "Content-Type: application/json" -d '{"question": "What is the capital of France?", "answer": "Paris", "owner_id": 1}' http://localhost:8000/questions
    """

    db_question = Question(**question.dict())
    db.add(db_question)
    db.commit()
    db.refresh(db_question)
    return db_question

@app.get('/questions/{question_id}', response_model=QuestionSchema)
def get_question(question_id: int, db: Session = Depends(get_db)):
    """Get a question

    Args:
        question_id (int): Question id
        db (Session, optional): Database session. Defaults to Depends(get_db).

    Returns:
        QuestionSchema: Question
    """

    question = db.query(Question).filter(Question.id == question_id).first()
    return question

@app.put('/questions/{question_id}', response_model=QuestionSchema)
def update_question(question_id: int, question: QuestionSchema, db: Session = Depends(get_db)):
    """Update a question

    Args:
        question_id (int): Question id
        question (QuestionSchema): Question to update
        db (Session, optional): Database session. Defaults to Depends(get_db).

    Returns:
        QuestionSchema: Updated question
    """

    db_question = db.query(Question).filter(Question.id == question_id).first()
    db_question.question = question.question
    db_question.answer = question.answer
    db_question.owner_id = question.owner_id
    db_question.owner = question.owner
    db.commit()
    db.refresh(db_question)
    return db_question

@app.delete('/questions/{question_id}')
def delete_question(question_id: int, db: Session = Depends(get_db)):
    """Delete a question

    Args:
        question_id (int): Question id
        db (Session, optional): Database session. Defaults to Depends(get_db).
    """

    db.query(Question).filter(Question.id == question_id).delete()
    db.commit()

#crud types for QuestionQCM
@app.post('/questions-qcm', response_model=QuestionQCMSchema)
def create_questionQCM(questionQCM: QuestionQCMSchema, db: Session = Depends(get_db)):
    """Create a question

    Args:
        question (QuestionSchema): Question to create
        db (Session, optional): Database session. Defaults to Depends(get_db).

    Returns:
        QuestionSchema: Created question
    """

    db_questionQCM = QuestionQCM(**questionQCM.dict())
    db.add(db_questionQCM)
    db.commit()
    db.refresh(db_questionQCM)
    return db_questionQCM

@app.get('/questions-qcm/{question_id}', response_model=QuestionQCMSchema)
def get_questionQCM(question_id: int, db: Session = Depends(get_db)):
    """Get a question

    Args:
        question_id (int): Question id
        db (Session, optional): Database session. Defaults to Depends(get_db).

    Returns:
        QuestionSchema: Question
    """

    questionQCM = db.query(QuestionQCM).filter(QuestionQCM.id == question_id).first()
    return questionQCM

@app.put('/questions-qcm/{question_id}', response_model=QuestionQCMSchema)
def update_questionQCM(question_id: int, questionQCM: QuestionQCMSchema, db: Session = Depends(get_db)):
    """Update a question

    Args:
        question_id (int): Question id
        question (QuestionSchema): Question to update
        db (Session, optional): Database session. Defaults to Depends(get_db).

    Returns:
        QuestionSchema: Updated question
    """

    db_questionQCM = db.query(QuestionQCM).filter(QuestionQCM.id == question_id).first()
    db_questionQCM.question = questionQCM.question
    db_questionQCM.answer = questionQCM.answer
    db_questionQCM.owner_id = questionQCM.owner_id
    db_questionQCM.owner = questionQCM.owner
    db.commit()
    db.refresh(db_questionQCM)
    return db_questionQCM

@app.delete('/questions-qcm/{question_id}')
def delete_questionQCM(question_id: int, db: Session = Depends(get_db)):
    """Delete a question

    Args:
        question_id (int): Question id
        db (Session, optional): Database session. Defaults to Depends(get_db).
    """

    db.query(QuestionQCM).filter(QuestionQCM.id == question_id).delete()
    db.commit()




def main():
    uvicorn.run('main:app', host='localhost', port=8000, reload=True)

if __name__ == '__main__':
    main()
