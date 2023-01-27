import dash
from dash import html, dcc
import flask
from layout_2 import layout

app = dash.Dash(__name__)
app.layout = layout

server = flask.Flask(__name__)
server = app.server
app.run_server(host='0.0.0.0', port=8050, debug=True,use_reloader=False)