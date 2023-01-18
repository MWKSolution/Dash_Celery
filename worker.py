from celery import Celery
from requests import get

LOCAL_FAPI = 'http://127.0.0.1/8888'

capp = Celery('worker',
                broker="redis://192.168.99.100:6379/0",
                backend="redis://192.168.99.100:6379/1")


@capp.task(name='addTask')  # Named task
def call_api(msg):
    print('Task started')
    params = {'msg': msg}
    r = get(LOCAL_FAPI, params=params)
    print('Task ended')
    return r.text


if __name__ == '__main__':
    w = capp.worker_main(argv=['-A', 'worker', 'worker', '--loglevel=INFO', '-P', 'eventlet'])
    w.start()
