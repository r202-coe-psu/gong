from flask import Blueprint, render_template, redirect, url_for
import datetime

from ... import models
from .. import caches

module = Blueprint("site", __name__)


@module.route("/")
@caches.cache.cached(timeout=600)
def index():
    now = datetime.datetime.now()
    gongs = models.Gong.objects(status="active")
    gongs_shrines = []
    for gong in gongs:
        gongs_shrines.append((len(gong.get_shrines()), gong))

    gongs_shrines.sort(
        key=lambda gong_shrine: (gong_shrine[0], gong_shrine[1].name), reverse=True
    )
    return render_template("/site/index.html", gongs_shrines=gongs_shrines)
