import unittest
from flask import Flask, jsonify
from app import create_app, db
from app.models import Destination

class WanderlustTestCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app('sqlite:///:memory:')
        self.client = self.app.test_client()
        with self.app.app_context():
            db.create_all()

    def tearDown(self):
        with self.app.app_context():
            db.session.remove()
            db.drop_all()

    def test_get_destinations(self):
        response = self.client.get('/destinations')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, [])

    def test_create_destination(self):
        data = {
            'name': 'Paris',
            'description': 'City of Love',
            'location': 'France'
        }
        response = self.client.post('/destinations', json=data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json['name'], 'Paris')

    def test_get_destinations_after_creation(self):
        data = {
            'name': 'Tokyo',
            'description': 'Vibrant City',
            'location': 'Japan'
        }
        self.client.post('/destinations', json=data)

        response = self.client.get('/destinations')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json), 1)
        self.assertEqual(response.json[0]['name'], 'Tokyo')

    # Add more test cases for other functionalities (Itinerary, Expense, etc.)

if __name__ == '__main__':
    unittest.main()
