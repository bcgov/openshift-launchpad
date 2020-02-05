import os
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_migrate import Migrate
from app.api.models.db import DB
from app.api.blueprints.foo import FOO_BLUEPRINT


def create_app():
    # Instantiate the app
    app = Flask(__name__)

    # Enable CORS
    CORS(app)

    # Get config
    app.config.from_object('app.config.Config')

    # Set up extensions
    DB.init_app(app)

    # instantiate Migrate
    migrate = Migrate(app, db)

    # Register blueprints (add more as needed)
    app.register_blueprint(FOO_BLUEPRINT)

    return app
