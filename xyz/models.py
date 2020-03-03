from django.db import models
from django.urls import reverse
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

    def get_absolute_url(self):
        return reverse('term', kwargs=dict(id=self.id))

    class MPTTMeta:
        order_insertion_by = ['name']
