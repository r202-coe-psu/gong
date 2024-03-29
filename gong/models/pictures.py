import mongoengine as me
import datetime


class BasePicture(me.Document):
    meta = {"allow_inheritance": True, "collection": "kimsin_pictures"}

    file = me.ImageField()
    description = me.StringField()
    owner = me.ReferenceField("User")

    is_cover = me.BooleanField(default=False)
    created_date = me.DateTimeField(required=True, default=datetime.datetime.now)
    updated_date = me.DateTimeField(required=True, default=datetime.datetime.now)

    ip_address = me.StringField(required=True)

    status = me.StringField(status="active")


class GongPicture(BasePicture):

    gong = me.ReferenceField("Gong")


class GimSinPicture(BasePicture):

    gimsin = me.ReferenceField("GimSin")


class ShrinePicture(BasePicture):

    shire = me.ReferenceField("Shrine")
