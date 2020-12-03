from django.apps import AppConfig
from django.db.models.signals import post_migrate
from django.urls import reverse


class Simple21Config(AppConfig):
    name = 'simple21'

