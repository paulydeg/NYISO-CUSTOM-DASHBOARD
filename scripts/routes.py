from flask import Blueprint, render_template, request, send_file
from .data_processing import fetch_data, filter_data, calculate_metrics, export_csv, NYISO_ZONES
from .visualization import create_interactive_plot
import json
import plotly
from datetime import datetime

main_bp = Blueprint('main', __name__)
export_bp = Blueprint('export', __name__)
tools_bp = Blueprint('tools', __name__)

@main_bp.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        selected_zones = request.form.getlist('zones')
        start_date = request.form.get('start_date', '2024-01-01')
        end_date = request.form.get('end_date', '2024-01-31')
    else:
        # Default empty selection
        selected_zones = []
        start_date = '2024-01-01'
        end_date = '2024-01-31'

    # Use start_date and end_date instead of year
    data = fetch_data(start_date=start_date, end_date=end_date)
    filtered_data = filter_data(data, zones=selected_zones, start_date=start_date, end_date=end_date)

    if not selected_zones or filtered_data.empty:
        # No data selected or empty data
        metrics = {}
        fig = None
    else:
        metrics = calculate_metrics(filtered_data)
        fig = create_interactive_plot(filtered_data)

    graph_json = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder) if fig else None

    return render_template('index.html', 
                           graph_json=graph_json, 
                           zones=NYISO_ZONES,
                           metrics=metrics, 
                           selected_zones=selected_zones, 
                           start_date=start_date, 
                           end_date=end_date)

@export_bp.route('/export', methods=['GET', 'POST'])
def export_view():
    if request.method == 'POST':
        selected_zones = request.form.getlist('zones')
        start_date = request.form.get('start_date', '2024-01-01')
        end_date = request.form.get('end_date', '2024-01-31')

        # Use start_date and end_date instead of year
        data = fetch_data(start_date=start_date, end_date=end_date)
        filtered_data = filter_data(data, zones=selected_zones, start_date=start_date, end_date=end_date)

        if filtered_data.empty:
            # If no data, perhaps show a flash message or redirect back
            return render_template('export.html', zones=NYISO_ZONES, message="No data available for the selected criteria.")

        filename = f"nyiso_export_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
        filepath = export_csv(filtered_data, filename)
        return send_file(filepath, as_attachment=True)

    return render_template('export.html', zones=NYISO_ZONES)
