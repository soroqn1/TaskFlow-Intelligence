from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_create_task():
    # make post request to /tasks endpoint
    response = client.post(
        "/tasks",
        json={"title": "Test Task", "description": "Test Desc", "priority": "high"}
    )
    
    # check status code
    assert response.status_code == 200
    
    # check response data
    data = response.json()
    assert data["title"] == "Test Task"
    assert "id" in data