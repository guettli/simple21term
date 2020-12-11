import os

import html2text

os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'
import django

django.setup()

from simple21.testutils import AbstractPageTest

from django.template import Context, Template


class MenuTest(AbstractPageTest):
    def test_templatetag_menu(self):
        self.assertEqual(1, self.root.get_children().count())
        self.assertEqual(['S21', '*', 'Hello,', 'USER', '*', 'foo', '/', 'myPage'],
                         html2text.html2text(
                             Template('''{% load menu %} {% menu %}''').render(context=Context())).split())
