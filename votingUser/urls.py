from django.contrib import admin
from django.urls import path
from votingUser import views

urlpatterns = [
  path('', views.votingUser, name='votingUser'),
  path('login.html', views.login_page, name='login'),
  path('signup.html', views.signup, name='signup'),
  path('register', views.register, name="register"),
  path('login_user', views.login_user, name='login_user'),
  path('logout_user', views.logout_user, name='logout_user'),
] 