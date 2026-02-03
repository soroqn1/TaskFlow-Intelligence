import httpx
from .celery_app import celery_app
from pandas import pd

@celery_app.task
def parce_users_list():
    response = httpx.get("https://jsonplaceholder.typicode.com/users")
    users = response.json()
    df = pd.DataFrame(users)
    df = df[["id", "name", "username", "email"]]
    df.to_csv("users.csv", index=False)

    return "Users parsed successfully"