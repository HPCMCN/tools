# coding = utf-8
# broker
BROKER_URL = "redis://127.0.0.1/1"
# backend
CELERY_RESULT_BACKEND = "redis://127.0.0.1/2"
# time
CELERY_TIMEZONE = "Asia/Shanghai"
# tasks
CELERY_IMPORTS = [
    "celery_tasks.tasks.sum",
    "celery_tasks.tasks.multiplications",
]
