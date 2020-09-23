from django import template

register = template.Library()


@register.filter()
def format_int(value):
    """
    Разбивает число на разряды
    """
    if value:
        return '{0:,}'.format(value).replace(',', ' ')
    else:
        return value
