import os
import html2text

os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'
import django

django.setup()

from simple21.testutils import AbstractPageTest
from django.urls import reverse

from simple21 import views
from django.test import Client

from simple21.views import get_queryset


class PageTests(AbstractPageTest):

    def test_get_ancestors(self):
        self.assertEqual([''], [page.name for page in self.page.get_ancestors()])

    def test_get_ancestors__include_self(self):
        self.assertEqual(['', 'myPage'], [page.name for page in self.page.get_ancestors(include_self=True)])

    def test_page__get_absolute_url(self):
        self.assertEqual('/page/{}/'.format(self.page.id), self.page.get_absolute_url())

    def test_str_of_page(self):
        self.assertEqual('myPage', str(self.page))

    def test_page_view(self):
        self.assertEqual('/page/{}/'.format(self.page.id), self.page.get_absolute_url())
        response = Client().get(self.page.get_absolute_url())
        assert self.page.text in str(response.content)

    def test_search_view(self):
        page = self.page
        response = Client().get(reverse(views.search), dict(q='fun'))
        text = html2text.html2text(str(response.content)).replace('\\n', ' ')
        assert 'fun sub-page' in text

    def test_get_queryset(self):
        self.assertEqual('myPage', str(self.page))
        self.assertEqual(['myPage'], [page.name for page in get_queryset('fun')])

    def test_root__str(self):
        self.assertEqual('<root>', str(self.root))
