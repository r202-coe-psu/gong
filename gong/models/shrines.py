import mongoengine as me
import datetime


class Shrine(me.Document):
    meta = {"collection": "shrines"}

    name = me.StringField(min_length=5, max_length=256)
    name_zh = me.StringField(min_length=5, max_length=256)

    opened_date = me.DateTimeField()
    biography = me.StringField()
    pictures = me.ListField(me.ReferenceField("Picture"))

    links = me.ListField(me.StringField())

    presidents = me.ListField(me.ReferenceField("GimSin"))

    location = me.PointField()

    creator = me.ReferenceField("User")
    created_date = me.DateTimeField(required=True, default=datetime.datetime.now)
    updated_date = me.DateTimeField(
        required=True, default=datetime.datetime.now, auto_now=True
    )
