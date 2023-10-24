from wtforms import validators
from wtforms import fields
from .fields import TextListField

from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed
from flask_mongoengine.wtf import model_form

from .. import models


BaseGongForm = model_form(
    models.gongs.Gong,
    FlaskForm,
    exclude=[
        "created_date",
        "updated_date",
        "creator",
        "updater",
    ],
    field_args={
        "title": {"label": "Title"},
        "first_name": {"label": "First Name"},
        "last_name": {"label": "Last Name"},
        "title_th": {"label": "Thai Title"},
        "first_name_th": {"label": "Thai First Name"},
        "last_name_th": {"label": "Thai Last Name"},
        "biography": {"label": "Biography"},
        "email": {"label": "Email"},
    },
)


class GongForm(BaseGongForm):
    pic = fields.FileField(
        "Picture", validators=[FileAllowed(["png", "jpg"], "allow png and jpg")]
    )
