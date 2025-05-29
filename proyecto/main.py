import writer as wf
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# This is a placeholder to get you started or refresh your memory.
# Delete it or adapt it as necessary.
# Documentation is available at https://dev.writer.com/framework

# Shows in the log when the app starts
df = pd.read_csv("https://raw.githubusercontent.com/jorisvandenbossche/pandas-tutorial/master/data/flowdata.csv",index_col=0)
df.index = pd.to_datetime(df.index)
#df = df.resample('10min').mean() #Para reducir el tamaño de la base de datos

# Its name starts with _, so this function won't be exposed
def update_tabUnivariado(state):
    state['figTabUnivariado'] = px.line(df, y=state['selectName'], title=f'{state["selectName"]}')

def update_tabBivariado(state):
    fig = go.Figure()
    fig.add_trace(go.Histogram(x=df[state['selectName']]))
    fig.add_trace(go.Histogram(x=df[state['selectName2']]))
    state['figTabBivariado'] = fig
    #px.histogram(df, x=[state['selectName'],state['selectName2']])

def update_Fechas(state):
    df2 = df.loc[state['fechaIni']:state['fechaFin'], [state['fechaVar']]]
    state["figFechas"] = px.line(df2, y=state['fechaVar'], title=state['fechaVar'])

# Initialise the state

# "_my_private_element" won't be serialised or sent to the frontend,
# because it starts with an underscore

initial_state = wf.init_state({
    "my_app": {
        "title": "MY APP"
    },
    "colNames": {name:name for name in df.columns[1:]},
    "selectName": df.columns[1],
    "figTabUnivariado": None,
    'selectName2': df.columns[2],
    "figTabBivariado": None,
    "fechaIni": df.index.min().date(),
    "fechaFin": df.index.max().date(),
    "fechaVar": df.columns[0],
    "figFechas": None,
})