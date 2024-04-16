import mongoengine as me
import datetime


class ShrinePresident(me.EmbeddedDocument):
    order = me.IntField(default=0)
    gimsin = me.ReferenceField("GimSin", dbref=True)


class Shrine(me.Document):
    meta = {"collection": "shrines"}

    name = me.StringField(min_length=1, max_length=256)
    name_zh = me.StringField(max_length=256)
    name_en = me.StringField(max_length=256)

    opened_date = me.DateTimeField()
    open_time = me.StringField(max_length=256)
    close_time = me.StringField(max_length=256)

    biography = me.StringField()

    links = me.ListField(me.StringField())

    presidents = me.EmbeddedDocumentListField(ShrinePresident, default=[])

    creator = me.ReferenceField("User")

    created_date = me.DateTimeField(required=True, default=datetime.datetime.now)
    updated_date = me.DateTimeField(
        required=True, default=datetime.datetime.now, auto_now=True
    )

    coordinates = me.PointField(auto_index=False)
    location = me.StringField(max_length=256)

    status = me.StringField(default="active")

    presidents_label_modifier = lambda gimsin: gimsin.name

    def has_cover_image(self):
        from . import pictures

        picture = pictures.ShrinePicture.objects(is_cover=True, shrine=self).first()
        if picture:
            return True

        return False

    def get_cover_image(self):
        from . import pictures

        return pictures.ShrinePicture.objects(is_cover=True, shrine=self).first()

    def get_images(self):
        from . import pictures

        return pictures.ShrinePicture.objects(shrine=self)

    def get_gimsins(self):
        from . import gimsins

        return gimsins.GimSin.objects(shrine=self)
