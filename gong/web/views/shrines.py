from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, current_user

from gong import models
from .. import forms

import datetime

module = Blueprint("shrines", __name__, url_prefix="/shrines")


@module.route("")
@login_required
def index():
    shrines = models.Shrine.objects()
    return render_template("/shrines/index.html", shrines=shrines)


@module.route("/create", methods=["GET", "POST"], defaults=dict(shrine_id=None))
@module.route("/<shrine_id>/edit", methods=["GET", "POST"])
@login_required
def create_or_edit(shrine_id):
    shrine = None

    form = forms.shrines.ShrineForm()
    if shrine_id:
        shrine = models.Shrine.objects.get(id=shrine_id)
        form = forms.shrines.ShrineForm(obj=shrine)

    if not form.validate_on_submit():
        return render_template("/shrines/create-or-edit.html", form=form)

    if not shrine:
        shrine = models.Shrine()

    form.populate_obj(shrine)
    shrine.save()

    return redirect(url_for("shrines.view", shrine_id=shrine.id))


@module.route("/<shrine_id>")
def view(shrine_id):
    shrine = models.Shrine.objects.get(id=shrine_id, status="active")
    if not shrine:
        return redirect(url_for("shrines.index"))

    return render_template("/shrines/view.html", shrine=shrine)
