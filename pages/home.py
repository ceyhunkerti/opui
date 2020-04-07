import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
from datetime import datetime as dt, timedelta
import dash_table
import pandas as pd
import plotly.express as px
import numpy as np


def __range(df):
    days = np.flip(np.sort(df['day'].unique()))
    return [days[min(len(days), 15)], dt.strptime(days[0], '%Y-%m-%d') + timedelta(days=1)]


def bar_figure(df, system):
    data = df.query(f"system == '{system}'")
    fig = px.bar(data, x='day', y='duration', width=1600, height=500,
                 color='plan',
                 barmode='group',
                 )

    fig.update_layout(
        xaxis_title="Date",
        yaxis_title="Duration(sec)",
        xaxis=dict(
            tickangle=90,
            tickmode='linear',
            range=__range(df),
            rangeslider=dict(visible=True),
        ),
        updatemenus=[
            dict(
                type = "buttons",
                direction = "left",
                buttons=list([
                    dict(
                        args=[{'type': 'bar'}],
                        label="Bar",
                        method="update"
                    ),
                    dict(
                        args=[{'type': 'line'}],
                        label="Line",
                        method="update",
                    )
                ]),
                pad={"r": 10, "t": 10},
                showactive=True,
                x=0.0,
                xanchor="left",
                y=1.2,
                yanchor="top"
            ),
        ]
    )
    return fig


def bar_chart(df, system):
    return dcc.Graph(
        id='bar-chart',
        figure=bar_figure(df, system)
    )


def lp_table(df, system, date=None):
    date = date or df['date'].max()
    day = date.strftime("%Y-%m-%d")
    data = df.query(f"system == '{system}' and day == '{day}'")

    data = data[['system', 'plan', 'start', 'end', 'duration', 'average']]

    data = data.sort_values(by=['duration'], ascending=False).rename(
        columns={'duration': 'duration(sec)', 'average': 'average(sec)'})

    table = dash_table.DataTable(
        id='main-table',
        sort_action="native",
        sort_mode="single",
        style_as_list_view=True,
        columns=[{"name": str.capitalize(i), "id": i} for i in data.columns],
        data=data.to_dict('records'),
        style_cell={'textAlign': 'left',
                    'paddingLeft': '5px', 'paddingRight': '5px'},
        css=[{'selector': 'tr:hover td', 'rule': 'background-color: #e3f2fd !important;'}],
        style_data_conditional=[
            {
                'if': {
                    'filter_query': '{duration(sec)} > {average(sec)}'
                },
                'color': '#ef5350',
            },
        ],
    )
    return table


def date_picker(df):
    return dcc.DatePickerSingle(
        min_date_allowed=df['date'].min(),
        max_date_allowed=df['date'].max(),
        display_format='YYYY.MM.DD',
        date=df['date'].max(),
        id='lp-date-picker'
    )

def home(df):
    return html.Div(id="home", style={}, children=[
        dbc.Row([
            bar_chart(df, 'BEDAS')
        ], justify="start", id='bar-chart-container'),
        dbc.Row([date_picker(df)], className='ml-4'),
        html.Div([
            lp_table(df, 'BEDAS')
        ], style={
            'padding': '40px',
            'padding-top': '20px'
        }, id='lp-table-container')
    ])