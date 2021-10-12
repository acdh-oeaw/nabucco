from django.core.management.base import BaseCommand
from django.conf import settings
from appcreator.import_utils import run_import

# imports for custom things
from tqdm import tqdm
import pandas as pd

from archiv.models import Glossary, Place, Bibliography, Archiv, Tablet



class Command(BaseCommand):
    help = "Import Data"

    def handle(self, *args, **kwargs):
        df_archive = pd.read_csv('./data/csv/Archiv.csv')
        df_place = pd.read_csv('./data/csv/Place.csv')
        df_glossary = pd.read_csv('./data/csv/Glossary.csv')
        #df['Related tablets'] = df.apply(lambda _: '', axis=1)
       
        for i, row in df_archive.iterrows():
            archive_id = row['Archive ID']
            related_object_id = row['Related objects']
            #check if Related Objects refers to Place/Bibliography or else
            try:
                archive = Archiv.objects.get(legacy_pk=archive_id) 
            except:
                continue
            if archive:
                try:
                    rel_tab = Tablet.objects.get(legacy_pk=related_object_id)
                    archive.related_tablets.add(rel_tab)
                except:
                    rel_tab = None
                
                try: 
                    rel_bib = Bibliography.objects.get(legacy_pk=related_object_id) 
                    archive.related_bib_items.add(rel_bib)
                except:
                    rel_bib = None
                

        for i, row in df_place.iterrows():
            place_id = row['Place id']
            related_object_id = row['Related objects']
            try:
                place = Place.objects.get(legacy_pk=place_id) 
            except:
                continue
            if place:
                try:
                    rel_tab = Tablet.objects.get(legacy_pk=related_object_id)
                    place.related_tablets.add(rel_tab)
                except:
                    rel_tab = None
                
                try: 
                    rel_bib = Bibliography.objects.get(legacy_pk=related_object_id) 
                    place.related_bib_items.add(rel_bib)
                except:
                    rel_bib = None
            
            #print(str(place.name) + ':' + str(place.related_bib_items.all()) + ':' + str(place.related_tablets.all()))
            
        for i, row in df_glossary.iterrows():
            glossary_item_id = row['Concept ID']
            related_object_id = row['Related objects']

            try:
                entry = Glossary.objects.get(legacy_pk=glossary_item_id) 
            except:
                continue
            if entry:
                try:
                    rel_tab = Tablet.objects.get(legacy_pk=related_object_id)
                    entry.related_tablets.add(rel_tab)
                except:
                    rel_tab = None
                
                try: 
                    rel_bib = Bibliography.objects.get(legacy_pk=related_object_id) 
                    entry.related_bib_items.add(rel_bib)
                except:
                    rel_bib = None

            #print(str(entry.pref_label) + ':' + str(entry.related_bib_items.all()) + ':' + str(entry.related_tablets.all()))
            
            
            


            
