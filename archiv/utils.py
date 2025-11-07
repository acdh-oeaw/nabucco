import html

from django.utils.html import strip_tags
from tinymce.models import HTMLField


def decode_html_entities(text):
    if not isinstance(text, str):
        return text
    return strip_tags(html.unescape(text))


def remove_html_encoding(self):
    text = ""
    for field in self._meta.fields:
        if isinstance(field, HTMLField) and getattr(self, field.name):
            value = getattr(self, field.name)
            text = text + decode_html_entities(value) + " "
    text = text.replace("\xa0", " ").replace("  ", " ")
    return text.strip()
