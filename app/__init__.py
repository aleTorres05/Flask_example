from flask import Flask
from .blueprint.example_blueprint import geolocation_main, geolocation

def create_app() -> Flask:
    app = Flask(__name__)

    app.register_blueprint(geolocation_main)
    app.register_blueprint(geolocation)

    return app


    