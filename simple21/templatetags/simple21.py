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
    if not parent_term:
        parent_term = Term.get_root()
    return format_html_join('', '<a href="{}" class="nav-link">{}</a>',
                            [(term.get_absolute_url(), term.name) for term in Term.objects.filter(parent=parent_term).order_by('name')])
