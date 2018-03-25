from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$' ,views.post_home,name = "post_home"),
    url(r'^detail/$' ,views.post_detail, name = "post_detail"),
]