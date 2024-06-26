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
    return render_template("/site/index.html", gongs=gongs)
