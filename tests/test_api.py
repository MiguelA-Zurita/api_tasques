import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Task
from schemas import TaskCreate, TaskUpdate
from services import get_tasks, create_tasks, update_tasks, delete_tasks

# Configuración para la base de datos en memoria
SQLALCHEMY_DATABASE_URL = "sqlite:///:memory:"

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Crear tablas
Base.metadata.create_all(bind=engine)

@pytest.fixture()
def db():
    # Crear sesión de base de datos
    db = SessionLocal()
    yield db
    db.close()

def test_get_tasks(db):
    # Insertamos algunos datos de prueba
    task_1 = Task(title="Task 1", description="Test Task 1")
    task_2 = Task(title="Task 2", description="Test Task 2")
    db.add(task_1)
    db.add(task_2)
    db.commit()
    db.refresh(task_1)
    db.refresh(task_2)

    # Llamamos a la función get_tasks
    tasks = get_tasks(db)

    # Verificamos que los resultados sean los correctos
    assert len(tasks) == 2
    assert tasks[0].title == "Task 1"
    assert tasks[1].title == "Task 2"

def test_create_tasks(db):
    # Creamos un nuevo TaskCreate con datos de prueba
    task_create = TaskCreate(title="New Task", description="A test task")

    # Llamamos a la función create_tasks
    new_task = create_tasks(db, task_create)

    # Verificamos que el task se haya creado correctamente
    assert new_task.title == "New Task"
    assert new_task.description == "A test task"
    assert new_task.id is not None  # El ID debe ser generado

def test_update_tasks(db):
    # Insertamos un task de prueba
    task = Task(title="Old Task", description="Old Description")
    db.add(task)
    db.commit()
    db.refresh(task)

    # Creamos el esquema de actualización
    task_update = TaskUpdate(title="Updated Task", description="Updated Description")

    # Llamamos a la función update_tasks
    updated_task = update_tasks(db, task.id, task_update)

    # Verificamos que el task haya sido actualizado correctamente
    assert updated_task.title == "Updated Task"
    assert updated_task.description == "Updated Description"

def test_delete_tasks(db):
    # Insertamos un task de prueba
    task = Task(title="Task to Delete", description="This task will be deleted")
    db.add(task)
    db.commit()
    db.refresh(task)

    # Llamamos a la función delete_tasks
    deleted_task = delete_tasks(db, task.id)

    # Verificamos que el task haya sido eliminado correctamente
    assert deleted_task is not None
    assert deleted_task.title == "Task to Delete"

    # Verificamos que el task ya no exista en la base de datos
    task_in_db = db.query(Task).filter(Task.id == task.id).first()
    assert task_in_db is None