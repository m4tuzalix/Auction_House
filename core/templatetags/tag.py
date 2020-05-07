from django import template
from django.utils import timezone
register = template.Library()

@register.filter
def date_checker(element):
    if element.date() == timezone.now().date():
        return "Today"
    return element

@register.filter
def days_counter(element):
    today = timezone.now()
    date = today - element
    return date.days