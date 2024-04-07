from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, current_user

from gong import models
from .. import forms
import mongoengine as me

import datetime

module = Blueprint("gongs", __name__, url_prefix="/gongs")


@module.route("")
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

    return redirect(url_for("gongs.view", gong_id=gong.id))


@module.route("/clans/<clan>")
def show_by_clan(clan):
    gongs = models.Gong.objects(
        (me.Q(clan=clan) | me.Q(clan_zh=clan) | me.Q(clan_en=clan)),
        status="active",
    )
    if not gongs:
        return redirect(url_for("gongs.index"))

    return render_template("/gongs/index.html", gongs=gongs)


@module.route("/blessings/<blessing>")
def show_by_blessing(blessing):
    gongs = models.Gong.objects(
        blessings=blessing,
        status="active",
    )
    if not gongs:
        return redirect(url_for("gongs.index"))

    return render_template("/gongs/index.html", gongs=gongs)


@module.route("/religions/<religion>")
def show_by_religion(religion):
    gongs = models.Gong.objects(
        religions=religion,
        status="active",
    )
    if not gongs:
        return redirect(url_for("gongs.index"))

    return render_template("/gongs/index.html", gongs=gongs)


@module.route("/<gong_id>")
def view(gong_id):
    gong = models.Gong.objects.get(id=gong_id, status="active")
    if not gong:
        return redirect(url_for("gongs.index"))

    return render_template("/gongs/view.html", gong=gong)
