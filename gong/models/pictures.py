import mongoengine as me
import datetime

PICTURE_PUBLIC_CHOICES = [
    ("cc-by", "CC BY"),
    ("cc-by-sa", "CC BY SA"),
    ("cc-by-nc", "CC BY NC"),
    ("cc-by-nc-sa", "CC BY NC SA"),
    ("cc-by-nd", "CC BY ND"),
    ("cc-by-nc-nd", "CC BY NC ND"),
    ("cc0", "CC Zero"),
]


class BasePicture(me.Document):
    meta = {"allow_inheritance": True, "collection": "pictures"}

    file = me.ImageField()
    description = me.StringField()
    owner = me.ReferenceField("User")

    is_cover = me.BooleanField(default=False)
    created_date = me.DateTimeField(required=True, default=datetime.datetime.now)
    updated_date = me.DateTimeField(required=True, default=datetime.datetime.now)

    ip_address = me.StringField(required=True)

    status = me.StringField(status="active")
    public = me.StringField(default="cc-by-nc-sa", choices=PICTURE_PUBLIC_CHOICES)


class GongPicture(BasePicture):

    gong = me.ReferenceField("Gong")


class GimSinPicture(BasePicture):

    gimsin = me.ReferenceField("GimSin")


class ShrinePicture(BasePicture):

    shrine = me.ReferenceField("Shrine")
