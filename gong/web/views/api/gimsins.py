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
from .. import add_date_url


module = Blueprint("gimsins", __name__, url_prefix="/gimsins")


@module.route("")
def index():
    args = request.args
    gimsins = []
    if args.get("shrine_id"):
        shrine = models.Shrine.objects(
            id=args.get("shrine_id"), status="active"
        ).first()
        gimsins = models.GimSin.objects(status="active", shrine=shrine)
    else:
        gimsins = models.GimSin.objects(status="active")

    datas = []
    for gimsin in gimsins:
        cover_image = gimsin.get_cover_image()
        url = None
        if cover_image:
            url = add_date_url(
                url_for(
                    "pictures.download",
                    picture_id=cover_image.id,
                    filename=cover_image.file.filename,
                )
            )

        data = dict(
            id=gimsin.id,
            name=gimsin.name,
            name_zh=gimsin.name_zh,
            name_en=gimsin.name_en,
            gong=dict(
                id=gimsin.gong.id,
                name=gimsin.gong.name,
                name_zh=gimsin.gong.name_zh,
                name_en=gimsin.gong.name_en,
            ),
            shrine=dict(
                id=gimsin.shrine.id,
                name=gimsin.shrine.name,
                name_zh=gimsin.shrine.name_zh,
                name_en=gimsin.shrine.name_en,
            ),
            coordinates=gimsin.coordinates,
            cover_image_url=url,
        )

        datas.append(data)
    return jsonify(datas)
