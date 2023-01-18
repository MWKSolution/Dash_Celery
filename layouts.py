from dash import html

layout = html.Div([html.Div([html.P(id="paragraph_id", children=["Button not clicked"])]),
                   html.Button(id="button_id", children="Run Job!"),
                   html.Button(id="cancel_button_id", children="Cancel Running Job!"), ])