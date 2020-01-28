from app import db


class Foo(db.Model):
    __tablename__ = 'foo'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    string_field = db.Column(db.String(128), nullable=False)

    def __init__(self, string_field):
        self.string_field = string_field

    def to_json(self):
        return {
            'id': self.id,
            'string_field': self.string_field,
        }
