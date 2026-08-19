from django.http import JsonResponse
from django.views.generic import TemplateView

from archiv.filters import TabletListFilter
from archiv.models import Tablet
from stats.utils import group_count


class TabletDashboard(TemplateView):
    template_name = "stats/tablet-stats.html"


def tablet_stats_data(request):
    STATISTICS = {
        "kings": "related_king",
        "periods": "period_object",
        "work_packages": "work_package",
        "type_content": "type_content",
        "format": "tablet_format",
    }
    query_params = request.GET
    qs = TabletListFilter(query_params, queryset=Tablet.objects.all()).qs
    data = {name: group_count(qs, field) for name, field in STATISTICS.items()}

    return JsonResponse(data, json_dumps_params={"ensure_ascii": False})
