import time
import dash
from dash import html
from dash.long_callback import CeleryLongCallbackManager
from dash.dependencies import Input, Output
from worker import capp, call_api


long_callback_manager = CeleryLongCallbackManager(capp)

app = dash.Dash('dashapp',
                long_callback_manager=long_callback_manager,
                prevent_initial_callbacks=True)

app.layout = html.Div([html.Div([html.P(id="paragraph_id", children=["Button not clicked"])]),
                       html.Button(id="button_id", children="Run Job!"),
                       html.Button(id="cancel_button_id", children="Cancel Running Job!"), ])


@app.long_callback(
    output=Output("paragraph_id", "children"),
    inputs=Input("button_id", "n_clicks"),
    running=[(Output("button_id", "disabled"), True, False),
             (Output("cancel_button_id", "disabled"), False, True), ],
    cancel=Input("cancel_button_id", "n_clicks"))
def callback(n_clicks):
    task = call_api('some text')
    return [f"Clicked {n_clicks} times"]


if __name__ == "__main__":
    app.run_server(debug=True)