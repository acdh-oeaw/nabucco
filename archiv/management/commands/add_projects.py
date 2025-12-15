from auditlog.context import disable_auditlog
from django.core.management.base import BaseCommand
from tqdm import tqdm

from archiv.models import Tablet
from infos.models import AboutTheProject


class Command(BaseCommand):
    help = "Link all DigEanna Tablets to DigEanna Project"

    def handle(self, *args, **options):
        project = AboutTheProject.objects.get(title="DigEanna")
        items = Tablet.digeanna_objects.all()
        with disable_auditlog():
            for x in tqdm(items, total=items.count()):
                x.project.add(project)
        print("done")
