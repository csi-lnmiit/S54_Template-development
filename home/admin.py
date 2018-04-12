# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from home.models import *

# Register your models here.

class AddressInLine(admin.TabularInline):
	model = Address


class EquipmentInLine(admin.TabularInline):
	model = Equipment
	extra = 2


class PhotosInLine(admin.TabularInline):
	model = Photos
	extra = 3

class Content_LongInLine(admin.TabularInline):
	model = Content_Long


class GymModelAdmin(admin.ModelAdmin):
	list_display = ["id","title","updated","timestamp"]
	list_display_links=["title"]
	list_filter=["updated","timestamp"]
	search_fields=["title","text"]
	inlines = [AddressInLine,EquipmentInLine,Content_LongInLine,PhotosInLine,]


class AddressModelAdmin(admin.ModelAdmin):
	list_display = ["gym_id","locality","city"]


class EquipmentModelAdmin(admin.ModelAdmin):
	list_display = ["gym_id","name"]
	list_display_links=["name"]
	list_filter=["purpose","specs"]
	search_fields = ["name","purpose"]


class Content_LongModelAdmin(admin.ModelAdmin):
	list_display = ["gym_id"]


class PhotosModelAdmin(admin.ModelAdmin):
	list_display = ["gym_id","name"]

admin.site.register(Gym,GymModelAdmin)
admin.site.register(Address,AddressModelAdmin)
admin.site.register(Equipment,EquipmentModelAdmin)
admin.site.register(Content_Long,Content_LongModelAdmin)
admin.site.register(Photos,PhotosModelAdmin)