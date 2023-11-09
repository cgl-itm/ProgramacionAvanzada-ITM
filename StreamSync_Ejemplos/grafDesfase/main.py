import streamsync as ss
import numpy as np
import plotly.express as px
t = np.linspace(0,1,500)

def update(state):
    f = state["freq"]
    y = np.sin(2*np.pi*f*t+np.radians(state["desfase"]))
    fig = px.line(x=t,y=y)
    state["grafico"] = fig

# Initialise the state
initial_state = ss.init_state({
    "my_app": {
        "title": "My App"
    },
    "desfase": 0,
    "freq": 1,
})

update(initial_state)