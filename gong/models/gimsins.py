import mongoengine as me
import datetime


class GimSin(me.Document):
    meta = {"collection": "gimsins"}

    name = me.StringField(min_length=1, max_length=256)
    name_zh = me.StringField(max_length=256)
    name_en = me.StringField(max_length=256)

    biography = me.StringField()

    gong = me.ReferenceField("Gong")
    shrine = me.ReferenceField("Shrine")

    creator = me.ReferenceField("User")
    contributor = me.ReferenceField("User")

    created_date = me.DateTimeField(required=True, default=datetime.datetime.now)
    updated_date = me.DateTimeField(
        required=True, default=datetime.datetime.now, auto_now=True
    )

    coordinates = me.PointField(auto_index=False, default=[0, 0])

    status = me.StringField(default="active")

    def has_cover_image(self):
        from . import pictures

        picture = pictures.GimSinPicture.objects(is_cover=True, gimsin=self).first()
        if picture:
            return True

        return False

    def get_cover_image(self):
        from . import pictures

        return pictures.GimSinPicture.objects(is_cover=True, gimsin=self).first()

    def get_images(self):
        from . import pictures

        return pictures.GimSinPicture.objects(gimsin=self)
