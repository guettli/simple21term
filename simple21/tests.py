# Create your tests here.
import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'
import django
django.setup()

from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
from django.utils.functional import cached_property

from . import views
from .models import Term, Type
from django.test import Client

from .views import get_queryset


class TermTests(TestCase):

    @cached_property
    def type(self):
        return Type.objects.update_or_create(name="testtype")[0]

    @cached_property
    def term(self):
        return Term.objects.update_or_create(name="foo", defaults=dict(text="bar", type=self.type))[0]

    @cached_property
    def sub_term(self):
        return Term.objects.update_or_create(name="sub", defaults=dict(
            parent=self.term,
            text="sub-bar funny", type=self.type))[0]

    def test_term__get_absolute_url(self):
        self.assertEqual('/terms/{}/'.format(self.term.id), self.term.get_absolute_url())

    def test_str_of_sub_term(self):
        self.assertEqual('foo / sub', str(self.sub_term))

    def test_term_view(self):
        c = Client()
        response = c.get(self.term.get_absolute_url())
        self.assertContains(response, '<dd>bar</dd>')

        response = c.get(reverse(views.index), dict(q='foo'))
        self.assertContains(response, '<dd>bar</dd>')

    def test_get_queryset(self):
        self.assertTrue('sub-bar funny', self.sub_term)
        self.assertEqual(['sub'], [term.name for term in get_queryset('fun')])
