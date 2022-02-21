from django.core.management.base import BaseCommand

import pandas as pd
import re


class Command(BaseCommand):
    help = "Import Data"

    def handle(self, *args, **kwargs):
        clean = re.compile('<.*?>')
        data = pd.read_json('./data/json/nabucco161021.json')
        df_json = pd.json_normalize(data.nodes)
        # print(df_json)

        for i, row in df_json.iterrows():
            museum_id = row['node.Museum No']
            # paraphrase = row['node.Paraphrase']
            period = row['node.Period']
            day = row['node.Babylonian Day']
            # clean
            king = row['node.Babylonian King']
            if king:
                clean_king = re.sub(clean, '', king).lstrip().rstrip()

            month = row['node.Babylonian Month']
            if month:
                clean_month = re.sub(clean, '', month).replace('\n', '').lstrip().rstrip()
            king = row['node.Babylonian King']
            if king:
                clean_king = re.sub(clean, '', king).lstrip().rstrip()
            # FK-relations
            place = row['node.Place of issue']
            if place:
                clean_place = re.sub(clean, '', place)
            archive = row['node.Archive:']
            if archive:
                clean_archive = re.sub(clean, '', archive).replace('\n', '').lstrip().rstrip()
            type_content = row['node.Type and content']
            if type_content:
                clean_type_content = re.sub(clean, '', type_content).replace('\n', '').lstrip().rstrip()
            if place:
                clean_place = re.sub(clean, '', place)
                clean_place.lstrip().rstrip()

            print(museum_id, clean_place, period, clean_king[0:3], clean_month[0:2], day, clean_archive, clean_type_content)
