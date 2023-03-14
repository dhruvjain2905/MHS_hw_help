import click
from flask.cli import with_appcontext

from .extensions import db
from .models import User, Question


def create_tables(app):
    db.create_all(app=app)
