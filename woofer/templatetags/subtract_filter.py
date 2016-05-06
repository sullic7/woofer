"""This file contains a template filter that should exist by default."""
from django import template

register = template.Library()

@register.filter
def subtract(value, arg):
    return value - arg