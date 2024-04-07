from wtforms import validators
from wtforms import fields, widgets
from .fields import TextListField, CoordinatesField

from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed
from flask_mongoengine.wtf import model_form

from .. import models


BaseShrineForm = model_form(
    models.Shrine,
    FlaskForm,
    exclude=["created_date", "updated_date", "creator", "status"],
    field_args=dict(
        name=dict(label="Name"),
        name_zh=dict(label="Chinese Name"),
        name_en=dict(label="English Name"),
        opened_date=dict(label="Opened Date", validators=[validators.Optional()]),
        biography=dict(label="Biograpy"),
        presidents=dict(label="Presidents"),
        coordinates=dict(label="Coordinates"),
        location=dict(label="Location"),
    ),
)


class ShrineForm(BaseShrineForm):
    coordinates = CoordinatesField("Coordinates", widget=widgets.TextInput())
    links = TextListField("Links", widget=widgets.TextInput())
