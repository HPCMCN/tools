# coding = utf-8
import time
import os
import sys

sys.path.append(os.path.abspath(os.path.dirname(os.getcwd())))
from celery_tasks.tasks import *


if __name__ == '__main__':
    result = t1.delay(1, 2)
    while True:
        time.sleep(1)
        if result.ready():
            print(result.get())
            break
