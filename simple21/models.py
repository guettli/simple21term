from django.contrib.auth.models import User
from django.db import models
from django.db.models import CheckConstraint, Q
from django.urls import reverse
from django.contrib.postgres.fields import ArrayField

class Page(models.Model):
    parent = models.ForeignKey('Page', null=True, blank=True, on_delete=models.RESTRICT)
    name = models.CharField(max_length=120, unique=True)
    text = models.TextField(default='', blank=True)

    def __str__(self):
        if not self.parent_id:
            if self.name:
                return self.name
            return '<root>'
        return ' / '.join([page.name for page in self.get_ancestors(include_self=True) if page.name])

    def get_ancestors(self, include_self=False):
        ret = []
        if include_self:
            parent = self
        else:
            parent = self.parent
        while parent:
            ret.insert(0, parent)
            parent = parent.parent
        return ret

    def get_children(self):
        return Page.objects.filter(parent=self)

    @classmethod
    def get_root(cls):
        return cls.objects.get(parent=None)

    def get_absolute_url(self):
        return reverse('page', kwargs=dict(id=self.id))

class SearchLog(models.Model):
    query = models.CharField(max_length=1024)
    datetime = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    result_count = models.PositiveIntegerField()
    page_ids = ArrayField(models.IntegerField())

    def __str__(self):
        return '{} ({})'.format(self.query, self.result_count)

class GlobalConfig(models.Model):
    anonymous_user = models.ForeignKey(User, on_delete=models.PROTECT)
    anonymous_user_name = 'anonymous'
    ID=1

    @classmethod
    def get(cls):
        config = cls.objects.filter(id=cls.ID).first()
        if config:
            return config
        return cls.objects.create(anonymous_user=User.objects.get_or_create(username=cls.anonymous_user_name)[0])
