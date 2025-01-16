from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from browsing.utils import (
    BaseDetailView,
    BaseCreateView,
    BaseUpdateView,
)
from news.models import NewsEntry


class NewsEntryDetailView(BaseDetailView):
    model = NewsEntry
    template_name = "news/news_detail.html"


class NewsEntryCreate(BaseCreateView):

    model = NewsEntry

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(NewsEntryCreate, self).dispatch(*args, **kwargs)


class NewsEntryUpdate(BaseUpdateView):

    model = NewsEntry

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(NewsEntryUpdate, self).dispatch(*args, **kwargs)
