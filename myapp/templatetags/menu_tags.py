from django import template
from django.urls import reverse
from myapp.models import MenuItem


register = template.Library()

@register.inclusion_tag('myapp/menu.html', takes_context=True)
def draw_menu(context):
    menu_items = MenuItem.objects.all()
    return {'menu_items': menu_items}