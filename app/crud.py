from sqlalchemy.orm import Session
from models import Task
from schemas import TaskCreate, TaskUpdate


def get_tasks(db: Session):
    """
    Input:
        db: database session
    Output:
        List all tasks
    """
    # TODO: El vostre codi va aqui
    pass


def create_tasks(db: Session, task: TaskCreate):
    """
    Input:
        db: database session
    Output:
        Return the new task
    """
    # TODO: El vostre codi va aqui
    pass


def update_tasks(db: Session, task_id: int, task_update: TaskUpdate):
    """
    Input:
        db: database session
    Output:
        Updated some task fields
    """
    # TODO: El vostre codi va aqui
    stmnt = db.query(Task).where(Task.id == task_id)
    pass


def delete_tasks(db: Session, task_id: int):
    """
    Input:
        db: database session
    Output:
        Return delete task
    """
    # TODO: El vostre codi va aqui
    Session.delete(task_id)
