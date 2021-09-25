import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import DefaultConfig


db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config.from_object(f"config.{os.environ.get('ENV', 'Default')}Config")

    # blueprint
    from . import routes
    app.register_blueprint(routes.bp)
    # Database
    db.init_app(app)

    return app


from app import models



