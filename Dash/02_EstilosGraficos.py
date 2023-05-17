import dash
from dash import html
from dash import dcc
import plotly.graph_objs as go
import numpy as np

# Instanciate the app
app = dash.Dash()

# Simulated data
np.random.seed(42)
random_x = np.random.randint(1, 101, 100)
random_y = np.random.randint(1, 101, 100)

#Markers and Styiling
#https://plotly.com/python/marker-style/

# Define de layout
app.layout = html.Div([
    dcc.Graph(
      id = "scatter_plot",
      figure = {
        "data": [
          go.Scatter(
            x = random_x,
            y = random_y,
            mode = "markers",
            marker = dict(
              size = 12,
              color = "rgb(51, 204, 153)",
              symbol = "pentagon",
              line = dict(
                width = 2
              )
            )
          )
        ],
        "layout": go.Layout(
          title = "Scatter Plot",
          xaxis = dict(
            title = "X axis"
          )
        )
      }
    ),
    dcc.Graph(
      id = "new_scatter_plot",
      figure = {
        "data": [
          go.Scatter(
            x = random_x,
            y = random_y,
            mode = "markers",
            marker = dict(
              size = 12,
              color = "rgb(200, 204, 53)",
              symbol = "pentagon",
              line = dict(
                width = 2
              )
            )
          )
        ],
        "layout": go.Layout(
          title = "Second Scatter Plot",
          xaxis = dict(
            title = "X axis"
          )
        )
      }
    )
])

# Run server
if __name__ == "__main__":
  app.run_server(debug = True)