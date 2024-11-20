from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Fieldset
from crispy_forms.bootstrap import AccordionGroup
from crispy_bootstrap5.bootstrap5 import BS5Accordion


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
                css_id="basic_search_fields",
            ),
            BS5Accordion(
                AccordionGroup(
                    "Advanced search",
                    "short_title",
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
            Fieldset(
                "",
                "museum_id",
                "cdli_no",
                css_id="basic_search_fields",
            ),
            BS5Accordion(
                AccordionGroup(
                    "Advanced search",
                    "place_of_issue",
                    "mentioned_place",
                    "type_content",
                    "paraphrase",
                    "paraphrase_negative",
                    "paraphrase_custom",
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
                    "julian_date_year",
                    "bibliography",
                    "inferred_date",
                    css_id="more",
                ),
                AccordionGroup(
                    "admin",
                    "id",
                    "legacy_id",
                    "legacy_pk",
                    "imported",
                    css_id="admin_search",
                ),
            ),
        )


class TabletForm(forms.ModelForm):

    class Meta:
        model = Tablet
        exclude = ["orig_data_csv", "legacy_id", "legacy_pk"]

    def __init__(self, *args, **kwargs):
        super(TabletForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = True
        self.helper.form_class = "form-horizontal"
        self.helper.label_class = "col-md-3"
        self.helper.field_class = "col-md-9"
        self.helper.add_input(
            Submit("submit", "save"),
        )
