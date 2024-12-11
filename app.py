# app.py

from flask import Flask
from scripts.routes import main_bp, export_bp, tools_bp

def create_app():
    app = Flask(__name__)
    app.register_blueprint(main_bp, url_prefix='/')
    app.register_blueprint(export_bp, url_prefix='/')
    app.register_blueprint(tools_bp, url_prefix='/')
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
