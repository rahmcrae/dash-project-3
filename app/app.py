import dash
from dash import html, dcc
import flask
from layout import layout
import pandas_datareader as pdr
from dash.dependencies import Input, Output, State
from datetime import datetime
import pandas as pd
import os

app = dash.Dash(__name__)
app.layout = layout

@app.callback(
    Output('my_graph', 'figure'),
    [Input('submit-button', 'n_clicks')],
    [State('my_ticker_symbol', 'value'),
    State('my_date_picker', 'start_date'),
    State('my_date_picker', 'end_date')])
def update_graph(n_clicks, stock_ticker, start_date, end_date):
    start = datetime.strptime(start_date[:10], '%Y-%m-%d')
    end = datetime.strptime(end_date[:10], '%Y-%m-%d')
    traces = []
    for tic in stock_ticker:               
        df = pdr.get_data_tiingo(tic, api_key=os.getenv('TIINGO_API_KEY')).reset_index().set_index('date')
        traces.append({'x':df.index, 'y': df['close'], 'name':tic})
    fig = {
        'data': traces,
        'layout': {'title':', '.join(stock_ticker)+' Closing Prices'}
    }
    return fig

server = flask.Flask(__name__)
server = app.server
app.run_server(host='0.0.0.0', port=8050, debug=True,use_reloader=False)