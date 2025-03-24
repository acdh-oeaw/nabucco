from django.urls import path
from digeanna import views

app_name = "digeanna"
urlpatterns = [
    path("", views.DigeannaIndexView.as_view(), name="index"),
    path("about", views.DigeannaAbout.as_view(), name="about"),
    path("my-activities", views.UserAuditLog.as_view(), name="my_activities"),
    path("all-activities", views.AuditLog.as_view(), name="all_activities"),
]
