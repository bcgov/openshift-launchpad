import os

class Config:
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL',  'postgres://admin:password@database:5432/sample_db')
    SECRET_KEY = 'temp'

class TestConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_TEST_URL', 'postgres://admin:password@database:5432/sample_db_test')
