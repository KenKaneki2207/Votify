from django.contrib import admin
from django.urls import path,include
from votingContact import views

urlpatterns = [
  path('', views.contact, name='contact'),
  path('query', views.query, name='query'),
]