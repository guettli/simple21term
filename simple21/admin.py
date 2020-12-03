from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .models import Page, SearchLog


class PageAdmin(ModelAdmin):
    class Media:
        css = {
            "all": ("//cdn.quilljs.com/1.3.6/quill.snow.css",)
        }
        js = (
            "//cdn.quilljs.com/1.3.6/quill.min.js",
            "/static/simple21/quill-textarea.js",
            "/static/simple21/load_quill.js",
              )
    list_display = ['id', '__str__']

admin.site.register(Page, PageAdmin)

class SearchLogAdmin(ModelAdmin):
    list_display = ['query', 'user', 'datetime', 'result_count']
    readonly_fields = list_display
admin.site.register(SearchLog, SearchLogAdmin)