from flask import Blueprint

# Define the blueprint
main = Blueprint('main', __name__)

# Import routes defined in main.py
from . import main