import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
from datetime import datetime as dt, timedelta
import dash_table
import pandas as pd
import plotly.express as px
import numpy as np

from reader import df


max_date = df['date'].max()
min_date = df['date'].min()

df = df[['date', 'system', 'plan', 'start', 'end', 'duration']]
df['day'] = pd.DatetimeIndex(df.date).strftime("%Y-%m-%d")
df.drop(['date'], axis=1, inplace=True)
df = df[['day', 'system', 'plan', 'start', 'end', 'duration']]


df['average'] = df.assign(duration=pd.to_numeric(
    df['duration'])).groupby(['plan', 'system']).transform('mean').apply(np.ceil)
df['average'] = df.groupby(['plan', 'system']).transform('mean').apply(np.ceil)


days = np.flip(np.sort(df['day'].unique()))
_range = [days[min(len(days), 15)], dt.strptime(
    days[0], '%Y-%m-%d') + timedelta(days=1)]


def bar_figure(system):
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
            range=_range,
            rangeslider=dict(visible=True),
        ),
    )
    return fig


def bar_chart(system):
    return dcc.Graph(
        id='bar-chart',
        figure=bar_figure(system)
    )


def lp_table(system, date=max_date):
    d = date.strftime("%Y-%m-%d")
    data = df.query(f"system == '{system}' and day == '{d}'")

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


date_picker = dcc.DatePickerSingle(
    min_date_allowed=min_date,
    max_date_allowed=max_date,
    display_format='YYYY.MM.DD',
    date=max_date,
    id='lp-date-picker'
)


home = html.Div(id="home", style={}, children=[
    dbc.Row([
        bar_chart('BEDAS')
    ], justify="start", id='bar-chart-container'),
    dbc.Row([date_picker], className='ml-4'),
    html.Div([
        lp_table('BEDAS')
    ], style={
        'padding': '40px',
        'padding-top': '20px'
    }, id='lp-table-container')
])
