from flask import Blueprint

example_blueprint = Blueprint("emaple_blueprint", __name__)

@example_blueprint.route("/")
def index():
    return "This is an example app"