"""
Convenience methods for tests
"""

from app.api.models.db import DB
from app.api.models.foo import Foo

# Helper function to add a sample string to Foo
def create_foo_string(foo_string):
    """Create Foo record in DB"""
    foo_table_element = Foo(string_field=foo_string)
    DB.session.add(foo_table_element)
    DB.session.commit()
    return foo_table_element
