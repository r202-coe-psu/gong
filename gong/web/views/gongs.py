import datetime
import markdown
import mongoengine as me

from flask import (
    Blueprint,
    render_template,
    url_for,
    redirect,
    request,
    session,
    current_app,
    send_file,
    abort,
)
from flask_login import login_required, current_user

from ... import models
from .. import forms

module = Blueprint("gongs", __name__, url_prefix="/gongs")


@module.route("")
@login_required
def index():
    return render_template("/gongs/index.html")


@module.route("/<gong_id>")
def view(gong_id):
    return render_template("/gongs/index.html")
