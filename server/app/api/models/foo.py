# pylint: disable=blacklisted-name; delete or rename Foo entity

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

    def save(self):
        DB.session.add(self)
        DB.session.commit()

    def delete(self):
        DB.session.delete(self)
        DB.session.commit()

    @staticmethod
    def update():
        DB.session.commit()

    @staticmethod
    def find_all():
        return Foo.query.all()

    @staticmethod
    def find_all_by_string_field(string_field):
        return Foo.query.filter_by(string_field=string_field).all()

    @staticmethod
    def find_by_id(foo_id):
        return Foo.query.filter_by(id=foo_id).first()
