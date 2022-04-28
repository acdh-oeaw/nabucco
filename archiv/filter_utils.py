from django.db.models import Q

from django_filters import FilterSet


def get_query(queryset, iterator, name):
    q = Q()
    for x in iterator:
        q |= Q(**{f'{name}__icontains': x})
    return queryset.filter(q)


def schreder_filter(queryset, name, value):
    to_include = []
    to_exclude = []
    to_consider = []
    for x in value.split():
        if x.startswith('+'):
            to_include.append(x[1:])
        elif x.startswith('-'):
            to_exclude.append(x[1:])
        else:
            to_consider.append(x)
    for x in to_exclude:
        queryset = queryset.exclude(**{f'{name}__icontains': x})
    for x in to_include:
        queryset = queryset.filter(**{f'{name}__icontains': x})
    final_qs = get_query(queryset, to_consider, name)
    return final_qs


class SchrederFilter(FilterSet):

    def scheder_filtering(self, queryset, name, value):
        qs = schreder_filter(queryset, name, value)
        return qs
