import html
from django.core.management.base import BaseCommand
from django.utils.html import strip_tags
from tqdm import tqdm

from archiv.models import TextForm, LegalPurpose


def decode_html_entities(text):
    """Convert HTML entities to UTF-8 characters."""
    if not isinstance(text, str):
        return text
    return html.unescape(text)


class Command(BaseCommand):
    help = "removes HTML encoding of verbum_regens properties"

    def handle(self, *args, **options):
        for x in tqdm(LegalPurpose.objects.all()):
            x.verbum_regens = decode_html_entities(strip_tags(x.verbum_regens))
            x.save()
        for x in tqdm(TextForm.objects.all()):
            x.verbum_regens = decode_html_entities(strip_tags(x.verbum_regens))
            x.save()
        print("done")
