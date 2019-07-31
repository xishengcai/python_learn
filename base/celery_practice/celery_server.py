from celery import Celery
from celery.schedules import crontab
from datetime import timedelta
import time
import os

"""
usage:
    start server
    celery -A celery_practice worker -l info or  celery -A celery_practice:app worker -l info

    start producer:
    from tasks import hello
    t= hello.delay()
    t.get() 

"""

broker = 'redis://localhost:30010/2'
backend = 'redis://localhost:30010/2'

app = Celery('tasks', broker=broker, backend=backend)

# Optional configuration, see the application user guide.
app.conf.update(
    result_expires=3600,
)
app.conf.CELERY_TIMEZONE = 'Asia/Shanghai'


app.conf.CELERYBEAT_SCHEDULE = {
    'add every 10 second': {
        'task': 'celery_practice.add',
        'schedule': timedelta(seconds=10),
        'args': (1, 2)
    },
    'upper every 2 minutes': {
        'task': 'celery_practice.upper',
        'schedule': crontab(minute='*/2'),
        'args': ('abc',),
    },
}


@app.task
def add(x, y):
    print("compute two num sum : %s %s" % (x, y))
    return x+y


@app.task
def upper(v):
    for i in range(10):
        time.sleep(1)
        print(i)
    return v.upper()


@app.task
def hello(seconds_):
    time.sleep(seconds_)
    return "hello world"


if __name__ == "__main__":
    os.system("celery -A celery_server worker -l info")


