from sqlalchemy.orm import Session
from models import Task
from schemas import TaskCreate

def get_tasks(db: Session):
    """
    Input:
        db: database session
    Output:
        List all tasks
    """
    return db.query(Task).all()

def create_tasks(db: Session, task: TaskCreate):
    """
    Input:
        db: database session
        task: TaskCreate schema object
    Output:
        Return the new task
    """
    new_task = Task(**task.dict())
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task

def update_tasks(db: Session, task_id: int, task_update: TaskUpdate):
    """
    Input:
        db: database session
    Output:
        Updated some task fields
    """
    # TODO: El vostre codi va aqui
    pass


def delete_tasks(db: Session, task_id: int):
    """
    Input:
        db: database session
    Output:
        Return delete task
    """
    # TODO: El vostre codi va aqui
    pass
