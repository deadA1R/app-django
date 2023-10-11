from django import template
from myapp.models import MenuItem

register = template.Library()

@register.inclusion_tag('myapp/menu.html')
def draw_menu(menu_name):
    menu_items = MenuItem.objects.filter(parent=None)
    return {'menu_items': menu_items}