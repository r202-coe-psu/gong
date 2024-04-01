from flask import Blueprint, render_template, request, redirect, url_for, send_file
from flask_login import login_required, current_user

from gong import models
from .. import forms

import datetime

module = Blueprint("pictures", __name__, url_prefix="/pictures")


@module.route("")
@login_required
def index():
    pictures = models.BasePicture.objects()
    return render_template("/pictures/index.html", pictures=pictures)


@module.route("/<picture_id>/download/<filename>")
def download(picture_id, filename):

    picture = models.BasePicture.objects.get(id=picture_id)

    if not picture or not picture.file or picture.file.filename != filename:
        return abort(403)

    response = send_file(
        picture.file,
        download_name=picture.file.filename,
        mimetype=picture.file.content_type,
    )

    return response


@module.route("/<picture_id>/set-cover/<type_>/<type_id>")
def set_cover_image(picture_id, type_, type_id):

    picture = models.BasePicture.objects.get(id=picture_id)
    type_objs = None
    if type_ == "gong":
        type_obj = models.Gong.objects(id=type_id, status="active").first()
        models.GongPicture.objects(gong=type_obj).update(set__is_cover=False)
    elif type_ == "shrine":
        type_obj = models.Shrine.objects(id=type_id, status="active").first()
        models.ShrinePicture.objects(shrine=type_obj).update(set__is_cover=False)
    elif type_ == "gimsin":
        type_obj = models.GimSin.objects(id=type_id, status="active").first()
        models.GimSinPicture.objects(gimsin=type_obj).update(set__is_cover=False)

    picture.is_cover = True
    picture.save()

    return redirect(url_for("pictures.manage", type_=type_, type_id=type_id))


@module.route(
    "/<type_>/<type_id>",
    methods=["GET", "POST"],
)
@login_required
def manage(type_, type_id):
    type_obj = None
    pictures = []
    if type_ == "gong":
        type_obj = models.Gong.objects(id=type_id, status="active").first()
        pictures = models.GongPicture.objects(gong=type_obj)
    elif type_ == "shrine":
        type_obj = models.Shrine.objects(id=type_id, status="active").first()
        pictures = models.ShrinePicture.objects(shrine=type_obj)
    elif type_ == "gimsin":
        type_obj = models.GimSin.objects(id=type_id, status="active").first()
        pictures = models.GimSinPicture.objects(gimsin=type_obj)

    form = forms.pictures.UploadPicturesForm()

    return render_template(
        "/pictures/manage.html",
        form=form,
        type_=type_,
        type_obj=type_obj,
        type_id=type_id,
        pictures=pictures,
    )


@module.route(
    "/upload/<type_>/<type_id>",
    methods=["GET", "POST"],
)
@login_required
def upload(type_, type_id):

    type_obj = None
    if type_ == "gong":
        type_obj = models.Gong.objects(id=type_id, status="active").first()
    elif type_ == "shrine":
        type_obj = models.Shrine.objects(id=type_id, status="active").first()
    elif type_ == "gimsin":
        type_obj = models.GimSin.objects(id=type_id, status="active").first()

    form = forms.pictures.UploadPicturesForm()

    if not form.validate_on_submit():
        return redirect(url_for("pictures.manage", type_=type_, type_id=type_id))

    for f in form.uploaded_files.data:
        if type_ == "gong":
            picture = models.GongPicture()
            picture.gong = type_obj
        elif type_ == "shrine":
            picture = models.ShrinePicture()
            picture.shrine = type_obj

        elif type_ == "gimsin":
            picture = models.GimSinPicture()
            picture.gimsin = type_obj

        picture.public = form.public.data
        picture.updated_date = datetime.datetime.now()
        picture.owner = current_user._get_current_object()
        picture.ip_address = request.headers.get("X-Forwarded-For", request.remote_addr)

        picture.file.put(
            f,
            filename=f.filename,
            content_type=f.content_type,
        )
        picture.save()

    return redirect(url_for("pictures.manage", type_=type_, type_id=type_id))
