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


module = Blueprint("shrines", __name__, url_prefix="/shrines")


@module.route("")
def index():
    shrines = models.Shrine.objects()
    return jsonify(shrines)
