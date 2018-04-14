# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from home.models import Gym
from accounts.models import *

class Review(models.Model):
	gym_id = models.ForeignKey('home.Gym')
	user_id = models.ForeignKey('accounts.User')
	content = models.TextField(null=True)
	rating = models.DecimalField(default=0,max_digits=2,decimal_places=1)
	likes = models.IntegerField(default=0)

class Comment(models.Model):
	review_id = models.ForeignKey('review.Review')
	user_id = models.ForeignKey('accounts.User')
	comment = models.TextField(null=True)
# Create your models here.
