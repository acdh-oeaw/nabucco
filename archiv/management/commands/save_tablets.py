from auditlog.context import disable_auditlog
from django.core.management.base import BaseCommand
from tqdm import tqdm

from archiv.models import Tablet


class Command(BaseCommand):
    help = "Saves all Tablets"

    def handle(self, *args, **options):
        items = Tablet.objects.all()
        with disable_auditlog():
            for x in tqdm(items, total=items.count()):
                x.save()
        print("done")
