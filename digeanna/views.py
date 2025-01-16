from django.views.generic import TemplateView

from news.models import NewsEntry


class DigeannaIndexView(TemplateView):
    template_name = "digeanna/index.html"

    def get_context_data(self, **kwargs):
        kwargs["news"] = NewsEntry.objects.all()[:3]
        return super().get_context_data(**kwargs)


class DigeannaAbout(TemplateView):
    template_name = "digeanna/about.html"
