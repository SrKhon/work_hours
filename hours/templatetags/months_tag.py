from django import template

from hours.models import Month



register = template.Library()


@register.simple_tag()
def get_months():
    return Month.objects.all()
