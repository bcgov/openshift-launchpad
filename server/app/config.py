# pylint: disable=too-few-public-methods; just a config object
import os

DB_URL_ENV_VAR_NAME = 'DATABASE_URL'
DB_URL_DEFAULT = 'postgres://admin:password@database:5432/sample_db'

class Config:

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = os.environ.get(DB_URL_ENV_VAR_NAME,
                                             DB_URL_DEFAULT)
    SECRET_KEY = 'temp'
