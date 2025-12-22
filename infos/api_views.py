from rest_framework import viewsets

from .models import AboutTheProject
from .serializers import AboutTheProjectSerializer


class AboutTheProjectViewSet(viewsets.ModelViewSet):
    queryset = AboutTheProject.objects.all()
    serializer_class = AboutTheProjectSerializer
