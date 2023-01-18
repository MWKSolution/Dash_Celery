# Using Dash with Celery + Redis with API calls to FastAPI

## Starting locally


1. Start redis server on docker locally using Dockerfile
2. Start API server

3. Start cellery using command line
```commandline
celery -A dashapp worker --loglevel=INFO -P eventlet
```
use eventlet for Windows  
3. Start dash app