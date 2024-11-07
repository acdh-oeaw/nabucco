from django.apps import apps
from django.test import TestCase, Client
from django.contrib.auth.models import User

MODELS = list(apps.all_models["archiv"].values())
intro = apps.get_model("archiv", "introduction")
to_check = [x for x in MODELS if x != intro]


client = Client()
USER = {"username": "testuser", "password": "somepassword"}


class ArchivTestCase(TestCase):
    fixtures = ["dump.json"]

    def setUp(self):
        # Create two users
        User.objects.create_user(**USER)

    def test_002_listviews(self):
        for x in to_check:
            try:
                url = x.get_listview_url()
            except AttributeError:
                url = False
            if url:
                response = client.get(url)
                self.assertEqual(response.status_code, 200)

    def test_003_detailviews(self):
        for x in to_check:
            item = x.objects.first()
            try:
                url = item.get_absolute_url()
            except AttributeError:
                url = False
            if url:
                response = client.get(url, {"pk": item.id})
                self.assertEqual(response.status_code, 200)

    def test_004_editviews(self):
        client.login(**USER)
        for x in to_check:
            item = x.objects.first()
            try:
                url = item.get_edit_url()
            except AttributeError:
                url = False
            if url:
                response = client.get(url, {"pk": item.id})
                self.assertEqual(response.status_code, 200)

    def test_005_createviews_not_logged_in(self):
        for x in to_check:
            item = x.objects.first()
            try:
                url = item.get_createview_url()
            except AttributeError:
                url = False
            if url:
                response = client.get(url, {"pk": item.id})
                self.assertEqual(response.status_code, 302)

    def test_006_createviews_logged_in(self):
        client.login(**USER)
        for x in to_check:
            item = x.objects.first()
            try:
                url = item.get_createview_url()
            except AttributeError:
                url = False
            if url:
                response = client.get(url, {"pk": item.id})
                self.assertEqual(response.status_code, 200)
