import os

os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'
import django

django.setup()

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
