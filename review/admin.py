# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import *
# Register your models here.
class ReviewModelAdmin(admin.ModelAdmin):
	list_display = ["gym_id","user_id","rating"]
class CommentModelAdmin(admin.ModelAdmin):
	list_display = ["review_id","user_id","comment"]

admin.site.register(Review,ReviewModelAdmin)
admin.site.register(Comment,CommentModelAdmin)