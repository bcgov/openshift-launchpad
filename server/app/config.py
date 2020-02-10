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

DB_URL_ENV_VAR_NAME = 'DATABASE_URL'
DB_URL_DEFAULT = 'postgres://admin:password@database:5432/sample_db'

class Config:
    """Defines values that are known to and consumed by a Flask app"""

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = os.environ.get(DB_URL_ENV_VAR_NAME,
                                             DB_URL_DEFAULT)
    SECRET_KEY = 'temp'
