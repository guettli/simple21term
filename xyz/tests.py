# Create your tests here.
from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from . import views
from .models import Term, Type
from django.test import Client

class TermTests(TestCase):

    def create_type(self):
        return Type.objects.create(name="testtype")

    def create_term(self):
        return Term.objects.create(name="foo", text="bar", type=self.create_type())

    def test_term__get_absolute_url(self):
        term = self.create_term()
        self.assertEqual('/terms/{}/'.format(term.id), term.get_absolute_url())

    def test_term_view(self):
        term = self.create_term()
        c = Client()
        response = c.get(term.get_absolute_url())
        self.assertContains(response, '<dd>bar</dd>')

        response = c.get(reverse(views.index), dict(q='foo'))
        self.assertContains(response, '<dd>bar</dd>')

