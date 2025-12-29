from django.apps import apps
from django.contrib.auth.models import User
from django.test import Client, TestCase

from archiv.forms import TabletForm
from archiv.models import Tablet
from custom_user_app.models import CustomUser

MODELS = list(apps.all_models["archiv"].values())
intro = apps.get_model("archiv", "introduction")
to_check = [x for x in MODELS if x != intro]


client = Client()
USER = {"username": "testuser", "password": "somepassword"}


class ArchivTestCase(TestCase):
    fixtures = ["dump.json"]

    def setUp(self):
        # Create two users
        cur_user = User.objects.create_user(**USER)
        CustomUser.objects.create(user=cur_user, tablet_form="default")

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


class TabletFormTestCase(TestCase):
    """Test TabletForm custom layout logic based on user preferences"""

    fixtures = ["dump.json"]

    def setUp(self):
        """Create test users with different form preferences"""
        # User with default form preference
        self.user_default = User.objects.create_user(
            username="user_default", password="testpass123"
        )
        CustomUser.objects.create(user=self.user_default, tablet_form="default")

        # User with navico form preference
        self.user_navico = User.objects.create_user(
            username="user_navico", password="testpass123"
        )
        CustomUser.objects.create(user=self.user_navico, tablet_form="navico")

    def test_form_with_default_layout(self):
        """Test that form uses default layout when user has 'default' preference"""
        form = TabletForm(user=self.user_default)
        self.assertIsNone(form.helper.layout)

    def test_form_with_navico_layout(self):
        """Check if the navico form helper layout contains a Fieldset with "Identifiers" """
        form = TabletForm(user=self.user_navico)
        self.assertIsNotNone(form.helper.layout)
        fieldset_found = False
        for item in form.helper.layout:
            if hasattr(item, "legend") and item.legend == "Identifiers":
                fieldset_found = True
                break
        self.assertTrue(
            fieldset_found,
            "Fieldset with 'Identifiers' legend not found in form layout",
        )
