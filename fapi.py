import time
from fastapi import FastAPI
import uvicorn


app = FastAPI()


@app.get('/')
def root(msg: str):
    time.sleep(5)
    return {'message': 'API: ' + msg}


if __name__ == '__main__':
    uvicorn.run('fapi:app', host='127.0.0.1', port=8888, log_level='debug')
