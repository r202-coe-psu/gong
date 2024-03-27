from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, current_user

from gong import models
from .. import forms

import datetime

module = Blueprint("pictures", __name__, url_prefix="/pictures")


@module.route("")
@login_required
def index():
    pictures = models.pictures.Gong.objects()
    return render_template("/pictures/index.html", pictures=pictures)


@module.route("/<picture_id>/download/<file_name>")
def download(picture_id, file_name):
    picture = models.Picture.objects.get(id=picture_id)

    if not picture or not picture.picture or picture.file.filename != filename:
        return abort(403)

    response = send_file(
        picture.file,
        download_name=picture.picture.filename,
        mimetype=picture.picture.content_type,
    )

    return response


@module.route(
    "/upload/{type_}/{type_id}",
    methods=["POST"],
)
@login_required
def upload(type_, type_id):

    form = forms.pictures.PictureForm()

    if not form.validate_on_submit():
        return render_template(
            "/meetings/report.html",
            form=form,
        )

    picture = None
    url = ""

    if type_ == "gong":
        picture = models.GongPictur()
        picture.gong = type_obj
        url = url_for("gongs.view", gong_id=type_obj.id)
    elif type_ == "shrine":
        picture = models.GongPictur()
        picture.shrine = type_obj
        url = url_for("shrines.view", shrines_id=type_obj.id)
    elif type_ == "gimsin":
        picture = models.GimSinPicture()
        picture.gimsin = type_obj
        url = url_for("gimsins.view", gimsins_id=type_obj.id)

    if picture:
        picture.save()

    form.populate_obj(picture)
    picture.updated_date = datetime.datetime.now()
    picture.owner = current_user._get_current_object()
    picture.ip_address = request.headers.get("X-Forwarded-For", request.remote_addr)

    picture.file.put(
        form.uploaded_file.data,
        filename=form.uploaded_file.data.filename,
        content_type=form.uploaded_file.data.content_type,
    )

    return redirect(url)
