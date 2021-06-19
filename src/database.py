from decouple import config

DATABASE_URI = f"postgresql://{config('DB_USER', default='admin')}:{config('DB_PASSWD', default='admin')}" \
               f"@{config('DB_HOST', default='localhost')}:5432/workshop_db"

SQLALCHEMY_TRACK_MODIFICATIONS = False
JSON_SORT_KEY = False


def flask_config(name):
    from flask import Flask
    flask = Flask(name)
    flask.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI
    flask.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = SQLALCHEMY_TRACK_MODIFICATIONS
    flask.config['JSON_SORT_KEYS'] = JSON_SORT_KEY
    return flask


def table_creator():
    from src.models import db
    from src.models.user import User
    db.create_all()
    db.session.commit()

