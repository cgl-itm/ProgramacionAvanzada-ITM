import writer as wf
import pandas as pd
import numpy as np
import plotly.express as px

# This is a placeholder to get you started or refresh your memory.
# Delete it or adapt it as necessary.
# Documentation is available at https://dev.writer.com/framework

df = pd.read_csv('https://raw.githubusercontent.com/datasciencedojo/datasets/refs/heads/master/titanic.csv')
df['Died'] = 1-df['Survived']


# Its name starts with _, so this function won't be exposed
def prueba(state):
    dftemp = df if state['sex_select']=='all' else df[df['Sex']==state['sex_select']]
    state['AvAge'] = np.round(dftemp['Age'].mean())
    state['TotalFare'] = dftemp['Fare'].sum()
    state['AvgFare'] = dftemp['Fare'].mean()
    state['TotalPass'] = dftemp.shape[0]

    dfgroup = dftemp.groupby('Sex')['Died'].sum()
    state['fig1'] = px.pie(values =dfgroup.values , names =dfgroup.index,  title='Count of survivers for Died by Sex')
    dfgroup = dftemp.groupby('Sex')['Survived'].sum()
    state['fig2'] = px.pie(values =dfgroup.values , names =dfgroup.index,  title='Count of survivers for Survived by Sex')
    dfgroup = dftemp.groupby('Pclass')['Survived'].sum()
    state['fig3'] = px.pie(values =dfgroup.values , names =dfgroup.index,  title='Count of survivers for Pclass by Sex')

    
# Initialise the state

# "_my_private_element" won't be serialised or sent to the frontend,
# because it starts with an underscore

initial_state = wf.init_state({
    "my_app": {
        "title": "Titanic"
    },
    "_my_private_element": 1337,
    "message": None,
    "counter": 26,
    "sex_select": 'all',
    "AvAge": 0.0,
    "TotalFare": 0.0,
    'AvgFare': 0.0,
    'TotalPass': 0.0,
    'fig1': None
})

prueba(initial_state)