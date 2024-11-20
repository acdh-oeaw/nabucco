# generated by appcreator
import django_tables2 as tables

from browsing.utils import MergeColumn
from .models import Archiv, Bibliography, Glossary, Place, Tablet, Dossier


class DossierTable(tables.Table):

    name = tables.LinkColumn(verbose_name="Name")
    merge = MergeColumn(verbose_name="keep | remove", accessor="pk")

    class Meta:
        model = Dossier
        sequence = (
            "id",
            "name",
            "archiv",
            "description",
        )


class ArchivTable(tables.Table):

    name = tables.LinkColumn(verbose_name="Name")
    merge = MergeColumn(verbose_name="keep | remove", accessor="pk")

    class Meta:
        model = Archiv
        sequence = (
            "name",
            "alt_name",
            "part_of",
        )


class BibliographyTable(tables.Table):

    title = tables.LinkColumn()
    merge = MergeColumn(verbose_name="keep | remove", accessor="pk")
    mentioned_place = tables.columns.ManyToManyColumn()
    mentioned_archive = tables.columns.ManyToManyColumn()
    mentioned_glossary_item = tables.columns.ManyToManyColumn()

    class Meta:
        model = Bibliography
        sequence = (
            "author",
            "publication_year",
            "title",
            "short_title",
        )


class GlossaryTable(tables.Table):
    pref_label = tables.LinkColumn(verbose_name="Document Type")
    broader_concept = tables.LinkColumn(verbose_name="Document Class")
    merge = MergeColumn(verbose_name="keep | remove", accessor="pk")

    class Meta:
        model = Glossary
        sequence = ("pref_label",)


class PlaceTable(tables.Table):

    name = tables.LinkColumn(verbose_name="Name")
    merge = MergeColumn(verbose_name="keep | remove", accessor="pk")

    class Meta:
        model = Place
        sequence = ("name",)


class TabletTable(tables.Table):
    id = tables.LinkColumn(verbose_name="ID")
    museum_id = tables.LinkColumn(verbose_name="Museum No.")
    merge = MergeColumn(verbose_name="keep | remove", accessor="pk")
    mentioned_place = tables.columns.ManyToManyColumn(
        verbose_name="Place mentioned on Tablet"
    )
    mentioned_archiv = tables.columns.ManyToManyColumn(
        verbose_name="Archiv mentioned on Tablet"
    )
    mentioned_in_pub = tables.columns.ManyToManyColumn(
        verbose_name="Mentioned in Publication"
    )

    class Meta:
        model = Tablet
        sequence = (
            "id",
            "publication_name",
            "text_number",
            "period",
        )
