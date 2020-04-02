from django.apps import AppConfig
from django.db.models.signals import post_migrate
from django.urls import reverse


class Simple21Config(AppConfig):
    name = 'simple21'

    def ready(self):
        post_migrate.connect(self.create_initial_tree)

    @classmethod
    def create_initial_tree(cls, **kwargs):
        from simple21.models import Term
        root = Term.objects.get_or_create(slug=Term.ROOT_SLUG, defaults=dict(name=''))[0]
        django_admin = Term.objects.get_or_create(slug=Term.DJANGO_ADMIN_SLUG, defaults=dict(name='Django Admin',
                                                                              parent=root))[0]
        Term.objects.get_or_create(slug=Term.DJANGO_ADMIN_TERM_SLUG,
                                                defaults=dict(name='Term', parent=django_admin,
                                                              url=reverse('admin:simple21_term_changelist')))
