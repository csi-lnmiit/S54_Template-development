# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.
class Gym(models.Model):
	title=models.CharField(max_length=120,null=False)
	cover_image=models.ImageField(default="...",blank=True)
	content_short=models.TextField(null=True)
	timing = models.TextField(null=True)
	charges = models.CharField(max_length=150,null=True)
	contact = models.CharField(max_length=100,null=True)
	updated=models.DateTimeField(auto_now=True,auto_now_add=False)
	timestamp=models.DateTimeField(auto_now=False,auto_now_add=True)
    	
	def __unicode__(self):
		return self.title
	def __str__(self):
		return self.title


class Address(models.Model):
	gym_id = models.OneToOneField(Gym,on_delete=models.CASCADE,primary_key=True,)
	locality = models.CharField(max_length=40,null=True)
	city = models.CharField(max_length=40,null=True)
	complete_add= models.CharField(verbose_name="complete address",max_length=100,null=True)
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
	gym_id = models.OneToOneField(Gym,on_delete=models.CASCADE,primary_key=True)
	detail1 = models.CharField(max_length=100,null=True)
	detail2 = models.CharField(max_length=100,null=True)
	detail3 = models.CharField(max_length=100,null=True)
	updated=models.DateTimeField(auto_now=True,auto_now_add=False)
	timestamp=models.DateTimeField(auto_now=False,auto_now_add=True)
	def __unicode__(self):
		return self.detail1
	def __str__(self):
		return self.detail1


class Photos(models.Model):
	gym_id = models.ForeignKey('Gym')
	image = models.ImageField(default="...",null=True,blank=True)
	name = models.CharField(max_length=20,null=True)
	updated=models.DateTimeField(auto_now=True,auto_now_add=False)
	timestamp=models.DateTimeField(auto_now=False,auto_now_add=True)
	def __unicode__(self):
		return self.name
	def __str__(self):
		return self.name