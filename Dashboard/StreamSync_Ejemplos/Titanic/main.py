import streamsync as ss
import pandas as pd
import plotly.express as px

# This is a placeholder to get you started or refresh your memory.
# Delete it or adapt it as necessary.
# Documentation is available at https://streamsync.cloud

# Shows in the log when the app starts
dataset = pd.read_csv('https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv')


# Its name starts with _, so this function won't be exposed
def update(state):
    data = dataset.copy()
    if state['sex']=='female':
        data = dataset[dataset['Sex']=='female']
    if state['sex']=='male':
        data = dataset[dataset['Sex']=='male'] 
    state['averageAge'] = "{:.2f}".format(data['Age'].mean())
    state['totalFare'] = "{:.2f}".format(data['Fare'].sum())
    state['averageFare'] = "{:.2f}".format(data['Fare'].mean())
    state['countMale'] = ((data['Sex']=='male')*1.0).sum()
    state['countFemale'] = ((data['Sex']=='female')*1.0).sum()
    dataDeads = data.loc[data['Survived']==0,['Survived','Sex']].groupby(by='Sex').count()
    state['figDeads'] = px.pie(dataDeads, values='Survived', names=dataDeads.index, hole=.3, title='Died by Sex', width = 380, height = 250)
    dataDeads = data.loc[data['Survived']==1,['Survived','Sex']].groupby(by='Sex').count()
    state['figSurvs'] = px.pie(dataDeads, values='Survived', names=dataDeads.index, hole=.3, title='Survived by Sex', width = 380, height = 250)
    dataDeads = data.loc[data['Survived']==1,['Survived','Pclass']].groupby(by='Pclass').count()
    state['figPclass'] = px.pie(dataDeads, values='Survived', names=dataDeads.index, hole=.3, title='Survived by Class', width = 380, height = 250)
    #dataDeads = data[['PassengerId','Survived','Age']].groupby(by=['Survived','Age']).count()
    #dat = dataDeads.index.to_frame()
    #print(dat.Survived.values.astype(str))
    #state['figSurvAge'] = px.bar(dataDeads, x=dat.Age.values, y=dataDeads.PassengerId.values, color=dat.Survived.values.astype(str), title="Long-Form Input")
    state['figSurvAge'] = px.histogram(data, x="Age", color="Survived", nbins=21, width = 380, height = 1.5*250)
    
    dataSib10 = data.sort_values(by='SibSp', ascending=False).iloc[:10,[3,6]]
    state['figSibSp'] = px.bar(dataSib10.sort_values(by='SibSp'), x="SibSp", y="Name", orientation='h', width = 380, height = 1.5*250)  
    dataDeads = data.loc[data['Survived']==1,['Survived','Embarked']].groupby(by='Embarked').count()
    state['figEmbarked'] = px.bar(dataDeads,x=dataDeads.index, y="Survived", width = 380, height = 1.5*250)

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
    'figSibSp': None,
    'figEmbarked': None,
    'sex': 'all',
})

update(initial_state)