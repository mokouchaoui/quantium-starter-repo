import dash
from dash import dcc, html
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

# Define the layout
app.layout = html.Div(children=[
    html.H1(children="Pink Morsels Sales Analysis", style={"textAlign": "center"}),

    html.P("Visualizing sales data before and after the price increase on January 15, 2021."),

    # Line chart for sales over time
    dcc.Graph(
        id="sales-line-chart",
        figure=px.line(
            df,
            x="date",
            y="sales",
            color="region",
            title="Sales Trend Over Time",
            labels={"date": "Date", "sales": "Total Sales", "region": "Region"},
            line_shape="linear",
        )
    )
])

# Run the app
if __name__ == "__main__":
    app.run_server(debug=True)
