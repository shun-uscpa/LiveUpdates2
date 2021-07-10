import datetime

import dash
import dash_html_components as html

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
app.layout = html.H1('The time is: ' + str(datetime.datetime.now()))

if __name__ == '__main__':
    app.run_server(debug=True)