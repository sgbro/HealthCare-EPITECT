import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
from dash.dependencies import Input, Output

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

df = pd.read_csv('Output/output_modified.csv')
df2 = pd.read_csv('Output/output_new.csv')
df3= pd.read_csv('Output/output.csv')
colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}

# LINE CHART TEMPLATE CODE
fig = go.Figure()
fig.add_trace(go.Scatter(y=df2['confirmed cases'], x=df2['DateP'], name='predicted cases',
                         line=dict(color='firebrick', width=2,dash='dashdot') # dash options include 'dash', 'dot', and 'dashdot'
))
fig.add_trace(go.Scatter(x=df2['DateP'], y=df2['recoved cases'], name='recovered cases',
                         line=dict(color='blue', width=2,dash='dashdot') # dash options include 'dash', 'dot', and 'dashdot'
))

figg = go.Figure()
figg.add_trace(go.Scatter(y=df2['death cases'], x=df2['DateP'], name='death cases',
                         line=dict(color='firebrick', width=2,dash='dashdot') # dash options include 'dash', 'dot', and 'dashdot'
))
figg.add_trace(go.Scatter(x=df2['DateP'], y=df2['recoved cases'], name='recovered cases',
                         line=dict(color='blue', width=2,dash='dashdot') # dash options include 'dash', 'dot', and 'dashdot'
))
# END OF LINE CHART

# BAR GRAPH TEMPLATE CODE###################################

fig2 = go.Figure(data=[
    go.Bar(name='Confirmed', y=df2['confirmed cases'], x=df2['DateP'], hovertemplate="Confirmed : %{y}",
           marker={'color': 'rgb(49,0,0)'}),
    go.Bar(name='Death ', x=df2['DateP'], y=df2['death cases'], hovertemplate="Death : %{y}",
           marker={'color': 'rgb(255,0,0)'})
])

fig2.update_layout(title="Confirmed vs Death rates of REGION with particular date", barmode='group',bargap=0)

fig3 = go.Figure(data=[
    go.Bar(name='Confirmed', y=df2['confirmed cases'], x=df2['DateP'], hovertemplate="Confirmed : %{y}",
           marker={'color': 'rgb(49,0,0)'}),
    go.Bar(name='Recovery', x=df2['DateP'], y=df2['recoved cases'], hovertemplate="Recovered : %{y}",
           marker={'color': 'rgb(156,0,0)'}),
])

fig3.update_layout(title="Confirmed vs Recovery rates of REGION with particular date", barmode='group',bargap=0)

fig4 = go.Figure(data=[
    go.Bar(name='Death ', x=df2['DateP'], y=df2['death cases'], hovertemplate="Death : %{y}",
           marker={'color': 'rgb(255,0,0)'}),
    go.Bar(name='Recovery', x=df2['DateP'], y=df2['recoved cases'], hovertemplate="Recovered : %{y}",
           marker={'color': 'rgb(100,0,0)'})
])

fig4.update_layout(title="Recovery vs Death rates of REGION with particular date", barmode='group',bargap=0)
# END OF BAR CHART CODE##############################


# MAP#####################################################

token='pk.eyJ1Ijoic2dicm8iLCJhIjoiY2s4MjZ2bXR6MGl3YzNmcHFjNGd5cXN6bSJ9.LVIXScq3Dzv6odXDKjcSnA'
cities = pd.read_csv('Output/output_modified.csv', engine='python')
f = px.scatter_mapbox(cities, lat="Lat", lon="Long"
                      , hover_data=['confirmed cases','recoved cases','death cases', 'DateP'],zoom=1)
f.update_layout(mapbox_style="dark",mapbox_accesstoken=token)
f.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})

# END MAP#################################################
app.title='EPITECT'
app.layout = html.Div(style={'text-align': 'center', 'font-weight': 'bolder'}, children=[
    html.H1(children='EPITECT DISEASE SURVEILLANCE AND PREDICTION SYSTEM'),

    html.Div(style={'height': '20px', 'width': '800px',
                    'color': '#7FDBFF',
                    }),
    html.Div(
        dcc.Dropdown(id='dropdown',style={'width':'800px', 'align':'center'},
                     options=[
                         {'label': i, 'value': i} for i in df3.Location.unique()],
                     searchable=False,
                     placeholder='Select the region'
                     )),
    html.Div(
        style={'height': '800px', 'width': '800px'},
        children=[html.H3(html.B("Predicted Areas")),
        dcc.Graph(
            id='map',
            figure=f
        )]
    ),
    html.Div(
        style={'height': '800px', 'width': '800px'},
        children=
        dcc.Graph(
            id='line-graph',
           figure=fig
        )
    ),
    html.Div([html.Div(
        style={'height': '800px', 'width': '800px'},
        children=
        dcc.Graph(
            id='line-graph2',
           figure=figg
        )
    ),
    html.Div(
        style={'height': '800px', 'width': '800px'},
        children=
        dcc.Graph(
            id='bar-graph',
            figure=fig2
            )
        )
    ]),
    html.Div(
        style={'height': '800px', 'width': '800px'},
        children=
        dcc.Graph(
            id='bar-graph2',
            figure=fig3
        )
    ),
    html.Div(
        style={'height': '800px', 'width': '800px'},
        children=
        dcc.Graph(
            id='bar-graph3',
            figure=fig4
        )
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
