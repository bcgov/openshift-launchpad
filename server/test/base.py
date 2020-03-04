"""
Base test case class for tests
"""

from flask_testing import TestCase
from app import create_app, DB

APP = create_app()

class BaseTestCase(TestCase):
    """Test case parent class"""
    def create_app(self):
        """Create app object from test config"""
        APP.config.from_object('app.config.TestConfig')
        return APP

    def setUp(self):
        """Setup DB before tests"""
        DB.create_all()
        DB.session.commit()

    def tearDown(self):
        """Tear down DB after tests"""
        DB.session.remove()
        DB.drop_all()
