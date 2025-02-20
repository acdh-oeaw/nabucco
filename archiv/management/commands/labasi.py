import requests
import pandas as pd
from django.core.management.base import BaseCommand
from django.core.exceptions import ObjectDoesNotExist

from archiv.models import Tablet


class Command(BaseCommand):
    help = "Links Nabucco-Tablets to Labasi-Tablets via CDLI P-Identifier"

    def handle(self, *args, **options):
        data = []
        next = True
        url = "https://labasi.acdh.oeaw.ac.at/data/api/tablets/?limit=100"
        while next:
            print(f"loading {url}")
            r = requests.get(url).json()
            if r["next"]:
                next = True
                url = r["next"]
                results = r["results"]
                for y in results:
                    cdli = y.get("cdli_no")
                    if cdli:
                        labasi_id = y["url"].split("/")[-2]
                        data.append([labasi_id, cdli])
                    else:
                        continue
            else:
                next = False

        df = pd.DataFrame(data, columns=["labasi_id", "cdli"])
        for i, row in df.iterrows():
            try:
                tablet = Tablet.objects.get(cdli_no=row["cdli"])
                tablet.labasi_id = row["labasi_id"]
                tablet.save()
                print(tablet.id, tablet.labasi_id)
            except ObjectDoesNotExist:
                continue
        print("done")
