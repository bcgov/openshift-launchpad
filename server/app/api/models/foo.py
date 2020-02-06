"""
Defines the model for a single REST resource called 'Foo'

This example application uses SQLAlchemy to manage the object-relational mapping. It's a bit tricky
but very good practice to lean on the ORM as much as possible for searches and relationships
instead of writing custom SQL. This example is too simple to really demonstrate these features, but
they are in the SQLAlchemy documentation.

This example includes the higher-order service methods (save, find_all_by_string_field) for
convenience. If the models start to get really complicated, it's a good idea to put a service layer
in front of the model so that the business logic is easily tracked all in one spot.

"""

# pylint: disable=blacklisted-name; delete or rename Foo entity

from .db import DB

class Foo(DB.Model):
    """A dummy entity to demonstrate database access from SQLAlchemy"""
    __tablename__ = 'foo'
    id = DB.Column(DB.Integer, primary_key=True, autoincrement=True)
    string_field = DB.Column(DB.String(128), nullable=False)

    def __init__(self, string_field):
        self.string_field = string_field

    def to_json(self):
        """
        A method to convert a Foo to its representation in json format.

        Returns:
        json: A Foo instance in json format

        """
        return {
            'id': self.id,
            'string_field': self.string_field,
        }

    def save(self):
        '''A utility method to save the state of a Foo object to the database.'''
        DB.session.add(self)
        DB.session.commit()

    def delete(self):
        '''A utility method to remove a Foo instance from the database.'''
        DB.session.delete(self)
        DB.session.commit()

    @staticmethod
    def update():
        '''A utility method to save pending changes to a Foo instance to the database.'''
        DB.session.commit()

    @staticmethod
    def find_all():
        """
        A utility method to retrieve all instances of Foo from the database.

        Returns:
        list: A list of all Foo records

        """
        return Foo.query.all()

    @staticmethod
    def find_all_by_string_field(string_field):
        """
        A utility method to find all instances of Foo in the database whose value for the
        property 'string_field' matches an input value.

        Parameters:
        string_field (str): A value that is potentially non-unique across Foo instances

        Returns:
        json: A list of Foo records that match the criteria

        """
        return Foo.query.filter_by(string_field=string_field).all()

    @staticmethod
    def find_by_id(foo_id):
        """
        A utility method to find a unique instances of Foo in the database with a value for 'id'
        that matches an input value.

        Parameters:
        foo_id (int): A value that is potentially unique across Foo instances

        Returns:
        Foo: A single Foo record that matches the criteria

        """
        return Foo.query.filter_by(id=foo_id).first()
