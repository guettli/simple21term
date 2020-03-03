from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


class Type(models.Model):
    name = models.CharField(max_length=120, unique=True)
    text = models.TextField(default='', blank=True)
    def __str__(self):
        return self.name

class Term(MPTTModel):
    name = models.CharField(max_length=120, unique=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    type = models.ForeignKey(Type, on_delete=models.PROTECT)
    text = models.TextField(default='', blank=True)

    def __str__(self):
        return self.name

    class MPTTMeta:
        order_insertion_by = ['name']
