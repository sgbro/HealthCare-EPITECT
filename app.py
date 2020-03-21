import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go
import pandas as pd
import numpy as np

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)


df = pd.read_csv('C:/Users/sourabh gupta/Desktop/sg.csv')

#LINE CHART TEMPLATE CODE

fig = go.Figure()
fig.add_trace(go.Scatter(y=df['predicted C'], x=df['sl'], name='predicted cases',
                         line=dict(color='firebrick', width=2,
                              dash='dash')
))
fig.add_trace(go.Scatter(x=df['sl'], y=df['confirmed cases'], name='confirmed cases',
                         line=dict(color='blue', width=2)
))

#END OF LINE CHART

#BAR GRAPH TEMPLATE CODE

fig2 = go.Figure(data=[
    go.Bar(name='Predicted', x=df['sl'], y=df['predicted C'], hovertemplate="Predicted : %{y}", marker={'color':'rgb(0,11,111)'}),
    go.Bar(name='Confirmed', x=df['sl'], y=df['confirmed cases'], hovertemplate="Confirmed : %{y}", marker={'color':'rgb(100,100,100)'})
])

fig2.update_layout(title="Prediction vs Confirmation",barmode='group')

#END OF BAR CHART CODE


app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),

    html.Div(children='''
        Dash: A web application framework for Python.
    '''),

    dcc.Graph(
        id='example-graph',
        figure=fig
    ),
    dcc.Graph(
        id='dd',
        figure=fig2
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)