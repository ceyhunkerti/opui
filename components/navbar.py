import dash
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
from datetime import datetime as dt, timedelta

menu = {
    'aedas': "Akdeniz Dagitim",
    'bedas': "Bogazici Dagitim",
    'cedas': "Camlibel Dagitim",
    'akepsas': "Akdeniz Perakende",
    'bepsas': 'Bogazici Perakende',
    'cepesas': "Camlibel Perakende"
}

def dropdown():
    return dbc.DropdownMenu(
        children=[
            dbc.DropdownMenuItem(menu['aedas'], id='ndd-aedas', href="aedas"),
            dbc.DropdownMenuItem(menu['bedas'], id='ndd-bedas', href="bedas"),
            dbc.DropdownMenuItem(menu['cedas'], id='ndd-cedas', href="cedas"),
            dbc.DropdownMenuItem(divider=True),
            dbc.DropdownMenuItem(menu['akepsas'], id='ndd-akepsas', href="akepsas"),
            dbc.DropdownMenuItem(menu['bepsas'], id='ndd-bepsas', href="bepsas"),
            dbc.DropdownMenuItem(menu['cepesas'], id='ndd-cepesas', href="cepesas"),
        ],
        nav=True,
        in_navbar=True,
        label="Systems",
        id='nav-dropdown'
    )


def navbar():
    return dbc.NavbarSimple(
        children=[
            dropdown(),
        ],
        brand="OPUI",
        brand_href="#",
        sticky="top",
        className="mb-5",
    )
