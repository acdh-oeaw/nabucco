from django.urls import path

from digeanna import views

app_name = "digeanna"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("about", views.About.as_view(), name="about"),
    path("my-activities", views.UserAuditLog.as_view(), name="my_activities"),
    path("all-activities", views.AuditLog.as_view(), name="all_activities"),
]
