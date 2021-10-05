from django.core.management.base import BaseCommand
from django.conf import settings
from appcreator.import_utils import run_import

# imports for custom things
from tqdm import tqdm
import pandas as pd

from archiv.models import Place, Bibliography, Archiv, Tablet



class Command(BaseCommand):
    help = "Import Data"

    def handle(self, *args, **kwargs):
        df = pd.read_csv('./data/csv/Archiv.csv')
        #df['Related tablets'] = df.apply(lambda _: '', axis=1)
       
        for i, row in df.iterrows():
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
                

            print(str(archive.name) + ':' + str(archive.related_bib_items.all()) + ':' + str(archive.related_tablets.all()))
            
            

   
            
