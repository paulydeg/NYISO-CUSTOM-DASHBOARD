NYISO Custom Dashboard

Overview

This project is a custom NYISO (New York Independent System Operator) dashboard designed to retrieve, process, and visualize energy market data. The dashboard is built with Flask and integrates the NYISO Toolkit, allowing users to fetch data, filter it by various criteria, and perform analysis. The primary goal is to support energy load forecasting and related tasks for the NYISO energy market.

Features

Data Retrieval

Fetch hourly load data (load_h) for any year from NYISO.

Filter data by specific NYISO zones and date ranges.

Support for additional datasets, including LBMP (Locational Based Marginal Pricing) and generator schedules.

Visualization

Interactive graphs for hourly load data.

Visualize data for specific zones or aggregate metrics like NYCA (New York Control Area).

The dashboard uses Plotly for interactive plotting.

Data Export

Export filtered data to CSV format.

Easy integration with additional formats if needed.

Web Interface

Intuitive web interface built with Flask and Bootstrap.

Dynamic theming with Bootstrap themes (e.g., Cyborg).

Navigation links for main features: data visualization, export tools, and custom tools.

Backend Capabilities

Powered by the NYISO Toolkit for data processing and API calls.

Modular structure for scalability.

Project Structure

image_q/
├── app.py                # Main Flask application entry point
├── scripts/              # Custom scripts for processing and visualization
│   ├── data_processing.py
│   ├── visualization.py
│   └── routes.py
├── templates/            # HTML templates for the web interface
│   ├── layout.html       # Base layout
│   └── index.html        # Main dashboard page
├── static/               # Static files (CSS, JS)
├── models/               # Placeholder for machine learning models
├── exports/              # Directory for exported CSV files
├── venv/                 # Python virtual environment
├── README.md             # Project documentation
└── requirements.txt      # Python dependencies

Installation

Prerequisites

Python 3.10 or higher

pip (Python package manager)

Virtualenv (recommended)

Steps

Clone the repository:

git clone git@github.com:paulydeg/NYISO-CUSTOM-DASHBOARD.git
cd NYISO-CUSTOM-DASHBOARD

Set up a virtual environment:

python3 -m venv venv
source venv/bin/activate

Install required packages:

pip install -r requirements.txt

Run the Flask app:

flask run

Open the dashboard in your browser at:
http://127.0.0.1:5000

Key Components

NYISO Toolkit

The NYISO Toolkit is used to fetch and process NYISO data. Key features include:

Fetching datasets such as load_h, lbmp_dam_h, and lbmp_rt_5m.

Support for multiple years of data.

Data quality checks and preprocessing.

Flask Routes

/: Main dashboard page for visualizing data.

/export: Export filtered data to CSV.

/custom_tools: Placeholder for additional custom tools.

Scripts

data_processing.py:

Fetch and filter NYISO data.

Calculate metrics like average and peak loads.

Export data to CSV.

visualization.py:

Generate interactive Plotly graphs.

routes.py:

Define Flask routes for the dashboard.

Customizations

Themes

The dashboard supports Bootstrap themes. Current setup uses the Cyborg theme. Other themes can be easily integrated.

Adding New Datasets

To support additional datasets:

Update SUPPORTED_DATASETS in nyisodata.py.

Add corresponding logic in data_processing.py and visualization.py.

Future Enhancements

Integration with Generator Scheduling

Extend API calls to fetch generator scheduling data.

Enhanced ML Capabilities

Use machine learning models for predictive analytics.

Improved Export Options

Support for exporting in additional formats (e.g., Excel, JSON).

User Authentication

Add user login and access control.

Real-Time Data Updates

Fetch and display real-time NYISO data.

Contributions

Contributions are welcome! Please submit a pull request with detailed information on proposed changes.

License

This project is licensed under the MIT License.

Contact

For questions or support, please contact:

GitHub: paulydeg

Email: paulydeg@example.com

Happy forecasting!