import dash
from dash import dcc, html, dash_table
from dash.dependencies import Input, Output
import pandas as pd

# Sample Data
data = {
    "Date": ["2024-01-01", "2024-01-02", "2024-01-03", "2024-01-04"],
    "Distance (km)": [30, 45, 25, 60],
    "Elevation Gain (m)": [300, 500, 250, 600],
    "Average Speed (km/h)": [25, 30, 20, 28],
}
df = pd.DataFrame(data)

# Initialize Dash App
app = dash.Dash(__name__)
app.title = "Cycling Activity Dashboard"

# Layout
app.layout = html.Div([
    html.H1("Cycling Activity Dashboard"),
    dcc.Graph(
        id="line-chart",
        config={"displayModeBar": False},
    ),
    dash_table.DataTable(
        id="data-table",
        columns=[{"name": col, "id": col} for col in df.columns],
        data=df.to_dict("records"),
        style_table={'overflowX': 'auto'},
        style_cell={
            'textAlign': 'left',
            'padding': '10px',
        },
    ),
    dcc.Dropdown(
        id="metric-dropdown",
        options=[
            {"label": "Distance (km)", "value": "Distance (km)"},
            {"label": "Elevation Gain (m)", "value": "Elevation Gain (m)"},
            {"label": "Average Speed (km/h)", "value": "Average Speed (km/h)"},
        ],
        value="Distance (km)",
        clearable=False,
        style={"width": "50%"},
    )
])

# Callback for Line Chart
@app.callback(
    Output("line-chart", "figure"),
    [Input("metric-dropdown", "value")]
)
def update_line_chart(metric):
    return {
        "data": [{
            "x": df["Date"],
            "y": df[metric],
            "type": "line",
            "name": metric,
            "line": {"width": 3}
        }],
        "layout": {
            "title": f"{metric} Over Time",
            "xaxis": {"title": "Date"},
            "yaxis": {"title": metric},
        }
    }

# Run the App
if __name__ == "__main__":
    app.run_server(debug=True)
