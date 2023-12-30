
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('logout', views.quit, name='quit'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('<str:username>', views.your_profile, name="your_profile"),
    path('<str:username>/edit', views.edit, name="edit_profile")

]
