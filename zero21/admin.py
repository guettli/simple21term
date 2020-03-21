from django.contrib import admin
from django.contrib.admin import ModelAdmin
from mptt.admin import MPTTModelAdmin

from .models import Term, Type, SearchLog


class TermAdmin(MPTTModelAdmin):
    class Media:
        css = {
            "all": ("//cdn.quilljs.com/1.3.6/quill.snow.css",)
        }
        js = (
            "//cdn.quilljs.com/1.3.6/quill.min.js",
            "/static/zero21/quill-textarea.js",
            "/static/zero21/load_quill.js",
              )
    list_display = ['__str__', 'type']

admin.site.register(Term, TermAdmin)
admin.site.register(Type)

class SearchLogAdmin(ModelAdmin):
    list_display = ['query', 'user', 'datetime', 'result_count']
    readonly_fields = list_display
admin.site.register(SearchLog, SearchLogAdmin)