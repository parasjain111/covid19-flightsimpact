import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
import numpy as np
import pandas as pd
import dash_bootstrap_components as dbc
from app import app
df=pd.read_csv("flights.csv")
print(df.head())


layout = html.Div(children=[
    html.H1("Total Flights v/s Date ", style={'text-align': 'center'}),
    html.Div(id='app-1-display-value'),
    dcc.Link('Go to App 2', href='/apps/app2'),
    dcc.Link('Go to App 3', href='/apps/app3'),
    dcc.Link('Go to App 4', href='/apps/app4'),
    dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': df.day, 'y': df.total_flights, 'type': "bar", 'name':"Total flights"},
                             
                
            ],
            'layout': {
                'title': "nice"
            }
        }
    ),
    html.H1("Total flights for each country v/s Dates", style={'text-align': 'center'}),


    dcc.Input(id='input', value='India', type='text'),
    dcc.Input(id='input1', value='', type='text'),
    html.Div(id='output-graph2'),
])


@app.callback(
    Output(component_id='output-graph2', component_property='children'),
    [Input(component_id='input', component_property='value'),
    Input(component_id='input1', component_property='value')]
)
def update_value(input_data,input1_data):
    df=pd.read_csv("flights.csv")
    df=df[df['country']==input_data]
    return dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': df.day, 'y': df.total_flights, 'type': input1_data, 'name': input_data},
            ],
            'layout': {
                'title': "nice"
            }
        }
    ),


    
