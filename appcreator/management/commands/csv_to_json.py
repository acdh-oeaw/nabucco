from django.core.management.base import BaseCommand
import csv
import json


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        csv_file_path = r'C:\Users\Reinhard\Desktop\nabucco\data\csv\Bibliography.csv'
        json_file_path = r'C:\Users\Reinhard\Desktop\nabucco\data\json\Bibliography.json'

        def csv_to_json(csv_file_path, json_file_path):
            json_array = []

            with open(csv_file_path, encoding='utf-8') as csv_file_handler:
                csv_reader = csv.DictReader(csv_file_handler)
                
                for row in csv_reader:
                    json_array.append(row)

            with open(json_file_path, 'w', encoding='utf-8') as json_file_handler:
                json_file_handler.write(json.dumps(json_array, indent=4))

        csv_to_json(csv_file_path, json_file_path)
        print("success")
