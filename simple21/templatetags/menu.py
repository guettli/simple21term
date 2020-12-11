from django import template
from simple21.models import Page

register = template.Library()


@register.inclusion_tag('simple21/menu.html')
def menu(current_page_id=None, takes_context=True):
    if not current_page_id:
        page = Page.get_root()
    else:
        page = Page.objects.get(id=current_page_id)
    return {'children': page.get_children()}
