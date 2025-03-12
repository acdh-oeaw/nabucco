from django.apps import apps
from django.test import TestCase, Client
from django.contrib.auth.models import User

from archiv.models import Tablet

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

    def test_007_custom_manager(self):
        all_items = Tablet.objects.all().count()
        digeanna_items = Tablet.digeanna_objects.all().count()
        self.assertGreater(all_items, digeanna_items)

    def test_008_api_endpoints(self):
        from djangobaseproject.urls import router

        for prefix, viewset, basename in router.registry:
            url = f"/api/{prefix}/"
            response = client.get(url)
            self.assertEqual(
                response.status_code,
                200,
                f"API endpoint {url} returned {response.status_code}",
            )

    def test_009_api_detail_endpoints(self):
        from djangobaseproject.urls import router

        for prefix, viewset, basename in router.registry:
            # Get the model class from the viewset
            model = viewset.queryset.model
            # Get the first object
            first_obj = model.objects.first()
            if first_obj:
                url = f"/api/{prefix}/{first_obj.id}/"
                response = client.get(url)
                self.assertEqual(
                    response.status_code,
                    200,
                    f"API detail endpoint {url} returned {response.status_code}",
                )

    def text_010_modern_date(self):
        """
        Tests the modern_date property of Tablet objects to ensure correct date format based on available Julian date components.
        The test verifies that:
        - When julian_date_day exists: modern_date has 2 slashes (full date format)
        - When only julian_date_month exists: modern_date has 1 slash (month/year format)
        - When only julian_date_year exists: modern_date has no slashes (year only)
        - When no Julian date components exist: modern_date is False
        Returns:
            None
        Raises:
            AssertionError: If any of the date format validations fail
        """  # noqa: E501

        for x in Tablet.objects.all():
            if self.julian_date_day:
                modern_date = x.modern_date
                self.assertEqual(modern_date.count("/"), 2)
            elif self.julian_date_month:
                modern_date = x.modern_date
                self.assertEqual(modern_date.count("/"), 1)
            elif self.julian_date_year:
                modern_date = x.modern_date
                self.assertEqual(modern_date.count("/"), 0)
            else:
                self.assertFalse(x.modern_date)
