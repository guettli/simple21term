from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('terms/<int:id>/', views.term, name='term'),
    ]