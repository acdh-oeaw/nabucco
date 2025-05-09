# generated by appcreator
from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin
from django.apps import apps
from .models import Glossary


for x in list(apps.all_models["archiv"].values()):
    model_name = x.__name__
    if model_name == "Glossary" or "mentioned" in model_name:
        pass
    else:
        admin.site.register(x)


@admin.register(Glossary)
class GlossaryAdmin(DraggableMPTTAdmin):
    model = Glossary

    list_filter = (("broader_concept", admin.RelatedOnlyFieldListFilter),)
    search_fields = ["pref_label"]
    autocomplete_fields = ["broader_concept"]
    mptt_level_indent = 50
