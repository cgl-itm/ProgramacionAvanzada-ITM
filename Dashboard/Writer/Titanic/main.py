import writer as wf
import pandas as pd
import plotly.express as px

df = pd.read_csv('https://raw.githubusercontent.com/datasciencedojo/datasets/refs/heads/master/titanic.csv')

df['Died'] = 1-df['Survived'] #0->1 y 1->0

def update(state):
    state["promedioEdad"] = "{0:.2f}".format(df['Age'].mean())
    state["totalFare"] = "{0:.2f}".format(df['Fare'].sum())
    state["averageFare"] = "{0:.2f}".format(df['Fare'].mean())
    state["cantidadMale"] = str((df['Sex']=='male').sum())
    state["cantidadFemale"] = str((df['Sex']=='female').sum())
    state['figDiedSex'] = px.pie(df, values='Died', names='Sex', title="Died by Sex")
    state['figSurSex'] = px.pie(df, values='Survived', names='Sex', title="Survived by Sex")
    state['figClassSex'] = px.pie(df, values='Survived', names='Pclass', title="Survived by Sex")
    
    state['figCountAge'] =  px.histogram(df, x="Age", color="Survived", nbins=21)
    dfSort = df.sort_values('SibSp',ascending=False)
    dfTop = dfSort.iloc[:10,[3,6]]
    
    state['figSiblings'] = px.bar(dfTop, x='SibSp', y="Name", orientation='h')
    dfEm = df.groupby('Embarked')['Survived'].sum()
    print(dfEm)
    state['figEmbar'] = px.bar(dfEm)
    dfEmC = df.groupby('Embarked')['Name'].count()
    state['figEmC'] = px.bar(dfEmC)

initial_state = wf.init_state({
    "promedioEdad": 0,
    "totalFare": 0,
    "averageFare": 0,
    "cantidadMale": 0,
    "cantidadFemale": 0,
    "seleccion": "A",
    "figSurSex": None,
    "figDiedSex": None,
    'figClassSex': None,
    'figCountAge': None,
    'figSiblings': None,
    'figEmbar': None,
    'figEmC': None
})

update(initial_state)