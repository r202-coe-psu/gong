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

from ... import forms
from ... import acl
from .... import models

module = Blueprint("gongs", __name__, url_prefix="/gongs")


@module.route("")
@login_required
@acl.roles_required("admin")
def index():
    return render_template("/admin/gongs/index.html")


@module.route("/create", defaults=dict(gong_id=None), methods=["GET", "POST"])
@module.route("/<gong_id>/edit", methods=["GET", "POST"])
@acl.roles_required("admin")
def create_or_edit(gong_id):
    form = forms.gongs.GongForm()
    gong = None
    if gong_id:
        gong = models.gongs.Gong.objects.get(id=gong_id)
        form = forms.gongs.Gong(obj=gong)

    if not form.validate_on_submit():
        return render_template("/admin/gongs/create-or-edit.html", form=form)

    return render_template("/admin/gongs/index.html")
