from django.urls import path

from navico import views

app_name = "navico"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("about", views.About.as_view(), name="about"),
]
