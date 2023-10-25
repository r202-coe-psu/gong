from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, current_user

from gong import models
from .. import forms

import datetime

module = Blueprint("dashboard", __name__, url_prefix="/dashboard")


@module.route("/admin")
@login_required
def index_admin():
    return render_template(
        "/dashboard/index-admin.html",
    )


def index_user():
    return render_template("/dashboard/index-user.html")


@module.route("")
@login_required
def index():
    user = current_user
    dev = request.args.get("dev")
    if dev == "test":
        return index_student()
    if "admin" in user.roles:
        return redirect(url_for("dashboard.index_admin"))

    return index_user()
