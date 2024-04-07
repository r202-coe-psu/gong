from flask_mongoengine import MongoEngine

from . import users
from . import oauth2
from . import gongs
from . import gimsins
from . import shrines
from . import pictures

from .gongs import Gong
from .users import User
from .gimsins import GimSin
from .shrines import Shrine, ShrinePresident
from .pictures import BasePicture, GongPicture, GimSinPicture, ShrinePicture

db = MongoEngine()


def init_db(app):
    db.init_app(app)
