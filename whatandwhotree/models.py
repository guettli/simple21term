from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


class Type(models.Model):
    name = models.CharField(max_length=120, unique=True)
    text = models.TextField(default='')

class Term(MPTTModel):
    name = models.CharField(max_length=120, unique=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    type = models.ForeignKey(Type)
    text = models.TextField(default='')

    class MPTTMeta:
        order_insertion_by = ['name']
