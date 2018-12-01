# coding = utf-8
from celery import Celery

app = Celery("celery")
app.config_from_object("celery_tasks.config")
app.autodiscover_tasks(["celery_tasks.tasks"])
