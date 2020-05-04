from django.contrib.auth.models import User
from django.db import models
from django.db.models import CheckConstraint, Q
from django.urls import reverse
from mptt.models import MPTTModel, TreeForeignKey

class Term(MPTTModel):
    name = models.CharField(max_length=120, unique=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    slug = models.SlugField(null=True, blank=True, db_index=True)
    text = models.TextField(default='', blank=True)
    url = models.CharField(default='', blank=True, max_length=10000)

    ROOT_SLUG = 'root'
    DJANGO_ADMIN_SLUG = 'django_admin'
    DJANGO_ADMIN_TERM_SLUG = 'django_admin_term'

    def __str__(self):
        if self.slug == self.ROOT_SLUG:
            return self.slug
        return ' / '.join([term.name for term in self.get_ancestors(include_self=True) if term.name])

    @classmethod
    def get_root(cls):
        return cls.objects.get(slug=cls.ROOT_SLUG)

    def get_absolute_url(self):
        return reverse('term', kwargs=dict(id=self.id))

    class Meta:
        constraints = [
            CheckConstraint(name='parent_must_exist__or__is_root',
                            check=Q(parent__isnull=False)|Q(slug='root'))
        ]
    class MPTTMeta:
        order_insertion_by = ['name']

class SearchLog(models.Model):
    query = models.CharField(max_length=1024)
    datetime = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    result_count = models.PositiveIntegerField()

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
