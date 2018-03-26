from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$' ,views.main,name = "main"),
    # url(r'^detail/$' ,views.detail, name = "detail"),
    url(r'^(?P<id>\d+)/$' ,views.detail, name = "detail"),
    url(r'^html_test$' ,views.html_test, name = "html_test"),
    url(r'^detail/$' ,views.detail, name = "detail"),
	]