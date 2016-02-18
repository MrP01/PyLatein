from django import template
import importlib

register = template.Library()

@register.filter
def isinst(value, class_str):
    split = class_str.split(".")
    return isinstance(value, getattr(importlib.import_module(".".join(split[:-1])), split[-1]))