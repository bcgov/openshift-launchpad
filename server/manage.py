from app import create_app, db
from app.api.models.foo import Foo

app = create_app()

if __name__ == '__main__':
    app.run()
