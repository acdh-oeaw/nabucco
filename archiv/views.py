# generated by appcreator
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import DeleteView
from . filters import (
    ArchivListFilter,
    BibliographyListFilter,
    GlossaryListFilter,
    PlaceListFilter,
    TabletListFilter
)
from . forms import (
    ArchivForm,
    ArchivFilterFormHelper,
    BibliographyForm,
    BibliographyFilterFormHelper,
    GlossaryForm,
    GlossaryFilterFormHelper,
    PlaceFilterFormHelper,
    PlaceForm,
    TabletFilterFormHelper,
    TabletForm
)
from . tables import (
    ArchivTable,
    BibliographyTable,
    GlossaryTable,
    PlaceTable,
    TabletTable
)
from . models import (
    Archiv,
    Bibliography,
    Glossary,
    Place,
    Tablet
)
from browsing.browsing_utils import (
    GenericListView, BaseCreateView, BaseUpdateView, BaseDetailView
)


class ArchivListView(GenericListView):

    model = Archiv
    filter_class = ArchivListFilter
    formhelper_class = ArchivFilterFormHelper
    table_class = ArchivTable
    init_columns = [
        'name', 'part_of'
    ]
    enable_merge = False
    template_name = 'archiv/generic_list.html'


class ArchivDetailView(BaseDetailView):

    model = Archiv
    template_name = 'archiv/generic_detail.html'


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
    template_name = 'webpage/confirm_delete.html'
    success_url = reverse_lazy('archiv:archiv_browse')

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ArchivDelete, self).dispatch(*args, **kwargs)


class BibliographyListView(GenericListView):

    model = Bibliography
    filter_class = BibliographyListFilter
    formhelper_class = BibliographyFilterFormHelper
    table_class = BibliographyTable
    init_columns = [
        'title', 'short_title', 'publication_year', 'author',
    ]
    enable_merge = True


class BibliographyDetailView(BaseDetailView):

    model = Bibliography
    template_name = 'archiv/generic_detail.html'


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
    template_name = 'webpage/confirm_delete.html'
    success_url = reverse_lazy('archiv:bibliography_browse')

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(BibliographyDelete, self).dispatch(*args, **kwargs)


class GlossaryListView(GenericListView):

    model = Glossary
    filter_class = GlossaryListFilter
    formhelper_class = GlossaryFilterFormHelper
    table_class = GlossaryTable
    init_columns = [
        'pref_label', 'broader_concept',
    ]
    enable_merge = True,
    template_name = 'archiv/glossary_list.html'


class GlossaryDetailView(BaseDetailView):

    model = Glossary
    template_name = 'archiv/generic_detail.html'


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
    template_name = 'webpage/confirm_delete.html'
    success_url = reverse_lazy('archiv:glossary_browse')

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(GlossaryDelete, self).dispatch(*args, **kwargs)


class PlaceListView(GenericListView):

    model = Place
    regions = Place.objects.all().values_list('part_of__name', flat=True).order_by('part_of__name').distinct('part_of__name')
    filter_class = PlaceListFilter
    formhelper_class = PlaceFilterFormHelper
    table_class = PlaceTable
    init_columns = [
        'name', 'part_of',
    ]
    enable_merge = True
    template_name = 'archiv/generic_list.html'

    def get_context_data(self, **kwargs):
        context = super(PlaceListView, self).get_context_data(**kwargs)
        context['regions'] = self.regions
        return context


class PlaceDetailView(BaseDetailView):

    model = Place
    template_name = 'archiv/generic_detail.html'


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
    template_name = 'webpage/confirm_delete.html'
    success_url = reverse_lazy('archiv:place_browse')

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(PlaceDelete, self).dispatch(*args, **kwargs)


class RegionView(ListView):

    model = Place
    template_name = 'archiv/regions.html'
    regions = PlaceListView.regions

    def get_context_data(self, **kwargs):
        context = super(RegionView, self).get_context_data(**kwargs)
        context['regions'] = self.regions
        return context

class TabletListView(GenericListView):

    model = Tablet
    filter_class = TabletListFilter
    formhelper_class = TabletFilterFormHelper
    table_class = TabletTable
    init_columns = [
        'museum_id', 'publication', 'archiv', 'type_content', 'place_of_issue'
    ]
    enable_merge = True
    template_name = 'archiv/generic_list.html'


class TabletDetailView(BaseDetailView):

    model = Tablet
    template_name = 'archiv/generic_detail.html'


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
    template_name = 'webpage/confirm_delete.html'
    success_url = reverse_lazy('archiv:tablet_browse')

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(TabletDelete, self).dispatch(*args, **kwargs)
