import writer as wf
import numpy as np
#import plotly.express as px
import plotly.graph_objects as go

# This is a placeholder to get you started or refresh your memory.
# Delete it or adapt it as necessary.
# Documentation is available at https://dev.writer.com/framework

t = np.linspace(0,1,101)
dicDesfase = {'0': 45, '1': 135, '2': -135, '3': -45}

def update(state):
    desfase = np.radians(dicDesfase[state['seleccion']])
    y = np.sin(2*np.pi*t+desfase)
    
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=t, y=y,
                    mode='lines',
                    name='desfasado'))
    fig.add_trace(go.Scatter(x=t, 
                             y=np.sin(2*np.pi*t),
                    mode='lines+markers',
                    name='cero grados'))
    fig.update_layout(
        title=f"Desafe de {str(dicDesfase[state['seleccion']])}"
        )
    state["grafico"] = fig

    
# Initialise the state

# "_my_private_element" won't be serialised or sent to the frontend,
# because it starts with an underscore

initial_state = wf.init_state({
    "seleccion":'0',
})

update(initial_state)