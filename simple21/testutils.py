from django.utils.functional import cached_property

from django.test import TestCase
from simple21.models import Page


class AbstractPageTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Page.objects.all().delete()
        cls.root


    @cached_property
    def root(self):
        return Page.objects.update_or_create(name='', defaults=dict(text='Root Page'))[0]


    @cached_property
    def page(self):
        return Page.objects.update_or_create(name='myPage', defaults=dict(
            parent=self.root,
            text='My first fun sub-page'))[0]
