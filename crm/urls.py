# demo/urls.py
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^NumberReport/', views.NumberReport, name='NumberReport'),
    url(r'^NumberOrganizeReport/', views.NumberOrganizeReport, name='NumberOrganizeReport'),
]