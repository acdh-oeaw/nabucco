import pandas as pd
from django.core.management.base import BaseCommand
from tqdm import tqdm


from archiv.models import Glossary


class Command(BaseCommand):
    help = "Import Data"

    def handle(self, *args, **kwargs):
        df = pd.read_csv('./data/csv/glos_hierarchy.csv').dropna()
        for i, row in tqdm(df.iterrows(), total=len(df)):
            cur = Glossary.objects.get(pref_label=row[0])
            broader = Glossary.objects.get(pref_label=row[1])
            cur.broader_concept = broader
            cur.save()
