# generated by appcreator
from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin

from . models import (
    Archiv,
    Bibliography,
    Glossary,
    Introduction,
    Place,
    Tablet
)


@admin.register(Glossary)
class GlossaryAdmin(DraggableMPTTAdmin):
    model = Glossary

    list_filter = (
        ('broader_concept', admin.RelatedOnlyFieldListFilter),
    )
    search_fields = ['pref_label']
    autocomplete_fields = ['broader_concept']
    mptt_level_indent = 50


admin.site.register(Archiv)
admin.site.register(Bibliography)
admin.site.register(Place)
admin.site.register(Tablet)
admin.site.register(Introduction)
