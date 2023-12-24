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
    ],
    field_args={
        "name": {"label": "Name"},
        "name_zh": {"label": "Chinese Name"},
        "alternative_name": {"label": "Chinese Name"},
        "alternative_name_zh": {"label": "Chinese Name"},
        "avatar": {"label": "Gong"},
        "day_of_birth": {"label": "Date of Birth"},
        "day_of_death": {"label": "Date of Death"},
        "day_of_attainment": {"label": "Date of Attainment"},
        "place_of_birth": {"label": "Place of Birth"},
        "clan": {"label": "Clan"},
        "clan_ch": {"label": "Chinese Clan"},
        "blessings": {"label": "Blessings"},
        "picture": {"label": "Picture"},
        "biography": {"label": "Biograpy"},
    },
)


class GongForm(BaseGongForm):
    pass
    # pic = fields.FileField(
    #     "Picture", validators=[FileAllowed(["png", "jpg"], "allow png and jpg")]
    # )
