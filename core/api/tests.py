"""
This file demonstrates two different styles of tests (one doctest and one
unittest). These will both pass when you run "manage.py test".

Replace these with more appropriate tests for your application.
"""

from django.test import TestCase
from django.contrib.auth.models import User
from django.test.client import Client
import logging

LOG_FILENAME = 'test.log'
logging.basicConfig(filename=LOG_FILENAME, level=logging.DEBUG,
                    format='%(asctime)s %(lineno)d %(levelname)-8s %(message)s')

class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.failUnlessEqual(1 + 1, 2)


class ApiTestCase(TestCase):

    def setUp(self):
        User.objects.create_user('user_test',
                                 'user@email.tld',
                                 'user_password')
    
    def test_no_username(self):
        """Test that correct error is thrown when no username is sent."""
        client = Client()
        data = {'password': 'random_password'}
        response = client.post('/api/users/', data)
        self.assertEqual(response.status_code, 400)

    def test_no_password(self):
        """Test that correct error is thrown when no password is sent."""
        client = Client()
        data = {'username': 'random_username'}
        response = client.post('/api/users/', data) 
        self.assertEqual(response.status_code, 400)

    def test_no_email(self):
        """Test that correct error is thrown when no email is sent."""
        client = Client()
        data = {'username': 'random_username',
                'password': 'random_password',
                }
        response = client.post('/api/users/', data)
        self.assertEqual(response.status_code, 400)

    def test_user_exists(self):
        """Test if error is thrown when trying to create existing user."""
        client = Client()
        data = {'username': 'user_test',
                'password': 'user_password',
                'email': 'user@email.tld',
                }
        response = client.post('/api/users/', data)
        self.assertEqual(response.status_code, 409)

    def test_create_user(self):
        client = Client()
        data = {'username': 'new_user_test',
                'password': 'user_password',
                'email': 'user@email.tld',
                }

        response = client.post('/api/users/', data)
        user_created = User.objects.get(username=data['username'])
        self.assertEqual(response.status_code, 201)
        self.assertEqual(user_created.username, data['username'] )


class UserTestCase(TestCase):
    def setUp(self):
        self.existing_user = User.objects.create_user('user_test',
                                                 'user@email.tld',
                                                 'user_password')

    def test_user_exists(self):
        """Tests that a user already exists"""
        self.assertEqual(User.objects.get(username='user_test'), self.existing_user)

    def test_user_does_not_exist(self):
        """Tests that a user doesn't exists."""
            
        self.assertRaises(User.DoesNotExist,
                User.objects.get, username='unexistent_user')


