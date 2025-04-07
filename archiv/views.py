# generated by appcreator
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView

from .filters import (
    ArchivListFilter,
    BibliographyListFilter,
    GlossaryListFilter,
    PlaceListFilter,
    TabletListFilter,
)
from .forms import (
    ArchivForm,
    ArchivFilterFormHelper,
    BibliographyForm,
    BibliographyFilterFormHelper,
    GlossaryForm,
    GlossaryFilterFormHelper,
    PlaceFilterFormHelper,
    PlaceForm,
    TabletFilterFormHelper,
    TabletForm,
)
from .tables import (
    ArchivTable,
    BibliographyTable,
    GlossaryTable,
    PlaceTable,
    TabletTable,
    DossierTable,
)
from .models import (
    Archiv,
    Bibliography,
    Glossary,
    Place,
    Tablet,
    Introduction,
    Dossier,
    WorkPackage,
    VanDrielFiles,
    TextForm,
    LegalPurpose,
    TransActionType,
    Domain,
)
from browsing.utils import (
    GenericListView,
    BaseCreateView,
    BaseUpdateView,
    BaseDetailView,
)


class ArchivListView(GenericListView):
    model = Archiv
    filter_class = ArchivListFilter
    formhelper_class = ArchivFilterFormHelper
    table_class = ArchivTable
    init_columns = ["name", "part_of"]
    enable_merge = False
    try:
        archive, created = Introduction.objects.get_or_create(title="Archives")
    except Exception as e:
        print(e)
        archive = e

    def get_context_data(self, **kwargs):
        context = super(ArchivListView, self).get_context_data(**kwargs)
        if self.archive:
            context["introduction"] = self.archive
        return context


class ArchivDetailView(BaseDetailView):

    model = Archiv
    template_name = "archiv/archiv_detail.html"


class ArchivCreate(BaseCreateView):

    model = Archiv
    form_class = ArchivForm

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ArchivCreate, self).dispatch(*args, **kwargs)


class ArchivUpdate(BaseUpdateView):

    model = Archiv
    form_class = ArchivForm

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ArchivUpdate, self).dispatch(*args, **kwargs)


class ArchivDelete(DeleteView):
    model = Archiv
    template_name = "webpage/confirm_delete.html"
    success_url = reverse_lazy("archiv:archiv_browse")

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ArchivDelete, self).dispatch(*args, **kwargs)


class BibliographyListView(GenericListView):

    model = Bibliography
    filter_class = BibliographyListFilter
    formhelper_class = BibliographyFilterFormHelper
    table_class = BibliographyTable
    init_columns = [
        "title",
        "short_title",
        "publication_year",
        "author",
    ]
    enable_merge = True


class BibliographyDetailView(BaseDetailView):

    model = Bibliography
    template_name = "archiv/biblio_detail.html"


class BibliographyCreate(BaseCreateView):

    model = Bibliography
    form_class = BibliographyForm

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(BibliographyCreate, self).dispatch(*args, **kwargs)


class BibliographyUpdate(BaseUpdateView):

    model = Bibliography
    form_class = BibliographyForm

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(BibliographyUpdate, self).dispatch(*args, **kwargs)


class BibliographyDelete(DeleteView):
    model = Bibliography
    template_name = "webpage/confirm_delete.html"
    success_url = reverse_lazy("archiv:bibliography_browse")

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(BibliographyDelete, self).dispatch(*args, **kwargs)


class GlossaryListView(GenericListView):

    model = Glossary
    filter_class = GlossaryListFilter
    formhelper_class = GlossaryFilterFormHelper
    table_class = GlossaryTable
    init_columns = [
        "pref_label",
        "broader_concept",
    ]
    enable_merge = (True,)
    template_name = "archiv/glossary_list.html"


class GlossaryDetailView(BaseDetailView):

    model = Glossary
    template_name = "archiv/glossary_detail.html"


class GlossaryCreate(BaseCreateView):

    model = Glossary
    form_class = GlossaryForm

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(GlossaryCreate, self).dispatch(*args, **kwargs)


class GlossaryUpdate(BaseUpdateView):

    model = Glossary
    form_class = GlossaryForm

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(GlossaryUpdate, self).dispatch(*args, **kwargs)


class GlossaryDelete(DeleteView):
    model = Glossary
    template_name = "webpage/confirm_delete.html"
    success_url = reverse_lazy("archiv:glossary_browse")

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(GlossaryDelete, self).dispatch(*args, **kwargs)


class PlaceListView(GenericListView):

    model = Place
    filter_class = PlaceListFilter
    formhelper_class = PlaceFilterFormHelper
    table_class = PlaceTable
    init_columns = [
        "name",
        "part_of",
    ]
    enable_merge = True

    def get_context_data(self, **kwargs):
        context = super(PlaceListView, self).get_context_data(**kwargs)
        return context


class PlaceDetailView(BaseDetailView):

    model = Place
    template_name = "archiv/place_detail.html"


class PlaceCreate(BaseCreateView):

    model = Place
    form_class = PlaceForm

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(PlaceCreate, self).dispatch(*args, **kwargs)


class PlaceUpdate(BaseUpdateView):

    model = Place
    form_class = PlaceForm

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(PlaceUpdate, self).dispatch(*args, **kwargs)


class PlaceDelete(DeleteView):
    model = Place
    template_name = "webpage/confirm_delete.html"
    success_url = reverse_lazy("archiv:place_browse")

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(PlaceDelete, self).dispatch(*args, **kwargs)


class TabletListView(GenericListView):

    model = Tablet
    filter_class = TabletListFilter
    formhelper_class = TabletFilterFormHelper
    table_class = TabletTable
    template_name = "archiv/tablet_list.html"
    init_columns = [
        "id",
        "publication_name",
        "text_number",
        "museum_id",
        "type_content",
        "archiv",
        "place_of_issue",
        "period",
    ]
    enable_merge = True


class TabletDetailView(BaseDetailView):

    model = Tablet
    template_name = "archiv/tablet_detail.html"


class TabletCreate(BaseCreateView):

    model = Tablet
    form_class = TabletForm

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(TabletCreate, self).dispatch(*args, **kwargs)


class TabletUpdate(BaseUpdateView):

    model = Tablet
    form_class = TabletForm

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(TabletUpdate, self).dispatch(*args, **kwargs)


class TabletDelete(DeleteView):
    model = Tablet
    template_name = "webpage/confirm_delete.html"
    success_url = reverse_lazy("archiv:tablet_browse")

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(TabletDelete, self).dispatch(*args, **kwargs)


class DossierListView(GenericListView):

    model = Dossier
    init_columns = [
        "name",
    ]
    enable_merge = True
    table_class = DossierTable


class DossierDetailView(BaseDetailView):

    model = Dossier


class DossierCreate(BaseCreateView):

    model = Dossier

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(DossierCreate, self).dispatch(*args, **kwargs)


class DossierUpdate(BaseUpdateView):

    model = Dossier

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(DossierUpdate, self).dispatch(*args, **kwargs)


class DossierDelete(DeleteView):
    model = Dossier
    template_name = "webpage/confirm_delete.html"
    success_url = reverse_lazy("archiv:dossier_browse")

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(TabletDelete, self).dispatch(*args, **kwargs)


class WorkPackageListView(GenericListView):

    model = WorkPackage
    init_columns = ["id", "wp_number", "title"]
    enable_merge = True


class WorkPackageDetailView(BaseDetailView):
    model = WorkPackage
    template_name = "archiv/workpackage_detail.html"


class WorkPackageCreate(BaseCreateView):

    model = WorkPackage

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(WorkPackageCreate, self).dispatch(*args, **kwargs)


class WorkPackageUpdate(BaseUpdateView):

    model = WorkPackage

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(WorkPackageUpdate, self).dispatch(*args, **kwargs)


class WorkPackageDelete(DeleteView):
    model = WorkPackage
    template_name = "webpage/confirm_delete.html"
    success_url = reverse_lazy("archiv:workpackage_browse")

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(TabletDelete, self).dispatch(*args, **kwargs)


class VanDrielFilesListView(GenericListView):

    model = VanDrielFiles
    init_columns = ["id", "file", "sub_file"]
    enable_merge = True


class VanDrielFilesDetailView(BaseDetailView):
    model = VanDrielFiles
    template_name = "archiv/vandrielfile_detail.html"


class VanDrielFilesCreate(BaseCreateView):

    model = VanDrielFiles

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(VanDrielFilesCreate, self).dispatch(*args, **kwargs)


class VanDrielFilesUpdate(BaseUpdateView):

    model = VanDrielFiles

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(VanDrielFilesUpdate, self).dispatch(*args, **kwargs)


class VanDrielFilesDelete(DeleteView):
    model = VanDrielFiles
    template_name = "webpage/confirm_delete.html"
    success_url = reverse_lazy("archiv:workpackage_browse")

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(TabletDelete, self).dispatch(*args, **kwargs)


class TextFormListView(GenericListView):

    model = TextForm
    init_columns = ["id", "name", "verbum_regens"]
    enable_merge = True


class TextFormDetailView(BaseDetailView):
    model = TextForm
    template_name = "archiv/domain_et_all_detail.html"


class TextFormCreate(BaseCreateView):

    model = TextForm

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(TextFormCreate, self).dispatch(*args, **kwargs)


class TextFormUpdate(BaseUpdateView):

    model = TextForm

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(TextFormUpdate, self).dispatch(*args, **kwargs)


class TextFormDelete(DeleteView):
    model = TextForm
    template_name = "webpage/confirm_delete.html"
    success_url = reverse_lazy("archiv:textform_browse")

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(TextFormDelete, self).dispatch(*args, **kwargs)


class LegalPurposeListView(GenericListView):

    model = LegalPurpose
    init_columns = ["id", "name", "verbum_regens"]
    enable_merge = True


class LegalPurposeDetailView(BaseDetailView):
    model = LegalPurpose
    template_name = "archiv/domain_et_all_detail.html"


class LegalPurposeCreate(BaseCreateView):

    model = LegalPurpose

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(LegalPurposeCreate, self).dispatch(*args, **kwargs)


class LegalPurposeUpdate(BaseUpdateView):

    model = LegalPurpose

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(LegalPurposeUpdate, self).dispatch(*args, **kwargs)


class LegalPurposeDelete(DeleteView):
    model = LegalPurpose
    template_name = "webpage/confirm_delete.html"
    success_url = reverse_lazy("archiv:legalpurpose_browse")

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(LegalPurposeDelete, self).dispatch(*args, **kwargs)


class TransActionTypeListView(GenericListView):

    model = TransActionType
    init_columns = ["id", "name", "description"]
    enable_merge = True


class TransActionTypeDetailView(BaseDetailView):
    model = TransActionType
    template_name = "archiv/domain_et_all_detail.html"


class TransActionTypeCreate(BaseCreateView):

    model = TransActionType

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(TransActionTypeCreate, self).dispatch(*args, **kwargs)


class TransActionTypeUpdate(BaseUpdateView):

    model = TransActionType

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(TransActionTypeUpdate, self).dispatch(*args, **kwargs)


class TransActionTypeDelete(DeleteView):
    model = TransActionType
    template_name = "webpage/confirm_delete.html"
    success_url = reverse_lazy("archiv:transactiontype_browse")

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(TransActionTypeDelete, self).dispatch(*args, **kwargs)


class DomainListView(GenericListView):

    model = Domain
    init_columns = ["id", "name", "description"]
    enable_merge = True


class DomainDetailView(BaseDetailView):
    model = Domain
    template_name = "archiv/domain_et_all_detail.html"


class DomainCreate(BaseCreateView):

    model = Domain

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(DomainCreate, self).dispatch(*args, **kwargs)


class DomainUpdate(BaseUpdateView):

    model = Domain

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(DomainUpdate, self).dispatch(*args, **kwargs)


class DomainDelete(DeleteView):
    model = Domain
    template_name = "webpage/confirm_delete.html"
    success_url = reverse_lazy("archiv:domain_browse")

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(DomainDelete, self).dispatch(*args, **kwargs)
