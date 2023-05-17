# Ejemplo: Hello World
import dash
from dash import html
from dash import dcc

app = dash.Dash()

colors = {'background':'#111111','text':'#7FDBFF'}

app.layout = html.Div(style={'background':colors['background']},children=[
    html.H1('Hello Dash!',style={'textAlign':'center','color':colors['text']}), 
    html.Div('Dash: Web Dashboards with Python'),
    dcc.Graph(id='example', 
              figure = {'data':[
                            {'x':[1,2,3],'y':[4,1,2],'type':'bar','name':'Medellin'},
                            {'x':[1,2,3],'y':[2,4,5],'type':'bar','name':'Envigado'}
                            ],
                        'layout':{
                            'plot_bgcolor':colors['background'],
                            'paper_bgcolor':colors['background'],
                            'font':{'color':colors['text']},
                            'title':'BAR PLOTS!'
                            }
                        }
            )
])

if __name__ == '__main__':
    app.run_server()