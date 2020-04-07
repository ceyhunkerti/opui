import dash
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
from datetime import datetime as dt, timedelta

dropdown = dbc.DropdownMenu(
    children=[
        dbc.DropdownMenuItem("Akdeniz Dagitim", id='ndd-aedas'),
        dbc.DropdownMenuItem("Bogazici Dagitim", id='ndd-bedas'),
        dbc.DropdownMenuItem("Camlibel Dagitim", id='ndd-cedas'),
        dbc.DropdownMenuItem(divider=True),
        dbc.DropdownMenuItem("Akdeniz Perakende", id='ndd-akepsas'),
        dbc.DropdownMenuItem("Bogazici Perakende", id='ndd-bepsas'),
        dbc.DropdownMenuItem("Camlibel Perakende", id='ndd-cepesas'),
    ],
    nav=True,
    in_navbar=True,
    label="Systems",
    id='nav-dropdown'
)


navbar = dbc.NavbarSimple(
    children=[
        dropdown,
    ],
    brand="OPUI",
    brand_href="#",
    sticky="top",
    className="mb-5",
)
