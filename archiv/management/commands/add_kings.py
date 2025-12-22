from auditlog.context import disable_auditlog
from django.core.management.base import BaseCommand
from tqdm import tqdm

from archiv.models import King, Tablet


class Command(BaseCommand):
    help = "Link Kings to tablets"

    def handle(self, *args, **options):
        items = Tablet.digeanna_objects.exclude(king="").exclude(king="-")
        with disable_auditlog():
            for x in tqdm(items, total=items.count()):
                king_label = x.king
                king, _ = King.objects.get_or_create(
                    name=king_label, abbreviation=king_label
                )
                x.related_king = king
                x.save()
                print(x.related_king)
        print("done")
