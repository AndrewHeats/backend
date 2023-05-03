from flask import Flask
from flask_smorest import Api

from db import db


def create_app(db_url=None):
    app = Flask(__name__)
    db.init_app(app)
    api = Api(app)
    return app
