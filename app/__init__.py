from flask import Flask
from .blueprint.example_blueprint import geolocation 

def create_app():
    app = Flask(__name__)

    app.register_blueprint(geolocation)

    return app


    