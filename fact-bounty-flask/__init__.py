from flask import Flask
from . import config
from flask_pagedown import PageDown
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
pagedown = PageDown()

login_manager = LoginManager()
login_manager.login_view = 'auth.login'

def create_app(config_class=config):
  app = Flask(__name__)
  app.config.from_object(config_class)

  db.init_app(app)
  login_manager.init_app(app)
  pagedown.init_app(app)

  from .api import api as api_blueprint
  app.register_blueprint(api_blueprint, url_prefix='/api')

  return app