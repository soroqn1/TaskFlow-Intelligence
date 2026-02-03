import httpx
from .celery_app import celery_app
import pandas as pd

@celery_app.task
def parse_users_list():
    response = httpx.get("https://jsonplaceholder.typicode.com/users")
    users = response.json()
    df = pd.DataFrame(users)
    df = df[["id", "name", "username", "email"]]
    df.to_csv("data/users.csv", index=False)

    return "Users parsed successfully"