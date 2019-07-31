from celery_server import hello

if __name__ == "__main__":
    # schedule task
    t = hello.delay(2)

    # check task status
    print t.ready()

    # get task result
    print t.get(timeout=11)
