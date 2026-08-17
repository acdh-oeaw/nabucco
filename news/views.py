from browsing.utils import (
    BaseCreateView,
    BaseDetailView,
    BaseUpdateView,
)
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic.list import ListView

from news.models import NewsEntry


class NewsEntryListView(ListView):
    model = NewsEntry


class NewsEntryDetailView(BaseDetailView):
    model = NewsEntry
    template_name = "news/newsentry_detail.html"


class NewsEntryCreate(BaseCreateView):

    model = NewsEntry

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class NewsEntryUpdate(BaseUpdateView):

    model = NewsEntry

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
