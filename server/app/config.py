"""
A simple config object to be consumed by the Flask App

This is a good place to bundle configuration items that are fairly constant.
Although the config object can be swapped out at runtime to match different
environments, be careful about checking environment variables into code. Try
to keep your Docker containers environment-agnostic so that you can have a single
image build promoted in successive environments (dev -> test -> staging -> prod).
If you don't have to rebuild, then you know for sure you are putting the exact same
thing into production that you tested in test and staging. For example, the
'SECRET_KEY' value should be moved into an environment variable that can be read
from outside the container so that you can have a different one in each environment
without having to manage this in the code. Try to avoid environment 'switches' in
the code because it means that your app will do different things in different
environments which will invalidate your testing.

"""

# pylint: disable=too-few-public-methods; just a config object
import os

DB_URL = 'postgres://{}:{}@{}:5432/{}'.format(
    os.environ.get('POSTGRESQL_USER', 'admin'),
    os.environ.get('POSTGRESQL_PASSWORD', 'password'),
    os.environ.get('POSTGRESQL_SERVICE', 'database'),
    os.environ.get('POSTGRESQL_DATABASE', 'sample_db'))

DB_TEST_URL = 'postgres://{}:{}@{}:5432/{}'.format(
    os.environ.get('POSTGRESQL_USER', 'admin'),
    os.environ.get('POSTGRESQL_PASSWORD', 'password'),
    os.environ.get('POSTGRESQL_SERVICE', 'database'),
    os.environ.get('POSTGRESQL_DATABASE', 'sample_db_test'))

class Config:
    """Defines values that are known to and consumed by a Flask app"""

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = DB_URL
    SECRET_KEY = os.urandom(24)

class TestConfig(Config):
    """Defines values for testing"""

    TESTING = True
    SQLALCHEMY_DATABASE_URI = DB_TEST_URL
