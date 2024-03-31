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


module = Blueprint("gimsins", __name__, url_prefix="/gimsins")


@module.route("")
def index():
    gimsins = models.GimSin.objects(status="active")
    datas = []
    for gimsin in gimsins:
        cover_image = gimsin.get_cover_image()
        url = None
        if cover_image:
            url = url_for(
                "pictures.download",
                picture_id=cover_image.id,
                filename=cover_image.file.filename,
            )

        data = dict(
            id=gimsin.id,
            name=gimsin.name,
            name_zh=gimsin.name_zh,
            name_en=gimsin.name_en,
            gong=gimsin.gong.id,
            shrine=gimsin.shrine.id,
            coordinates=gimsin.coordinates,
            cover_image_url=url,
        )

        datas.append(data)
    return jsonify(datas)
