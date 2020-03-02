from django.http import HttpResponse
from django.template import loader

from xyz.models import Term


def index(request):
    template = loader.get_template('xyz/index.html')
    context = dict()
    context['queryset']=get_queryset(request.GET)
    return HttpResponse(template.render(context, request))

def get_queryset(query_dict):
    if not query_dict:
        return []
    return Term.objects.filter(name__icontains=query_dict.get('q'))