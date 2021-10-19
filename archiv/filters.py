# generated by appcreator
import django_filters
from django import forms

from dal import autocomplete

from . models import (
    Archiv,
    Bibliography,
    Glossary,
    Place,
    Tablet
)


class ArchivListFilter(django_filters.FilterSet):
    legacy_id = django_filters.CharFilter(
        lookup_expr='icontains',
        help_text=Archiv._meta.get_field('legacy_id').help_text,
        label=Archiv._meta.get_field('legacy_id').verbose_name
    )
    name = django_filters.CharFilter(
        lookup_expr='icontains',
        help_text=Archiv._meta.get_field('name').help_text,
        label=Archiv._meta.get_field('name').verbose_name
    )
    part_of = django_filters.ModelMultipleChoiceFilter(
        queryset=Place.objects.all(),
        help_text=Archiv._meta.get_field('part_of').help_text,
        label=Archiv._meta.get_field('part_of').verbose_name,
        widget=autocomplete.Select2Multiple(
            url="archiv-ac:place-autocomplete",
        )
    )
    alt_name = django_filters.CharFilter(
        lookup_expr='icontains',
        help_text=Archiv._meta.get_field('alt_name').help_text,
        label=Archiv._meta.get_field('alt_name').verbose_name
    )
    title = django_filters.CharFilter(
        lookup_expr='icontains',
        help_text=Archiv._meta.get_field('title').help_text,
        label=Archiv._meta.get_field('title').verbose_name
    )

    class Meta:
        model = Archiv
        fields = [
            'id',
            'legacy_id',
            'legacy_pk',
            'name',
            'part_of',
            'alt_name',
            'title',
            ]


class BibliographyListFilter(django_filters.FilterSet):
    legacy_id = django_filters.CharFilter(
        lookup_expr='icontains',
        help_text=Bibliography._meta.get_field('legacy_id').help_text,
        label=Bibliography._meta.get_field('legacy_id').verbose_name
    )
    short_title = django_filters.CharFilter(
        lookup_expr='icontains',
        help_text=Bibliography._meta.get_field('short_title').help_text,
        label=Bibliography._meta.get_field('short_title').verbose_name
    )
    author = django_filters.CharFilter(
        lookup_expr='icontains',
        help_text=Bibliography._meta.get_field('author').help_text,
        label=Bibliography._meta.get_field('author').verbose_name
    )
    publication_year = django_filters.CharFilter(
        lookup_expr='icontains',
        help_text=Bibliography._meta.get_field('publication_year').help_text,
        label=Bibliography._meta.get_field('publication_year').verbose_name
    )
    title = django_filters.CharFilter(
        lookup_expr='icontains',
        help_text=Bibliography._meta.get_field('title').help_text,
        label=Bibliography._meta.get_field('title').verbose_name
    )
    volume_nr = django_filters.CharFilter(
        lookup_expr='icontains',
        help_text=Bibliography._meta.get_field('volume_nr').help_text,
        label=Bibliography._meta.get_field('volume_nr').verbose_name
    )
    pages = django_filters.CharFilter(
        lookup_expr='icontains',
        help_text=Bibliography._meta.get_field('pages').help_text,
        label=Bibliography._meta.get_field('pages').verbose_name
    )
    journal = django_filters.CharFilter(
        lookup_expr='icontains',
        help_text=Bibliography._meta.get_field('journal').help_text,
        label=Bibliography._meta.get_field('journal').verbose_name
    )
    editor = django_filters.CharFilter(
        lookup_expr='icontains',
        help_text=Bibliography._meta.get_field('editor').help_text,
        label=Bibliography._meta.get_field('editor').verbose_name
    )
    book = django_filters.CharFilter(
        lookup_expr='icontains',
        help_text=Bibliography._meta.get_field('book').help_text,
        label=Bibliography._meta.get_field('book').verbose_name
    )
    mentioned_place = django_filters.ModelMultipleChoiceFilter(
        queryset=Place.objects.all(),
        help_text=Bibliography._meta.get_field('mentioned_place').help_text,
        label=Bibliography._meta.get_field('mentioned_place').verbose_name,
        widget=autocomplete.Select2Multiple(
            url="archiv-ac:place-autocomplete",
        )
    )
    mentioned_archive = django_filters.ModelMultipleChoiceFilter(
        queryset=Archiv.objects.all(),
        help_text=Bibliography._meta.get_field('mentioned_archive').help_text,
        label=Bibliography._meta.get_field('mentioned_archive').verbose_name,
        widget=autocomplete.Select2Multiple(
            url="archiv-ac:archiv-autocomplete",
        )
    )
    mentioned_glossary_item = django_filters.ModelMultipleChoiceFilter(
        queryset=Glossary.objects.all(),
        help_text=Bibliography._meta.get_field('mentioned_glossary_item').help_text,
        label=Bibliography._meta.get_field('mentioned_glossary_item').verbose_name,
        widget=autocomplete.Select2Multiple(
            url="archiv-ac:glossary-autocomplete",
        )
    )
    related_publications = django_filters.CharFilter(
        lookup_expr='icontains',
        help_text=Bibliography._meta.get_field('related_publications').help_text,
        label=Bibliography._meta.get_field('related_publications').verbose_name
    )

    class Meta:
        model = Bibliography
        fields = [
            'id',
            'legacy_id',
            'legacy_pk',
            'short_title',
            'author',
            'publication_year',
            'title',
            'volume_nr',
            'pages',
            'journal',
            'editor',
            'book',
            'mentioned_place',
            'mentioned_archive',
            'mentioned_glossary_item',
            'related_publications',
            ]


class GlossaryListFilter(django_filters.FilterSet):
    legacy_id = django_filters.CharFilter(
        lookup_expr='icontains',
        help_text=Glossary._meta.get_field('legacy_id').help_text,
        label=Glossary._meta.get_field('legacy_id').verbose_name
    )
    pref_label = django_filters.CharFilter(
        lookup_expr='icontains',
        help_text=Glossary._meta.get_field('pref_label').help_text,
        label=Glossary._meta.get_field('pref_label').verbose_name
    )
    hierarchy = django_filters.CharFilter(
        lookup_expr='icontains',
        help_text=Glossary._meta.get_field('hierarchy').help_text,
        label=Glossary._meta.get_field('hierarchy').verbose_name
    )
    title = django_filters.CharFilter(
        lookup_expr='icontains',
        help_text=Glossary._meta.get_field('title').help_text,
        label=Glossary._meta.get_field('title').verbose_name
    )

    class Meta:
        model = Glossary
        fields = [
            'id',
            'legacy_id',
            'legacy_pk',
            'pref_label',
            'hierarchy',
            'type',
            'title',
            ]


class PlaceListFilter(django_filters.FilterSet):
    legacy_id = django_filters.CharFilter(
        lookup_expr='icontains',
        help_text=Place._meta.get_field('legacy_id').help_text,
        label=Place._meta.get_field('legacy_id').verbose_name
    )
    name = django_filters.CharFilter(
        lookup_expr='icontains',
        help_text=Place._meta.get_field('name').help_text,
        label=Place._meta.get_field('name').verbose_name
    )
    part_of = django_filters.ModelMultipleChoiceFilter(
        queryset=Place.objects.all(),
        help_text=Place._meta.get_field('part_of').help_text,
        label=Place._meta.get_field('part_of').verbose_name,
        widget=autocomplete.Select2Multiple(
            url="archiv-ac:place-autocomplete",
        )
    )
    title = django_filters.CharFilter(
        lookup_expr='icontains',
        help_text=Place._meta.get_field('title').help_text,
        label=Place._meta.get_field('title').verbose_name
    )

    class Meta:
        model = Place
        fields = [
            'id',
            'legacy_id',
            'legacy_pk',
            'name',
            'part_of',
            'title',
            ]


class TabletListFilter(django_filters.FilterSet):
    legacy_id = django_filters.CharFilter(
        lookup_expr='icontains',
        help_text=Tablet._meta.get_field('legacy_id').help_text,
        label=Tablet._meta.get_field('legacy_id').verbose_name
    )
    museum_id = django_filters.CharFilter(
        lookup_expr='icontains',
        help_text=Tablet._meta.get_field('museum_id').help_text,
        label=Tablet._meta.get_field('museum_id').verbose_name
    )
    place_of_issue = django_filters.ModelMultipleChoiceFilter(
        queryset=Place.objects.all(),
        help_text=Tablet._meta.get_field('place_of_issue').help_text,
        label=Tablet._meta.get_field('place_of_issue').verbose_name,
        widget=autocomplete.Select2Multiple(
            url="archiv-ac:place-autocomplete",
        )
    )
    mentioned_place = django_filters.ModelMultipleChoiceFilter(
        queryset=Place.objects.all(),
        help_text=Tablet._meta.get_field('mentioned_place').help_text,
        label=Tablet._meta.get_field('mentioned_place').verbose_name,
        widget=autocomplete.Select2Multiple(
            url="archiv-ac:place-autocomplete",
        )
    )
    type_content = django_filters.ModelMultipleChoiceFilter(
        queryset=Glossary.objects.all(),
        help_text=Tablet._meta.get_field('type_content').help_text,
        label=Tablet._meta.get_field('type_content').verbose_name,
        widget=autocomplete.Select2Multiple(
            url="archiv-ac:glossary-autocomplete",
        )
    )
    key_word = django_filters.ModelMultipleChoiceFilter(
        queryset=Glossary.objects.all(),
        help_text=Tablet._meta.get_field('key_word').help_text,
        label=Tablet._meta.get_field('key_word').verbose_name,
        widget=autocomplete.Select2Multiple(
            url="archiv-ac:glossary-autocomplete",
        )
    )
    paraphrase = django_filters.CharFilter(
        lookup_expr='icontains',
        help_text=Tablet._meta.get_field('paraphrase').help_text,
        label=Tablet._meta.get_field('paraphrase').verbose_name
    )
    transliteration = django_filters.CharFilter(
        lookup_expr='icontains',
        help_text=Tablet._meta.get_field('transliteration').help_text,
        label=Tablet._meta.get_field('transliteration').verbose_name
    )
    archiv = django_filters.ModelMultipleChoiceFilter(
        queryset=Archiv.objects.all(),
        help_text=Tablet._meta.get_field('archiv').help_text,
        label=Tablet._meta.get_field('archiv').verbose_name,
        widget=autocomplete.Select2Multiple(
            url="archiv-ac:archiv-autocomplete",
        )
    )
    mentioned_archiv = django_filters.ModelMultipleChoiceFilter(
        queryset=Archiv.objects.all(),
        help_text=Tablet._meta.get_field('mentioned_archiv').help_text,
        label=Tablet._meta.get_field('mentioned_archiv').verbose_name,
        widget=autocomplete.Select2Multiple(
            url="archiv-ac:archiv-autocomplete",
        )
    )
    mentioned_in_pub = django_filters.ModelMultipleChoiceFilter(
        queryset=Bibliography.objects.all(),
        help_text=Tablet._meta.get_field('mentioned_in_pub').help_text,
        label=Tablet._meta.get_field('mentioned_in_pub').verbose_name,
        widget=autocomplete.Select2Multiple(
            url="archiv-ac:bibliography-autocomplete",
        )
    )
    publication_name = django_filters.CharFilter(
        lookup_expr='icontains',
        help_text=Tablet._meta.get_field('publication_name').help_text,
        label=Tablet._meta.get_field('publication_name').verbose_name
    )
    period = django_filters.CharFilter(
        lookup_expr='icontains',
        help_text=Tablet._meta.get_field('period').help_text,
        label=Tablet._meta.get_field('period').verbose_name
    )
    day = django_filters.CharFilter(
        lookup_expr='icontains',
        help_text=Tablet._meta.get_field('day').help_text,
        label=Tablet._meta.get_field('day').verbose_name
    )
    month = django_filters.CharFilter(
        lookup_expr='icontains',
        help_text=Tablet._meta.get_field('month').help_text,
        label=Tablet._meta.get_field('month').verbose_name
    )
    year = django_filters.CharFilter(
        lookup_expr='icontains',
        help_text=Tablet._meta.get_field('year').help_text,
        label=Tablet._meta.get_field('year').verbose_name
    )
    king = django_filters.CharFilter(
        lookup_expr='icontains',
        help_text=Tablet._meta.get_field('king').help_text,
        label=Tablet._meta.get_field('king').verbose_name
    )
    imported = django_filters.CharFilter(
        lookup_expr='icontains',
        help_text=Tablet._meta.get_field('imported').help_text,
        label=Tablet._meta.get_field('imported').verbose_name
    )
    bibliography = django_filters.CharFilter(
        lookup_expr='icontains',
        help_text=Tablet._meta.get_field('bibliography').help_text,
        label=Tablet._meta.get_field('bibliography').verbose_name
    )

    class Meta:
        model = Tablet
        fields = [
            'id',
            'legacy_id',
            'legacy_pk',
            'museum_id',
            'place_of_issue',
            'mentioned_place',
            'type_content',
            'key_word',
            'paraphrase',
            'transliteration',
            'archiv',
            'mentioned_archiv',
            'mentioned_in_pub',
            'publication_name',
            'period',
            'day',
            'month',
            'year',
            'king',
            'imported',
            'julian_date_year',
            'bibliography',
            ]


