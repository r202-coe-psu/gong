import mongoengine as me


class Remark(me.EmbeddedDocument):
    updater = me.ReferenceField("user")
    updated_date = me.DateTimeField(required=True, default=datetime.datetime.now)
    message = me.StringField()
    ip_address = me.StringField(required=True)
