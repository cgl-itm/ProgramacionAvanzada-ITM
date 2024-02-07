import dash
from dash import dcc
from dash import html
import plotly.graph_objs as go
import numpy as np

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Generador de Forma de Onda"),
    html.Div([
        html.Label("Tipo de Función:"),
        dcc.Dropdown(
            id='listaFun',
            options=[
                {'label': 'Seno', 'value': 'sin'},
                {'label': 'Coseno', 'value': 'cos'}
            ],
            value='sin'
        )
    ]),
    html.Div([
        html.Label("Frecuencia:"),
        dcc.Input(id='inputFrecuencia', type='number', value=1)
    ]),
    html.Div([
        html.Label("Tiempo:"),
        dcc.Input(id='inputTiempo', value='1')
    ]),
    dcc.Graph(id='grafico')
])

@app.callback(
    dash.dependencies.Output('grafico', 'figure'),
    [dash.dependencies.Input('listaFun', 'value'),
     dash.dependencies.Input('inputFrecuencia', 'value'),
     dash.dependencies.Input('inputTiempo', 'value')])
def update_waveform_graph(tipoFuncion, frequency, time):
    t = np.linspace(0,float(time),500)
    if tipoFuncion == 'sin':
        y = np.sin(2*np.pi*frequency*t)
    elif tipoFuncion == 'cos':
        y = np.cos(2*np.pi*frequency*t)

    trace = go.Scatter(x=t, y=y, mode='lines', name='Grafico')
    layout = go.Layout(title='Forma de Onda', xaxis={'title': 'Tiempo [s]'}, yaxis={'title': 'Amplitud'})
    figure = go.Figure(data=[trace], layout=layout)
    return figure

if __name__ == '__main__':
    app.run_server(debug=True)