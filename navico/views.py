from django.core.exceptions import ObjectDoesNotExist
from django.views.generic import TemplateView

from infos.models import AboutTheProject
from news.models import NewsEntry


class IndexView(TemplateView):
    template_name = "navico/index.html"

    def get_context_data(self, **kwargs):
        kwargs["news"] = NewsEntry.objects.all()[:3]
        return super().get_context_data(**kwargs)


class About(TemplateView):
    template_name = "navico/about.html"

    def get_context_data(self, **kwargs):
        try:
            kwargs["object"] = AboutTheProject.objects.get(title="Navico")
        except ObjectDoesNotExist:
            kwargs["object"] = {"error": True}
        return super().get_context_data(**kwargs)
