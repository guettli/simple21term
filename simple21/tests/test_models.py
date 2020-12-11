import os

from django.db import IntegrityError

os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'
import django

django.setup()
from simple21.models import Page

from simple21.testutils import AbstractPageTest


class PageTests(AbstractPageTest):

    def test_get_ancestors(self):
        self.assertEqual([''], [page.name for page in self.page.get_ancestors()])

    def test_get_ancestors__include_self(self):
        self.assertEqual(['', 'myPage'], [page.name for page in self.page.get_ancestors(include_self=True)])

    def test_page__get_absolute_url(self):
        self.assertEqual('/page/{}/'.format(self.page.id), self.page.get_absolute_url())

    def test_str_of_page(self):
        self.assertEqual('myPage', str(self.page))

    def test_root__str(self):
        self.assertEqual('<root>', str(self.root))

    def test_get_children__of_leaf(self):
        self.assertEqual('<QuerySet []>', repr(self.page.get_children()))

    def test_get_children__of_root(self):
        self.assertEqual('<QuerySet [<Page: myPage>]>', repr(self.root.get_children()))

    def test_page_tree_must_have_only_one_root(self):
        self.assertRaises(IntegrityError, Page.objects.create, name='root2')
