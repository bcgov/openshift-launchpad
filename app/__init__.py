"""
Top-level package for the openshift launchpad application

This is a Flask app with minimal dependencies. The purpose is to provide a clean starting template
without any tech debt that can be run on OpenShift. The app provides http endpoints for a REST web
service that connects to a PostgreSQL database. Database versioning if provided and demonstrated
using Flask Migrate.

Not included in this version: authorization, automated testing, CI/CD entity versioning (alembic),
paging of large resource lists, etc.

"""

from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate
from app.api.models.db import DB
from app.api.blueprints.foo import FOO_BLUEPRINT

def create_app():
    '''Initializes the Flask application including extensions (like SQLAlchemy).'''
    # Instantiate the app
    app = Flask(__name__)

    # Enable CORS
    CORS(app)

    # Get config
    # Resist the urge to put conditional logic here for environments
    # -- use environment variables at the container level instead.
    app.config.from_object('app.config.Config')

    # Set up extensions
    DB.init_app(app)

    # Setup database migrations
    Migrate(app, DB)

    # Register blueprints (add more as needed)
    app.register_blueprint(FOO_BLUEPRINT)

    return app
