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


module = Blueprint("shrines", __name__, url_prefix="/shrines")


@module.route("")
def index():
    shrines = models.Shrine.objects(status="active")
    datas = []
    for shrine in shrines:
        cover_image = shrine.get_cover_image()
        url = None
        if cover_image:
            url = url_for(
                "pictures.download",
                picture_id=cover_image.id,
                filename=cover_image.file.filename,
            )

        data = dict(
            id=shrine.id,
            name=shrine.name,
            name_zh=shrine.name_zh,
            name_en=shrine.name_en,
            presidents=[
                dict(
                    id=president.gimsin.id,
                    name=president.gimsin.name,
                    name_zh=president.gimsin.name_zh,
                    name_en=president.gimsin.name_en,
                    cover_image_url=(
                        url_for(
                            "pictures.download",
                            picture_id=president.gimsin.get_cover_image().id,
                            filename=president.gimsin.get_cover_image().file.filename,
                        )
                        if president.gimsin.has_cover_image()
                        else ""
                    ),
                )
                for president in shrine.presidents
                if president.gimsin
            ],
            coordinates=shrine.coordinates,
            cover_image_url=url,
        )

        datas.append(data)
    return jsonify(datas)
