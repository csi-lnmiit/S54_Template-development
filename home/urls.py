from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$' ,"home.views.post_home"),
    url(r'^page/$' ,"home.views.post_list"),
]