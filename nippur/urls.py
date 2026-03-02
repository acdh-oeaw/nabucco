from django.urls import path

from nippur import views

app_name = "nippur"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("about", views.About.as_view(), name="about"),
]
