from browsing.utils import (
    BaseDetailView,
)
from news.models import NewsEntry


class NewsEntryDetailView(BaseDetailView):
    model = NewsEntry
    template_name = "news/news_detail.html"
