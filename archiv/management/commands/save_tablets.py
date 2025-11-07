from django.core.management.base import BaseCommand
from tqdm import tqdm

from archiv.models import Tablet


class Command(BaseCommand):
    help = "Saves all Tablets"

    def handle(self, *args, **options):
        items = Tablet.objects.all()
        for x in tqdm(items, total=items.count()):
            x.save()
        print("done")
