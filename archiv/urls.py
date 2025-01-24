# generated by appcreator
from django.urls import path
from . import views

app_name = "archiv"
urlpatterns = [
    path("archiv/", views.ArchivListView.as_view(), name="archiv_browse"),
    path(
        "archiv/detail/<int:pk>",
        views.ArchivDetailView.as_view(),
        name="archiv_detail",
    ),
    path("archiv/create/", views.ArchivCreate.as_view(), name="archiv_create"),
    path("archiv/edit/<int:pk>", views.ArchivUpdate.as_view(), name="archiv_edit"),
    path(
        "archiv/delete/<int:pk>",
        views.ArchivDelete.as_view(),
        name="archiv_delete",
    ),
    path(
        "bibliography/",
        views.BibliographyListView.as_view(),
        name="bibliography_browse",
    ),
    path(
        "bibliography/detail/<int:pk>",
        views.BibliographyDetailView.as_view(),
        name="bibliography_detail",
    ),
    path(
        "bibliography/create/",
        views.BibliographyCreate.as_view(),
        name="bibliography_create",
    ),
    path(
        "bibliography/edit/<int:pk>",
        views.BibliographyUpdate.as_view(),
        name="bibliography_edit",
    ),
    path(
        "bibliography/delete/<int:pk>",
        views.BibliographyDelete.as_view(),
        name="bibliography_delete",
    ),
    path("glossary/", views.GlossaryListView.as_view(), name="glossary_browse"),
    path(
        "glossary/detail/<int:pk>",
        views.GlossaryDetailView.as_view(),
        name="glossary_detail",
    ),
    path("glossary/create/", views.GlossaryCreate.as_view(), name="glossary_create"),
    path(
        "glossary/edit/<int:pk>",
        views.GlossaryUpdate.as_view(),
        name="glossary_edit",
    ),
    path(
        "glossary/delete/<int:pk>",
        views.GlossaryDelete.as_view(),
        name="glossary_delete",
    ),
    path("place/", views.PlaceListView.as_view(), name="place_browse"),
    path(
        "place/detail/<int:pk>",
        views.PlaceDetailView.as_view(),
        name="place_detail",
    ),
    path("place/create/", views.PlaceCreate.as_view(), name="place_create"),
    path("place/edit/<int:pk>", views.PlaceUpdate.as_view(), name="place_edit"),
    path("place/delete/<int:pk>", views.PlaceDelete.as_view(), name="place_delete"),
    path("tablet/", views.TabletListView.as_view(), name="tablet_browse"),
    path(
        "tablet/detail/<int:pk>",
        views.TabletDetailView.as_view(),
        name="tablet_detail",
    ),
    path("tablet/create/", views.TabletCreate.as_view(), name="tablet_create"),
    path("tablet/edit/<int:pk>", views.TabletUpdate.as_view(), name="tablet_edit"),
    path(
        "tablet/delete/<int:pk>",
        views.TabletDelete.as_view(),
        name="tablet_delete",
    ),
    path("dossier/", views.DossierListView.as_view(), name="dossier_browse"),
    path(
        "dossier/detail/<int:pk>",
        views.DossierDetailView.as_view(),
        name="dossier_detail",
    ),
    path("dossier/create/", views.DossierCreate.as_view(), name="dossier_create"),
    path("dossier/edit/<int:pk>", views.DossierUpdate.as_view(), name="dossier_edit"),
    path(
        "dossier/delete/<int:pk>",
        views.DossierDelete.as_view(),
        name="dossier_delete",
    ),
    path(
        "workpackage/", views.WorkPackageListView.as_view(), name="workpackage_browse"
    ),
    path(
        "workpackage/detail/<int:pk>",
        views.WorkPackageDetailView.as_view(),
        name="workpackage_detail",
    ),
    path(
        "workpackage/create/",
        views.WorkPackageCreate.as_view(),
        name="workpackage_create",
    ),
    path(
        "workpackage/edit/<int:pk>",
        views.WorkPackageUpdate.as_view(),
        name="workpackage_edit",
    ),
    # path(
    #     "workpackage/delete/<int:pk>",
    #     views.WorkPackageDelete.as_view(),
    #     name="workpackage_delete",
    # ),
]
