from django.test import TestCase, Client
from django.urls import reverse


client = Client()


class DigeannaTestCase(TestCase):
    fixtures = ["dump.json"]

    def test_001_index(self):
        url = reverse("digeanna:index")
        response = client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_002_about(self):
        url = reverse("digeanna:about")
        response = client.get(url)
        self.assertEqual(response.status_code, 200)
