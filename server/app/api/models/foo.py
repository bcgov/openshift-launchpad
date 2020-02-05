# pylint: disable=blacklisted-name; delete or rename Foo entity
# pylint: disable=too-few-public-methods; a real entity would have more

from .db import DB

class Foo(DB.Model):
    __tablename__ = 'foo'
    id = DB.Column(DB.Integer, primary_key=True, autoincrement=True)
    string_field = DB.Column(DB.String(128), nullable=False)

    def __init__(self, string_field):
        self.string_field = string_field

    def to_json(self):
        return {
            'id': self.id,
            'string_field': self.string_field,
        }

