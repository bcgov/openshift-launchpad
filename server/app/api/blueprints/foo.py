# pylint: disable=blacklisted-name; delete Foo entity
from flask import Blueprint, jsonify, request
from app.api.models.db import DB
from app.api.models.foo import Foo


FOO_BLUEPRINT = Blueprint('foo', __name__)

@FOO_BLUEPRINT.route('/api/foo', methods=['POST'], strict_slashes=False)
def post():
    post_data = request.get_json()
    if not post_data:
        return jsonify({'errors': ['Invalid request.']}), 400

    string_field = post_data.get('string_field')

    # Validate request data
    if len(Foo.query.filter_by(string_field=string_field).all()) > 0:
        response_object = {
            'errors': [f'String "{string_field}" already exists']
        }
        return jsonify(response_object), 400

    record = Foo(string_field=string_field)
    DB.session.add(record)
    DB.session.commit()

    return jsonify(record.to_json()), 201


@FOO_BLUEPRINT.route('/api/foo', methods=['GET'], strict_slashes=False)
def get_all():
    response_object = {
        'records': [foos.to_json() for foos in Foo.query.all()]
    }
    return jsonify(response_object), 200


@FOO_BLUEPRINT.route('/api/foo/<int:foo_id>', methods=['GET'], strict_slashes=False)
def get(foo_id):
    record = Foo.query.filter_by(id=foo_id).first()
    if not record:
        return jsonify({
            'errors': [f'No record with id={foo_id} found.']
        }), 404
    return jsonify(record.to_json()), 200


@FOO_BLUEPRINT.route('/api/foo/<int:foo_id>', methods=['PUT'], strict_slashes=False)
def put(foo_id):
    put_data = request.get_json()
    if not put_data:
        return jsonify({'errors': ['Invalid request.']}), 400

    new_string_field = put_data.get('string_field')

    # Validate request data
    record = Foo.query.filter_by(id=foo_id).first()
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
    DB.session.commit()

    return jsonify(record.to_json()), 200


@FOO_BLUEPRINT.route('/api/foo/<int:foo_id>', methods=['DELETE'], strict_slashes=False)
def delete(foo_id):
    # Validate request data
    record = Foo.query.filter_by(id=foo_id).first()
    if not record:
        response_object = {
            'errors': [f'No record with id={foo_id} found.']
        }
        return jsonify(response_object), 404

    DB.session.delete(record)
    DB.session.commit()

    return jsonify({}), 200
