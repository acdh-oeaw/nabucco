from django.conf import settings
from django.db import models
from django.urls import reverse_lazy
from tinymce.models import HTMLField
from next_prev import next_in_order, prev_in_order


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

    class Meta:

        ordering = [
            "updated",
        ]
        verbose_name = "News Entry"
        verbose_name_plural = "News Entries"

    def __str__(self):
        return self.title

    def get_next(self):
        try:
            next = next_in_order(self)
        except ValueError:
            return False
        if next:
            return reverse_lazy("news:news_detail", kwargs={"pk": next.id})
        return False

    def get_prev(self):
        try:
            prev = prev_in_order(self)
        except ValueError:
            return False
        if prev:
            return reverse_lazy("news:news_detail", kwargs={"pk": prev.id})
        return False
