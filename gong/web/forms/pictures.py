from wtforms import validators, fields, widgets
from .fields import TextListField

from flask_wtf import FlaskForm
from flask_wtf.file import MultipleFileField, FileRequired, FileAllowed

from flask_mongoengine.wtf import model_form

from .. import models


BasePictureForm = model_form(
    models.BasePicture,
    FlaskForm,
    only=[
        "description",
    ],
    field_args={
        "description": {"label": "Description"},
    },
)


class PictureForm(BasePictureForm):
    pass


class UploadPicturesForm(FlaskForm):
    public = fields.SelectField(
        "Public", default="cc-by-nc-sa", choices=models.pictures.PICTURE_PUBLIC_CHOICES
    )
    uploaded_files = fields.MultipleFileField(
        "Upload File: JPG, PNG or, webp",
        validators=[
            FileAllowed(["png", "jpg", "jpeg", "webp"], "file extension not allow")
        ],
    )
