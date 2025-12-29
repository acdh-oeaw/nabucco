from crispy_bootstrap5.bootstrap5 import BS5Accordion
from crispy_forms.bootstrap import AccordionGroup
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Fieldset, Layout, Submit
from dal import autocomplete
from django import forms

from .models import Archiv, Bibliography, Glossary, Place, Tablet


class ArchivFilterFormHelper(FormHelper):
    def __init__(self, *args, **kwargs):
        super(ArchivFilterFormHelper, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.form_class = "genericFilterForm"
        self.form_method = "GET"
        self.form_tag = False
        self.layout = Layout(
            Fieldset("", "name", "part_of", css_id="basic_search_fields"),
            BS5Accordion(
                AccordionGroup(
                    "Advanced search", "paragraph", "description", css_id="more"
                ),
                AccordionGroup(
                    "Admin", "id", "legacy_id", "legacy_pk", css_id="admin_search"
                ),
            ),
        )


class ArchivForm(forms.ModelForm):
    class Meta:
        model = Archiv
        # fields = "__all__"
        exclude = ["orig_data_csv", "legacy_id", "legacy_pk"]

    def __init__(self, *args, **kwargs):
        super(ArchivForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = True
        self.helper.form_class = "form-horizontal"
        self.helper.label_class = "col-md-3"
        self.helper.field_class = "col-md-9"
        self.helper.add_input(
            Submit("submit", "save"),
        )


class BibliographyFilterFormHelper(FormHelper):
    def __init__(self, *args, **kwargs):
        super(BibliographyFilterFormHelper, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.form_class = "genericFilterForm"
        self.form_method = "GET"
        self.form_tag = False
        self.layout = Layout(
            Fieldset(
                "",
                "author",
                "publication_year",
                "title",
                "short_title",
                css_id="basic_search_fields",
            ),
            BS5Accordion(
                AccordionGroup(
                    "Advanced search",
                    "volume_nr",
                    "pages",
                    "journal",
                    "editor",
                    "mentioned_place",
                    "mentioned_archive",
                    "mentioned_glossary_item",
                    css_id="more",
                ),
                AccordionGroup(
                    "admin", "id", "legacy_id", "legacy_pk", css_id="admin_search"
                ),
            ),
        )


class BibliographyForm(forms.ModelForm):
    class Meta:
        model = Bibliography
        exclude = ["orig_data_csv", "legacy_id", "legacy_pk"]

    def __init__(self, *args, **kwargs):
        super(BibliographyForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = True
        self.helper.form_class = "form-horizontal"
        self.helper.label_class = "col-md-3"
        self.helper.field_class = "col-md-9"
        self.helper.add_input(
            Submit("submit", "save"),
        )


class GlossaryFilterFormHelper(FormHelper):
    def __init__(self, *args, **kwargs):
        super(GlossaryFilterFormHelper, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.form_class = "genericFilterForm"
        self.form_method = "GET"
        self.form_tag = False
        self.layout = Layout(
            Fieldset("", "id", css_id="basic_search_fields"),
            BS5Accordion(
                AccordionGroup(
                    "Advanced search",
                    "legacy_pk",
                    "pref_label",
                    "glossary_collection",
                    "type",
                    "title",
                    css_id="more",
                ),
                AccordionGroup("admin", "legacy_id", css_id="admin_search"),
            ),
        )


class GlossaryForm(forms.ModelForm):
    class Meta:
        model = Glossary
        exclude = ["orig_data_csv", "legacy_id", "legacy_pk"]

    def __init__(self, *args, **kwargs):
        super(GlossaryForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = True
        self.helper.form_class = "form-horizontal"
        self.helper.label_class = "col-md-3"
        self.helper.field_class = "col-md-9"
        self.helper.add_input(
            Submit("submit", "save"),
        )


class PlaceFilterFormHelper(FormHelper):
    def __init__(self, *args, **kwargs):
        super(PlaceFilterFormHelper, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.form_class = "genericFilterForm"
        self.form_method = "GET"
        self.form_tag = False
        self.layout = Layout(
            Fieldset("", "name", css_id="basic_search_fields"),
            BS5Accordion(
                AccordionGroup("Advanced search", "part_of", css_id="more"),
                AccordionGroup(
                    "admin", "id", "legacy_id", "legacy_pk", css_id="admin_search"
                ),
            ),
        )


class PlaceForm(forms.ModelForm):
    class Meta:
        model = Place
        exclude = ["orig_data_csv", "legacy_id", "legacy_pk"]

    def __init__(self, *args, **kwargs):
        super(PlaceForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = True
        self.helper.form_class = "form-horizontal"
        self.helper.label_class = "col-md-3"
        self.helper.field_class = "col-md-9"
        self.helper.add_input(
            Submit("submit", "save"),
        )


class TabletFilterFormHelper(FormHelper):
    def __init__(self, *args, **kwargs):
        super(TabletFilterFormHelper, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.form_class = "genericFilterForm"
        self.form_method = "GET"
        self.form_tag = False
        self.layout = Layout(
            BS5Accordion(
                AccordionGroup(
                    "Basic search",
                    "ft_search",
                    "publication_name",
                    "text_number",
                    "museum_id",
                    "cdli_no",
                    css_id="basic_search_fields",
                ),
                AccordionGroup(
                    "Advanced search",
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
                    "place_of_issue",
                    "mentioned_place",
                    "regional_setting",
                    "type_content",
                    "paraphrase",
                    "legacy_paraphrase",
                    "paraphrase_negative",
                    "paraphrase_custom",
                    "transliteration",
                    "archiv",
                    "mentioned_in_pub",
                    "period",
                    "day",
                    "month",
                    "year",
                    "related_king",
                    "julian_date_year",
                    "bibliography",
                    "inferred_date",
                    "private_context",
                    "direct_speech",
                    "remark",
                    css_id="more",
                ),
                AccordionGroup(
                    "Admin search",
                    "id",
                    "project",
                    "legacy_id",
                    "legacy_pk",
                    "imported",
                    css_id="admin_search",
                ),
                always_open=False,
            ),
        )


class TabletForm(forms.ModelForm):
    class Meta:
        model = Tablet
        exclude = ["orig_data_csv", "legacy_id", "legacy_pk", "cleaned_text"]
        widgets = {
            "place_of_issue": autocomplete.ModelSelect2(
                url="archiv-ac:place-autocomplete"
            ),
            "regional_setting": autocomplete.ModelSelect2(
                url="archiv-ac:place-autocomplete"
            ),
            "related_king": autocomplete.ModelSelect2(
                url="archiv-ac:king-autocomplete"
            ),
            "mentioned_place": autocomplete.ModelSelect2Multiple(
                url="archiv-ac:place-autocomplete"
            ),
            "dossier": autocomplete.ModelSelect2(url="archiv-ac:dossier-autocomplete"),
            "type_content": autocomplete.ModelSelect2(
                url="archiv-ac:glossary-autocomplete"
            ),
            "mentioned_in_pub": autocomplete.ModelSelect2Multiple(
                url="archiv-ac:bibliography-autocomplete"
            ),
            "work_package": autocomplete.ModelSelect2Multiple(
                url="archiv-ac:workpackage-autocomplete"
            ),
            "van_driel_files": autocomplete.ModelSelect2Multiple(
                url="archiv-ac:vandrielfiles-autocomplete"
            ),
        }

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop("user", None)
        try:
            self.default_form = self.user.customuser.tablet_form
        except AttributeError:
            self.default_form = "default"
        super(TabletForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = True
        self.helper.form_class = "form-horizontal"
        self.helper.label_class = "col-md-3"
        self.helper.field_class = "col-md-9"
        self.helper.add_input(
            Submit("submit", "save"),
        )
        if self.default_form == "navico":
            self.helper.layout = Layout(
                Fieldset(
                    "Identifiers",
                    "museum_id",
                    "publication_name",
                    "text_number",
                    "cdli_no",
                ),
                Fieldset(
                    "Location and Dating",
                    "place_of_issue",
                    "regional_setting",
                    "mentioned_place",
                    "period",
                    "day",
                    "month",
                    "year",
                    "related_king",
                    "julian_date_year",
                    "julian_date_month",
                    "julian_date_day",
                    "inferred_date",
                ),
                Fieldset(
                    "Content",
                    "paraphrase",
                    "legacy_paraphrase",
                    "archiv",
                    "text_form",
                    "legal_purpose",
                    "navico_theme",
                    "slave_role",
                    "slave_descriptor",
                    "sealings",
                ),
                Fieldset(
                    "Misc.",
                    "bibliography",
                    "project",
                    "work_package",
                    "public",
                ),
            )
