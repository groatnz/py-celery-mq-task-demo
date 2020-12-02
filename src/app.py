from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

from tasks.worker import add

# Create the FastAPI app
app = FastAPI()


# Use pydantic to keep track of the input request payload
class Numbers(BaseModel):
    x: float
    y: float


@app.post('/add')
def enqueue_add(n: Numbers):
    print('post /add', n)
    # We use celery delay method in order to enqueue the task with the given parameters
    add.delay(n.x, n.y)


@app.get("/")
def read_root():
    print('get /')
    return {"Hello": "World"}


if __name__ == "__main__":
    print('start uvicorn')
    add.delay(5,6)
    uvicorn.run("app:app", host="127.0.0.1", port=8080, log_level="info")
