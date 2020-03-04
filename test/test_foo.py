"""
Test API for Foo model
"""

import json
from test.base import BaseTestCase
from test.helpers import create_foo_string

class TestFooService(BaseTestCase):
    """Test API for Foo model"""
    def test_get_all_foo(self):
        """Test records returned"""
        create_foo_string('foo_string_1')
        create_foo_string('foo_string_2')
        create_foo_string('foo_string_3')
        with self.client:
            response = self.client.get('/api/foo')
        data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(data['records']), 3)

    def test_get_foo(self):
        """Test retrieving single record"""
        record = create_foo_string('foo_string_1')
        with self.client:
            response = self.client.get(f'/api/foo/{record.id}')
        data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['id'], record.id)

    def test_get_foo_not_found(self):
        """Test record that does not exist"""
        with self.client:
            response = self.client.get(f'/api/foo/9999')
        self.assertEqual(response.status_code, 404)

    def test_post_foo(self):
        """Test for content of record"""
        test_string = 'I am a test string'
        with self.client:
            response = self.client.post('/api/foo',
                                        data=json.dumps({
                                            'string_field': test_string,
                                        }),
                                        content_type='application/json',
                                        )
        self.assertEqual(response.status_code, 201)
        data = json.loads(response.data.decode())
        self.assertEqual(data['string_field'], test_string)

    def test_post_foo_exists(self):
        """Test creating duplicate record"""
        test_string = 'I am a test string'
        create_foo_string(test_string)
        with self.client:
            response = self.client.post('/api/foo',
                                        data=json.dumps({
                                            'string_field': test_string,
                                        }),
                                        content_type='application/json',
                                        )
        self.assertEqual(response.status_code, 400)

    def test_put_foo(self):
        """Test updating record"""
        record = create_foo_string('foo_string_1')
        with self.client:
            response = self.client.put(f'/api/foo/{record.id}',
                                       data=json.dumps({
                                           'string_field': 'I am a test string',
                                       }),
                                       content_type='application/json',
                                       )
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data.decode())
        self.assertEqual(data['string_field'], 'I am a test string')

    def test_put_foo_not_found(self):
        """Test updating non-existant record"""
        with self.client:
            response = self.client.put(f'/api/foo/9999',
                                       data=json.dumps({
                                           'string_field': 'I am a test string',
                                       }),
                                       content_type='application/json',
                                       )
        self.assertEqual(response.status_code, 404)

    def test_put_foo_invalid_string(self):
        """Test updating with invalid string"""
        record = create_foo_string('string')
        with self.client:
            response = self.client.put(f'/api/foo/{record.id}',
                                       data=json.dumps({
                                           'string_field': None,
                                       }),
                                       content_type='application/json',
                                       )
        self.assertEqual(response.status_code, 400)

    def test_delete_foo(self):
        """Test delete record"""
        record = create_foo_string('foo_string_1')
        with self.client:
            response = self.client.delete(f'/api/foo/{record.id}')
        self.assertEqual(response.status_code, 200)

    def test_delete_foo_not_found(self):
        """Test delete non-existant record"""
        with self.client:
            response = self.client.delete(f'/api/foo/9999')
        self.assertEqual(response.status_code, 404)
