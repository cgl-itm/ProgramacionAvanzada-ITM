import streamsync as ss
import pandas as pd
import plotly.express as px

data_link = "https://raw.githubusercontent.com/jorisvandenbossche/pandas-tutorial/master/data/flowdata.csv"
data = pd.read_csv(data_link, index_col=0, parse_dates=True)

# Its name starts with _, so this function won't be exposed
def update(state):
    print(type(state["fecha_ini"]),type(state["fecha_fin"]))
    df = data[state["fecha_ini"]:state["fecha_fin"]]
    fig = px.line(df, x=df.index, y="L06_347")
    state["grafico"] = fig
    
    
# Initialise the state
initial_state = ss.init_state({
    "my_app": {
        "title": "My App"
    },
    "dataframe": data,
    "fecha_ini": data.index.min().date(),
    "fecha_fin": data.index.max().date(),
    "grafico": None,
})

update(initial_state)