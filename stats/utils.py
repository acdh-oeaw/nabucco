from django.db.models import Count


def group_count(queryset, field):
    qs = (
        queryset.values(field)
        .annotate(count=Count("pk", distinct=True))
        .order_by("-count")
    )

    rows = list(qs)

    model_field = queryset.model._meta.get_field(field)

    related_objects = {}

    if model_field.is_relation:
        related_model = model_field.remote_field.model
        ids = [row[field] for row in rows if row[field] is not None]

        related_objects = related_model.objects.in_bulk(ids)

    result = []

    for row in rows:
        value = row[field]

        if model_field.is_relation:
            obj = related_objects.get(value)
            label = str(obj) if obj else None
        else:
            label = value
        if value and label:
            result.append(
                {
                    "value": value,
                    "label": label,
                    "count": row["count"],
                }
            )

    return result
