from flask import (
    Blueprint,
    render_template,
    request,
    redirect,
    url_for,
    send_file,
    jsonify,
)
from flask_login import login_required, current_user

from gong import models


module = Blueprint("gongs", __name__, url_prefix="/gongs")


@module.route("")
def index():
    gongs = models.Gong.objects(status="active")
    return jsonify(gongs)
