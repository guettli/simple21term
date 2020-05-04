# Create your tests here.
import os


os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'
import django
django.setup()


from simple21.testutils import AbstractTermTest
from simple21.templatetags.simple21 import navbar
from django.urls import reverse

from . import views
from .models import Term
from django.test import Client

from .views import get_queryset


class TermTests(AbstractTermTest):

    def test_term__get_absolute_url(self):
        self.assertEqual('/terms/{}/'.format(self.term.id), self.term.get_absolute_url())

    def test_str_of_term(self):
        self.assertEqual('myterm', str(self.term))

    def test_term_view(self):
        self.assertEqual('/terms/{}/'.format(self.term.id), self.term.get_absolute_url())
        response = Client().get(self.term.get_absolute_url())
        self.assertContains(response, '<dd>myterm funny</dd>')

        response = Client().get(reverse(views.index), dict(q='fun'))
        self.assertContains(response, '<dd>myterm funny</dd>')

    def test_get_queryset(self):
        self.assertEqual('myterm', str(self.term))
        self.assertEqual(['myterm'], [term.name for term in get_queryset('fun')])

    def test_root__str(self):
        self.assertEqual('root', str(self.root))

    def test_term_with_url_redirects_to_url(self):
        term = Term.objects.create(parent=self.root, url='/123', name=self.id())
        response = Client().get(term.get_absolute_url())
        self.assertEqual(302, response.status_code)
        self.assertEqual('/123', response['location'])

class TestNavbar(AbstractTermTest):
    def test_navbar(self):
        term = Term.objects.create(parent=self.root, name='sub')
        self.assertEqual('<a href="/terms/{}/" class="nav-link">sub</a>'.format(term.id), navbar(self.root))