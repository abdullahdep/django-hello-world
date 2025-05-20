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