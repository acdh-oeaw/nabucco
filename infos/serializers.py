from rest_framework import serializers

from .models import AboutTheProject


class AboutTheProjectSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AboutTheProject
        fields = "__all__"
        depth = 1
