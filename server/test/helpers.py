from app import db
from app.api.models.foo import Foo

# Helper function to add a sample string to Foo
def create_foo_string(foo_string):
    foo_table_element = Foo(string_field=foo_string)
    db.session.add(foo_table_element)
    db.session.commit()
    return foo_table_element
