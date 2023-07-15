#!/usr/bin/python3
"""
Web server 
"""

from flask import Blueprint, jsonify
from api.v1.views import app_views
from flask import Flask

app = Flask(__name__)
#app_views = Blueprint('app_views', __name__)


@app_views.route('/api/v1/status', methods=['GET'])
def get_status():
    """Handler for /api/v1/status route"""
    return jsonify({"status": "API is running"})


# Other routes for your application...


# Register the blueprint
app.register_blueprint(app_views)
