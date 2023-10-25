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
        "name": {"label": "Name"},
        "name_cn": {"label": "Name CN"},
        "other_name": {"label": "Other Name"},
        "other_name_cn": {"label": "Other Name CN"},
        "avatar": {"label": "Avatar"},
        "place_of_birth": {"label": "Place of Birth"},
        "clan": {"label": "Clan (แซ่)"},
        "clan_cn": {"label": "Clan CN (แซ่)"},
        "blessings": {"label": "Blessings"},
        "biography": {"label": "Biography"},
        "groups": {"label": "Groups"},
        "links": {"label": "Links"},
    },
)


class GongForm(BaseGongForm):
    pass
    # pic = fields.FileField(
    #     "Picture", validators=[FileAllowed(["png", "jpg"], "allow png and jpg")]
    # )
