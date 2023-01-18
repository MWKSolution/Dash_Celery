import dash
from celery import Celery
from dash.long_callback import CeleryLongCallbackManager
from layouts import layout
from tasks import get_tasks

API_URL = 'http://127.0.0.1:8888'

app = Celery('worker',
             broker="redis://192.168.99.100:6379/0",
             backend="redis://192.168.99.100:6379/1")

long_callback_manager = CeleryLongCallbackManager(app)

dash_app = dash.Dash('dashapp',
                     long_callback_manager=long_callback_manager,
                     prevent_initial_callbacks=True)

dash_app.layout = layout

get_tasks(dash_app, API_URL)


if __name__ == "__main__":
    dash_app.run_server(debug=True)
