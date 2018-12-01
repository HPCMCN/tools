# coding = utf-8
from celery_tasks import app


@app.task(name="task_1")
def t2(a, b):
    print("worker do...", a*b)
    return a*b


