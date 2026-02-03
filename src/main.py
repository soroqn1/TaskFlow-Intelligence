from fastapi import FastAPI, HTTPException
from src.models.task import Task, TaskCreate, TaskUpdate
from src.services.task_service import TaskService
from src.worker.tasks import parse_users_list
from src.ml.predictor import predict_priority

app = FastAPI(title="TaskFlow Intelligence")
service = TaskService()

@app.get("/tasks", 
response_model=list[Task])
async def get_tasks():
    result = service.get_all()
    return result

@app.post("/tasks", 
response_model=Task)
async def create_task(task: TaskCreate):
    result = service.create_task(task)
    if not result:
        raise HTTPException(status_code=404, detail="Task not found")
    return result

@app.put("/tasks/{id}", 
response_model=Task)
async def update_task(id: int, task: TaskUpdate):
    result = service.update_task(id, task)
    if not result:
        raise HTTPException(status_code=404, detail="Task not found")
    return result

@app.delete("/tasks/{id}")
async def delete_task(id: int):
    result = service.delete_task(id)
    if not result:
        raise HTTPException(status_code=404, detail="Task not found")
    return {"message": "Task deleted successfully"}

@app.post("/tasks/parse-users-list")
async def app_parse_users_list():
    result = parse_users_list.delay()
    return {"task_id": result.id, "status": "Task sent to worker"}

@app.post("/predict")
async def app_predict_priority(description: str):
    result = predict_priority(description)
    return {"priority": result}