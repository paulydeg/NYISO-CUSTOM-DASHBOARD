# scripts/visualization.py

import plotly.graph_objs as go
from plotly.subplots import make_subplots

def create_interactive_plot(df):
    # Create a line plot for each selected zone
    fig = make_subplots(specs=[[{"secondary_y": False}]])
    for col in df.columns:
        fig.add_trace(go.Scatter(x=df.index, y=df[col], mode='lines', name=col))
    fig.update_layout(
        title='NYISO Load Data',
        xaxis_title='Date and Time',
        yaxis_title='Load (MW)',
        hovermode='x'
    )
    return fig
