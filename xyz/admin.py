from django.contrib import admin
from mptt.admin import MPTTModelAdmin

from .models import Term, Type

class TermAdmin(MPTTModelAdmin):
    class Media:
        css = {
            "all": ("//cdn.quilljs.com/1.3.6/quill.snow.css",)
        }
        js = (
            "//cdn.quilljs.com/1.3.6/quill.min.js",
            "/static/xyz/quill-textarea.js",
            "/static/xyz/load_quill.js",
              )

admin.site.register(Term, TermAdmin)
admin.site.register(Type)
