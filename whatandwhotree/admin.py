from django.contrib import admin
from mptt.admin import MPTTModelAdmin

from .models import Term, Type

admin.site.register(Term, MPTTModelAdmin)
admin.site.register(Type)
