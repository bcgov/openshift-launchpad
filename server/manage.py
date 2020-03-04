import unittest
from flask.cli import FlaskGroup
from app import create_app

CLI = FlaskGroup(create_app=create_app)

@CLI.command()
def test():
    """Discovers and runs unit tests without coverage"""
    tests = unittest.TestLoader().discover('test', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    return 0 if result.wasSuccessful() else 1

if __name__ == '__main__':
    CLI()
