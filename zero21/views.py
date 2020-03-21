from django.db.models import Q
from django.http import HttpResponse
from django.template import loader

from zero21.models import Term, SearchLog, GlobalConfig


def index(request):
    template = loader.get_template('zero21/index.html')
    query = get_query_from_request(request)
    queryset = get_queryset(query)
    create_search_log(request, query, queryset)
    return HttpResponse(template.render(dict(queryset=queryset), request))

def create_search_log(request, query, queryset):
    if request.user.is_authenticated:
        user = request.user
    else:
        user = GlobalConfig.get().anonymous_user
    SearchLog.objects.create(query=query, user=user, result_count=queryset.count())

def get_query_from_request(request):
    if not request.GET:
        return ''
    return request.GET.get('q', '')

def get_queryset(query):
    return Term.objects.filter(Q(name__icontains=query)|Q(text__icontains=query)).distinct()

def term(request, id):
    template = loader.get_template('zero21/term.html')
    term = Term.objects.get(id=id)
    return HttpResponse(template.render(dict(term=term), request))
