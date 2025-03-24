from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from auditlog.models import LogEntry

from news.models import NewsEntry


class DigeannaIndexView(TemplateView):
    template_name = "digeanna/index.html"

    def get_context_data(self, **kwargs):
        kwargs["news"] = NewsEntry.objects.all()[:3]
        return super().get_context_data(**kwargs)


class DigeannaAbout(TemplateView):
    template_name = "digeanna/about.html"


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
