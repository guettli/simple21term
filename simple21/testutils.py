from django.utils.functional import cached_property

from django.test import TestCase
from simple21.models import Page


class AbstractPageTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.root = cls.get_root()
        cls.page = cls.get_page()


    @classmethod
    def get_root(cls):
        return Page.objects.update_or_create(parent=None, defaults=dict(text='Root Page'))[0]


    @classmethod
    def get_page(cls):
        return Page.objects.update_or_create(name='myPage', defaults=dict(
            parent=cls.root,
            text='My first fun sub-page'))[0]
