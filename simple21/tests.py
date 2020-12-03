# Create your tests here.
import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'
import django
django.setup()


from simple21.testutils import AbstractPageTest
from django.urls import reverse

from simple21 import views
from simple21.models import Page
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
        self.assertEqual('mypage', str(self.page))

    def test_page_view(self):
        self.assertEqual('/page/{}/'.format(self.page.id), self.page.get_absolute_url())
        response = Client().get(self.page.get_absolute_url())
        assert self.page.text in str(response.content)

        response = Client().get(reverse(views.index), dict(q='fun'))
        self.assertContains(response, '<dd>mypage funny</dd>')


    def test_get_queryset(self):
        self.assertEqual('myPage', str(self.page))
        self.assertEqual(['myPage'], [page.name for page in get_queryset('fun')])

    def test_root__str(self):
        self.assertEqual('root', str(self.root))

    def test_page_with_url_redirects_to_url(self):
        page = Page.objects.create(parent=self.root, url='/123', name=self.id())
        response = Client().get(page.get_absolute_url())
        self.assertEqual(302, response.status_code)
        self.assertEqual('/123', response['location'])

class TestNavbar(AbstractPageTest):
    def test_navbar(self):
        page = Page.objects.create(parent=self.root, name='sub')
        self.assertEqual('<a href="/pages/{}/" class="nav-link">sub</a>'.format(page.id), navbar(self.root))