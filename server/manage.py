from flask.cli import FlaskGroup
from app import create_app, db
from app.api.models.foo import Foo

app = create_app()
cli = FlaskGroup(create_app=create_app)


if __name__ == '__main__':
    cli()
