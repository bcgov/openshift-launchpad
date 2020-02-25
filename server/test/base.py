from flask_testing import TestCase
from app import create_app, DB

app = create_app()

class BaseTestCase(TestCase):
    def create_app(self):
        app.config.from_object('app.config.TestConfig')
        return app

    def setUp(self):
        DB.create_all()
        DB.session.commit()

    def tearDown(self):
        DB.session.remove()
        DB.drop_all()