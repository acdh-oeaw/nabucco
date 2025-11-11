import django_filters
from acdh_django_widgets.widgets import MartinAntonMuellerWidget
from dal import autocomplete
from django.contrib.postgres.search import SearchVector
from django.db.models import Q

from .models import Archiv, Bibliography, Glossary, Place, Tablet


class ArchivListFilter(django_filters.FilterSet):
    legacy_id = django_filters.CharFilter(
        lookup_expr="icontains",
        help_text=Archiv._meta.get_field("legacy_id").help_text,
        label=Archiv._meta.get_field("legacy_id").verbose_name,
    )
    name = django_filters.CharFilter(
        lookup_expr="icontains",
        help_text=Archiv._meta.get_field("name").help_text,
        label=Archiv._meta.get_field("name").verbose_name.capitalize(),
    )
    part_of = django_filters.ModelMultipleChoiceFilter(
        queryset=Place.objects.all(),
        help_text=Archiv._meta.get_field("part_of").help_text,
        label=Archiv._meta.get_field("part_of").verbose_name.capitalize(),
        widget=autocomplete.Select2Multiple(
            url="archiv-ac:place-autocomplete",
        ),
    )
    alt_name = django_filters.CharFilter(
        lookup_expr="icontains",
        help_text=Archiv._meta.get_field("alt_name").help_text,
        label=Archiv._meta.get_field("alt_name").verbose_name,
    )
    description = django_filters.CharFilter(
        lookup_expr="icontains",
        help_text=Archiv._meta.get_field("description").help_text,
        label=Archiv._meta.get_field("description").verbose_name.capitalize(),
    )
    paragraph = django_filters.CharFilter(
        lookup_expr="icontains",
        help_text=Archiv._meta.get_field("paragraph").help_text,
        label=Archiv._meta.get_field("paragraph").verbose_name.capitalize(),
    )

    class Meta:
        model = Archiv
        fields = [
            "id",
            "legacy_id",
            "legacy_pk",
            "name",
            "part_of",
            "paragraph",
            "description",
        ]


class BibliographyListFilter(django_filters.FilterSet):
    legacy_id = django_filters.CharFilter(
        lookup_expr="icontains",
        help_text=Bibliography._meta.get_field("legacy_id").help_text,
        label=Bibliography._meta.get_field("legacy_id").verbose_name,
    )
    short_title = django_filters.CharFilter(
        lookup_expr="icontains",
        help_text=Bibliography._meta.get_field("short_title").help_text,
        label=Bibliography._meta.get_field("short_title").verbose_name,
    )
    author = django_filters.CharFilter(
        lookup_expr="icontains",
        help_text=Bibliography._meta.get_field("author").help_text,
        label=Bibliography._meta.get_field("author").verbose_name,
    )
    publication_year = django_filters.CharFilter(
        lookup_expr="icontains",
        help_text=Bibliography._meta.get_field("publication_year").help_text,
        label=Bibliography._meta.get_field("publication_year").verbose_name,
    )
    title = django_filters.CharFilter(
        lookup_expr="icontains",
        help_text=Bibliography._meta.get_field("title").help_text,
        label=Bibliography._meta.get_field("title").verbose_name,
    )
    volume_nr = django_filters.CharFilter(
        lookup_expr="icontains",
        help_text=Bibliography._meta.get_field("volume_nr").help_text,
        label=Bibliography._meta.get_field("volume_nr").verbose_name,
    )
    pages = django_filters.CharFilter(
        lookup_expr="icontains",
        help_text=Bibliography._meta.get_field("pages").help_text,
        label=Bibliography._meta.get_field("pages").verbose_name,
    )
    journal = django_filters.CharFilter(
        lookup_expr="icontains",
        help_text=Bibliography._meta.get_field("journal").help_text,
        label=Bibliography._meta.get_field("journal").verbose_name,
    )
    editor = django_filters.CharFilter(
        lookup_expr="icontains",
        help_text=Bibliography._meta.get_field("editor").help_text,
        label=Bibliography._meta.get_field("editor").verbose_name,
    )
    mentioned_place = django_filters.ModelMultipleChoiceFilter(
        queryset=Place.objects.all(),
        help_text=Bibliography._meta.get_field("mentioned_place").help_text,
        label=Bibliography._meta.get_field("mentioned_place").verbose_name,
        widget=autocomplete.Select2Multiple(
            url="archiv-ac:place-autocomplete",
        ),
    )
    mentioned_archive = django_filters.ModelMultipleChoiceFilter(
        queryset=Archiv.objects.all(),
        help_text=Bibliography._meta.get_field("mentioned_archive").help_text,
        label=Bibliography._meta.get_field("mentioned_archive").verbose_name,
        widget=autocomplete.Select2Multiple(
            url="archiv-ac:archiv-autocomplete",
        ),
    )
    mentioned_glossary_item = django_filters.ModelMultipleChoiceFilter(
        queryset=Glossary.objects.all(),
        help_text=Bibliography._meta.get_field("mentioned_glossary_item").help_text,
        label=Bibliography._meta.get_field("mentioned_glossary_item").verbose_name,
        widget=autocomplete.Select2Multiple(
            url="archiv-ac:glossary-autocomplete",
        ),
    )

    class Meta:
        model = Bibliography
        fields = [
            "id",
            "legacy_id",
            "legacy_pk",
            "short_title",
            "author",
            "publication_year",
            "title",
            "volume_nr",
            "pages",
            "journal",
            "editor",
            "mentioned_place",
            "mentioned_archive",
            "mentioned_glossary_item",
        ]


class GlossaryListFilter(django_filters.FilterSet):
    legacy_id = django_filters.CharFilter(
        lookup_expr="icontains",
        help_text=Glossary._meta.get_field("legacy_id").help_text,
        label=Glossary._meta.get_field("legacy_id").verbose_name,
    )
    pref_label = django_filters.CharFilter(
        lookup_expr="icontains",
        help_text=Glossary._meta.get_field("pref_label").help_text,
        label=Glossary._meta.get_field("pref_label").verbose_name,
    )
    title = django_filters.CharFilter(
        lookup_expr="icontains",
        help_text=Glossary._meta.get_field("title").help_text,
        label=Glossary._meta.get_field("title").verbose_name,
    )

    class Meta:
        model = Glossary
        fields = [
            "id",
            "legacy_id",
            "legacy_pk",
            "pref_label",
            "title",
        ]


class PlaceListFilter(django_filters.FilterSet):
    legacy_id = django_filters.CharFilter(
        lookup_expr="icontains",
        help_text=Place._meta.get_field("legacy_id").help_text,
        label=Place._meta.get_field("legacy_id").verbose_name,
    )
    name = django_filters.CharFilter(
        lookup_expr="icontains",
        help_text=Place._meta.get_field("name").help_text,
        label=Place._meta.get_field("name").verbose_name.capitalize(),
    )
    part_of = django_filters.ModelMultipleChoiceFilter(
        queryset=Place.objects.all(),
        help_text=Place._meta.get_field("part_of").help_text,
        label=Place._meta.get_field("part_of").verbose_name.capitalize(),
        widget=autocomplete.Select2Multiple(
            url="archiv-ac:region-autocomplete",
        ),
    )
    place_collection = django_filters.CharFilter(
        lookup_expr="icontains",
        help_text=Place._meta.get_field("place_collection").help_text,
        label=Place._meta.get_field("place_collection").verbose_name,
    )

    class Meta:
        model = Place
        fields = [
            "id",
            "legacy_id",
            "legacy_pk",
            "name",
            "part_of",
            "title",
            "place_collection",
        ]


class TabletListFilter(django_filters.FilterSet):
    legacy_id = django_filters.CharFilter(
        lookup_expr="icontains",
        help_text=Tablet._meta.get_field("legacy_id").help_text,
        label=Tablet._meta.get_field("legacy_id").verbose_name,
    )
    museum_id = django_filters.CharFilter(
        lookup_expr="icontains",
        help_text=Tablet._meta.get_field("museum_id").help_text,
        label=Tablet._meta.get_field("museum_id").verbose_name,
    )
    cdli_no = django_filters.CharFilter(
        lookup_expr="icontains",
        help_text=Tablet._meta.get_field("cdli_no").help_text,
        label=Tablet._meta.get_field("cdli_no").verbose_name,
    )
    place_of_issue = django_filters.ModelMultipleChoiceFilter(
        queryset=Place.objects.all(),
        help_text=Tablet._meta.get_field("place_of_issue").help_text,
        label=Tablet._meta.get_field("place_of_issue").verbose_name,
        widget=autocomplete.Select2Multiple(
            url="archiv-ac:place-autocomplete",
        ),
    )
    regional_setting = django_filters.ModelMultipleChoiceFilter(
        queryset=Place.objects.all(),
        help_text=Tablet._meta.get_field("regional_setting").help_text,
        label=Tablet._meta.get_field("regional_setting").verbose_name,
        widget=autocomplete.Select2Multiple(
            url="archiv-ac:place-autocomplete",
        ),
    )
    mentioned_place = django_filters.ModelMultipleChoiceFilter(
        queryset=Place.objects.all(),
        help_text=Tablet._meta.get_field("mentioned_place").help_text,
        label=Tablet._meta.get_field("mentioned_place").verbose_name,
        widget=autocomplete.Select2Multiple(
            url="archiv-ac:place-autocomplete",
        ),
    )
    type_content = django_filters.ModelMultipleChoiceFilter(
        queryset=Glossary.objects.all(),
        help_text=Tablet._meta.get_field("type_content").help_text,
        label=Tablet._meta.get_field("type_content").verbose_name,
        widget=autocomplete.Select2Multiple(
            url="archiv-ac:glossary-autocomplete",
        ),
    )
    paraphrase = django_filters.CharFilter(
        method="additive_filtering",
        help_text=Tablet._meta.get_field("paraphrase").help_text
        + ": one or more search terms",
        label=Tablet._meta.get_field("paraphrase").verbose_name,
    )

    def additive_filtering(self, queryset, name, value):
        lookup = "__".join([name, "contains"])
        for x in value.split():
            queryset = queryset.filter(**{lookup: x})
        return queryset

    paraphrase_negative = django_filters.CharFilter(
        method="negative_filtering",
        field_name="paraphrase",
        help_text=Tablet._meta.get_field("paraphrase").help_text
        + ": exclude one or more search terms",
        label="Exclude paraphrase search term",
    )

    def negative_filtering(self, queryset, name, value):
        lookup = "__".join([name, "contains"])
        for x in value.split():
            queryset = queryset.exclude(**{lookup: x})
        return queryset

    paraphrase_custom = django_filters.CharFilter(
        method="custom_filtering",
        field_name="paraphrase",
        help_text=Tablet._meta.get_field("paraphrase").help_text
        + ": search for any of the terms given",
        label="Extended search",
    )

    def custom_filtering(self, queryset, name, value):
        lookup = "__".join([name, "contains"])
        q = Q()
        for x in value.split():
            q |= Q(**{lookup: x})
        return queryset.filter(q)

    transliteration = django_filters.CharFilter(
        lookup_expr="icontains",
        help_text=Tablet._meta.get_field("transliteration").help_text,
        label=Tablet._meta.get_field("transliteration").verbose_name,
    )
    archiv = django_filters.ModelMultipleChoiceFilter(
        queryset=Archiv.objects.all(),
        help_text=Tablet._meta.get_field("archiv").help_text,
        label=Tablet._meta.get_field("archiv").verbose_name,
        widget=autocomplete.Select2Multiple(
            url="archiv-ac:archiv-autocomplete",
        ),
    )
    mentioned_in_pub = django_filters.ModelMultipleChoiceFilter(
        queryset=Bibliography.objects.all(),
        help_text=Tablet._meta.get_field("mentioned_in_pub").help_text,
        label=Tablet._meta.get_field("mentioned_in_pub").verbose_name,
        widget=autocomplete.Select2Multiple(
            url="archiv-ac:bibliography-autocomplete",
        ),
    )
    publication_name = django_filters.CharFilter(
        lookup_expr="icontains",
        help_text=Tablet._meta.get_field("publication_name").help_text,
        label=Tablet._meta.get_field("publication_name").verbose_name,
    )
    text_number = django_filters.CharFilter(
        lookup_expr="icontains",
        help_text=Tablet._meta.get_field("text_number").help_text,
        label=Tablet._meta.get_field("text_number").verbose_name,
    )
    period = django_filters.CharFilter(
        lookup_expr="icontains",
        help_text=Tablet._meta.get_field("period").help_text,
        label=Tablet._meta.get_field("period").verbose_name,
    )
    day = django_filters.CharFilter(
        lookup_expr="icontains",
        help_text=Tablet._meta.get_field("day").help_text,
        label=Tablet._meta.get_field("day").verbose_name,
    )
    month = django_filters.CharFilter(
        lookup_expr="icontains",
        help_text=Tablet._meta.get_field("month").help_text,
        label=Tablet._meta.get_field("month").verbose_name,
    )
    year = django_filters.CharFilter(
        lookup_expr="icontains",
        help_text=Tablet._meta.get_field("year").help_text,
        label=Tablet._meta.get_field("year").verbose_name,
    )
    king = django_filters.CharFilter(
        lookup_expr="icontains",
        help_text=Tablet._meta.get_field("king").help_text,
        label=Tablet._meta.get_field("king").verbose_name,
    )
    imported = django_filters.CharFilter(
        lookup_expr="icontains",
        help_text=Tablet._meta.get_field("imported").help_text,
        label=Tablet._meta.get_field("imported").verbose_name,
    )
    bibliography = django_filters.CharFilter(
        lookup_expr="icontains",
        help_text=Tablet._meta.get_field("bibliography").help_text,
        label=Tablet._meta.get_field("bibliography").verbose_name,
    )
    inferred_date = django_filters.CharFilter(
        lookup_expr="icontains",
        help_text=Tablet._meta.get_field("inferred_date").help_text,
        label=Tablet._meta.get_field("inferred_date").verbose_name,
    )
    remark = django_filters.CharFilter(
        lookup_expr="icontains",
        help_text=Tablet._meta.get_field("remark").help_text,
        label=Tablet._meta.get_field("remark").verbose_name,
    )
    julian_date_year = django_filters.RangeFilter(
        help_text=Tablet._meta.get_field("julian_date_year").help_text,
        label=Tablet._meta.get_field("julian_date_year").verbose_name,
        widget=MartinAntonMuellerWidget,
    )
    ft_search = django_filters.CharFilter(
        field_name="museum_id",
        method="search_fulltext",
        label="Search all",
        help_text="Searches in: Museum No., Publication name, Text number, Paraphrase, Legacy Paraphrase",
    )

    def search_fulltext(self, queryset, field_name, value):
        search_term = value
        queryset = queryset.annotate(
            search=SearchVector(
                "museum_id",
                "publication_name",
                "text_number",
                "paraphrase",
                "legacy_paraphrase",
            )
        ).filter(search=search_term)
        return queryset

    class Meta:
        model = Tablet
        fields = [
            "ft_search",
            "id",
            "legacy_id",
            "legacy_pk",
            "museum_id",
            "place_of_issue",
            "regional_setting",
            "mentioned_place",
            "type_content",
            "paraphrase",
            "legacy_paraphrase",
            "transliteration",
            "archiv",
            "mentioned_in_pub",
            "publication_name",
            "text_number",
            "period",
            "day",
            "month",
            "year",
            "king",
            "imported",
            "julian_date_year",
            "bibliography",
            "inferred_date",
            "work_package",
            "van_driel_files",
            "text_form",
            "legal_purpose",
            "transaction_type",
            "second_order_accounting",
            "formatting",
            "formatting_remarks",
            "tablet_format",
            "sealings",
            "domain",
            "private_context",
            "direct_speech",
            "remark",
        ]
