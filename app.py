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

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])
# app = dash.Dash(external_stylesheets=[dbc.themes.JOURNAL])
# app = dash.Dash(external_stylesheets=[dbc.themes.SKETCHY])

app.config['suppress_callback_exceptions'] = True
app.title = 'DWH'

app.layout = html.Div([
    navbar,
    dbc.Container(id="content", style={"padding": "20px"}, children=[
        home
    ])
])

nav_clicks = {
    'aedas': 0, 'bedas': 0, 'cedas': 0,
    'akepsas': 0, 'bepsas': 0, 'cepesas': 0
}
@app.callback(
    Output("nav-dropdown", "label"),
    [
        Input("ndd-aedas", "n_clicks"),
        Input("ndd-bedas", "n_clicks"),
        Input("ndd-cedas", "n_clicks"),
        Input("ndd-akepsas", "n_clicks"),
        Input("ndd-bepsas", "n_clicks"),
        Input("ndd-cepesas", "n_clicks")
    ]
)
def nav_dropdwon(aedas, bedas, cedas, akepsas, bepsas, cepesas):

    if aedas and aedas > nav_clicks['aedas']: nav_clicks['aedas'] = aedas; return "AEDAS"
    if bedas and bedas > nav_clicks['bedas']: nav_clicks['bedas'] = bedas; return "BEDAS"
    if cedas and cedas > nav_clicks['cedas']: nav_clicks['cedas'] = cedas; return "CEDAS"
    if akepsas and akepsas > nav_clicks['akepsas']: nav_clicks['akepsas'] = akepsas; return "AKEPSAS"
    if bepsas and bepsas > nav_clicks['bepsas']: nav_clicks['bepsas'] = bepsas; return "BEPSAS"
    if cepesas and cepesas > nav_clicks['cepesas']: nav_clicks['cepesas'] = cepesas; return "CEPESAS"
    return "BEDAS"


current_system='BEDAS'
@app.callback(Output('bar-chart-container', "children"), [Input("nav-dropdown", "label")])
def system_click_chart(val):
    current_system = val
    return bar_chart(val)


@app.callback(Output('lp-table-container', "children"), [
    Input("nav-dropdown", "label"),
    Input('lp-date-picker', 'date')
])
def system_click_table(system, date):
    d = dt.strptime(date[:10], '%Y-%m-%d')
    return lp_table(system, d)

debug = os.getenv("OPUI_DEBUG") == 'true'
port = os.getenv("OPUI_PORT")

if __name__ == "__main__":
    app.run_server(debug=debug, port=(port or 8080))