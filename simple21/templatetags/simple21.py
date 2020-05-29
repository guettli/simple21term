from django import template
from django.template.defaultfilters import join
from django.utils.html import format_html, format_html_join
from simple21.models import Term

register = template.Library()

@register.simple_tag
def navbar(parent_term=None):
    '''
            <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
          Dropdown
        </a>
        <div class="dropdown-menu" aria-labelledby="navbarDropdown">
          <a class="dropdown-item" href="#">Action</a>
    :return:
    '''
    ul_classes = ['menu']
    if not parent_term:
        parent_term = Term.get_root()
    if not parent_term.is_root_node():
        ul_classes.append('dropdown')
    return format_html('<ul class="{}">{}</ul>', join(ul_classes, ' '), join(
        [navbar_item(term) for term in
            Term.objects.filter(parent=parent_term).order_by('name')], ' '))

def navbar_item(term):
    link_classes=['menu-link']
    if not term.is_leaf_node():
        link_classes.append('dropdown-toggle')
    link = format_html('<a class="{}" href="{}">{}</a>', join(link_classes, ' '), term.get_absolute_url(), term)
    if term.is_leaf_node():
        return format_html('<li class="menu-item">{}</li>', link)
    return format_html('<li class="menu-item dropdown">{}{}</li>', link, navbar(term))
