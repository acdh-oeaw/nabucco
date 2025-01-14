# generated by appcreator
from django.db.models import Q
from dal import autocomplete
from .models import (
    Archiv,
    Bibliography,
    Glossary,
    Place,
    Tablet,
)


class ArchivAC(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = Archiv.objects.all()

        if self.q:
            qs = qs.filter(Q(legacy_id__icontains=self.q) | Q(name__icontains=self.q))
        return qs


class BibliographyAC(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = Bibliography.objects.all()

        if self.q:
            qs = qs.filter(
                Q(legacy_id__icontains=self.q) | Q(short_title__icontains=self.q)
            )
        return qs


class GlossaryAC(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = Glossary.objects.all()

        if self.q:
            qs = qs.filter(
                Q(legacy_id__icontains=self.q) | Q(pref_label__icontains=self.q)
            )
        return qs


class PlaceAC(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = Place.objects.all()

        if self.q:
            qs = qs.filter(Q(legacy_id__icontains=self.q) | Q(name__icontains=self.q))
        return qs


class RegionAC(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = Place.objects.filter(part_of__isnull=True)

        if self.q:
            qs = qs.filter(Q(legacy_id__icontains=self.q) | Q(name__icontains=self.q))
        return qs


class TabletAC(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = Tablet.objects.all()

        if self.q:
            qs = qs.filter(
                Q(legacy_id__icontains=self.q) | Q(museum_id__icontains=self.q)
            )
        return qs
