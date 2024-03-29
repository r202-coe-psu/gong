from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, current_user

from gong import models
from .. import forms

import datetime

module = Blueprint("tags", __name__, url_prefix="/tags")


@module.route("/<tag>")
@login_required
def view(tag):
    gongs = models.Gong.objects(tags=tag)
    return render_template("/tags/view.html", gongs=gongs, tag=tag)
