from django.views.generic import TemplateView


class DigeannaIndexView(TemplateView):
    template_name = "digeanna/index.html"


class DigeannaAbout(TemplateView):
    template_name = "digeanna/about.html"
