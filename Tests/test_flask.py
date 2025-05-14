#tests for app

import unittest
from app import app

class FlaskTestCase(unittest.TestCase):
    def test_route_index(self):
        tester = app.test_client(self)
        response = tester.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Welcome to the Pokemon API!', response.data)