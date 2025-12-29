from django.contrib.auth.models import User
from django.db import models


class CustomUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    tablet_form = models.CharField(
        default="default",
        max_length=50,
        choices=(
            ("default", "Default form"),
            ("navico", "Navico form"),
        ),
        verbose_name="Tablet create/edit form",
        help_text="Select you're prefered form layout to create and edit tablets",
    )
