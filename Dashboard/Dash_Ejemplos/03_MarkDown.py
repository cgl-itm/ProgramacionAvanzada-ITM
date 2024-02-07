from os import stat_result
import dash
from dash import html
from dash import dcc

# Instanciate the app
app = dash.Dash()

markdown_text = """
### Dash and Markdown

Dash apps can be written in Markdown. Dash uses the [CommonMark](http://commonmark.org/) specification of Markdown.

Check out their [60 Second Markdown Tutorial](http://commonmark.org/help/) if this is your first introduction to Markdown!

Markdown includes syntax for things like **bold text** and *italics*, [links](http://commonmark.org/help), inline `code` snippets, lists, quotes, and more.
"""

# Define the layout
app.layout = html.Div([
  dcc.Markdown(children = markdown_text)
])

# Run app
if __name__ == "__main__":
  app.run_server(debug = True)