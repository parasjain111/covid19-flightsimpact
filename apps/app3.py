import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
import numpy as np
import pandas as pd
from app import app
df=pd.read_csv("flights.csv")
print(df.head())



layout = html.Div(children=[
    html.H1("International Arrival , International Departures, Domestic Flights  for Each country ", style={'text-align': 'center'}),
    dcc.Link('Go to App 1', href='/apps/app1'),
    dcc.Link('Go to App 2', href='/apps/app2'),
    dcc.Link('Go to App 4', href='/apps/app4'),
    dcc.Input(id='input', value='India', type='text'),
    dcc.Input(id='input1', value='', type='text'),
    html.Div(id='output-graph1'),
])

@app.callback(
    Output(component_id='output-graph1', component_property='children'),
    [Input(component_id='input', component_property='value'),
    Input(component_id='input1', component_property='value')]
)
def update_value(input_data,input1_data):
    df=pd.read_csv("flights.csv")
    df=df[df['country']==input_data]
    if(input1_data=="international_departures"):
        return dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': df.day, 'y':df.international_departures, 'type': input1_data, 'name': input_data},
                
            ],
            'layout': {
                'title': "nice"
            }
        }
    )
    if(input1_data=="international_arrivals"):
       return dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': df.day, 'y': df.international_arrivals, 'type': input1_data, 'name': input_data},
                
            ],
            'layout': {
                'title': "nice"
            }
        }
    )
    if(input1_data=="domestic_flights"):
        return dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': df.day, 'y': df.domestic_flights, 'type': input1_data, 'name': input_data},

            ],
            'layout': {
                'title': "nice"
            }
        }
    )
    
