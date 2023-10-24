import mongoengine as me
import datetime


class Picture(me.Document):
    meta = {"collection": "pictures"}

    image = me.ImageField()
    description = me.StringField()
    owner = me.ImageField()
    created_date = me.DateTimeField(required=True, default=datetime.datetime.now)
