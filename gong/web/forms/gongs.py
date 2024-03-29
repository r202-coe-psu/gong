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
    field_args={
        "name": {"label": "Name"},
        "name_zh": {"label": "Chinese Name"},
        "name_en": {"label": "English Name"},
        "alternative_names": {"label": "Alternative Name"},
        "alternative_names_zh": {"label": "Chinese Alternative Name"},
        "alternative_names_en": {"label": "English Alternative Name"},
        "avatar": {"label": "Avatar"},
        "day_of_birth": {"label": "Date of Birth"},
        "day_of_death": {"label": "Date of Death"},
        "day_of_attainment": {"label": "Date of Attainment"},
        "place_of_birth": {"label": "Place of Birth"},
        "place_of_birth_zh": {"label": "Place of Birth in Chinese"},
        "place_of_birth_en": {"label": "Place of Birth in English"},
        "clan": {"label": "Clan"},
        "clan_zh": {"label": "Chinese Clan"},
        "clan_en": {"label": "English Clan"},
        "blessings": {"label": "Blessings"},
        "biography": {"label": "Biograpy"},
    },
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

    # pic = fields.FileField(
    #     "Picture", validators=[FileAllowed(["png", "jpg"], "allow png and jpg")]
    # )
