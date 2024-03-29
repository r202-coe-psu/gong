from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, current_user

from ... import models
from .. import forms

import datetime

module = Blueprint("gimsins", __name__, url_prefix="/gimsins")


@module.route("")
@login_required
def index():
    gimsins = models.gimsins.Gong.objects()
    return render_template("/gimsins/index.html", gimsins=gimsins)


@module.route("/create", methods=["GET", "POST"], defaults=dict(gimsin_id=None))
@module.route("/<gimsin_id>/edit", methods=["GET", "POST"])
@login_required
def create_or_edit(gimsin_id):
    gimsin = None

    form = forms.gimsins.GongForm()
    if gimsin_id:
        gimsin = models.gimsins.Gong.objects.get(id=gimsin_id)
        form = forms.gimsins.GongForm(obj=gimsin)

    if not form.validate_on_submit():
        print(form.errors)
        return render_template("/gimsins/create-or-edit.html", form=form)

    if not gimsin:
        gimsin = models.Gong()

    form.populate_obj(gimsin)
    gimsin.save()

    return redirect(url_for("gimsins.index"))


@module.route("/<gimsin_id>")
def view(gimsin_id):
    return render_template("/gimsins/index.html")
