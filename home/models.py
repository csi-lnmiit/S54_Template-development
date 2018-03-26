# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# def upload_location(instance,filename):
# 	return "%s/%s" %(instance.id,filename)

# Create your models here.
class Gym(models.Model):
	title=models.CharField(max_length=120,null=False)
	cover_image=models.ImageField(default="...",blank=True)
	content_short=models.TextField(null=True)
	timing = models.CharField(max_length=120,null=True)
	charges = models.CharField(max_length=150,null=True)
	contact = models.CharField(max_length=100,null=True)	
	updated=models.DateTimeField(auto_now=True,auto_now_add=False)
	timestamp=models.DateTimeField(auto_now=False,auto_now_add=True)

	def __unicode__(self):
		return self.title
	def __str__(self):
		return self.title


class Address(models.Model):
	gym_id = models.ForeignKey('Gym',on_delete=models.CASCADE)
	locality = models.CharField(max_length=40,null=True)
	city = models.CharField(max_length=40,null=True)
	complete_add= models.CharField(max_length=100,null=True)
	google_maps_add = models.CharField(max_length=100,null=True)
	updated=models.DateTimeField(auto_now=True,auto_now_add=False)
	timestamp=models.DateTimeField(auto_now=False,auto_now_add=True)
	def __unicode__(self):
		return self.complete_add
	def __str__(self):
		return self.complete_add


class Equipment(models.Model):
	gym_id = models.ForeignKey('Gym')
	name = models.CharField(max_length=100,null=True)
	purpose = models.CharField(max_length=100,null=True)
	specs = models.CharField(max_length=100,null=True)
	complete = models.CharField(max_length=200,null=True)
	updated=models.DateTimeField(auto_now=True,auto_now_add=False)
	timestamp=models.DateTimeField(auto_now=False,auto_now_add=True)
	def __unicode__(self):
		return self.name
	def __str__(self):
		return self.name


class Content_Long(models.Model):
	gym_id = models.ForeignKey('Gym')
	detail1 = models.CharField(max_length=100,null=True)
	detail2 = models.CharField(max_length=100,null=True)
	detail3 = models.CharField(max_length=100,null=True)
	updated=models.DateTimeField(auto_now=True,auto_now_add=False)
	timestamp=models.DateTimeField(auto_now=False,auto_now_add=True)
	def __unicode__(self):
		return self.gym_id
	def __str__(self):
		return self.gym_id


class Photos(models.Model):
	gym_id = models.ForeignKey('Gym')
	image = models.ImageField(null=True,blank=True)
	name = models.CharField(max_length=20,null=True)
	updated=models.DateTimeField(auto_now=True,auto_now_add=False)
	timestamp=models.DateTimeField(auto_now=False,auto_now_add=True)
	def __unicode__(self):
		return self.name
	def __str__(self):
		return self.name
	

# http://127.0.0.1:8000/media/car.jpg
# http://127.0.0.1:8000/media/23/car_Rhzw6Lu.jpg