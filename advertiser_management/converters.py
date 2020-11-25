from django.utils import timezone
from datetime import time


class DateConverter:
    regex = '[0-9]{4}-[0-9]{2}-[0-9]{2}'

    def to_python(self, value):
        return timezone.datetime.strptime(value, '%Y-%m-%d')

    def to_url(self, value):
        return value.strftime('%Y-%m-%d')


class DateTimeConverter:
    # time = ^((?:[01]\d|2[0-3]):[0-5]\d:[0-5]\d$)
    regex = '[0-9]{4}-[0-9]{2}-[0-9]{2}-[0-9]{2}:[0-9]{2}'

    def to_python(self, value):
        t = timezone.datetime.strptime(value, '%Y-%m-%d-%H:%M')
        return t

    def to_url(self, value):
        return value.strftime('%Y-%m-%d-%H:%M')
