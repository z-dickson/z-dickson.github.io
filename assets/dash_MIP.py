import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

import plotly.express as px

# Function to create the Plotly figure
def create_figure():
    df = px.data.iris()  # Sample data
    fig = px.scatter(df, x='sepal_width', y='sepal_length', color='species')
    return fig

# Initialize the Dash app
app = dash.Dash(__name__)

# Layout of the Dash app
app.layout = html.Div([
    html.H1("My Plotly Figure"),
    dcc.Graph(figure=create_figure())
])

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
