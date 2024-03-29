import mongoengine as me
import datetime


class GimSin(me.Document):
    meta = {"collection": "gimsins"}

    name = me.StringField(min_length=1, max_length=256)
    name_zh = me.StringField(min_length=1, max_length=256)
    name_en = me.StringField(min_length=1, max_length=256)

    biography = me.StringField()

    gong = me.ReferenceField("Gong")
    shrine = me.ReferenceField("Shrine")

    creator = me.ReferenceField("User")
    contributor = me.ReferenceField("User")

    created_date = me.DateTimeField(required=True, default=datetime.datetime.now)
    updated_date = me.DateTimeField(
        required=True, default=datetime.datetime.now, auto_now=True
    )

    status = me.StringField(default="active")
