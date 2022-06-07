# Task: Bibliographicals reference add "publication_name" to "mentioned_in_bib"
from django.core.management.base import BaseCommand

import pandas as pd

from archiv.models import Bibliography, Tablet


class Command(BaseCommand):
    help = "Import Data"

    def handle(self, *args, **kwargs):
        df_tab = pd.read_csv('./data/csv/Tablet.csv')
        df_bib = pd.read_csv('./data/csv/Bibliography.csv')

        fks = []
        for i, row in df_tab.iterrows():
            tab_id = row["Object ID"]
            try:
                tablet = Tablet.objects.get(legacy_pk=tab_id)
            except ValueError:
                continue
            if tablet:
                if row['Publication']:
                    fk_raw = row['Publication']
                    # other way to check for "nan"?
                    if isinstance(fk_raw, str):
                        fks.append(fk_raw)
        # print(set(fks))
        # print(len(set(fks)))

        for i, row in df_bib.iterrows():
            bib_items = Bibliography.objects.filter(short_title__in=fks)
        # print(len(bib_items))

        for i, row in df_tab.iterrows():
            tab_id = row["Object ID"]
            fk_raw = row['Publication']
            try:
                tablet = Tablet.objects.get(legacy_pk=tab_id)
            except ValueError:
                continue
            if tablet:
                for x in bib_items:
                    if x.short_title == tablet.publication_name:
                        tablet.mentioned_in_pub.add(x)
