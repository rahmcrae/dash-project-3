import dash_html_components as html
import dash_core_components as dcc
import plotly.graph_objs as go
import pandas as pd


# Create a DataFrame from the .csv file:
df = pd.read_csv('../data/OldFaithful.csv')

# Create a Dash layout that contains a Graph component:
layout = html.Div([
    dcc.Graph(
        id='old_faithful',
        figure={
            'data': [
                go.Scatter(
                    x = df['X'], 
                    y = df['Y'],
                    mode = 'markers'
                )
            ],
            'layout': go.Layout(
                title = 'Old Faithful Eruption Intervals v Durations',
                xaxis = {'title': 'Duration of eruption (minutes)'},
                yaxis = {'title': 'Interval to next eruption (minutes)'},
                hovermode='closest'
            )
        }
    )
])  