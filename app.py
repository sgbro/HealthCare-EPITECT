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

df = pd.read_csv('C:/Users/sourabh gupta/Desktop/sg.csv')
df2 = pd.read_csv('Output/output.csv')

colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}

# LINE CHART TEMPLATE CODE

fig = go.Figure()
fig.add_trace(go.Scatter(y=df['predicted C'], x=df['sl'], name='predicted cases',
                         line=dict(color='firebrick', width=2,
                                   dash='dash')
                         ))
fig.add_trace(go.Scatter(x=df['sl'], y=df['confirmed cases'], name='confirmed cases',
                         line=dict(color='blue', width=2)
                         ))

# END OF LINE CHART

# BAR GRAPH TEMPLATE CODE

fig2 = go.Figure(data=[
    go.Bar(name='Predicted', x=df['sl'], y=df['predicted C'], hovertemplate="Predicted : %{y}",
           marker={'color': 'rgb(0,11,111)'}),
    go.Bar(name='Confirmed', x=df['sl'], y=df['confirmed cases'], hovertemplate="Confirmed : %{y}",
           marker={'color': 'rgb(100,100,100)'})
])

fig2.update_layout(title="Prediction vs Confirmation", barmode='group')

# END OF BAR CHART CODE

# PIE CHART TEMPLATE

pc = np.array(df['predicted C'])
cc = np.array(df['confirmed cases'])
sum1 = np.sum(pc)
sum2 = np.sum(cc)
sum = sum1 + sum2
# Pie chart, where the slices will be ordered and plotted counter-clockwise:
labels = 'Predicted Case', 'Confirmed Case'
sizes = [sum1 * 100 / sum, sum2 * 100 / sum]
explode = (0, 0.1)  # only "explode" the 2nd slice (i.e. 'Hogs')

fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')
fg = go.Figure(plt.show())
# END OF PIE CHART TEMP

# MAP
cities = pd.read_csv('C:/Users/sourabh gupta/Downloads/Compressed/zomato/zomato.csv', engine='python')
f = px.scatter_mapbox(cities, lat="Latitude", lon="Longitude", hover_name="City"
                      , hover_data=['Address', 'Locality'])
f.update_layout(mapbox_style="open-street-map")
f.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
f.show()
# END MAP

app.layout = html.Div(style={'text-align': 'center', 'font-weight': 'bolder'}, children=[
    html.H1(children='EPITECT DISEASE SURVEILLANCE SYSTEM'),

    html.Div(style={'height': '20px', 'width': '800px',
                    'color': '#7FDBFF',
                    },
             children='''
            Dash: A web application framework for Python.
            '''),
    html.Div(
        dcc.Dropdown(id='dropdown',
                     options=[
                         {'label': i, 'value': i} for i in df2.Location.unique()],
                     searchable=False
                     )),
    html.Div(
        style={'height': '800px', 'width': '800px'},
        children=
        dcc.Graph(
            id='line-graph',
            figure=fig
        )
    ),
    html.Div(
        style={'height': '800px', 'width': '800px'},
        children=
        dcc.Graph(
            id='bar-graph',
            figure=fig2
        )
    ),
    html.Div(
        style={'height': '800px', 'width': '800px'},
        children=
        dcc.Graph(
            id='pie-graph',
            figure=fg
        )
    ),
    html.Div(
        style={'height': '800px', 'width': '800px'},
        children=
        dcc.Graph(
            id='map',
            figure=f
        )
    ),
    html.Div(id='output')
])

if __name__ == '__main__':
    app.run_server(debug=True)
