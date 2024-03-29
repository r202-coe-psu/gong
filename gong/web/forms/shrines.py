from wtforms import validators
from wtforms import fields, widgets
from .fields import TextListField

from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed
from flask_mongoengine.wtf import model_form

from .. import models


BaseShrineForm = model_form(
    models.Shrine,
    FlaskForm,
    exclude=["created_date", "updated_date", "creator", "status"],
    field_args={
        "name": {"label": "Name"},
        "name_zh": {"label": "Chinese Name"},
        "name_en": {"label": "English Name"},
        "opened_date": {"label": "Opened Date", "validators": [validators.Optional()]},
        "biography": {"label": "Biograpy"},
        "presidents": {"label": "Presidents"},
        "coordinates": {"label": "Coordinates"},
    },
)


class ShrineForm(BaseShrineForm):
    coordinates = TextListField("Coordinates", widget=widgets.TextInput())
    links = TextListField("Links", widget=widgets.TextInput())
