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
