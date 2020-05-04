from django.utils.functional import cached_property

from django.test import TestCase
from simple21.models import Term


class AbstractTermTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Term.objects.all().delete()
        cls.root


    @cached_property
    def root(self):
        return Term.objects.update_or_create(name='', defaults=dict(text="Root Term", slug=Term.ROOT_SLUG))[0]


    @cached_property
    def term(self):
        return Term.objects.update_or_create(name="myterm", defaults=dict(
            parent=self.root,
            text="myterm funny"))[0]
