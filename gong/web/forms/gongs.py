from wtforms import validators
from wtforms import fields, widgets
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
        "status",
    ],
    field_args=dict(
        name=dict(label="Name"),
        name_zh=dict(label="Chinese Name"),
        name_en=dict(label="English Name"),
        alternative_names=dict(label="Alternative Name"),
        alternative_names_zh=dict(label="Chinese Alternative Name"),
        alternative_names_en=dict(label="English Alternative Name"),
        avatar=dict(label="Avatar", label_modifier=lambda gong: gong.name),
        day_of_birth=dict(label="Date of Birth"),
        day_of_death=dict(label="Date of Death"),
        day_of_attainment=dict(label="Date of Attainment"),
        place_of_birth=dict(label="Place of Birth"),
        place_of_birth_zh=dict(label="Place of Birth in Chinese"),
        place_of_birth_en=dict(label="Place of Birth in English"),
        clan=dict(label="Clan"),
        clan_zh=dict(label="Chinese Clan"),
        clan_en=dict(label="English Clan"),
        blessings=dict(label="Blessings"),
        biography=dict(label="Biograpy"),
    ),
)


class GongForm(BaseGongForm):
    blessings = TextListField("Blessings", widget=widgets.TextInput())
    tags = TextListField("Tags", widget=widgets.TextInput())
    links = TextListField("Links", widget=widgets.TextInput())
    alternative_names = TextListField("Alternative Names", widget=widgets.TextInput())
    alternative_names_zh = TextListField(
        "Chinese Alternative Names", widget=widgets.TextInput()
    )
    alternative_names_en = TextListField(
        "English Alternative Names", widget=widgets.TextInput()
    )
