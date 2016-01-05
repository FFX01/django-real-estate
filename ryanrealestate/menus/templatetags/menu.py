from django import template

from menus.models import MenuModel


register = template.Library()


@register.inclusion_tag('menus/nav.html')
def render_menu(menu_slug):
    menu = MenuModel.objects.get(slug=menu_slug)
    items = menu.menu_item.order_by('-order')
    return {
        'items': items,
        'menu': menu,
    }
