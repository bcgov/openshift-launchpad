from app import DB
from app.api.models.foo import Foo

# Helper function to add a sample string to Foo
def create_foo_string(foo_string):
    foo_table_element = Foo(string_field=foo_string)
    DB.session.add(foo_table_element)
    DB.session.commit()
    return foo_table_element
