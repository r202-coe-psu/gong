from wtforms import validators
from wtforms import fields, widgets
from .fields import TextListField, CoordinatesField

from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed
from flask_mongoengine.wtf import model_form

from .. import models

BasePresidentForm = model_form(
    models.ShrinePresident,
    FlaskForm,
    field_args=dict(
        order=dict(label="Order"),
        gimsin=dict(
            label="GimSin",
            label_modifier=lambda gimsin: gimsin.name,
            allow_blank=True,
            blank_text="-",
        ),
    ),
)


class PresidentForm(BasePresidentForm):
    class Meta:
        csrf = False


BaseShrineForm = model_form(
    models.Shrine,
    FlaskForm,
    exclude=["created_date", "updated_date", "creator", "status"],
    field_args=dict(
        name=dict(label="Name"),
        name_zh=dict(label="Chinese Name"),
        name_en=dict(label="English Name"),
        opened_date=dict(
            label="Opened Date",
        ),
        open_time=dict(
            label="Open Time",
        ),
        close_time=dict(
            label="Close Time",
        ),
        biography=dict(label="Biograpy"),
        presidents=dict(label="Presidents"),
        coordinates=dict(label="Coordinates"),
        location=dict(label="Location"),
    ),
)


class ShrineForm(BaseShrineForm):
    presidents = fields.FieldList(
        fields.FormField(PresidentForm, default=models.ShrinePresident()), min_entries=3
    )
    coordinates = CoordinatesField("Coordinates", widget=widgets.TextInput())
    links = TextListField("Links", widget=widgets.TextInput())
