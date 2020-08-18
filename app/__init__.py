import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()
login = LoginManager()

def create_app(test_config=None):

    apps = Flask(__name__, instance_relative_config=False)

    if test_config is None:
        apps.config.from_object('config.Config')
    else:
        apps.config.from_mapping(test_config)

    db.init_app(apps)
    login.init_app(apps)
    login.login_view = 'login'

    with apps.app_context():
        from . import routes

        db.create_all()
        return apps