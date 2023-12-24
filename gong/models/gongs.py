import mongoengine as me
import datetime


class Gong(me.Document):
    name = me.StringField(min_length=5, max_length=256)
    name_ch = me.StringField(min_length=5, max_length=256)

    alternative_name = me.ListField(me.StringField(min_length=5, max_length=256))
    alternative_name_ch = me.ListField(me.StringField(min_length=5, max_length=256))

    avatar = me.ReferenceField("Gong")

    day_of_birth = me.DateTimeField()
    day_of_death = me.DateTimeField()
    day_of_attainment = me.DateTimeField()

    place_of_birth = me.StringField(max_length=64)

    clan = me.StringField(max_length=64)
    clan_ch = me.StringField(max_length=64)

    blessings = me.ListField(me.StringField())
    picture = me.ReferenceField("Picture")
    biography = me.StringField()

    groups = me.ListField(me.StringField())

    links = me.ListField(me.StringField())

    creator = me.ReferenceField("User")
    created_date = me.DateTimeField(required=True, default=datetime.datetime.now)
    updated_date = me.DateTimeField(
        required=True, default=datetime.datetime.now, auto_now=True
    )
