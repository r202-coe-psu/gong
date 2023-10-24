from flask_mongoengine import MongoEngine

from .users 
from .oauth2 import OAuth2Token

from . import gongs

db = MongoEngine()


def init_db(app):
    db.init_app(app)
