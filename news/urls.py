from django.urls import path

from news.views import NewsEntryDetailView


app_name = "news"

urlpatterns = [
    path(
        "<int:pk>",
        NewsEntryDetailView.as_view(),
        name="detail",
    ),
]
