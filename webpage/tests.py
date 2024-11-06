from django.contrib.auth.models import User
from django.test import Client, TestCase


class WebpageTest(TestCase):

    def setUp(self):
        self.client = Client()
        User.objects.create_user('temporary', 'temp@gmail.com', 'temporary')

    def test_webpage(self):
        rv = self.client.get('/')
        self.assertEqual(rv.status_code, 200)
        rv = self.client.get('/accounts/login/')
        self.assertContains(rv, 'Username')
