from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, current_user

from gong import models
from .. import forms

import datetime

module = Blueprint("gimsins", __name__, url_prefix="/gimsins")


@module.route("")
@login_required
def index():
    gimsins = models.gimsins.GimSin.objects()
    return render_template("/gimsins/index.html", gimsins=gimsins)
