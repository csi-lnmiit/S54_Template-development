from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$' ,"home.views.post_home"),
    url(r'^detail/$' ,"home.views.post_detail"),
]