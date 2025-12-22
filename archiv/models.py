from auditlog.models import AuditlogHistoryField
from auditlog.registry import auditlog
from browsing.utils import model_to_dict
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.urls import reverse_lazy
from mptt.models import MPTTModel, TreeForeignKey
from next_prev import next_in_order, prev_in_order
from tinymce.models import HTMLField

from archiv.utils import CrudUrlMixin, PrevNextMixin, decode_html_entities
from infos.models import AboutTheProject

WP_LEADS = [
    ("Jena", "Jena team"),
    ("Vienna", "Vienna team"),
    ("Warsaw", "Warsaw team"),
    ("ext", "diverse team"),
]

FILE_CATEGORIES = [
    ("01", "1. Administrative Management and Jurisdiction - General"),
    ("02", "2. Administrative Jurisdiction and Accounting - Animals"),
    ("03", "3. Administrative Jurisdiction and Accounting - Personnel"),
    ("04", "4. Accounting - Silver"),
    ("05", "5. Personnel and food rations"),
    ("06", "6. Prebends"),
    ("07", "7. Crafts"),
    ("08", "8. Real estate"),
    ("09", "9. Agricultural products"),
    ("10", "10. Animal husbandry"),
    ("11", "11. Letters"),
    ("12", "12. Unclassified"),
]


def set_extra(self, **kwargs):
    self.extra = kwargs
    return self


models.Field.set_extra = set_extra


class DigeannaManager(models.Manager):
    def get_queryset(self):
        return (
            super()
            .get_queryset()
            .filter(
                archiv__id__in=[
                    119,
                ]
            )
        )


class King(CrudUrlMixin, PrevNextMixin, models.Model):
    url_namespace = "archiv"
    url_basename = "king"
    name = models.CharField(
        default="Cyr",
        max_length=250,
        verbose_name="King",
        help_text="Traditional (usually biblical) name of the king",
    )
    alt_name = models.CharField(
        blank=True,
        null=True,
        max_length=250,
        verbose_name="Names",
        help_text="The name(s) of the king as it would be in the original language(s) of the texts.",
    )
    abbreviation = models.CharField(
        default="Cyr",
        max_length=50,
        verbose_name="Abbreviation",
        help_text="Abbreviation of the king's name as it should show up in the date formula",
    )
    begin_of_reign = models.IntegerField(
        default=1,
        verbose_name="Beginning of reign",
        help_text="The year BC in which a king took up reign.",
    )
    end_of_reign = models.IntegerField(
        blank=True,
        null=True,
        verbose_name="Ending of reign",
        help_text="The year BC in which a king's reign ended.",
    )
    description = models.TextField(
        blank=True,
        null=True,
        verbose_name="Description",
        help_text="Describe what characterized the king's reign in Babylonia",
    )

    class Meta:
        ordering = [
            "begin_of_reign",
        ]
        verbose_name = "King"
        verbose_name_plural = "Kings"

    def __str__(self):
        if self.end_of_reign:
            reign_period = f"({self.begin_of_reign}–{self.end_of_reign})"
        else:
            reign_period = f"({self.begin_of_reign}–)"
        return f"{self.name} {reign_period}"


class SlaveDescriptor(CrudUrlMixin, PrevNextMixin, models.Model):
    url_namespace = "archiv"
    url_basename = "slavedescriptor"
    descriptor = models.CharField(
        verbose_name="Oblate/Slave Descriptor",
        max_length=250,
        help_text="designation of a specific descriptor used in a text for an oblate/slave",
    )
    description = models.TextField(
        blank=True,
        null=True,
        verbose_name="Description",
        help_text="describe the significance of the descriptor",
    )

    class Meta:
        ordering = [
            "descriptor",
        ]
        verbose_name = "Oblate/Slave Descriptor"
        verbose_name_plural = "Oblate/Slave Descriptors"

    def __str__(self):
        return self.description


class SlaveRole(CrudUrlMixin, PrevNextMixin, models.Model):
    url_namespace = "archiv"
    url_basename = "slaverole"
    role = models.CharField(
        max_length=250,
        verbose_name="Role",
        help_text="designation of the slave's role in a text",
    )
    description = models.TextField(
        blank=True,
        null=True,
        verbose_name="Description",
        help_text="concisely describe the role and its significance in a text",
    )
    active_passive = models.CharField(
        max_length=50,
        choices=(
            ("active", "active role"),
            ("passive", "passive role"),
            ("ambiguous", "ambiguous role"),
        ),
        default="active",
        help_text="Does the role pertain to an active or passive action in a text?",
        verbose_name="Active/Passive",
    )

    class Meta:
        ordering = [
            "role",
        ]
        verbose_name = "Oblate/Slave Role"
        verbose_name_plural = "Oblate/Slave Roles"

    def __str__(self):
        return f"{self.role} ({self.active_passive})"


class NavicoTheme(CrudUrlMixin, PrevNextMixin, models.Model):
    url_namespace = "archiv"
    url_basename = "navicotheme"
    theme = models.CharField(
        verbose_name="Theme",
        help_text="designation of the theme concerning the reality of slaves in a text",
    )
    description = models.TextField(
        blank=True,
        null=True,
        verbose_name="Description",
        help_text="Description of the theme: what sphere of in life a slave does it pertain to? what is the historical significance?",  # noqa: E501
    )

    class Meta:
        ordering = [
            "theme",
        ]
        verbose_name = "Theme (Navico)"
        verbose_name_plural = "Themes (Navico)"

    def __str__(self):
        return self.theme


class Domain(CrudUrlMixin, PrevNextMixin, models.Model):
    url_namespace = "archiv"
    url_basename = "domain"
    name = models.CharField(
        max_length=250,
        default="change me",
        verbose_name="Domain",
        help_text="concise designation of the domain",
    )
    description = models.TextField(
        blank=True,
        null=True,
        verbose_name="Description",
        help_text="a brief description of the textual domain in the economic and administrative reality of Eanna",
    )

    class Meta:
        ordering = [
            "name",
        ]
        verbose_name = "Domain (Eanna)"
        verbose_name_plural = "Domains (Eanna)"

    def __str__(self):
        return self.name


class TransActionType(CrudUrlMixin, PrevNextMixin, models.Model):
    url_namespace = "archiv"
    url_basename = "transactiontype"
    name = models.CharField(
        max_length=250,
        default="change me",
        verbose_name="Transaction type",
        help_text="designation of the type, whether transactional or not, outgoing, incoming etc.",
    )
    description = models.TextField(
        blank=True,
        null=True,
        verbose_name="Description",
        help_text="a brief description of the transaction type as viewed by the administration",
    )

    class Meta:
        ordering = [
            "name",
        ]
        verbose_name = "Transaction type"
        verbose_name_plural = "Transaction types"

    def __str__(self):
        return self.name


class LegalPurpose(CrudUrlMixin, PrevNextMixin, models.Model):
    url_namespace = "archiv"
    url_basename = "legalpurpose"
    name = models.CharField(
        max_length=250,
        default="change me",
        verbose_name="Legal purpose",
        help_text="name of the type of purpose (as precise as possible in English)",
    )
    verbum_regens = models.CharField(
        max_length=250,
        default="...",
        verbose_name="verbum regens",
        help_text="verba regentia characteristic of and critical for the legal content of a text typ",
    )
    description = models.TextField(
        blank=True,
        null=True,
        verbose_name="Description",
        help_text="a brief description of the legal reality behind such a text",
    )

    class Meta:
        ordering = [
            "name",
        ]
        verbose_name = "Legal Purpose"
        verbose_name_plural = "Legal Purposes"

    def __str__(self):
        return f"{self.name} ({self.verbum_regens})"


class TextForm(CrudUrlMixin, PrevNextMixin, models.Model):
    url_namespace = "archiv"
    url_basename = "textform"
    name = models.CharField(
        max_length=250,
        default="change me",
        verbose_name="Designation",
        help_text="name or type of the text form",
    )
    verbum_regens = models.CharField(
        max_length=250,
        default="...",
        verbose_name="verbum regens",
        help_text="verba regentia characteristic of and critical for the text form",
    )
    description = models.TextField(
        blank=True,
        null=True,
        verbose_name="Description",
        help_text="further notes and definition of the text form",
    )

    class Meta:
        ordering = [
            "name",
        ]
        verbose_name = "Text Form"
        verbose_name_plural = "Text Forms"

    def __str__(self):
        return f"{self.name} ({self.verbum_regens})"


class VanDrielFiles(CrudUrlMixin, PrevNextMixin, models.Model):
    url_namespace = "archiv"
    url_basename = "vandrielfile"
    file = models.CharField(
        max_length=2,
        verbose_name="File",
        default="12",
        help_text="overarching file category",
        choices=FILE_CATEGORIES,
    )
    sub_file = models.CharField(
        max_length=250,
        default="z. not defined",
        verbose_name="Sub-file",
        help_text="Text type or topic",
    )
    verbum_regens = models.CharField(
        max_length=250,
        blank=True,
        null=True,
        verbose_name="Verbum regens",
        help_text="Akkadian key term for text identification",
    )
    description = models.TextField(
        blank=True,
        null=True,
        verbose_name="Description",
        help_text="General description and remarks concerning a file",
    )

    class Meta:
        ordering = ["file", "sub_file"]
        verbose_name = "File after van Driel, BiOr 55-1 (1998), 59-79"
        verbose_name_plural = "Files after van Driel, BiOr 55-1 (1998), 59-79"

    def __str__(self):
        file_nr = self.file.split(".")[0]
        sub_file_id = self.sub_file.split(".")[0]
        return f"{file_nr.lstrip('0')} {sub_file_id}"

    @classmethod
    def get_listview_url(self):
        return reverse_lazy("archiv:vandrielfile_browse")

    @classmethod
    def get_createview_url(self):
        return reverse_lazy("archiv:vandrielfile_create")

    def get_absolute_url(self):
        return reverse_lazy("archiv:vandrielfile_detail", kwargs={"pk": self.id})

    def get_delete_url(self):
        return reverse_lazy("archiv:vandrielfile_delete", kwargs={"pk": self.id})

    def get_edit_url(self):
        return reverse_lazy("archiv:vandrielfile_edit", kwargs={"pk": self.id})

    def get_next(self):
        try:
            next = next_in_order(self)
        except ValueError:
            return False
        if next:
            return reverse_lazy("archiv:vandrielfile_detail", kwargs={"pk": next.id})
        return False

    def get_prev(self):
        try:
            prev = prev_in_order(self)
        except ValueError:
            return False
        if prev:
            return reverse_lazy("archiv:vandrielfile_detail", kwargs={"pk": prev.id})
        return False


class Archiv(CrudUrlMixin, PrevNextMixin, models.Model):
    """Archive"""

    url_namespace = "archiv"
    url_basename = "archiv"
    legacy_id = models.CharField(max_length=300, blank=True, verbose_name="Legacy ID")
    legacy_pk = models.IntegerField(
        blank=True,
        null=True,
        verbose_name="Archive ID",
        help_text="NaBuCCo No.",
    ).set_extra(
        is_public=True,
        data_lookup="Archive id",
    )
    description = HTMLField(
        default="A short description of the archive",
        blank=True,
        verbose_name="Archive Description",
    )
    name = models.CharField(
        max_length=250,
        blank=True,
        verbose_name="Name",
        help_text="Following GMTR 1",
    ).set_extra(
        is_public=True,
        data_lookup="Archive name",
    )
    paragraph = models.CharField(
        max_length=25,
        blank=True,
        null=True,
        verbose_name="Paragraph",
        help_text="Siglum according to GMTR 1",
    ).set_extra(
        is_public=True,
    )
    part_of = models.ForeignKey(
        "Place",
        related_name="rvn_archiv_part_of_place",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Provenance",
        help_text="(Assumed) place of origin",
    ).set_extra(
        is_public=True,
        data_lookup="Is part of",
    )
    alt_name = models.CharField(
        max_length=250,
        blank=True,
        verbose_name="Alternative name",
        help_text="different name found in publications",
    ).set_extra(
        is_public=True,
        data_lookup="Alternative name",
    )
    orig_data_csv = models.TextField(
        blank=True, null=True, verbose_name="The original data"
    ).set_extra(is_public=True)

    class Meta:
        ordering = [
            "name",
        ]
        verbose_name = "Archive"
        verbose_name_plural = "Archives"

    def __str__(self):
        if self.name:
            return f"{self.name}"
        else:
            return f"{self.legacy_id}"

    def field_dict(self):
        return model_to_dict(self)


class Bibliography(CrudUrlMixin, PrevNextMixin, models.Model):
    """Bibliography"""

    url_namespace = "archiv"
    url_basename = "bibliography"
    legacy_id = models.CharField(max_length=300, blank=True, verbose_name="Legacy ID")
    legacy_pk = models.IntegerField(
        blank=True,
        null=True,
        verbose_name="alt id",
        help_text="whatever",
    ).set_extra(
        is_public=True,
        data_lookup="Occurrence ID",
    )
    short_title = models.CharField(
        max_length=250,
        blank=True,
        verbose_name="Short title",
        help_text="abbreviated title according to Archiv für Orientforschung",
    ).set_extra(
        is_public=True,
        data_lookup="Short title",
    )
    author = models.CharField(
        max_length=250,
        blank=True,
        verbose_name="Author",
        help_text="author(s) of the publication",
    ).set_extra(
        is_public=True,
        data_lookup="Author",
    )
    publication_year = models.CharField(
        max_length=250,
        blank=True,
        verbose_name="Publication year",
        help_text="year in which it was published",
    ).set_extra(
        is_public=True,
        data_lookup="Publication year",
    )
    title = models.CharField(
        max_length=250,
        blank=True,
        verbose_name="Title",
        help_text="title of the publication",
    ).set_extra(
        is_public=True,
        data_lookup="Title",
    )
    volume_nr = models.CharField(
        max_length=250,
        blank=True,
        verbose_name="Volume no.",
        help_text="issue of journal or series",
    ).set_extra(
        is_public=True,
        data_lookup="Volume no.",
    )
    pages = models.CharField(
        max_length=250,
        blank=True,
        verbose_name="Pages",
        help_text="pages in journal or sammelschrift",
    ).set_extra(
        is_public=True,
        data_lookup="Pages",
    )
    journal = models.CharField(
        max_length=250,
        blank=True,
        verbose_name="Journal",
        help_text="name of journal",
    ).set_extra(
        is_public=True,
        data_lookup="Journal",
    )
    editor = models.CharField(
        max_length=250,
        blank=True,
        verbose_name="Editor",
        help_text="editor(s) of the publication",
    ).set_extra(
        is_public=True,
        data_lookup="Editor",
    )
    mentioned_place = models.ManyToManyField(
        "Place",
        related_name="rvn_bibliography_mentioned_place_place",
        blank=True,
        verbose_name="Place mentioned on Tablet",
        help_text="whatever",
    ).set_extra(
        is_public=True,
    )
    mentioned_archive = models.ManyToManyField(
        "Archiv",
        related_name="rvn_bibliography_mentioned_archive_archiv",
        blank=True,
        verbose_name="Place mentioned on Tablet",
        help_text="whatever",
    ).set_extra(
        is_public=True,
    )
    mentioned_glossary_item = models.ManyToManyField(
        "Glossary",
        related_name="rvn_bibliography_mentioned_glossary_item_glossary",
        blank=True,
        verbose_name="mentioned_glossary_item",
        help_text="mentioned_glossary_item",
    ).set_extra(
        is_public=True,
    )
    orig_data_csv = models.TextField(
        blank=True, null=True, verbose_name="The original data"
    ).set_extra(is_public=True)

    class Meta:
        ordering = [
            "short_title",
        ]
        verbose_name = "Bibliography"
        verbose_name_plural = "Bibliographies"

    def __str__(self):
        if self.short_title:
            return f"{self.short_title}"
        else:
            return f"{self.legacy_id}"

    def field_dict(self):
        return model_to_dict(self)


class Glossary(CrudUrlMixin, PrevNextMixin, MPTTModel):
    url_namespace = "archiv"
    url_basename = "glossary"
    legacy_id = models.CharField(max_length=300, blank=True, verbose_name="Legacy ID")
    legacy_pk = models.IntegerField(
        blank=True,
        null=True,
        verbose_name="Concept ID",
        help_text="whatever",
    ).set_extra(
        is_public=True,
        data_lookup="Concept ID",
    )
    pref_label = models.CharField(
        max_length=250,
        blank=True,
        verbose_name="Label",
        help_text="type of document",
    ).set_extra(
        is_public=True,
        data_lookup="Label",
    )
    broader_concept = TreeForeignKey(
        "self",
        verbose_name="skos:broader",
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name="narrower_concepts",
        help_text="Concept with a broader meaning that this concept inherits from",
    )
    title = models.CharField(
        max_length=250,
        blank=True,
        verbose_name="Title",
        help_text="name of type of document",
    ).set_extra(
        is_public=True,
        data_lookup="Title",
    )
    orig_data_csv = models.TextField(
        blank=True, null=True, verbose_name="The original data"
    ).set_extra(is_public=True)

    class MPTTMeta:
        parent_attr = "broader_concept"
        ordering = [
            "pref_label",
        ]
        verbose_name = "Glossary"

    def __str__(self):
        if self.pref_label:
            return f"{self.pref_label}"
        else:
            return f"{self.legacy_id}"

    def field_dict(self):
        return model_to_dict(self)


class Place(CrudUrlMixin, PrevNextMixin, models.Model):
    url_namespace = "archiv"
    url_basename = "place"
    legacy_id = models.CharField(max_length=300, blank=True, verbose_name="Legacy ID")
    legacy_pk = models.IntegerField(
        blank=True,
        null=True,
        verbose_name="Place ID",
        help_text="whatever",
    ).set_extra(
        is_public=True,
        data_lookup="Place id",
    )
    name = models.CharField(
        max_length=250,
        blank=True,
        verbose_name="Name",
    ).set_extra(
        is_public=True,
        data_lookup="Place name",
    )
    description = HTMLField(
        default="Add information on the location",
        blank=True,
        null=True,
        verbose_name="Place description",
    )
    lng = models.FloatField(
        blank=True,
        null=True,
        verbose_name="Longitude",
    ).set_extra(
        is_public=True,
    )
    lat = models.FloatField(
        blank=True,
        null=True,
        verbose_name="Latitude",
    ).set_extra(
        is_public=True,
    )
    part_of = models.ForeignKey(
        "self",
        related_name="rvn_place_part_of_place",
        on_delete=models.SET_NULL,
        limit_choices_to={"part_of__exact": None},
        null=True,
        blank=True,
        verbose_name="Region",
        help_text="larger region",
    ).set_extra(
        is_public=True,
    )
    title = models.CharField(
        max_length=250,
        blank=True,
        verbose_name="Title",
        help_text="whatever",
    ).set_extra(
        is_public=True,
        data_lookup="Title",
    )
    pleiades_url = models.URLField(
        max_length=50,
        blank=True,
        null=True,
        verbose_name="Pleiades URL",
        help_text="https://pleiades.stoa.org/",
    )
    place_collection = models.CharField(
        max_length=250,
        blank=True,
        verbose_name="Collection",
        help_text="Collection to group Place entries",
    )
    orig_data_csv = models.TextField(
        blank=True, null=True, verbose_name="The original data"
    ).set_extra(is_public=True)

    class Meta:
        ordering = [
            "name",
        ]
        verbose_name = "Place"
        verbose_name_plural = "Places"

    def __str__(self):
        if self.name:
            return f"{self.name}"
        else:
            return f"{self.legacy_id}"

    def save(self, *args, **kwargs):
        if self.legacy_id and not self.name:
            self.name = self.legacy_id
        super(Place, self).save(*args, **kwargs)

    def field_dict(self):
        return model_to_dict(self)


class Tablet(CrudUrlMixin, PrevNextMixin, models.Model):
    url_namespace = "archiv"
    url_basename = "tablet"
    legacy_id = models.CharField(max_length=300, blank=True, verbose_name="Legacy ID")
    legacy_pk = models.IntegerField(
        blank=True,
        null=True,
        verbose_name="NaBuCCo No.",
        help_text="whatever",
    ).set_extra(
        is_public=True,
        data_lookup="Object ID",
    )
    museum_id = models.CharField(
        max_length=250,
        blank=True,
        verbose_name="Museum no.",
        help_text="Accession or collection number in museum",
    ).set_extra(
        is_public=True,
        data_lookup="Museum No.",
    )
    cdli_no = models.CharField(
        max_length=25,
        blank=True,
        verbose_name="CDLI P-identifier",
        help_text="Link to CDLI",
    ).set_extra(
        is_public=True,
        data_lookup="CDLI No.",
    )
    labasi_id = models.PositiveIntegerField(
        blank=True,
        null=True,
        verbose_name="LaBaSi identifier",
        help_text="https://labasi.acdh.oeaw.ac.at/",
    )
    place_of_issue = models.ForeignKey(
        "Place",
        related_name="rvn_tablet_place_of_issue_place",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Place of issue",
        help_text="select place of issue as specified on tablet",
    ).set_extra(
        is_public=True,
        data_lookup="Place of issue",
    )
    regional_setting = models.ForeignKey(
        "Place",
        related_name="rvn_tablet_regional_setting_place",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Regional setting",
        help_text="select the inferred region where the content of the text is set, if there is no place of issue given",  # noqa: E501
    )
    mentioned_place = models.ManyToManyField(
        "Place",
        related_name="rvn_tablet_mentioned_place_place",
        blank=True,
        verbose_name="Place mentioned on tablet",
        help_text="whatever",
    ).set_extra(
        is_public=True,
    )
    type_content = models.ForeignKey(
        "Glossary",
        related_name="rvn_tablet_type_content_glossary",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Type and content",
        help_text="select corresponding type of document",
    ).set_extra(
        is_public=True,
        data_lookup="Type and content",
    )
    paraphrase = HTMLField(
        blank=True,
        null=True,
        verbose_name="Paraphrase",
        help_text="Tablet content",
    ).set_extra(
        is_public=True,
        data_lookup="Paraphrase",
    )
    legacy_paraphrase = HTMLField(
        blank=True,
        null=True,
        verbose_name="Legacy paraphrase",
        help_text="first paraphrase created for NaBuCCo of a text that has subsequently been reworked in a new paraphrase",  # noqa: E501
    )
    transliteration = models.TextField(
        blank=True,
        null=True,
        verbose_name="Transliteration",
        help_text="transliterated text or link to transliteration (achemenet.com)",
    ).set_extra(
        is_public=True,
        data_lookup="Transliteration",
    )
    archiv = models.ForeignKey(
        "Archiv",
        related_name="rvn_tablet_archiv_archiv",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Archive",
        help_text="select corresponding archive",
    ).set_extra(
        is_public=True,
        data_lookup="Archive",
    )
    dossier = models.ForeignKey(
        "Dossier",
        related_name="rvn_tablet_archiv_dossier",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Dossier",
        help_text="select corresponding dossier within archive",
    )
    mentioned_in_pub = models.ManyToManyField(
        "Bibliography",
        related_name="rvn_tablet_mentioned_in_pub_bibliography",
        blank=True,
        verbose_name="Mentioned in publication",
        help_text="whatever",
    ).set_extra(
        is_public=True,
    )
    publication_name = models.CharField(
        max_length=250,
        blank=True,
        verbose_name="Publication name",
        help_text="primary publication (abbreviation)",
    ).set_extra(
        is_public=True,
        data_lookup="Publication",
    )
    text_number = models.CharField(
        max_length=250,
        blank=True,
        verbose_name="Text no.",
        help_text="text number within primary publication",
    ).set_extra(
        is_public=True,
        data_lookup="Text number",
    )
    PERIOD_CHOICES = [
        ("NB", "nB"),
        ("Each", "eAch"),
        ("ENB", "enB"),
        ("Ach", "lAch"),
        ("-", "-"),
    ]
    period = models.CharField(
        max_length=250,
        blank=True,
        choices=PERIOD_CHOICES,
        default="-",
        verbose_name="Period",
        help_text="select period in which the tablet was issued",
    ).set_extra(
        is_public=True,
        data_lookup="Period",
    )
    day = models.CharField(
        max_length=250,
        blank=True,
        verbose_name="Babylonian day",
        help_text="Day of month",
    ).set_extra(
        is_public=True,
        data_lookup="Day",
    )
    month = models.CharField(
        max_length=250,
        blank=True,
        verbose_name="Babylonian month",
        help_text="Babylonian month (I-XII)",
    ).set_extra(
        is_public=True,
        data_lookup="Month",
    )
    year = models.CharField(
        max_length=250,
        blank=True,
        verbose_name="Babylonian year",
        help_text="Regnal year",
    ).set_extra(
        is_public=True,
        data_lookup="Year",
    )
    KING_CHOICES = [
        ("-", "-"),
        ("Esar", "Esar"),
        ("Ššu", "Ššu"),
        ("Kan", "Kan"),
        ("Npl", "Npl"),
        ("Nbk", "Nbk"),
        ("AM", "AM"),
        ("Ner", "Ner"),
        ("Nbn", "Nbn"),
        ("Cyr", "Cyr"),
        ("Cam", "Cam"),
        ("Bar", "Bar"),
        ("Dar", "Dar"),
        ("Nbk III", "Nbk III"),
        ("Nbk IV", "Nbk IV"),
        ("Xer", "Xer"),
    ]
    related_king = models.ForeignKey(
        "King",
        related_name="has_tablet",
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        verbose_name="King",
        help_text="King",
    )
    imported = models.CharField(
        max_length=250,
        blank=True,
        verbose_name="Imported (Person, date)",
        help_text="whatever",
    ).set_extra(
        is_public=False,
        data_lookup="Imported",
    )
    julian_date_year = models.IntegerField(
        blank=True,
        null=True,
        verbose_name="Year BCE",
        help_text="Year BCE",
    ).set_extra(
        is_public=True,
        data_lookup="Julian date year",
    )
    julian_date_month = models.IntegerField(
        blank=True,
        null=True,
        verbose_name="Month BCE",
        help_text="modern month (numbered) as calculated from the Babylonian date of issue",
        validators=[MinValueValidator(1), MaxValueValidator(12)],
    ).set_extra(
        is_public=True,
        data_lookup="Julian date month",
    )
    julian_date_day = models.IntegerField(
        blank=True,
        null=True,
        verbose_name="Day BCE",
        help_text="modern day (numbered) as calculated from the Babylonian date of issue",
        validators=[MinValueValidator(1), MaxValueValidator(31)],
    ).set_extra(
        is_public=True,
        data_lookup="Julian date day",
    )
    inferred_date = models.CharField(
        max_length=250,
        blank=True,
        verbose_name="Inferred date",
        help_text="date range on basis of context and prosopography",
    )
    bibliography = models.CharField(
        max_length=250,
        blank=True,
        verbose_name="Bibliography",
        help_text="Bibliography",
    ).set_extra(
        is_public=True,
        data_lookup="Bibliography (free text)",
    )
    work_package = models.ManyToManyField(
        "WorkPackage",
        blank=True,
        verbose_name="Work packages",
        help_text="attribution of the tablet to one or more DigEanna Work packages",
        related_name="related_tablets",
    )
    van_driel_files = models.ManyToManyField(
        VanDrielFiles,
        blank=True,
        verbose_name="File after G. van Driel",
        help_text="choose the attribution of the text according to van Driel's categorization",
        related_name="related_tablets",
    )
    text_form = models.ForeignKey(
        TextForm,
        related_name="has_tablet",
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        verbose_name="Text form",
        help_text="select (one) attributable text form",
    )
    legal_purpose = models.ForeignKey(
        LegalPurpose,
        related_name="has_tablet",
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        verbose_name="Legal purpose",
        help_text="select (one) attributable legal purpose",
    )
    transaction_type = models.ForeignKey(
        TransActionType,
        blank=True,
        null=True,
        related_name="has_tablet",
        on_delete=models.SET_NULL,
        verbose_name="Transaction type",
        help_text="select (one) attributable transaction type",
    )
    second_order_accounting = models.BooleanField(
        default=False,
        verbose_name="second-order accounting",
        help_text="Does the text belong to or contain elements of second-order accounting, i.e. referring to other documents or similar?",  # noqa: E501
    )
    domain = models.ForeignKey(
        Domain,
        blank=True,
        null=True,
        related_name="has_tablet",
        on_delete=models.SET_NULL,
        verbose_name="Domain (Eanna)",
        help_text="select (one) attributable domain of the economic and administrative reality of Eanna",
    )
    formatting = models.BooleanField(
        default=False,
        verbose_name="Formatting",
        help_text="Is there any formatting in the text layout rather than simply scriptio continua?",
    )
    formatting_remarks = models.TextField(
        blank=True,
        null=True,
        verbose_name="Formatting remarks",
        help_text="Briefly describe any unusual or noteworthy points of text formatting",
    )
    tablet_format = models.CharField(
        blank=True,
        null=True,
        max_length=100,
        verbose_name="Format of the tablet",
        help_text="Choose the format of the physical tablet",
        choices=(
            ("landscape", "landscape format"),
            ("portrait", "portrait format"),
            ("square", "square-shaped"),
            ("unclear", "unclear format"),
        ),
    )
    sealings = models.BooleanField(
        default=False,
        verbose_name="Sealings",
        help_text="Does the tablet have seal impressions?",
    )
    private_context = models.BooleanField(
        default=False,
        verbose_name="Private context",
        help_text="Does the text pertain to a private (economic) context?",
    )
    direct_speech = models.BooleanField(
        default=False,
        verbose_name="Features Direct speech",
        help_text="Does the tablet quote any form of direct speech?",
    )
    remark = models.TextField(
        blank=True,
        null=True,
        verbose_name="Remarks",
        help_text="general remarks regarding the content and attribution of the tablet to a dossier",
    )
    orig_data_csv = models.TextField(
        blank=True, null=True, verbose_name="The original data"
    ).set_extra(is_public=True)

    cleaned_text = models.TextField(
        blank=True,
        null=True,
        verbose_name="Internal field",
        help_text="Used for searching",
    ).set_extra(is_public=False)
    public = models.BooleanField(
        default=True,
        verbose_name="Published",
        help_text="Ucheck to make tablet readable only for logged in users",
    )
    project = models.ManyToManyField(
        AboutTheProject,
        blank=True,
        related_name="tablets",
        verbose_name="Related Project(s)",
        help_text="Select Project related to this tablet",
    )
    navico_theme = models.ManyToManyField(
        NavicoTheme,
        blank=True,
        verbose_name="Themes (Navico)",
        help_text="select the tablet's theme relating to Navico",
        related_name="related_tablets",
    )
    slave_role = models.ManyToManyField(
        SlaveRole,
        blank=True,
        verbose_name="Slave role",
        help_text="select the active/passive role of the oblate/slave featuring in the tablet",
        related_name="related_tablets",
    )
    slave_descriptor = models.ManyToManyField(
        SlaveDescriptor,
        blank=True,
        verbose_name="Slave descriptor",
        help_text="select the descriptors used for the oblate/slave",
        related_name="related_tablets",
    )

    history = AuditlogHistoryField()

    objects = models.Manager()
    digeanna_objects = DigeannaManager()

    class Meta:
        ordering = [
            "id",
        ]
        verbose_name = "Tablet"
        verbose_name_plural = "Tablets"

    @classmethod
    def search_fields(self):
        return [
            "museum_id",
            "publication_name",
            "text_number",
            "paraphrase",
            "legacy_paraphrase",
        ]

    def save(self, *args, **kwargs):
        # self.cleaned_text = remove_html_encoding(self)
        for field in self._meta.fields:
            if isinstance(field, HTMLField) and getattr(self, field.name):
                value = decode_html_entities(getattr(self, field.name))
                setattr(self, field.name, value)
        super().save(*args, **kwargs)

    def __str__(self):
        if self.museum_id:
            return f"{self.museum_id}"
        else:
            return f"{self.legacy_id}"

    def field_dict(self):
        return model_to_dict(self)

    def labasi_detail_view(self):
        if self.labasi_id:
            return f"https://labasi.acdh.oeaw.ac.at/tablets/detail/{self.labasi_id}"
        else:
            return False

    def cdli_link(self):
        if self.cdli_no:
            cdli_no = self.cdli_no[1:]
            return f"https://cdli.mpiwg-berlin.mpg.de/artifacts/{cdli_no}"
        else:
            return False

    @property
    def modern_date(self):
        if self.julian_date_day and self.julian_date_month and self.julian_date_year:
            return f"{self.julian_date_day:02d}/{self.julian_date_month:02d}/{self.julian_date_year}"
        elif self.julian_date_month and self.julian_date_year:
            return f"{self.julian_date_month:02d}/{self.julian_date_year}"
        elif self.julian_date_year:
            return f"{self.julian_date_year}"
        else:
            return False


class Introduction(CrudUrlMixin, PrevNextMixin, models.Model):
    url_namespace = "archiv"
    url_basename = "introduction"

    intro_text = HTMLField(
        default="Add brief introductory text",
        blank=True,
    )
    title = models.CharField(
        max_length=250,
        blank=True,
    )

    class Meta:
        ordering = [
            "id",
        ]
        verbose_name = "Introduction"
        verbose_name_plural = "Introductions"

    def __str__(self):
        return f"{self.title}"


class Dossier(CrudUrlMixin, PrevNextMixin, models.Model):
    url_namespace = "archiv"
    url_basename = "dossier"

    name = models.CharField(
        max_length=250,
        default="generic dossier name (change me!)",
        verbose_name="Name of dossier",
        help_text="whatever",
    )
    description = models.TextField(
        blank=True, null=True, verbose_name="Description", help_text="whatever"
    )
    archiv = models.ForeignKey(
        Archiv,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name="has_dossier",
        verbose_name="Archiv",
        help_text="whatever",
    )

    class Meta:
        ordering = [
            "id",
        ]
        verbose_name = "Dossier"
        verbose_name_plural = "Dossiers"

    def __str__(self):
        return f"{self.name}"

    def field_dict(self):
        return model_to_dict(self)


class WorkPackage(CrudUrlMixin, PrevNextMixin, models.Model):
    url_namespace = "archiv"
    url_basename = "workpackage"
    wp_number = models.CharField(
        blank=True,
        null=True,
        max_length=250,
        verbose_name="Number of the work package",
        help_text="Number of the work package",
    )
    title = models.CharField(
        blank=True,
        null=True,
        max_length=250,
        verbose_name="Title of the work package",
        help_text="Title of the work package",
    )
    description = models.TextField(
        blank=True,
        null=True,
        verbose_name="Description",
        help_text="Description of the work package",
    )
    wp_lead = models.CharField(
        choices=WP_LEADS,
        blank=True,
        null=True,
        max_length=250,
        verbose_name="Work package lead",
        help_text="Lead of the work package",
    )

    class Meta:
        ordering = [
            "id",
        ]
        verbose_name = "Work Package"
        verbose_name_plural = "Work Packages"

    def __str__(self):
        if self.wp_number and self.title:
            return f"{self.wp_number}: {self.title}"
        elif self.wp_number:
            return f"{self.wp_number}"
        elif self.title:
            return f"{self.title}"
        else:
            return f"{self.id}"

    def field_dict(self):
        return model_to_dict(self)


auditlog.register(Tablet)
