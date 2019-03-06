from flask import Flask
from flask_login import LoginManager
from flask_pagedown import PageDown
from flask_sqlalchemy import SQLAlchemy
from elasticsearch import Elasticsearch
from . import commands
from .config import config

db = SQLAlchemy()
pagedown = PageDown()

login_manager = LoginManager()
login_manager.login_view = 'auth.login'


def create_app(config_name):
    """
    :param config_object: The configuration object to use.
    """
    app = Flask(__name__)
    app.config.from_object(config[config_name])


    regsiter_extensions(app)
    register_blueprint(app)
    register_commands(app)

    return app

def regsiter_extensions(app):
    """Register Flask extensions."""
    db.init_app(app)
    login_manager.init_app(app)
    pagedown.init_app(app)
    app.elasticsearch = Elasticsearch()

def register_blueprint(app):
    from .api import api as api_blueprint
    app.register_blueprint(api_blueprint, url_prefix='/api')

    from .api_es import api_es as api_es_blueprint
    app.register_blueprint(api_es_blueprint, url_prefix='/api_es')


def register_commands(app):
    """Register Click commands."""
    app.cli.add_command(commands.test)