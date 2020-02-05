import os

class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = os.environ.get(get_db_url_env_name(), get_db_url_default_value())
    SECRET_KEY = 'temp'

    @staticmethod
    def get_db_url_env_name():
        return 'DATABASE_URL'

    @staticmethod
    def get_db_url_default_value():
        return 'postgres://admin:password@database:5432/sample_db'
