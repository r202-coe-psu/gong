from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, current_user

from gong import models
from .. import forms

import datetime

module = Blueprint("gongs", __name__, url_prefix="/gongs")


@module.route("")
@login_required
def index():
    gongs = models.gongs.Gong.objects()
    return render_template("/gongs/index.html", gongs=gongs)


@module.route("/create", methods=["GET", "POST"], defaults=dict(gong_id=None))
@module.route("/<gong_id>/edit", methods=["GET", "POST"])
@login_required
def create_or_edit(gong_id):
    gong = None

    form = forms.gongs.GongForm()
    if gong_id:
        gong = models.gongs.Gong.objects.get(id=gong_id)
        form = forms.gongs.GongForm(obj=gong)

    if not form.validate_on_submit():
        return render_template("/gongs/create-or-edit.html", form=form)

    if not gong:
        gong = models.Gong()

    form.populate_obj(gong)
    gong.save()

    return redirect(url_for("gongs.index"))


@module.route("/<gong_id>")
def view(gong_id):
    return render_template("/gongs/index.html")
