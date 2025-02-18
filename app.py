import dash
import dash_bootstrap_components as dbc
from dash import html

# Initialize the Dash app
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Define the layout
app.layout = dbc.Container(
    [
        dbc.Row(
            dbc.Col(html.H1("Welcome to the Plotly Dash App"), className="text-center")
        ),
        dbc.Row(
            dbc.Col(html.P("This is a simple Dash application using Bootstrap components."), className="text-center")
        ),
    ],
    fluid=True,
)

# Run the app
if __name__ == "__main__":
    app.run_server(debug=True)
