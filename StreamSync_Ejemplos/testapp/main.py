import streamsync as ss
import numpy as np
import plotly.express as px

import plotly.graph_objects as go

t = np.linspace(0,1,500)
desfases = {'0':45, '1':135, '2':-135,'3':-45}

# This is a placeholder to get you started or refresh your memory.
# Delete it or adapt it as necessary.
# Documentation is available at https://streamsync.cloud

def update(state):
    y = np.sin(2*np.pi*t + np.radians(desfases[state["seleccionDrop"]]))
    #fig = px.line(x=t,y=y)
    #fig.add_trace(px.line(x=t,y=np.sin(2*np.pi*t)))

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=t, y=y,
                    mode='lines',
                    name='desfasado'))
    fig.add_trace(go.Scatter(x=t, 
                             y=np.sin(2*np.pi*t),
                    mode='lines+markers',
                    name='cero grados'))

    state["grafico"] = fig
    state["desfase"] = str(desfases[state["seleccionDrop"]])

initial_state = ss.init_state({
    "my_app": {
        "title": "Modulador QPSK"
    },
    "seleccionDrop": '0',
    "desfase": None,
})

update(initial_state)