from django.core.management.base import BaseCommand
from django.conf import settings
from appcreator.import_utils import run_import

# imports for custom things
from tqdm import tqdm
import pandas as pd



class Command(BaseCommand):
    help = "Import Data"

    def handle(self, *args, **kwargs):
        run_import(
            'archiv',
            file_class_map_dict=None,
            limit=False,
        )