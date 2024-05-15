import streamsync as ss
import pandas as pd
import plotly.express as px

# This is a placeholder to get you started or refresh your memory.
# Delete it or adapt it as necessary.
# Documentation is available at https://streamsync.cloud

# Shows in the log when the app starts
data = pd.read_csv('https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv')


# Its name starts with _, so this function won't be exposed
def update(state):
    state['averageAge'] = "{:.2f}".format(data['Age'].mean())
    state['totalFare'] = "{:.2f}".format(data['Fare'].sum())
    state['averageFare'] = "{:.2f}".format(data['Fare'].mean())
    state['countMale'] = ((data['Sex']=='male')*1.0).sum()
    state['countFemale'] = ((data['Sex']=='female')*1.0).sum()
    dataDeads = data.loc[data['Survived']==0,['Survived','Sex']].groupby(by='Sex').count()
    state['figDeads'] = px.pie(dataDeads, values='Survived', names=dataDeads.index, hole=.3, title='Died by Sex', width = 250, height = 250)
    dataDeads = data.loc[data['Survived']==1,['Survived','Sex']].groupby(by='Sex').count()
    state['figSurvs'] = px.pie(dataDeads, values='Survived', names=dataDeads.index, hole=.3, title='Survived by Sex', width = 250, height = 250)
    dataDeads = data.loc[data['Survived']==1,['Survived','Pclass']].groupby(by='Pclass').count()
    state['figPclass'] = px.pie(dataDeads, values='Survived', names=dataDeads.index, hole=.3, title='Survived by Class', width = 250, height = 250)
    dataDeads = data[['PassengerId','Survived','Age']].groupby(by=['Survived','Age']).count()
    dat = dataDeads.index.to_frame()
    state['figSurvAge'] = px.bar(dataDeads, x=dataDeads.index, y="Survived", color=dat.Survived, title="Long-Form Input")
# Initialise the state

# "_my_private_element" won't be serialised or sent to the frontend,
# because it starts with an underscore

initial_state = ss.init_state({
    "my_app": {
        "title": "My App"
    },
    "averageAge": 0.0,
    "totalFare": 0.0,
    "averageFare": 0.0,
    "countMale": 0,
    'countFemale': 0,
    'figDeads': None,
    'figSurvs': None,
    'figPclass': None,
})

update(initial_state)