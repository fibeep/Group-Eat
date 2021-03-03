import os
from unittest import TestCase

from datetime import date
from app import app, db, bcrypt
from app.models import User, Group, Restaurant


# Helper Functions

def create_user():
    password_hash = bcrypt.generate_password_hash('password').decode('utf-8')
    user = User(username='me1', password=password_hash, name='test')
    db.session.add(user)
    db.session.commit()


def login(client, username, password):
    return client.post('/login', data=dict(
        username=username,
        password=password
    ), follow_redirects=True)

# Tests

class AuthTests(TestCase):
    """Tests for authentication (login & signup)."""

    def setUp(self):
        """Executed prior to each test."""
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['DEBUG'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.app = app.test_client()
        db.drop_all()
        db.create_all()

    def test_homepage_logged_in(self):
        """Test that the books show up on the homepage."""
        # Set up
        create_user()
        login(self.app, 'me1', 'password')

        # Make a GET request
        response = self.app.get('/', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

        # Check that page contains all of the things we expect
        response_text = response.get_data(as_text=True)
        self.assertIn('me1', response_text)
        self.assertIn('Create Group', response_text)
        self.assertIn('Join Group', response_text)
        self.assertIn('Log Out', response_text)
