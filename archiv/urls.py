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
    path(
        "vandrielfile/",
        views.VanDrielFilesListView.as_view(),
        name="vandrielfile_browse",
    ),
    path(
        "vandrielfile/detail/<int:pk>",
        views.VanDrielFilesDetailView.as_view(),
        name="vandrielfile_detail",
    ),
    path(
        "vandrielfile/create/",
        views.VanDrielFilesCreate.as_view(),
        name="vandrielfile_create",
    ),
    path(
        "vandrielfile/edit/<int:pk>",
        views.VanDrielFilesUpdate.as_view(),
        name="vandrielfile_edit",
    ),
    path(
        "textform/",
        views.TextFormListView.as_view(),
        name="textform_browse",
    ),
    path(
        "textform/detail/<int:pk>",
        views.TextFormDetailView.as_view(),
        name="textform_detail",
    ),
    path(
        "textform/create/",
        views.TextFormCreate.as_view(),
        name="textform_create",
    ),
    path(
        "textform/edit/<int:pk>",
        views.TextFormUpdate.as_view(),
        name="textform_edit",
    ),
    path(
        "textform/delete/<int:pk>",
        views.TextFormDelete.as_view(),
        name="textform_delete",
    ),
    path(
        "legalpurpose/",
        views.LegalPurposeListView.as_view(),
        name="legalpurpose_browse",
    ),
    path(
        "legalpurpose/detail/<int:pk>",
        views.LegalPurposeDetailView.as_view(),
        name="legalpurpose_detail",
    ),
    path(
        "legalpurpose/create/",
        views.LegalPurposeCreate.as_view(),
        name="legalpurpose_create",
    ),
    path(
        "legalpurpose/edit/<int:pk>",
        views.LegalPurposeUpdate.as_view(),
        name="legalpurpose_edit",
    ),
    path(
        "legalpurpose/delete/<int:pk>",
        views.LegalPurposeDelete.as_view(),
        name="legalpurpose_delete",
    ),
    path(
        "transactiontype/",
        views.TransActionTypeListView.as_view(),
        name="transactiontype_browse",
    ),
    path(
        "transactiontype/detail/<int:pk>",
        views.TransActionTypeDetailView.as_view(),
        name="transactiontype_detail",
    ),
    path(
        "transactiontype/create/",
        views.TransActionTypeCreate.as_view(),
        name="transactiontype_create",
    ),
    path(
        "transactiontype/edit/<int:pk>",
        views.TransActionTypeUpdate.as_view(),
        name="transactiontype_edit",
    ),
    path(
        "transactiontype/delete/<int:pk>",
        views.TransActionTypeDelete.as_view(),
        name="transactiontype_delete",
    ),
    path(
        "domain/",
        views.DomainListView.as_view(),
        name="domain_browse",
    ),
    path(
        "domain/detail/<int:pk>",
        views.DomainDetailView.as_view(),
        name="domain_detail",
    ),
    path(
        "domain/create/",
        views.DomainCreate.as_view(),
        name="domain_create",
    ),
    path(
        "domain/edit/<int:pk>",
        views.DomainUpdate.as_view(),
        name="domain_edit",
    ),
    path(
        "domain/delete/<int:pk>",
        views.DomainDelete.as_view(),
        name="domain_delete",
    ),
]
