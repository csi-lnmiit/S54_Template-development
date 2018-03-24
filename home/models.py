# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


def upload_location(instance,filename):
	return "%s/%s" %(instance.id,filename)

# Create your models here.
class Post(models.Model):
	title=models.CharField(max_length=120)
	image=models.ImageField(null=True,blank=True)
	# height_field=models.IntegerField(default=0)
	# width_field=models.IntegerField(default=0)
	text=models.TextField()	
	updated=models.DateTimeField(auto_now=True,auto_now_add=False)
	timestamp=models.DateTimeField(auto_now=False,auto_now_add=True)
	def __unicode__(self):
		return self.title
	def __str__(self):
		return self.title
