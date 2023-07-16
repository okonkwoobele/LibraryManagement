from django.urls import path

from bookApp import views

urlPattern = [
    path('welcome/', views.welcome)


]
