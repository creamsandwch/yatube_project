from django.urls import path

from . import views

urls = [
    path('', views.index()),
    path('group/<slug:slug>', views.group_posts())
]