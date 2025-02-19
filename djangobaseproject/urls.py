from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from rest_framework import routers

from archiv import api_views

router = routers.DefaultRouter()
router.register(r"tablets", api_views.TabletViewSet)
router.register(r"domains", api_views.DomainViewSet)
router.register(r"transactiontypes", api_views.TransActionTypeViewSet)
router.register(r"legalpurposes", api_views.LegalPurposeViewSet)
router.register(r"textforms", api_views.TextFormViewSet)
router.register(r"vandrielfiles", api_views.VanDrielFilesViewSet)
router.register(r"archivs", api_views.ArchivViewSet)
router.register(r"bibliographies", api_views.BibliographyViewSet)
router.register(r"glossaries", api_views.GlossaryViewSet)
router.register(r"places", api_views.PlaceViewSet)
router.register(r"introductions", api_views.IntroductionViewSet)
router.register(r"dossiers", api_views.DossierViewSet)
router.register(r"workpackages", api_views.WorkPackageViewSet)


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls), name='api-root'),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
    path("tinymce/", include("tinymce.urls")),
    path("digeanna/", include("digeanna.urls", namespace="digeanna")),
    path("news/", include("news.urls", namespace="news")),
    path("browsing/", include("browsing.urls", namespace="browsing")),
    path("info/", include("infos.urls", namespace="info")),
    path("archiv/", include("archiv.urls", namespace="archiv")),
    path("archiv-ac/", include("archiv.dal_urls", namespace="archiv-ac")),
    path("", include("webpage.urls", namespace="webpage")),
]
