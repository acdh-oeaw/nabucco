from django.urls import path
from . import dal_views

app_name = "archiv"
urlpatterns = [
    path(
        "archiv-autocomplete/", dal_views.ArchivAC.as_view(), name="archiv-autocomplete"
    ),
    path(
        "bibliography-autocomplete/",
        dal_views.BibliographyAC.as_view(),
        name="bibliography-autocomplete",
    ),
    path(
        "glossary-autocomplete/",
        dal_views.GlossaryAC.as_view(),
        name="glossary-autocomplete",
    ),
    path("place-autocomplete/", dal_views.PlaceAC.as_view(), name="place-autocomplete"),
    path(
        "tablet-autocomplete/", dal_views.TabletAC.as_view(), name="tablet-autocomplete"
    ),
]
