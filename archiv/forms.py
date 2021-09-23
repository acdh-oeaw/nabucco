# generated by appcreator
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit,  Layout, Fieldset, Div, MultiField, HTML
from crispy_forms.bootstrap import Accordion, AccordionGroup

from . models import (
    Archiv,
    Bibliography,
    Glossary,
    Place,
    Tablet
)


class ArchivFilterFormHelper(FormHelper):
    def __init__(self, *args, **kwargs):
        super(ArchivFilterFormHelper, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.form_class = 'genericFilterForm'
        self.form_method = 'GET'
        self.helper.form_tag = False
        self.add_input(Submit('Filter', 'Search'))
        self.layout = Layout(
            Fieldset(
                'Basic search options',
                'id',
                css_id="basic_search_fields"
                ),
            Accordion(
                AccordionGroup(
                    'Advanced search',
                    
                    'legacy_pk',
                    'name',
                    'part_of',
                    'alt_name',
                    'title',
                    'related_objects',
                    css_id="more"
                    ),
                AccordionGroup(
                    'admin',
                    'legacy_id',
                    css_id="admin_search"
                    ),
                )
            )


class ArchivForm(forms.ModelForm):

    class Meta:
        model = Archiv
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(ArchivForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = True
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-md-3'
        self.helper.field_class = 'col-md-9'
        self.helper.add_input(Submit('submit', 'save'),)


class BibliographyFilterFormHelper(FormHelper):
    def __init__(self, *args, **kwargs):
        super(BibliographyFilterFormHelper, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.form_class = 'genericFilterForm'
        self.form_method = 'GET'
        self.helper.form_tag = False
        self.add_input(Submit('Filter', 'Search'))
        self.layout = Layout(
            Fieldset(
                'Basic search options',
                'id',
                css_id="basic_search_fields"
                ),
            Accordion(
                AccordionGroup(
                    'Advanced search',
                    
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
                    css_id="more"
                    ),
                AccordionGroup(
                    'admin',
                    'legacy_id',
                    css_id="admin_search"
                    ),
                )
            )


class BibliographyForm(forms.ModelForm):

    class Meta:
        model = Bibliography
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(BibliographyForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = True
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-md-3'
        self.helper.field_class = 'col-md-9'
        self.helper.add_input(Submit('submit', 'save'),)


class GlossaryFilterFormHelper(FormHelper):
    def __init__(self, *args, **kwargs):
        super(GlossaryFilterFormHelper, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.form_class = 'genericFilterForm'
        self.form_method = 'GET'
        self.helper.form_tag = False
        self.add_input(Submit('Filter', 'Search'))
        self.layout = Layout(
            Fieldset(
                'Basic search options',
                'id',
                css_id="basic_search_fields"
                ),
            Accordion(
                AccordionGroup(
                    'Advanced search',
                    
                    'legacy_pk',
                    'pref_label',
                    'hierarchy',
                    css_id="more"
                    ),
                AccordionGroup(
                    'admin',
                    'legacy_id',
                    css_id="admin_search"
                    ),
                )
            )


class GlossaryForm(forms.ModelForm):

    class Meta:
        model = Glossary
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(GlossaryForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = True
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-md-3'
        self.helper.field_class = 'col-md-9'
        self.helper.add_input(Submit('submit', 'save'),)


class PlaceFilterFormHelper(FormHelper):
    def __init__(self, *args, **kwargs):
        super(PlaceFilterFormHelper, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.form_class = 'genericFilterForm'
        self.form_method = 'GET'
        self.helper.form_tag = False
        self.add_input(Submit('Filter', 'Search'))
        self.layout = Layout(
            Fieldset(
                'Basic search options',
                'id',
                css_id="basic_search_fields"
                ),
            Accordion(
                AccordionGroup(
                    'Advanced search',
                    
                    'legacy_pk',
                    'name',
                    'part_of',
                    'related_objects',
                    css_id="more"
                    ),
                AccordionGroup(
                    'admin',
                    'legacy_id',
                    css_id="admin_search"
                    ),
                )
            )


class PlaceForm(forms.ModelForm):

    class Meta:
        model = Place
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(PlaceForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = True
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-md-3'
        self.helper.field_class = 'col-md-9'
        self.helper.add_input(Submit('submit', 'save'),)


class TabletFilterFormHelper(FormHelper):
    def __init__(self, *args, **kwargs):
        super(TabletFilterFormHelper, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.form_class = 'genericFilterForm'
        self.form_method = 'GET'
        self.helper.form_tag = False
        self.add_input(Submit('Filter', 'Search'))
        self.layout = Layout(
            Fieldset(
                'Basic search options',
                'id',
                css_id="basic_search_fields"
                ),
            Accordion(
                AccordionGroup(
                    'Advanced search',
                    
                    'legacy_pk',
                    'museum_id',
                    'place_of_issue',
                    'type_content',
                    'paraphrase',
                    'transliteration',
                    'archiv',
                    css_id="more"
                    ),
                AccordionGroup(
                    'admin',
                    'legacy_id',
                    css_id="admin_search"
                    ),
                )
            )


class TabletForm(forms.ModelForm):

    class Meta:
        model = Tablet
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(TabletForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = True
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-md-3'
        self.helper.field_class = 'col-md-9'
        self.helper.add_input(Submit('submit', 'save'),)

