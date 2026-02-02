from fastapi import FastAPI, HTTPException
from src.models.task import Task, TaskCreate, TaskUpdate
from src.services.task_service import TaskService

app = FastAPI(title="TaskFlow Intelligence")
service = TaskService()

@app.get("/tasks", 
response_model=list[Task])
async def get_tasks():
    return service.get_all_tasks()

@app.post("/tasks", 
response_model=Task)
async def create_task(task: TaskCreate):
    return service.create_task(task)

@app.put("/tasks/{id}", 
response_model=Task)
async def update_task(id: int, task: TaskUpdate):
    return service.update_task(id, task)

@app.delete("/tasks/{id}", 
response_model=Task)
async def delete_task(id: int):
    return service.delete_task(id)
