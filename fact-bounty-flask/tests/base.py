"""For testing"""
from flask_testing import TestCase
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from user_a import User

FLASKR = __import__('fact-bounty-flask')

config = FLASKR.config

app = Flask(__name__)

db= SQLAlchemy(app)
db.create_all(app)

class BaseTestCase(TestCase):
    """A base test case."""

    def create_app(self):
        app.config.from_object(config['testing'])
        return app

    def setUp(self):
        test = User('admin', 'admin', 'admin1@gmail.com')
        db.session.add(test)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()