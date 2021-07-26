from flask import Blueprint, render_template, request

from ..api.geolocation import get_location_info

# Created both blueprints for each endpoint needed, especified template folder 
geolocation_main = Blueprint("geolocation_main", __name__, template_folder='template')
geolocation = Blueprint("geolocation", __name__, template_folder='template')

# This is the main blueprint created placed in the root of the route 
@geolocation_main.route("/")
def get_location():
    return render_template('index.html')

# Endpoint for calculating the distance between location provided and Moscow Ring Road 
# Endpoint will recive a location and will run function get_location_info 
@geolocation.route("/distance", methods=['POST'])
def get_distance():
    if request.method == 'POST':
        address = request.form["address"]
        ubicacion = get_location_info(address)

    return ubicacion
