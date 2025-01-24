from django.core.management.base import BaseCommand
from archiv.models import WorkPackage

data = [
    ("WP4", "Dossiers in the Early Eanna Archive"),
    ("WP5", "Dossiers in the Late Eanna Archive"),
    ("WP6", "A Prosopography of the Eanna scribes and social network analysis"),
    ("WP7", "Scribes, Bureaus, and Filing Methods"),
    ("WP8", "The temple and its topographical footprint in the city"),
    ("WP9", "Milestone meeting with SAB and workshop at the Rencontre Assyriologique"),
    ("WP10", "Documents as tools of domination and manipulation"),
    ("WP11", "The Eanna Archive(s) in a comparative perspective"),
]


class Command(BaseCommand):
    help = "Add workpackages to the database"

    def handle(self, *args, **options):
        for x in data:
            WorkPackage.objects.get_or_create(wp_number=x[0], title=x[1])
            print(f"Added workpackage {x[0]}")
        print("Done")
