from wtforms import validators
from wtforms import fields, widgets
from .fields import TextListField

from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed
from flask_mongoengine.wtf import model_form

from .. import models


BasePictureForm = model_form(
    models.BasePicture,
    FlaskForm,
    exclude=[
        "created_date",
        "updated_date",
        "creator",
    ],
    field_args={
        "name": {"label": "Name"},
        "name_zh": {"label": "Chinese Name"},
        "alternative_names": {"label": "Alternative Name"},
        "alternative_names_zh": {"label": "Chinese Alternative Name"},
        "avatar": {"label": "Avatar"},
        "day_of_birth": {"label": "Date of Birth"},
        "day_of_death": {"label": "Date of Death"},
        "day_of_attainment": {"label": "Date of Attainment"},
        "place_of_birth": {"label": "Place of Birth"},
        "clan": {"label": "Clan"},
        "clan_zh": {"label": "Chinese Clan"},
        "blessings": {"label": "Blessings"},
        "biography": {"label": "Biograpy"},
    },
)


class PictureForm(BasePictureForm):
    blessings = TextListField("Blessings", widget=widgets.TextInput())
    tags = TextListField("Tags", widget=widgets.TextInput())
    links = TextListField("Links", widget=widgets.TextInput())
    alternative_names = TextListField("Alternative Names", widget=widgets.TextInput())
    alternative_names_zh = TextListField(
        "Chinese Alternative Names", widget=widgets.TextInput()
    )


class UploadPicturesForm(FlaskForm):
    uploaded_file = fields.FieldList(
        fields.FileField(
            "Upload File: JPG, PNG or, webp",
            validators=[
                FileAllowed(["png", "jpg", "jpeg", "webp"], "file extension not allow")
            ],
        )
    )
