"""
Defines the routes for a single REST resource called 'foo'

Blueprints are the most flexible and powerful way to define
routes in Flask. They are easy to read and they gather all
the routing logic together in one place. A common practice
is to have one blueprint per REST resource.+

A good practice is to handle all the http stuff (requests,
responses, error codes, etc.) in the blueprint file but
to keep application logic out as much as possible (single
responsibility principle). In this example, the blueprint
does not have direct access to the database but calls model
object methods that execute business functionality.

If the models start to get really complicated, it's a good idea
to put a service layer between the blueprint and the model
so that the business logic is easily tracked all in one spot.

"""

# pylint: disable=blacklisted-name; delete Foo entity
from flask import Blueprint, jsonify, request
from app.api.models.foo import Foo


FOO_BLUEPRINT = Blueprint('foo', __name__)

@FOO_BLUEPRINT.route('/api/foo', methods=['POST'], strict_slashes=False)
def post():
    """
    A route to handle a request to create a new instance of the resource.

    Parameters:
    foo_id (int): Unique identifier for a foo

    Returns:
    json: Newly created Foo record

    """
    post_data = request.get_json()
    if not post_data:
        return jsonify({'errors': ['Invalid request.']}), 400

    string_field = post_data.get('string_field')

    # Validate request data
    if len(Foo.find_all_by_string_field(string_field)) > 0:
        response_object = {
            'errors': [f'String "{string_field}" already exists']
        }
        return jsonify(response_object), 400

    record = Foo(string_field=string_field)
    record.save()

    return jsonify(record.to_json()), 201


@FOO_BLUEPRINT.route('/api/foo', methods=['GET'], strict_slashes=False)
def get_all():
    '''A route to handle a request for a list of all instances of the resource.'''
    response_object = {
        'records': [foos.to_json() for foos in Foo.find_all()]
    }
    return jsonify(response_object), 200


@FOO_BLUEPRINT.route('/api/foo/<int:foo_id>', methods=['GET'], strict_slashes=False)
def get(foo_id):
    """
    A route to handle a request for a single Foo record (looked up by its id).

    Parameters:
    foo_id (int): Unique identifier for a foo

    Returns:
    json: Corresponding Foo record

    """
    record = Foo.find_by_id(foo_id)
    if not record:
        return jsonify({
            'errors': [f'No record with id={foo_id} found.']
        }), 404
    return jsonify(record.to_json()), 200


@FOO_BLUEPRINT.route('/api/foo/<int:foo_id>', methods=['PUT'], strict_slashes=False)
def put(foo_id):
    """
    A route to handle a request to update single existing Foo record (looked up by its id).

    Parameters:
    foo_id (int): Unique identifier for a foo

    Returns:
    json: Corresponding Foo record

    """
    put_data = request.get_json()
    if not put_data:
        return jsonify({'errors': ['Invalid request.']}), 400

    new_string_field = put_data.get('string_field')

    # Validate request data
    record = Foo.find_by_id(foo_id)
    if not record:
        response_object = {
            'errors': [f'No record with id={foo_id} found.']
        }
        return jsonify(response_object), 404

    if not isinstance(new_string_field, str):
        response_object = {
            'errors': ['The string_field must be a string.']
        }
        return jsonify(response_object), 400

    record.string_field = new_string_field
    record.update()

    return jsonify(record.to_json()), 200


@FOO_BLUEPRINT.route('/api/foo/<int:foo_id>', methods=['DELETE'], strict_slashes=False)
def delete(foo_id):
    """
    A route to handle a request to delete an existing Foo record (looked up by its id).

    Parameters:
    foo_id (int): Unique identifier for a foo

    Returns:
    json: A response code

    """
    # Validate request data
    record = Foo.query.filter_by(id=foo_id).first()
    if not record:
        response_object = {
            'errors': [f'No record with id={foo_id} found.']
        }
        return jsonify(response_object), 404

    record.delete()

    return jsonify({}), 200
