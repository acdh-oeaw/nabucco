from django.test import Client, TestCase
from django.urls import reverse

client = Client()


class DigeannaTestCase(TestCase):
    fixtures = ["dump.json"]

    def test_001_index(self):
        url = reverse("navico:index")
        response = client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_002_about(self):
        url = reverse("navico:about")
        response = client.get(url)
        self.assertEqual(response.status_code, 200)
