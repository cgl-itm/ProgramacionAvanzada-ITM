import dash
from dash import html
from dash import dcc
import plotly.graph_objs as go
from dash.dependencies import Input, Output
import pandas as pd

# Load the data
df = pd.read_csv("https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv")

# Instanciate the app
app = dash.Dash()

# Usar la base de datos de Titanic 
# Graficar Survived (eje Y) vs Age (eje X)
# Poner color por genero
# En el selector usar las clases (Pclass)

# Run the app
if __name__ == "__main__":
  app.run_server(debug = True)