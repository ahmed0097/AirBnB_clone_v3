#!/usr/bin/python3
"""index"""

from api.v1.views import app_views
from flask import jsonify
from models import storage
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status():
    """Status of API"""
    if request.method == "GET":
        res = {"status: "OK"}
    return jsonify(res)


@app_views.route('/stats', methods=['GET'], strict_slashes=False)
def obj_number():
    """returns the count for all objects"""
    all_counts = {
        "amenities": storage.count(Amenity),
        "cities": storage.count(City),
        "places": storage.count(Place),
        "reviews": storage.count(Review),
        "states": storage.count(State),
        "users": storage.count(User)
    }
    return jsonify(all_counts)

@app_views.app_errorhandler(404)
def not_found(e):
    """Page not found."""
    response = {"error": "Not found"}
    return jsonify(response), e.code
    