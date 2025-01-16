from django.contrib import admin
from django.urls import path
from django.conf.urls import include


urlpatterns = [
    path("admin/", admin.site.urls),
    path("tinymce/", include("tinymce.urls")),
    path("digeanna/", include("digeanna.urls", namespace="digeanna")),
    path("news/", include("news.urls", namespace="news")),
    path("browsing/", include("browsing.urls", namespace="browsing")),
    path("info/", include("infos.urls", namespace="info")),
    path("archiv/", include("archiv.urls", namespace="archiv")),
    path("archiv-ac/", include("archiv.dal_urls", namespace="archiv-ac")),
    path("", include("webpage.urls", namespace="webpage")),
]
