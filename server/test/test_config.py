"""
Test app config obejcts
"""

from flask import current_app
from flask_testing import TestCase
from app import create_app

APP = create_app()

class TestConfig(TestCase):
    """Test standard app config"""
    def create_app(self):
        """Create app object from standard config"""
        APP.config.from_object('app.config.Config')
        return APP

    def test_config_works(self):
        """Test config properties"""
        self.assertTrue(APP.config['SQLALCHEMY_DATABASE_URI'])
        self.assertFalse(current_app is None)

class TestTestConfig(TestCase):
    """Test testing app config"""
    def create_app(self):
        """Create app object from test config"""
        APP.config.from_object('app.config.TestConfig')
        return APP

    def test_app_is_testing(self):
        """Test config properties"""
        self.assertTrue(APP.config['SQLALCHEMY_DATABASE_URI'])
        self.assertTrue(APP.config['TESTING'])
        self.assertFalse(APP.config['PRESERVE_CONTEXT_ON_EXCEPTION'])
