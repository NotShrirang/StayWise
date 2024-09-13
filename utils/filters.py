from django_filters import FilterSet
import django_filters
import pytz
from django.utils import timezone
from datetime import datetime, timedelta


class DateFilter(FilterSet):
    fromDate = django_filters.DateTimeFilter(field_name='createdAt', method='filter_fromDate')
    toDate = django_filters.DateTimeFilter(field_name='createdAt', method='filter_toDate')

    def filter_fromDate(self, queryset, name, value):
        try:
            tz = pytz.timezone(self.request.META.get('HTTP_X_TIMEZONE_REGION', 'UTC'))
        except Exception:
            tz = pytz.utc
        value = timezone.make_naive(value)
        value = tz.localize(value)
        return queryset.filter(createdAt__gte=value)

    def filter_toDate(self, queryset, name, value):
        try:
            tz = pytz.timezone(self.request.META.get('HTTP_X_TIMEZONE_REGION', 'UTC'))
        except Exception:
            tz = pytz.utc
        value = timezone.make_naive(value)
        value = tz.localize(value)
        value = value.replace(hour=23, minute=59, second=59, microsecond=999999)
        return queryset.filter(createdAt__lte=value)