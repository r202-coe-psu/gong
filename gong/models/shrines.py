import mongoengine as me
import datetime


class Shrine(me.Document):
    meta = {"collection": "shrines"}

    name = me.StringField(min_length=5, max_length=256)
    name_ch = me.StringField(min_length=5, max_length=256)

    day_of_open = me.DateTimeField()
    biography = me.StringField()
    pictures = me.ListField(me.ReferenceField("Picture"))

    links = me.ListField(me.StringField())

    presidents = me.ListField(me.ReferenceField("KimSin"))
    kimsins = me.ListField(me.ReferenceField("KimSin"))

    location = me.PointField()

    creator = me.ReferenceField("User")
    created_date = me.DateTimeField(required=True, default=datetime.datetime.now)
    updated_date = me.DateTimeField(
        required=True, default=datetime.datetime.now, auto_now=True
    )
