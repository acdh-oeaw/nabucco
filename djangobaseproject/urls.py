from django.contrib import admin
from django.urls import path
from django.conf.urls import include


urlpatterns = [
    path("admin/", admin.site.urls),
    path("browsing/", include("browsing.urls", namespace="browsing")),
    path("netvis/", include("netvis.urls", namespace="netvis")),
    path("info/", include("infos.urls", namespace="info")),
    path("archiv/", include("archiv.urls", namespace="archiv")),
    path("archiv-ac/", include("archiv.dal_urls", namespace="archiv-ac")),
    path("", include("webpage.urls", namespace="webpage")),
]
