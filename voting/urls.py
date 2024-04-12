from django.contrib import admin
from django.urls import path,include
from voting import views

urlpatterns = [
    path('voting', views.voting, name='voting'),
    path('result', views.result, name='result'),
    path('', views.home, name='home'),
    path('send_vote<str:candidate_name>', views.send_vote, name='send_vote'),
]
