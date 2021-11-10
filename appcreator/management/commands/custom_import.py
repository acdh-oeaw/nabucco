from os import name
from django.core.management.base import BaseCommand
# from django.conf import settings
# from appcreator.import_utils import run_import

# imports for custom things
# from tqdm import tqdm
import pandas as pd

from archiv.models import Glossary, Place, Bibliography, Archiv, Tablet
from archiv.views import PlaceCreate


class Command(BaseCommand):
    help = "Import Data"

    def handle(self, *args, **kwargs):
        df_archive = pd.read_csv('./data/csv/Archiv.csv')
        df_place = pd.read_csv('./data/csv/Place.csv')
        df_glossary = pd.read_csv('./data/csv/Glossary.csv')
        df_bib = pd.read_csv('./data/csv/Bibliography.csv')
        # df['Related tablets'] = df.apply(lambda _: '', axis=1)
        for i, row in df_archive.iterrows():
            archive_id = row['Archive ID']
            related_object_id = row['Related objects']
            # check if Related Objects refers to Place/Bibliography or else
            try:
                archive = Archiv.objects.get(legacy_pk=archive_id)
            except Archiv.DoesNotExist:
                continue
            if archive:
            # OBSOLETE: 'mentioned' tabletss are simly tablets belonging to the archiv
            #     try:
            #         tablet = Tablet.objects.get(legacy_pk=related_object_id)
            #         tablet.mentioned_archiv.add(archive)
            #     except:
            #         continue
                # print(tablet.mentioned_archiv.all())
                try:
                    bib_item = Bibliography.objects.get(legacy_pk=related_object_id)
                    bib_item.mentioned_archive.add(archive)
                except:
                    continue
                # print(bib_item.mentioned_archive.all())

        for i, row in df_glossary.iterrows():
            glossary_id = row['Concept ID']
            related_object_id = row['Related objects']
            glossary_type = row['Type']
            glossary_label = row['Label']
            # check if Related Objects refers to Place/Bibliography or else
            try:
                glossary_item = Glossary.objects.get(legacy_pk=glossary_id)
            except (Glossary.DoesNotExist, ValueError):
                continue
            if glossary_item:
                try:
                    related_tablet = Tablet.objects.get(legacy_pk=related_object_id)
                    related_tablet.key_word.add(glossary_item)
                except:
                    continue
                # print(related_tablet.key_word.all())
                try:
                    related_bib_item = Bibliography.objects.get(legacy_pk=related_object_id)
                    related_bib_item.mentioned_glossary_item.add(glossary_item)
                except:
                    continue
                # print(related_bib_item.mentioned_glossary_item.all())
                try: 
                    glossary_type == 148
                    Place.objects.get_or_create(name=glossary_label)
                    print('success')
                except:
                    continue
                    
        for i, row in df_place.iterrows():
            place_id = row['Place id']
            related_object_id = row['Related objects']
            # check if Related Objects refers to Place/Bibliography or else
            try:
                place = Place.objects.get(legacy_pk=place_id)
            except Place.DoesNotExist:
                continue
            if place:
                try:
                    related_tablet = Tablet.objects.get(legacy_pk=related_object_id)
                    related_tablet.mentioned_place.add(place)
                except:
                    continue
                # print(related_tablet.mentioned_place.all())
                try:
                    related_bib_item = Bibliography.objects.get(legacy_pk=related_object_id)
                    related_bib_item.mentioned_place.add(place)
                except:
                    continue
                # print(related_bib_item.mentioned_place.all())
        for i, row in df_bib.iterrows():
            bib_id = row['Occurrence ID']
            related_object_id = row['Related objects']
            # check if Related Objects refers to Place/Bibliography or else
            try:
                bib_item = Bibliography.objects.get(legacy_pk=bib_id)
            except Bibliography.DoesNotExist:
                continue
            if bib_item:
                try:
                    related_tablet = Tablet.objects.get(legacy_pk=related_object_id)
                    related_tablet.mentioned_in_pub.add(bib_item)
                except:
                    continue
                # print(related_tablet.mentioned_in_pub.all())
