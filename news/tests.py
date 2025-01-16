from django.apps import apps
from django.test import TestCase, Client
from django.contrib.auth.models import User


MODELS = list(apps.all_models["news"].values())
to_check = [x for x in MODELS]

client = Client()
USER = {"username": "testuser", "password": "somepassword"}


class NewsTestCase(TestCase):
    fixtures = ["dump.json"]

    def setUp(self):
        User.objects.create_user(**USER)

    def test_002_listviews(self):
        for x in to_check:
            url = x.get_listview_url()
            response = client.get(url)
            self.assertEqual(response.status_code, 200)

    def test_003_detailviews(self):
        for x in to_check:
            item = x.objects.first()
            url = item.get_absolute_url()
            response = client.get(url, {"pk": item.id})
            self.assertEqual(response.status_code, 200)

    def test_004_editviews(self):
        client.login(**USER)
        for x in to_check:
            item = x.objects.first()
            url = item.get_edit_url()
            response = client.get(url, {"pk": item.id})
            self.assertEqual(response.status_code, 200)

    def test_005_createviews_not_logged_in(self):
        for x in to_check:
            item = x.objects.first()
            url = item.get_createview_url()
            response = client.get(url, {"pk": item.id})
            self.assertEqual(response.status_code, 302)
