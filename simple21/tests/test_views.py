import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'
import django
django.setup()

import html2text
from simple21.models import GlobalConfig


from simple21.testutils import AbstractPageTest
from django.urls import reverse

from simple21 import views
from django.test import Client

from simple21.views import get_queryset, test_session_of_anonymous_user


class ViewTests(AbstractPageTest):

    def test_page_view(self):
        self.assertEqual('/page/{}/'.format(self.page.id), self.page.get_absolute_url())
        response = Client().get(self.page.get_absolute_url())
        assert self.page.text in str(response.content)

    def test_search_view(self):
        self.page
        response = Client().get(reverse(views.search), dict(q='fun'))
        text = html2text.html2text(str(response.content)).replace('\\n', ' ')
        assert 'fun sub-page' in text

    def test_get_queryset(self):
        self.assertEqual('myPage', str(self.page))
        self.assertEqual(['myPage'], [page.name for page in get_queryset('fun')])

    def test__test_session_of_anonymous_user(self):
        url = reverse(test_session_of_anonymous_user)
        user = GlobalConfig.get().anonymous_user
        client_one = Client()
        response = client_one.get(url, dict(me='client_one'))
        self.assertEqual(200, response.status_code)
        self.assertEqual([dict(data=dict(me='client_one'), user=user.username, id=user.id)], client_one.session['get'])

        client_two = Client()
        response = client_two.get(url, dict(me='client_two'))
        self.assertEqual(200, response.status_code)
        self.assertEqual([dict(data=dict(me='client_two'), user=user.username, id=user.id)], client_two.session['get'])

        response = client_one.get(url, dict(me='client_one'))
        self.assertEqual(200, response.status_code)
        self.assertEqual([dict(data=dict(me='client_one'), user=user.username, id=user.id),
                          dict(data=dict(me='client_one'), user=user.username, id=user.id),
                          ], client_one.session['get'])




