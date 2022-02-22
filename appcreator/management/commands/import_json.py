from django.core.management.base import BaseCommand

import pandas as pd
import re

from archiv.models import Archiv, Glossary, Place, Tablet


class Command(BaseCommand):
    help = "Import Data"

    def handle(self, *args, **kwargs):
        clean = re.compile('<.*?>')
        data = pd.read_json('./data/json/nabucco161021.json')
        df_json = pd.json_normalize(data.nodes)

        for i, row in df_json.iterrows():

            clean_id = row['node.Museum No'].replace("BM 0", "BM ").replace("AO 0", "AO ")
            month = row['node.Babylonian Month']
            king = row['node.Babylonian King']
            place = row['node.Place of issue']
            archive = row['node.Archive:']
            type_content = row['node.Type and content']
            period = row['node.Period']
            day = row['node.Babylonian Day']

            tablet, created = Tablet.objects.get_or_create(
                museum_id=clean_id)

            if created:
                tablet.paraphrase = row['node.Paraphrase']
                if period:
                    tablet.period = period
                else:
                    tablet.period = 'Each'
                if day:
                    tablet.day = day
                if king:
                    tablet.king = re.sub(clean, '', king).lstrip().rstrip()[0:3]
                if month:
                    tablet.month = re.sub(clean, '', month).replace('\n', '').lstrip().rstrip()[0:3]

                if archive:
                    clean_a = re.sub(clean, '', archive).replace('\n', '').lstrip().rstrip()
                    try:
                        tablet.archiv = Archiv.objects.get(name=clean_a)
                        tablet.save()
                    except Archiv.DoesNotExist:
                        continue

                if type_content:
                    clean_type_content = re.sub(clean, '', type_content).replace('\n', '').lstrip().rstrip()
                    try:
                        tablet.type_content = Glossary.objects.get(pref_label=clean_type_content)
                        tablet.save()
                    except Glossary.DoesNotExist:
                        continue

                if place:
                    clean_place = re.sub(clean, '', place).lstrip().rstrip()
                    try:
                        tablet.place_of_issue = Place.objects.get(name=clean_place)
                        tablet.save()
                    except Place.DoesNotExist:
                        continue
            tablet.save()
