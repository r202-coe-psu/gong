from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, current_user

from gong import models
from .. import forms

import datetime

module = Blueprint("shrines", __name__, url_prefix="/shrines")


@module.route("")
@login_required
def index():
    shrines = models.shrines.Gong.objects()
    return render_template("/shrines/index.html", shrines=shrines)
