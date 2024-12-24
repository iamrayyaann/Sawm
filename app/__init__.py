from flask import Flask
from app.routes.main import main  # Import the main blueprint

def create_app():
    app = Flask(__name__)
    app.register_blueprint(main)  # Register the blueprint here
    return app