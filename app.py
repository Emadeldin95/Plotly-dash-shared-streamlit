import dash
import dash_bootstrap_components as dbc
from dash import html, dash_table
import pandas as pd

# Initialize the Dash app
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Sample data for the table
data = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
})

# Define the layout
app.layout = html.Div([
    dbc.Container([
        dbc.Row([
            dbc.Col([
                html.H1("Data Table Example"),
                dash_table.DataTable(
                    id='data-table',
                    columns=[{"name": i, "id": i} for i in data.columns],
                    data=data.to_dict('records'),
                    style_table={'overflowX': 'auto'},
                    style_cell={
                        'textAlign': 'left',
                        'minWidth': '100px',
                        'width': '150px',
                        'maxWidth': '180px',
                        'whiteSpace': 'normal'
                    },
                    style_header={
                        'backgroundColor': '#007bff',
                        'color': 'white',
                        'fontWeight': 'bold'
                    }
                )
            ])
        ])
    ])
])

# Run the app
if __name__ == "__main__":
    app.run_server(debug=True)
