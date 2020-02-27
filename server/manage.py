"""The simplest possible entry into a Flask app."""

import unittest
from flask.cli import FlaskGroup
from app import create_app

create_app()
CLI = FlaskGroup(create_app=create_app)


@CLI.command()
def test():
    """Discover and run unit tests"""
    tests = unittest.TestLoader().discover('test', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1

if __name__ == '__main__':
    CLI()
