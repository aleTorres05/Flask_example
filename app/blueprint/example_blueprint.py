from flask import Blueprint, render_template

geolocation = Blueprint("geolocation", __name__, template_folder='template')

@geolocation.route("/")
def get_location():
    return render_template('index.html')

@geolocation.route("/distance", methods=['GET'])
def get_distance():
    ...
