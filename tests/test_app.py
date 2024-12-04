import pytest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'app')))
from app import app

@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_home(client):
    response = client.get("/")
    assert response.status_code == 200
    assert response.data.decode("utf-8") == "Hello this is Task Manager"

def test_add_task(client):
    response = client.post(
        "/tasks",
        json = {"title": "Тестировка приложения"}
    )
    assert response.status_code == 201
    json_data = response.get_json()
    assert json_data["title"] == "Тестировка приложения"
    assert json_data["done"] is False

def test_get_tasks(client):
    response = client.get("/tasks")
    assert response.status_code == 200
    json_data = response.get_json()
    assert isinstance(json_data,list)
    assert len(json_data) >= 1