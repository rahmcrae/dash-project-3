import dash_html_components as html
import dash_core_components as dcc
import pandas as pd
from numpy import random
import plotly.graph_objs as go

# Create a DataFrame from the .csv file:
df = pd.read_csv('../data/mpg.csv')

# Add a random "jitter" to model_year to spread out the plot
df['year'] = df['model_year'] + random.randint(-4,5,len(df))*0.10

layout = html.Div([
    html.Div([   # this Div contains our scatter plot
    dcc.Graph(
        id='mpg_scatter',
        figure={
            'data': [go.Scatter(
                x = df['year']+1900,  # our "jittered" data
                y = df['mpg'],
                text = df['name'],
                hoverinfo = 'text',
                mode = 'markers'
            )],
            'layout': go.Layout(
                title = 'mpg by model & year of make',
                xaxis = {'title': 'model year'},
                yaxis = {'title': 'miles per gallon'},
                hovermode='closest'
            )
        }
    )], style={'width':'50%','display':'inline-block'}),
    html.Div([  # this Div contains our output graph and vehicle stats
    dcc.Graph(
        id='mpg_line',
        figure={
            'data': [go.Scatter(
                x = [0,1],
                y = [0,1],
                mode = 'lines'
            )],
            'layout': go.Layout(
                title = 'acceleration',
                xaxis = {'title': 'xaxis'},
                yaxis = {'title': 'yaxis'},
                margin = {'l':0}
            )
        }
    ),
    dcc.Markdown(
        id='mpg_stats'
    )
    ], style={'width':'20%', 'height':'50%','display':'inline-block'})
])