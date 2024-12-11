import pandas as pd
from datetime import datetime
from nyisotoolkit import NYISOData
import os

NYISO_ZONES = [
    'CAPITL', 'CENTRL', 'DUNWOD', 'GENESE', 'HUD VL',
    'LONGIL', 'MHK VL', 'MILLWD', 'N.Y.C.', 'NORTH',
    'WEST', 'NYCA'
]

def fetch_data(start_date=None, end_date=None):
    """
    Fetch data for the specified date range.
    If no dates are provided, defaults to fetching the full year of 2024.
    """
    # Determine year range from start_date and end_date
    start_year = pd.to_datetime(start_date).year if start_date else 2024
    end_year = pd.to_datetime(end_date).year if end_date else 2024

    # Fetch data for each year in the range and combine them
    data_frames = []
    for year in range(start_year, end_year + 1):
        yearly_data = NYISOData(dataset='load_h', year=str(year)).df
        yearly_data.index = pd.to_datetime(yearly_data.index)
        yearly_data = yearly_data.tz_convert('US/Eastern')
        data_frames.append(yearly_data)

    # Combine all data into one DataFrame
    data = pd.concat(data_frames)

    # Filter data based on exact start_date and end_date
    if start_date:
        data = data[data.index >= pd.to_datetime(start_date).tz_localize(data.index.tz)]
    if end_date:
        data = data[data.index <= pd.to_datetime(end_date).tz_localize(data.index.tz)]

    return data

def filter_data(data, zones=None, start_date=None, end_date=None):
    df = data.copy()
    if zones and len(zones) > 0:
        cols_to_keep = [col for col in df.columns if col in zones]
        df = df[cols_to_keep]

    if start_date:
        start_ts = pd.to_datetime(start_date).tz_localize(df.index.tz)
        df = df[df.index >= start_ts]

    if end_date:
        end_ts = pd.to_datetime(end_date).tz_localize(df.index.tz)
        df = df[df.index <= end_ts]

    return df

def calculate_metrics(df):
    # Basic metrics: average and peak load
    metrics = {}
    for col in df.columns:
        metrics[col] = {
            'average_load': df[col].mean(),
            'peak_load': df[col].max()
        }
    return metrics

def export_csv(df, filename='exported_data.csv'):
    export_path = os.path.join('exports', filename)
    df.to_csv(export_path)
    return export_path
