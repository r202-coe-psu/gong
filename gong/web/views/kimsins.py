from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, current_user

from gong import models
from .. import forms

import datetime

module = Blueprint("kimsins", __name__, url_prefix="/kimsins")


@module.route("")
@login_required
def index():
    kimsins = models.kimsins.Gong.objects()
    return render_template("/kimsins/index.html", kimsins=kimsins)
