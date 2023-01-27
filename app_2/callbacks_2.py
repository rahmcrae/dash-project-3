from dash.dependencies import Input, Output, State
from app_2 import app
import plotly.graph_objs as go 
import pandas as pd
from numpy import random

# Create a DataFrame from the .csv file:
df = pd.read_csv('../data/mpg.csv')

# Add a random "jitter" to model_year to spread out the plot
df['year'] = df['model_year'] + random.randint(-4,5,len(df))*0.10

@app.callback(
    Output('mpg_line', 'figure'),
    [Input('mpg_scatter', 'hoverData')])
def callback_graph(hoverData):
    v_index = hoverData['points'][0]['pointIndex']
    fig = {
        'data': [go.Scatter(
            x = [0,1],
            y = [0,60/df.iloc[v_index]['acceleration']],
            mode='lines',
            line={'width':2*df.iloc[v_index]['cylinders']}
        )],
        'layout': go.Layout(
            title = df.iloc[v_index]['name'],
            xaxis = {'visible':False},
            yaxis = {'visible':False, 'range':[0,60/df['acceleration'].min()]},
            margin = {'l':0},
            height = 300
        )
    }
    return fig

@app.callback(
    Output('mpg_stats', 'children'),
    [Input('mpg_scatter', 'hoverData')])
def callback_stats(hoverData):
    v_index = hoverData['points'][0]['pointIndex']
    stats = """
        {} cylinders
        {}cc displacement
        0 to 60mph in {} seconds
        """.format(df.iloc[v_index]['cylinders'],
            df.iloc[v_index]['displacement'],
            df.iloc[v_index]['acceleration'])
    return stats