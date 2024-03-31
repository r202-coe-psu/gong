from wtforms import validators
from wtforms import fields, widgets
from .fields import TextListField, CoordinatesField

from flask_wtf import FlaskForm
from flask_mongoengine.wtf import model_form

from .. import models


BaseGimSinForm = model_form(
    models.GimSin,
    FlaskForm,
    exclude=[
        "created_date",
        "updated_date",
        "creator",
        "status",
    ],
    field_args=dict(
        name=dict(label="Name"),
        name_zh=dict(label="Chinese Name"),
        name_en=dict(label="English Name"),
        gong=dict(label="Gong", label_modifier=lambda g: g.name),
        shrine=dict(label="Shrine", label_modifier=lambda s: s.name),
        biography=dict(label="Biograpy"),
    ),
)


class GimSinForm(BaseGimSinForm):
    coordinates = CoordinatesField("Coordinates", widget=widgets.TextInput())
