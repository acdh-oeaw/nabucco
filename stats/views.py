from django.db.models import CharField, ForeignKey, ManyToManyField
from django.http import JsonResponse
from django.views.generic import TemplateView

from archiv.filters import TabletListFilter
from archiv.models import Tablet
from stats.utils import group_count


def _build_statistics():
    statistics = {}
    for field in Tablet._meta.get_fields():
        if isinstance(field, (ForeignKey, ManyToManyField)) or (
            isinstance(field, CharField) and field.choices
        ):
            statistics[str(field.verbose_name)] = field.name
    return statistics


class TabletDashboard(TemplateView):
    template_name = "stats/tablet-stats.html"


def tablet_stats_data(request):
    STATISTICS = _build_statistics()
    query_params = request.GET
    qs = TabletListFilter(query_params, queryset=Tablet.objects.all()).qs
    data = {name: group_count(qs, field) for name, field in STATISTICS.items()}

    return JsonResponse(data, json_dumps_params={"ensure_ascii": False})
