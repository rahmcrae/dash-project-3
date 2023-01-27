import dash_html_components as html
import dash_core_components as dcc
import pandas as pd
from numpy import random
import plotly.graph_objs as go
from datetime import datetime
import pandas_datareader.data as web
from tickers import symbols, names

nsdq = pd.DataFrame(list(zip(symbols,names)),columns=['Symbol','Name'])
nsdq.set_index('Symbol', inplace=True)

options = []
for tic in nsdq.index:
    options.append({'label':'{} {}'.format(tic,nsdq.loc[tic]['Name']), 'value':tic})

colors = {
    'background': '#ebeff5',
    'text': '#11111'
}

layout = html.Div([
    html.H1(children='Stock Ticker Dashboard',
            style = {
                'textAlign' : 'center',
                'color' : colors['text']
            }            
        ),
    html.H2(children='Udemy Milestone Project - Interactive Python Dashboards with Plotly & Dash', 
            style = {
                'textAlign' : 'center',
                'color' : colors['text']
            }            
        ),
    html.H3(children='By: Rah McRae 🌞',
            style = {
                'textAlign' : 'center',
                'color' : colors['text']
            }            
        ),
    html.Div([
        html.H3(children="""
                This dashboard can be used to analyze financial trends of 100+ tickers from the last ~20 years.                               
                Select parameters & click 'Submit' below to complete search query. 
                """, 
                style={                    
                    'textAlign' : 'center',
                    'color' : colors['text'],
                    'backgroundColor': colors['background']
                    }
                )]),    
    html.Div([
        html.H3('Select stock symbols:', style={'paddingRight':'30px'}),
        dcc.Dropdown(
            id='my_ticker_symbol',
            options=options,
            value=['MSFT','AMZN','AAPL','NFLX','GOOG'],
            multi=True
        )
    ], style={'display':'inline-block', 'verticalAlign':'top', 'width':'30%','paddingBottom':'10px'}),
    html.Div([
        html.H3('Select start and end dates:'),
        dcc.DatePickerRange(
            id='my_date_picker',
            min_date_allowed=datetime(1900, 1, 1),
            max_date_allowed=datetime.today(),
            start_date=datetime(2018, 1, 1),
            end_date=datetime.today()
        )
    ], style={'display':'inline-block','marginLeft':'10px'}),
    html.Div([
        html.Button(
            id='submit-button',
            n_clicks=0,
            children='Submit',
            style={'fontSize':24, 'marginLeft':'10px'}
        ),
    ], style={'display':'inline-block'}),
    dcc.Graph(
        id='my_graph',
        figure={
            'data': [
                {'x': [1,2], 'y': [3,1]}
            ],
            'layout':{'title':'Default Title'}
        },style={'border':'0.2px gray solid'}        
    ),
    html.Div([
        html.H3(children="Sourced from Tiingo API", 
                style={                    
                    'textAlign' : 'left',
                    'color' : colors['text'],
                    'fontSize':12
                    }
                )])
],style={'font-family':'sans-serif'})