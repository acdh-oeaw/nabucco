from django.urls import path

from stats import views

app_name = "network"
urlpatterns = [
    path("tablet-stats-data/", views.tablet_stats_data, name="tablet-stats-data"),
    path("tablet-dashboard/", views.TabletDashboard.as_view(), name="tablet-dashboard"),
]
