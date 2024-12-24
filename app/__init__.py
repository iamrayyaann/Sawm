from flask import Flask
from app.routes.main import main  # Import the main blueprint

def create_app():
    
    app = Flask(__name__, static_folder='static', template_folder='templates')
    from .routes.main import main_bp
    app.register_blueprint(main_bp)
    
    return app