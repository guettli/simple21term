from django.urls import path

from . import views

urlpatterns = [
    path('', views.search, name='search'),
    path('page/<int:id>/', views.page, name='page'),
    ]