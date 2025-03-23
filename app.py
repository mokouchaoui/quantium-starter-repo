import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px

# Load the processed sales data
df = pd.read_csv("data/formatted_sales_data.csv")

# Convert date column to datetime format
df["date"] = pd.to_datetime(df["date"])

# Sort data by date
df = df.sort_values("date")

# Create the Dash app
app = dash.Dash(__name__)

# Define the layout with radio buttons for region selection
app.layout = html.Div(children=[
    html.H1("Pink Morsels Sales Analysis", className="header"),

    html.P("Filter by region to explore sales data.", className="description"),

    # Radio buttons for selecting region
    dcc.RadioItems(
        id="region-selector",
        options=[
            {"label": "All", "value": "all"},
            {"label": "North", "value": "north"},
            {"label": "East", "value": "east"},
            {"label": "South", "value": "south"},
            {"label": "West", "value": "west"}
        ],
        value="all",
        inline=True,
        className="radio-buttons"
    ),

    # Line chart for sales over time
    dcc.Graph(id="sales-line-chart")
])

# Define callback to update the chart based on selected region
@app.callback(
    Output("sales-line-chart", "figure"),
    Input("region-selector", "value")
)
def update_chart(selected_region):
    # Filter data by selected region
    filtered_df = df if selected_region == "all" else df[df["region"].str.lower() == selected_region]

    # Generate the updated line chart
    fig = px.line(
        filtered_df,
        x="date",
        y="sales",
        color="region",
        title="Sales Trend Over Time",
        labels={"date": "Date", "sales": "Total Sales", "region": "Region"},
        line_shape="linear",
    )

    return fig

# Run the app
if __name__ == "__main__":
    app.run_server(debug=True)
