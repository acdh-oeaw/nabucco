from django.urls import path

from . import views

app_name = "news"

urlpatterns = [
    path(
        "<int:pk>",
        views.NewsEntryDetailView.as_view(),
        name="detail",
    ),
    path("create/", views.NewsEntryCreate.as_view(), name="create"),
    path("edit/<int:pk>", views.NewsEntryUpdate.as_view(), name="edit"),
]
