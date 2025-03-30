from fastapi.testclient import TestClient
from app.main import app
from app.crud import create_tasks, get_tasks, update_tasks, delete_tasks


client = TestClient(app)

# TODO: els vostres test venen aqui
def test_create_tasks():
    # Datos de ejemplo para crear una tarea
    task_data = {
        "title": "Test Task",
        "description": "This is a test task",
        "completed": False
    }

    # Realizar una solicitud POST al endpoint de creación de tareas
    response = client.post("/tasks/", json=task_data)

    # Verificar que la respuesta tenga un código de estado 201 (creado)
    assert response.status_code == 201

    # Verificar que los datos de la respuesta coincidan con los datos enviados
    response_data = response.json()
    assert response_data["title"] == task_data["title"]
    assert response_data["description"] == task_data["description"]
    assert response_data["completed"] == task_data["completed"]

    # Verificar que se haya generado un ID para la tarea
    assert "id" in response_data

def test_get_tasks():
    # Realizar una solicitud GET al endpoint de obtención de tareas
    response = client.get("/tasks/")

    # Verificar que la respuesta tenga un código de estado 200 (OK)
    assert response.status_code == 200

    # Verificar que la respuesta contenga una lista de tareas
    response_data = response.json()
    assert isinstance(response_data, list)
