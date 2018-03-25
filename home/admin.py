# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from home.models import Gym,Photos 

# Register your models here.

class GymModelAdmin(admin.ModelAdmin):
	list_display = ["id","title","updated","timestamp"]
	list_display_links=["updated"]
	list_editable=["title"]
	list_filter=["updated","timestamp"]
	search_fields=["title","text"]
	class Meta:
		model=Gym

class PhotosModelAdmin(admin.ModelAdmin):
	class Meta:
		model=Photos

admin.site.register(Gym,GymModelAdmin)
admin.site.register(Photos,PhotosModelAdmin)