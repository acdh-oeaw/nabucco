import html

from django.db import models
from django.urls import reverse_lazy
from next_prev import next_in_order, prev_in_order


class PrevNextMixin(models.Model):
    class Meta:
        abstract = True

    def get_next(self):
        try:
            obj = next_in_order(self)
        except ValueError:
            return None
        return obj.get_absolute_url() if obj else None

    def get_prev(self):
        try:
            obj = prev_in_order(self)
        except ValueError:
            return None
        return obj.get_absolute_url() if obj else None


class CrudUrlMixin(models.Model):
    url_namespace = None
    url_basename = None
    primary_key_field = "pk"

    class Meta:
        abstract = True

    @classmethod
    def _get_url_basename(cls):
        if cls.url_basename:
            return cls.url_basename
        return cls._meta.model_name

    @classmethod
    def _get_pk_field_name(cls):
        """
        Resolve the keyword argument used for URL reversing.

        Default: "pk"
        Override per model via `primary_key_field`.
        """
        return cls.primary_key_field or "pk"

    def _get_pk_value(self):
        """
        Resolve the actual primary key value to pass to reverse().
        """
        field_name = self._get_pk_field_name()
        return getattr(self, field_name)

    @classmethod
    def get_listview_url(cls):
        return reverse_lazy(f"{cls.url_namespace}:{cls._get_url_basename()}_browse")

    @classmethod
    def get_createview_url(cls):
        return reverse_lazy(f"{cls.url_namespace}:{cls._get_url_basename()}_create")

    def get_absolute_url(self):
        pk_kwarg = self._get_pk_field_name()
        return reverse_lazy(
            f"{self.url_namespace}:{self._get_url_basename()}_detail",
            kwargs={pk_kwarg: self._get_pk_value()},
        )

    def get_edit_url(self):
        pk_kwarg = self._get_pk_field_name()
        return reverse_lazy(
            f"{self.url_namespace}:{self._get_url_basename()}_edit",
            kwargs={pk_kwarg: self._get_pk_value()},
        )

    def get_delete_url(self):
        pk_kwarg = self._get_pk_field_name()
        return reverse_lazy(
            f"{self.url_namespace}:{self._get_url_basename()}_delete",
            kwargs={pk_kwarg: self._get_pk_value()},
        )


def decode_html_entities(text):
    if not isinstance(text, str):
        return text
    return html.unescape(text)
