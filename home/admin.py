# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from home.models import *

# Register your models here.

class GymModelAdmin(admin.ModelAdmin):
	list_display = ["id","title","updated","timestamp"]
	list_display_links=["updated"]
	list_editable=["title"]
	list_filter=["updated","timestamp"]
	search_fields=["title","text"]
	class Meta:
		model=Gym

class AddressModelAdmin(admin.ModelAdmin):
	class Meta:
		model=Address


class EquipmentModelAdmin(admin.ModelAdmin):
	class Meta:
		model=Equipment


class Content_LongModelAdmin(admin.ModelAdmin):
	class Meta:
		model=Content_Long


class PhotosModelAdmin(admin.ModelAdmin):
	class Meta:
		model=Photos

admin.site.register(Gym,GymModelAdmin)
admin.site.register(Address,AddressModelAdmin)
admin.site.register(Equipment,EquipmentModelAdmin)
admin.site.register(Content_Long,Content_LongModelAdmin)
admin.site.register(Photos,PhotosModelAdmin)