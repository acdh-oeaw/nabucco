from rest_framework import viewsets

from archiv.models import (
    Tablet,
    Domain,
    TransActionType,
    LegalPurpose,
    TextForm,
    VanDrielFiles,
    Archiv,
    Bibliography,
    Glossary,
    Place,
    Introduction,
    Dossier,
    WorkPackage,
)
from archiv.serializers import (
    TabletSerializer,
    DomainSerializer,
    TransActionTypeSerializer,
    LegalPurposeSerializer,
    TextFormSerializer,
    VanDrielFilesSerializer,
    ArchivSerializer,
    BibliographySerializer,
    GlossarySerializer,
    PlaceSerializer,
    IntroductionSerializer,
    DossierSerializer,
    WorkPackageSerializer,
)


class TabletViewSet(viewsets.ModelViewSet):
    queryset = Tablet.objects.all()
    serializer_class = TabletSerializer


class DomainViewSet(viewsets.ModelViewSet):
    queryset = Domain.objects.all()
    serializer_class = DomainSerializer


class TransActionTypeViewSet(viewsets.ModelViewSet):
    queryset = TransActionType.objects.all()
    serializer_class = TransActionTypeSerializer


class LegalPurposeViewSet(viewsets.ModelViewSet):
    queryset = LegalPurpose.objects.all()
    serializer_class = LegalPurposeSerializer


class TextFormViewSet(viewsets.ModelViewSet):
    queryset = TextForm.objects.all()
    serializer_class = TextFormSerializer


class VanDrielFilesViewSet(viewsets.ModelViewSet):
    queryset = VanDrielFiles.objects.all()
    serializer_class = VanDrielFilesSerializer


class ArchivViewSet(viewsets.ModelViewSet):
    queryset = Archiv.objects.all()
    serializer_class = ArchivSerializer


class BibliographyViewSet(viewsets.ModelViewSet):
    queryset = Bibliography.objects.all()
    serializer_class = BibliographySerializer


class GlossaryViewSet(viewsets.ModelViewSet):
    queryset = Glossary.objects.all()
    serializer_class = GlossarySerializer


class PlaceViewSet(viewsets.ModelViewSet):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer


class IntroductionViewSet(viewsets.ModelViewSet):
    queryset = Introduction.objects.all()
    serializer_class = IntroductionSerializer


class DossierViewSet(viewsets.ModelViewSet):
    queryset = Dossier.objects.all()
    serializer_class = DossierSerializer


class WorkPackageViewSet(viewsets.ModelViewSet):
    queryset = WorkPackage.objects.all()
    serializer_class = WorkPackageSerializer
