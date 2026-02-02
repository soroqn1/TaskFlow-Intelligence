from src.models.task import Task, TaskCreate, TaskUpdate

class TaskService:
    def __init__(self):
        self.tasks: dict[int, Task] = {}
        self.current_id = 0
        
    def get_all(self):
        return list(self.tasks.values())

    def get_by_id(self, task_id:int):
        return self.tasks.get(task_id)

    def create_task(self, task: TaskCreate):
        self.current_id += 1

        new_task = Task(id = self.current_id, **task.model_dump())

        self.tasks[self.current_id] = new_task
        return new_task

    def update_task(self, task_id: int, task_update: TaskUpdate):
        task = self.get_by_id(task_id)
        if not task:
            return None
    
        update_data = task_update.model_dump(exclude_unset=True)
        for key, value in update_data.items():
            setattr(task, key, value)
        return task
        
    def delete_task(self, task_id: int):
        if task_id in self.tasks:
            del self.tasks[task_id]
            return True
        return False
        