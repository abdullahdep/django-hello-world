# pages/templatetags/custom_filters.py

from django import template
import pprint

register = template.Library()

@register.filter
def multiply(value, arg):
    try:
        return float(value) * float(arg)
    except (ValueError, TypeError):
        return ''

@register.filter(name='delay_calc')
def delay_calc(counter):
    """Calculate animation delay based on loop counter"""
    return counter * 0.1

@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)

@register.filter(name='pprint')
def pprint_filter(value):
    """Pretty prints a Python object"""
    return pprint.pformat(value, indent=2)

@register.filter(name='get_mcq')
def get_mcq(mcqs, mcq_id):
    """Gets an MCQ from a queryset by ID"""
    try:
        mcq_id = int(mcq_id)
        if hasattr(mcqs, 'filter'):
            return mcqs.filter(id=mcq_id).first()
        return next(mcq for mcq in mcqs if mcq.id == mcq_id)
    except (ValueError, StopIteration, AttributeError):
        return None

@register.filter
def to_range(start, end):
    """Returns a range from start to end (inclusive)"""
    try:
        return range(int(start), int(end) + 1)
    except (ValueError, TypeError):
        return range(0)
