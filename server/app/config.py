import os

class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL',  'postgres://admin:password@database:5432/sample_db')
    SECRET_KEY = 'temp'
