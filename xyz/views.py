from django.http import HttpResponse
from django.template import loader

from xyz.models import Term


def index(request):
    template = loader.get_template('xyz/index.html')
    return HttpResponse(template.render(dict(queryset=get_queryset(request.GET)), request))

def get_queryset(query_dict):
    if not query_dict:
        return []
    return Term.objects.filter(name__icontains=query_dict.get('q'))

def term(request, id):
    template = loader.get_template('xyz/term.html')
    term = Term.objects.get(id=id)
    return HttpResponse(template.render(dict(term=term), request))
