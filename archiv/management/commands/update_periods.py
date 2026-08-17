from django.core.management.base import BaseCommand
from tqdm import tqdm

from archiv.models import PeriodObject, Tablet


class Command(BaseCommand):
    help = "copies values form Tablet.period to fk-field period_object"

    def handle(self, *args, **options):
        for x in tqdm(Tablet.objects.exclude(period="").exclude(period="-")):
            item = PeriodObject.objects.get_or_create(
                name=x.period, abbreviation=x.period
            )
            x.period_object = item[0]
            x.save()
        for x in PeriodObject.objects.all():
            print(x)
