from rest_framework import serializers

from archiv.models import (
    Archiv,
    Bibliography,
    Domain,
    Dossier,
    Glossary,
    Introduction,
    LegalPurpose,
    Place,
    Tablet,
    TextForm,
    TransActionType,
    VanDrielFiles,
    WorkPackage,
)


class TabletSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tablet
        fields = "__all__"
        depth = 1


class DomainSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Domain
        fields = "__all__"


class TransActionTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TransActionType
        fields = "__all__"


class LegalPurposeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = LegalPurpose
        fields = "__all__"


class TextFormSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TextForm
        fields = "__all__"


class VanDrielFilesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = VanDrielFiles
        fields = "__all__"


class ArchivSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Archiv
        fields = "__all__"


class BibliographySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Bibliography
        fields = "__all__"


class GlossarySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Glossary
        fields = "__all__"


class PlaceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Place
        fields = "__all__"


class IntroductionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Introduction
        fields = "__all__"


class DossierSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Dossier
        fields = "__all__"


class WorkPackageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = WorkPackage
        fields = "__all__"
