from django import template

register = template.Library()

@register.filter(name='multiply')
def multiply(value, arg):
    """Multiplies the value by the argument"""
    try:
        return float(value) * float(arg)
    except (ValueError, TypeError):
        return 0

@register.filter(name='delay_calc')
def delay_calc(counter):
    """Calculate animation delay based on loop counter"""
    return counter * 0.1

@register.filter(name='get_item')
def get_item(dictionary, key):
    """Gets an item from a dictionary using key"""
    return dictionary.get(str(key))  # Convert key to string to handle numeric IDs

@register.filter(name='pprint')
def pprint(value):
    """Pretty prints a Python object"""
    import pprint
    return pprint.pformat(value, indent=2)

@register.filter(name='get_mcq')
def get_mcq(mcqs, mcq_id):
    """Gets an MCQ from a queryset by ID"""
    try:
        # Convert mcq_id to integer since it might be a string
        mcq_id = int(mcq_id)
        # Try direct filter first for efficiency
        if hasattr(mcqs, 'filter'):
            return mcqs.filter(id=mcq_id).first()
        # Fallback to iteration if it's a list/tuple
        return next(mcq for mcq in mcqs if mcq.id == mcq_id)
    except (ValueError, StopIteration, AttributeError):
        return None