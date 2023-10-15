from django.contrib import admin
from django.urls import path , include
from . import  views

app_name = "blog"

urlpatterns = [
    path('', views.all_blog),
    path('<int:blog_id>', views.some_blog ,name = 'someblog'),
]