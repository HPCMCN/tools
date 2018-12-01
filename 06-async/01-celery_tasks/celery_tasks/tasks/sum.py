# coding = utf-8
from celery_tasks import app


@app.task(name="test1")
def t1(a, b):
    print("worker do...", a, b)
    return a, b
