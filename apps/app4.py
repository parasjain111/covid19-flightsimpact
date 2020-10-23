import pandas as pd
import pycountry
import dash
from dash.dependencies import Input, Output
import plotly.express as px
import dash_core_components as dcc
import dash_html_components as html
import numpy as np
from app import app
df=pd.read_csv("flights.csv")
print(df.head())


def do_fuzzy_search(country):
    try:
        result = pycountry.countries.search_fuzzy(country)
        return result[0].alpha_3
    except:
        return np.nan

iso_map = {country: do_fuzzy_search(country) for country in df["country"].unique()}
df["country_code"] = df["country"].map(iso_map)
print(df)
df['day'] = df['day'].astype(str)
unique_date = df.day.unique()
df['val'] = 0
print(unique_date)
optionss=[]
for i in unique_date:
    dict = {
        "label": i,
        "value":i
    }
    optionss.append(dict)
print(df.head())
print(optionss)

options2=[{"total_flights"},{"international_arrivals"},{"international_departures"},{"domestic_flights"}]
layout = html.Div([
    html.H1("Map Based Visulation of total flights , International Arrival , International Departures , domestic flights Day Wise", style={'text-align': 'center'}),
    dcc.Link('Go to App 1', href='/apps/app1'),
    dcc.Link('Go to App 2', href='/apps/app2'),
    dcc.Link('Go to App 3', href='/apps/app3'),
    dcc.Dropdown(id = 'slct_year',
    options = optionss,
        multi=False,
        value="",
        style={'width': "40%"}
    ),
dcc.Dropdown(id = 'menu_select',
    options =[
        {'label': 'total_flights', 'value': 'total_flights'},
        {'label': 'internation_arrivals', 'value': 'international_arrivals'},
        {'label': 'international_departures', 'value': 'international_departures'},
        {'label': 'domestic_flights', 'value': 'domestic_flights'}
    ],
        multi=False,
        value="",
        style={'width': "40%"}
    ),
    html.Div(id='output_container',children=[]),
    html.Br(),
    dcc.Graph(id='my_bee_map',figure={}),

    #dcc.Graph(id='my_bee_map',figure={}),
    ])

@app.callback(
    [Output(component_id = 'output_container',component_property='children'),
    Output(component_id='my_bee_map',component_property = 'figure')],
    [Input(component_id='slct_year',component_property='value'),
    Input(component_id='menu_select',component_property='value')]
)

def update_graph(option_slctd,menusel):
    print(option_slctd)
    print(type(option_slctd))

    container = "The year chosen by user was : {}".format(option_slctd)
    dfff = df[df['day'] == option_slctd]
    
    print(dfff)
    #plotly Express
    fig = px.choropleth(
        data_frame=dfff,
        locationmode='ISO-3',
        locations='country_code',
        color=menusel,
        hover_name='country',
        color_continuous_scale=px.colors.sequential.YlOrRd,
        width=1300,
        height =700,
    )

    return container, fig

