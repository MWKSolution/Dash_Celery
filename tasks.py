from dash.dependencies import Input, Output
from requests import get


def get_tasks(app, url):

    @app.long_callback(
        output=Output("paragraph_id", "children"),
        inputs=Input("button_id", "n_clicks"),
        running=[(Output("button_id", "disabled"), True, False),
                 (Output("cancel_button_id", "disabled"), False, True), ],
        cancel=Input("cancel_button_id", "n_clicks"))
    def call_api(n_clicks):
        print('Task started')
        params = {'msg': 'some text'}
        r = get(url, params=params)
        print('Task ended')
        return [f"Clicked {n_clicks} times"]

