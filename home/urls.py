from django.conf.urls import url
from django.contrib import admin
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
	url(r'^$' ,views.main,name = "main"),
	url(r'^search/$' ,views.search,name = "search"),
	url(r'^signup/$' ,views.signup , name = "signup"),
	url(r'^contact/$' ,views.contact , name = "contact"),
	url(r'^login/$' ,auth_views.login ,{'template_name': 'login.html'}, name = "login"),
	url(r'^profile/$' ,views.profile, name = "profile"),
	url(r'^logout/$' ,auth_views.logout , name = "logout"),
	url(r'^(?P<id>\d+)/$' ,views.detail, name = "detail"),
	url(r'^(?P<id>\d+)/photos/$' ,views.photo, name = "photo"),
	]