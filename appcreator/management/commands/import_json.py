from django.core.management.base import BaseCommand

import pandas as pd
import re

from archiv.models import Place, Tablet


class Command(BaseCommand):
    help = "Import Data"

    def handle(self, *args, **kwargs):
        clean = re.compile('<.*?>')
        data = pd.read_json('./data/json/nabucco161021.json')
        df_json = pd.json_normalize(data.nodes)

        for i, row in df_json.iterrows():
            tablet, _ = Tablet.objects.get_or_create(
                museum_id=row['node.Museum No'],
                paraphrase=row['node.Paraphrase']
            )
            tablet.save()

            place = row['node.Place of issue']
            if place:
                clean_place = re.sub(clean, '', place)
                try:
                    p = Place.objects.get(name=clean_place)
                    tablet.place_of_issue.add(p)
                except Place.DoesNotExist:
                    continue
                tablet.save()
