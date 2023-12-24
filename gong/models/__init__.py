from flask_mongoengine import MongoEngine
from . import users
from . import oauth2
from . import pictures
from . import gongs
from . import kimsins
from . import shrines


db = MongoEngine()


def init_db(app):
    db.init_app(app)
