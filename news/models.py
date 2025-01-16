from django.conf import settings
from django.db import models
from tinymce.models import HTMLField


class NewsEntry(models.Model):
    title = models.CharField(
        verbose_name="Title", help_text="Some title of the news entry", max_length=200
    )
    text = HTMLField(verbose_name="news text", help_text="The news text.")
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="news_entries",
        verbose_name="Created by",
        help_text="The user who created this news entry.",
    )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
