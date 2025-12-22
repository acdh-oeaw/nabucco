from auditlog.models import LogEntry
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.exceptions import ObjectDoesNotExist
from django.views.generic import TemplateView
from django.views.generic.list import ListView

from infos.models import AboutTheProject
from news.models import NewsEntry


class IndexView(TemplateView):
    template_name = "digeanna/index.html"

    def get_context_data(self, **kwargs):
        kwargs["news"] = NewsEntry.objects.all()[:3]
        return super().get_context_data(**kwargs)


class About(TemplateView):
    template_name = "digeanna/about.html"

    def get_context_data(self, **kwargs):
        try:
            kwargs["object"] = AboutTheProject.objects.filter(title="DigEanna")[0]
        except ObjectDoesNotExist:
            kwargs["object"] = {"error": True}
        return super().get_context_data(**kwargs)


class UserAuditLog(LoginRequiredMixin, ListView):
    template_name = "digeanna/log.html"
    paginate_by = 25

    def get_queryset(self, *args, **kwargs):
        return LogEntry.objects.filter(actor=self.request.user)


class AuditLog(UserPassesTestMixin, ListView):
    template_name = "digeanna/log.html"
    model = LogEntry
    paginate_by = 25

    def test_func(self):
        return self.request.user.is_superuser
