from flask import Blueprint, jsonify


module = Blueprint("api", __name__, url_prefix="/api")


@module.route("")
def index():
    return jsonify({})
