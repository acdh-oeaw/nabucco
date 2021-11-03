# generated by appcreator
import django_tables2 as tables
from django_tables2.utils import A

from browsing.browsing_utils import MergeColumn
from . models import (
    Archiv,
    Bibliography,
    Glossary,
    Place,
    Tablet
)


class ArchivTable(tables.Table):

    name = tables.LinkColumn(verbose_name='Name')
    merge = MergeColumn(verbose_name='keep | remove', accessor='pk')

    class Meta:
        model = Archiv
        sequence = ('name', 'alt_name', 'part_of',)
        attrs = {"class": "table table-responsive table-hover"}


class BibliographyTable(tables.Table):

    title = tables.LinkColumn()
    merge = MergeColumn(verbose_name='keep | remove', accessor='pk')
    mentioned_place = tables.columns.ManyToManyColumn()
    mentioned_archive = tables.columns.ManyToManyColumn()
    mentioned_glossary_item = tables.columns.ManyToManyColumn()

    class Meta:
        model = Bibliography
        sequence = ('title', 'short_title', 'publication_year', 'author',)
        attrs = {"class": "table table-responsive table-hover"}


class GlossaryTable(tables.Table):

    id = tables.LinkColumn(verbose_name='ID')
    merge = MergeColumn(verbose_name='keep | remove', accessor='pk')

    class Meta:
        model = Glossary
        sequence = ('id',)
        attrs = {"class": "table table-responsive table-hover"}


class PlaceTable(tables.Table):

    id = tables.LinkColumn(verbose_name='ID')
    merge = MergeColumn(verbose_name='keep | remove', accessor='pk')

    class Meta:
        model = Place
        sequence = ('id',)
        attrs = {"class": "table table-responsive table-hover"}


class TabletTable(tables.Table):

    id = tables.LinkColumn(verbose_name='ID')
    merge = MergeColumn(verbose_name='keep | remove', accessor='pk')
    mentioned_place = tables.columns.ManyToManyColumn()
    key_word = tables.columns.ManyToManyColumn()
    mentioned_archiv = tables.columns.ManyToManyColumn()
    mentioned_in_pub = tables.columns.ManyToManyColumn()

    class Meta:
        model = Tablet
        sequence = ('id',)
        attrs = {"class": "table table-responsive table-hover"}

