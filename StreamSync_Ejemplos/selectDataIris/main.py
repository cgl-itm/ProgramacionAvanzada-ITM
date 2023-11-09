import streamsync as ss
import pandas as pd
import plotly.express as px

# This is a placeholder to get you started or refresh your memory.
# Delete it or adapt it as necessary.
# Documentation is available at https://streamsync.cloud

data = pd.read_csv('https://gist.githubusercontent.com/netj/8836201/raw/6f9306ad21398ea43cba4f7d537619d0e07d5ae3/iris.csv')

def update_graph(state):
    clase = []
    print(type(state['SeleccionClase']))
    if type(state['SeleccionClase']) == 'str':
        clase.append(state['SeleccionClase'])
    else:
        clase = state['SeleccionClase'].copy()
    datafil = data[data['variety'].isin(clase)]
    fig = px.histogram(datafil, x=state['atributo'], color = "variety", nbins=20)
    state['fig'] = fig



initial_state = ss.init_state({
    "my_app": {
        "title": "Super App"
    },
    "SeleccionClase": ["Setosa","Versicolor"],
})

update_graph(initial_state)