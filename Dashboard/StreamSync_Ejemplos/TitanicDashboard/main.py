import streamsync as ss
import pandas as pd
import plotly.express as px
# This is a placeholder to get you started or refresh your memory.
# Delete it or adapt it as necessary.
# Documentation is available at https://streamsync.cloud

#df = pd.read_csv('https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv')
df = pd.read_csv('assets/titanic.csv')
df['Deaths'] = 1-df['Survived']

def update(state):
    print((df['Sex']=='female').sum())
    state['promEdad'] = df['Age'].mean().round()
    state['tarifaTotal'] = f"{df['Fare'].sum():.2f}"
    state['cantidadMujeres'] = df['Sex'][df['Sex']=='female'].shape[0]
    state['cantidadHombres'] = df['Sex'][df['Sex']=='male'].shape[0]
    state['promedioTarifa'] = f"{df['Fare'].mean():.2f}"
    #dfSurv = df[['Sex','Survived']][df['Survived']== 1]
    fig = px.pie(df, values='Survived', names='Sex', hole=.3)
    state['figSobrevivientes'] = fig
    fig = px.pie(df, values='Deaths', names='Sex', hole=.3)
    state['figMuertos'] = fig
    fig = px.pie(df, values='Survived', names='Pclass', hole=.3)
    state['figSumaPclass'] = fig
# Initialise the state

# "_my_private_element" won't be serialised or sent to the frontend,
# because it starts with an underscore

initial_state = ss.init_state({
    "my_app": {
        "title": "Titanic"
    },
    "promEdad": None,
    "tarifaTotal": None,
    "cantidadMujeres": None,
    "cantidadHombres": None,
    "promedioTarifa": None,
    "figSobrevivientes": None,
    "figSumaPclass": None,
})

update(initial_state)