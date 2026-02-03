from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_get_tasks():
    # make get request to /tasks endpoint
    response = client.get("/tasks")
    
    # check status code
    assert response.status_code == 200
    
    # check response data
    data = response.json()
    assert isinstance(data, list)
    assert len(data) >= 0