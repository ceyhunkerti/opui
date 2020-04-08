import dash_core_components as dcc
import os
from datetime import datetime as dt
import dash
import dash_bootstrap_components as dbc
import dash_html_components as html
from dash.dependencies import Input, Output, State
from components.navbar import navbar

from pages.home import home, bar_chart
from pages.file_upload import file_upload
from pages.home import bar_chart, lp_table
from reader import read
from components.navbar import menu

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])
# app = dash.Dash(external_stylesheets=[dbc.themes.JOURNAL])
# app = dash.Dash(external_stylesheets=[dbc.themes.SKETCHY])

app.config['suppress_callback_exceptions'] = True
app.title = 'DWH'

df = read()

def set_layout():
    global df
    df = read()
    return html.Div([
        dcc.Location(id='url', refresh=False),
        navbar(),
        dbc.Container(id="content", style={"padding": "20px"}, children=[
            home(df)
        ])
    ])

app.layout = set_layout



@app.callback(
    Output("nav-dropdown", "label"),
    [Input('url', 'pathname')]
)
def nav_dropdwon(path_name):
    return menu[path_name[1:]]


@app.callback(Output('bar-chart-container', "children"),
    [Input('url', 'pathname')]
)
def system_click_chart(path_name):
    return bar_chart(df, path_name[1:].upper())


@app.callback(Output('lp-table-container', "children"), [
    Input('url', 'pathname'),
    Input('lp-date-picker', 'date')
])
def system_click_table(path_name, date):
    d = dt.strptime(date[:10], '%Y-%m-%d')
    return lp_table(df, path_name[1:].upper(), d)

debug = os.getenv("OPUI_DEBUG")
if debug == None:
    debug = True
else:
    debug = os.getenv("OPUI_DEBUG") == 'true'

port = os.getenv("OPUI_PORT")

if __name__ == "__main__":
    app.run_server(debug=debug, port=(port or 8888), host='0.0.0.0')