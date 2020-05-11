from django import template
from django.utils import timezone
from datetime import datetime
register = template.Library()

@register.filter
def date_checker(element):
    new_element = element.replace(tzinfo=None)
    if new_element.date() == datetime.now().date():
        return "Today"
    print(element)
    return element

@register.filter
def days_counter(element):
    new_element = element.replace(tzinfo=None)
    today = datetime.now().date()
    date = today - new_element.date()
    return date.days