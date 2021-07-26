from flask import Flask
from .blueprint.example_blueprint import geolocation_main, geolocation

# created a function for running Flask app and to register the blueprints
def create_app() -> Flask:
    app = Flask(__name__)

    app.register_blueprint(geolocation_main)
    app.register_blueprint(geolocation)

    return app


    