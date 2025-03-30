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
        Updated task object or None if task not found
    """
    task_to_update = db.get(Task, task_id)
    if not task_to_update:
        return None  # Task not found

    # Update the fields of the task
    for key, value in task_update.model_dump(exclude_unset=True).items():
        setattr(task_to_update, key, value)

    db.commit()
    db.refresh(task_to_update)
    return task_to_update


def delete_tasks(db: Session, task_id: int):
    """
    Input:
        db: database session
        task_id: ID of the task to delete
    Output:
        True if the task was deleted, False if not found
    """
    task_to_delete = db.get(Task, task_id)
    if not task_to_delete:
        return False  # Task not found

    db.delete(task_to_delete)
    db.commit()
    return True
