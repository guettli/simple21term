from django.db.models import Q
from django.http import HttpResponse
from django.template import loader

from simple21.models import Page, SearchLog


def search(request):
    template = loader.get_template('simple21/index.html')
    query = get_query_from_request(request)
    queryset = get_queryset(query)
    create_search_log(request, query, queryset)
    return HttpResponse(template.render(dict(queryset=queryset), request))


def create_search_log(request, query, queryset):
    SearchLog.objects.create(query=query, user=request.user, result_count=queryset.count(),
                             page_ids=list(queryset.values_list('id', flat=True)))


def get_query_from_request(request):
    if not request.GET:
        return ''
    return request.GET.get('q', '')


def get_queryset(query):
    return Page.objects.filter(Q(name__icontains=query) | Q(text__icontains=query)).distinct()


def page(request, id):
    template = loader.get_template('simple21/page.html')
    page = Page.objects.get(id=id)
    return HttpResponse(template.render(dict(page=page), request))

def test_session_of_anonymouse_user(request):
    request.session['get']=dict(data=request.GET, user=request.user.username, id=request.user.id)
    return HttpResponse('ok')