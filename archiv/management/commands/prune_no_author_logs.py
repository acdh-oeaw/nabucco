from auditlog.models import LogEntry
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Deletes all LogEntry objects without actors"

    def handle(self, *args, **options):
        items = LogEntry.objects.filter(actor_id__isnull=True)
        if items.count():
            print(
                f"Found {items.count()} LogEntry objects without actor, deleting them NOW!!!!"
            )
            items.delete()
        else:
            print("Nothing to delete. Goodbye")
        print("Done")
