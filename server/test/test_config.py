import os
import unittest
from flask import current_app
from flask_testing import TestCase
from app import create_app

app = create_app()

class TestConfig(TestCase):
    def create_app(self):
        app.config.from_object('app.config.Config')
        return app

    def test_config_works(self):
        self.assertTrue(app.config['SECRET_KEY'] == 'temp')
        self.assertFalse(current_app is None)
        self.assertTrue(
            app.config['SQLALCHEMY_DATABASE_URI'] ==
            os.environ.get('DATABASE_URL')
        )

class TestTestConfig(TestCase):
    def create_app(self):
        app.config.from_object('app.config.TestConfig')
        return app

    def test_app_is_testing(self):
        self.assertTrue(app.config['SECRET_KEY'] == 'temp')
        self.assertTrue(app.config['TESTING'])
        self.assertFalse(app.config['PRESERVE_CONTEXT_ON_EXCEPTION'])
        self.assertTrue(
            app.config['SQLALCHEMY_DATABASE_URI'] ==
            os.environ.get('DATABASE_TEST_URL')
        )

if __name__ == '__main__':
    unittest.app()