import mongoengine as me
import datetime


class Gong(me.Document):
    meta = {"collection": "gongs"}
    name = me.StringField(min_length=2, max_length=256)
    name_zh = me.StringField(min_length=2, max_length=256)

    alternative_names = me.ListField(me.StringField(min_length=5, max_length=256))
    alternative_names_zh = me.ListField(me.StringField(min_length=5, max_length=256))
    avatar = me.ReferenceField("Gong")

    day_of_birth = me.DateTimeField()
    day_of_death = me.DateTimeField()
    day_of_attainment = me.DateTimeField()

    place_of_birth = me.StringField(max_length=64)

    clan = me.StringField(max_length=64)
    clan_zh = me.StringField(max_length=64)

    blessings = me.ListField(me.StringField())
    biography = me.StringField()

    tags = me.ListField(me.StringField())

    links = me.ListField(me.StringField())

    creator = me.ReferenceField("User")
    updater = me.ReferenceField("User")
    created_date = me.DateTimeField(required=True, default=datetime.datetime.now)
    updated_date = me.DateTimeField(
        required=True, default=datetime.datetime.now, auto_now=True
    )

    def has_cover_image(self):
        from . import pictures

        picture = pictures.GongPicture.objects(is_cover=True, gong=self).first()
        if picture:
            return True

        return False

    def get_cover_image(self):
        from . import pictures

        return pictures.GongPicture.objects(is_cover=True, gong=self).first()
